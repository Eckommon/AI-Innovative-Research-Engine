#!/usr/bin/env python3
"""C-EU-F01 outcome-blind EEA site × ERA5-Land source/access/identity gate.

Reads only EEA site identity/coordinate fields. Never requests industrial outcome/thematic
fields. Verifies ERA5-Land documentation/access metadata and probes the official ARCO
Zarr metadata route without credentials or authentication bypass. Never reads t2m values.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "C-EU-F01"
UA = "AI-Innovative-Research-Engine/C-EU-F01-outcome-blind"

LAYER_URL = "https://air.discomap.eea.europa.eu/arcgis/rest/services/Air/IED_SiteMap/MapServer/0"
QUERY_URL = LAYER_URL + "/query"
EEA_DATASET_URL = "https://industry.eea.europa.eu/industrial-emissions/dataset"
ERA5_TS_URL = "https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land-timeseries?tab=overview"
ERA5_PUG_URL = "https://confluence.ecmwf.int/spaces/CKB/pages/536218894/ERA5-Land%2Bhourly%2BAnalysis%2BReady%2BCloud%2BOptimised%2BARCO%2Bdata%2Bon%2Bsingle%2Blevels%2Bfrom%2B1950%2Bto%2Bpresent%2BProduct%2BUser%2BGuide%2BPUG"
ARCO_ROOT = "https://arco.datastores.ecmwf.int/cadl-arco-geo-007/arco/reanalysis_era5_land/sfc-2m-temperature/geoChunked.zarr"
ARCO_METADATA_CANDIDATES = [ARCO_ROOT + "/.zmetadata", ARCO_ROOT + "/zarr.json"]

ALLOWED_QUERY_FIELDS = ["OBJECTID", "InspireSiteId", "siteName", "countryCode", "x_4258", "y_4258", "Site_reporting_year"]
REQUIRED_FIELDS = {"InspireSiteId", "countryCode", "x_4258", "y_4258"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str, *, timeout: int = 60, max_bytes: int | None = None):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read() if max_bytes is None else r.read(max_bytes)
        return data, getattr(r, "status", 200), r.geturl(), dict(r.headers)


def fetch_retry(url: str, attempts: int = 3, timeout: int = 60):
    last = None
    for i in range(attempts):
        try:
            return fetch(url, timeout=timeout)
        except Exception as exc:
            last = exc
            if i + 1 < attempts:
                time.sleep(2 * (i + 1))
    raise last


def arcgis_json(base: str, params: dict[str, str | int]):
    url = base + "?" + urllib.parse.urlencode(params)
    data, status, final, headers = fetch_retry(url, timeout=90)
    obj = json.loads(data.decode("utf-8"))
    if "error" in obj:
        raise RuntimeError(f"ArcGIS error: {obj['error']}")
    return obj, {"url": url, "http": status, "final_url": final, "bytes": len(data), "sha256": sha256(data), "content_type": headers.get("Content-Type", "")}


def finite_float(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None


def norm_space(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def probe_unauth_arco():
    attempts = []
    for url in ARCO_METADATA_CANDIDATES:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                data = r.read(2_000_000)
                attempts.append({"url": url, "http": getattr(r, "status", 200), "bytes_read": len(data), "sha256": sha256(data), "error": None})
                if data:
                    return True, data, attempts
        except urllib.error.HTTPError as exc:
            body = exc.read(4096)
            attempts.append({"url": url, "http": exc.code, "bytes_read": len(body), "sha256": sha256(body), "error": "HTTPError"})
        except Exception as exc:
            attempts.append({"url": url, "http": None, "bytes_read": 0, "sha256": None, "error": type(exc).__name__})
    return False, None, attempts


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    layer, layer_audit = arcgis_json(LAYER_URL, {"f": "pjson"})
    fields = {f.get("name") for f in layer.get("fields", [])}
    geometry_point = layer.get("geometryType") == "esriGeometryPoint"
    required_fields_present = REQUIRED_FIELDS.issubset(fields)
    supports_query = "Query" in str(layer.get("capabilities", "")) or bool(layer.get("advancedQueryCapabilities"))

    count_obj, count_audit = arcgis_json(QUERY_URL, {"where": "1=1", "returnCountOnly": "true", "f": "json"})
    total_records = int(count_obj.get("count", 0))

    page_size = min(int(layer.get("maxRecordCount") or 1000), 1000)
    offset = 0
    rows = []
    page_hashes = []
    while True:
        params = {
            "where": "1=1",
            "outFields": ",".join(ALLOWED_QUERY_FIELDS),
            "returnGeometry": "false",
            "resultOffset": offset,
            "resultRecordCount": page_size,
            "orderByFields": "OBJECTID ASC",
            "f": "json",
        }
        page, audit = arcgis_json(QUERY_URL, params)
        feats = page.get("features", [])
        page_hashes.append({"offset": offset, "rows": len(feats), "sha256": audit["sha256"]})
        for feat in feats:
            attrs = feat.get("attributes") or {}
            # Persist/process only the explicitly allowed identity/support fields.
            rows.append({k: attrs.get(k) for k in ALLOWED_QUERY_FIELDS})
        if len(feats) < page_size:
            break
        offset += len(feats)
        if offset > total_records + page_size:
            raise RuntimeError("ArcGIS pagination exceeded reported count")

    coords_by_id = defaultdict(set)
    countries_by_id = defaultdict(set)
    all_ids = set()
    valid_coordinate_row_count = 0
    invalid_coordinate_row_count = 0
    for row in rows:
        sid = str(row.get("InspireSiteId") or "").strip()
        if not sid:
            continue
        all_ids.add(sid)
        cc = str(row.get("countryCode") or "").strip().upper()
        if cc:
            countries_by_id[sid].add(cc)
        lon = finite_float(row.get("x_4258"))
        lat = finite_float(row.get("y_4258"))
        if lon is None or lat is None or not (-180 <= lon <= 180) or not (-90 <= lat <= 90):
            invalid_coordinate_row_count += 1
            continue
        coords_by_id[sid].add((lon, lat))
        valid_coordinate_row_count += 1

    conflicting_ids = {sid for sid, pairs in coords_by_id.items() if len(pairs) > 1}
    qualified_ids = {sid for sid in all_ids if sid not in conflicting_ids and len(coords_by_id.get(sid, set())) == 1}
    qualified_countries = {cc for sid in qualified_ids for cc in countries_by_id.get(sid, set()) if cc}
    coord_rate = len(qualified_ids) / len(all_ids) if all_ids else 0.0

    # Official lineage/documentation pages. No thematic values are parsed.
    eea_dataset_bytes, eea_http, eea_final, _ = fetch_retry(EEA_DATASET_URL, timeout=60)
    ts_bytes, ts_http, ts_final, _ = fetch_retry(ERA5_TS_URL, timeout=60)
    pug_bytes, pug_http, pug_final, _ = fetch_retry(ERA5_PUG_URL, timeout=90)
    ts_text = norm_space(ts_bytes.decode("utf-8", errors="replace"))
    pug_text = norm_space(pug_bytes.decode("utf-8", errors="replace"))
    combined = ts_text + " " + pug_text

    semantic_checks = {
        "two_m_temperature": ("2m temperature" in combined) or ("2m_temperature" in combined) or ("sfc-2m-temperature" in combined),
        "units_k": (">k<" in combined) or (" kelvin" in combined) or ("units" in combined and " k " in combined),
        "hourly": "hourly" in combined,
        "coverage_1950_present": "1950" in combined and ("present" in combined or "to present" in combined),
        "resolution_0_1": ("0.1" in combined) and ("grid" in combined or "resolution" in combined or "degrees" in combined),
        "nearest_grid_semantics": ("nearest grid point" in combined) or ("closest" in combined and "0.1" in combined and "grid" in combined),
        "cds_api_key_documented": "cds api key" in combined or "cdsapi key" in combined,
        "official_arco_url_documented": "cadl-arco-geo-007" in combined and "sfc-2m-temperature" in combined,
    }
    era5_semantic_pass = all(semantic_checks[k] for k in ["two_m_temperature", "units_k", "hourly", "coverage_1950_present", "resolution_0_1", "nearest_grid_semantics", "cds_api_key_documented", "official_arco_url_documented"])

    unauth_ok, arco_meta_bytes, arco_attempts = probe_unauth_arco()
    statuses = {x.get("http") for x in arco_attempts}
    credential_blocked = (not unauth_ok) and bool(statuses & {401, 403}) and semantic_checks["cds_api_key_documented"]

    # F01 may only freeze grid identities from actual official coordinate arrays.
    # Without authenticated metadata/coordinate access we intentionally do not infer arrays from docs.
    authoritative_grid_metadata_retrieved = False
    grid_identity_count = 0
    grid_fingerprint = None
    if unauth_ok and arco_meta_bytes:
        # Metadata bytes alone are not assumed to contain authoritative coordinate values;
        # a future implementation may parse actual arrays only if the same official route is openly executable.
        authoritative_grid_metadata_retrieved = False

    requirements = {
        "eea_layer_accessible_and_hashed": layer_audit["http"] == 200 and count_audit["http"] == 200,
        "required_fields_and_point_geometry": required_fields_present and geometry_point and supports_query,
        "distinct_site_ids_ge_10000": len(all_ids) >= 10_000,
        "coordinate_qualified_rate_ge_95pct": coord_rate >= 0.95,
        "qualified_country_codes_ge_25": len(qualified_countries) >= 25,
        "conflicting_site_ids_zero": len(conflicting_ids) == 0,
        "era5_semantics_confirmed": era5_semantic_pass,
        "official_programmatic_grid_metadata_retrievable": authoritative_grid_metadata_retrieved,
        "grid_identities_ge_95pct_and_fingerprinted": bool(grid_fingerprint) and grid_identity_count >= math.ceil(0.95 * len(qualified_ids)),
        "outcome_and_temperature_values_unopened_relationship_not_computed_cost_zero": True,
    }

    first_six = all(requirements[k] for k in [
        "eea_layer_accessible_and_hashed",
        "required_fields_and_point_geometry",
        "distinct_site_ids_ge_10000",
        "coordinate_qualified_rate_ge_95pct",
        "qualified_country_codes_ge_25",
        "conflicting_site_ids_zero",
    ])
    if all(requirements.values()):
        gate = "PASS_C_EU_F01_SITE_HEAT_JOIN_READY"
    elif first_six and requirements["era5_semantics_confirmed"] and credential_blocked:
        gate = "PARTIAL_C_EU_F01_SITE_IDENTITY_READY__CDS_CREDENTIAL_REQUIRED"
    else:
        gate = "HOLD_C_EU_F01_SOURCE_OR_IDENTITY"

    source_audit = {
        "eea_layer_metadata": layer_audit,
        "eea_query_count": count_audit,
        "eea_query_pages": page_hashes,
        "eea_dataset_page": {"url": EEA_DATASET_URL, "http": eea_http, "final_url": eea_final, "bytes": len(eea_dataset_bytes), "sha256": sha256(eea_dataset_bytes)},
        "era5_timeseries_page": {"url": ERA5_TS_URL, "http": ts_http, "final_url": ts_final, "bytes": len(ts_bytes), "sha256": sha256(ts_bytes)},
        "era5_pug_page": {"url": ERA5_PUG_URL, "http": pug_http, "final_url": pug_final, "bytes": len(pug_bytes), "sha256": sha256(pug_bytes)},
        "arco_unauthenticated_metadata_probe": arco_attempts,
        "allowed_eea_query_fields": ALLOWED_QUERY_FIELDS,
    }
    (OUT / "STAGING_SOURCE_AUDIT.json").write_text(json.dumps(source_audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    result = {
        "gate": gate,
        "requirements": requirements,
        "eea": {
            "reported_layer_records": total_records,
            "queried_rows": len(rows),
            "distinct_nonblank_site_ids": len(all_ids),
            "coordinate_qualified_site_ids": len(qualified_ids),
            "coordinate_qualified_rate": coord_rate,
            "qualified_country_codes": len(qualified_countries),
            "conflicting_site_ids": len(conflicting_ids),
            "valid_coordinate_rows": valid_coordinate_row_count,
            "invalid_coordinate_rows": invalid_coordinate_row_count,
            "required_fields_present": required_fields_present,
            "geometry_point": geometry_point,
            "supports_query": supports_query,
        },
        "era5": {
            "semantic_checks": semantic_checks,
            "semantic_pass": era5_semantic_pass,
            "unauthenticated_arco_metadata_access": unauth_ok,
            "credential_blocked": credential_blocked,
            "authoritative_grid_metadata_retrieved": authoritative_grid_metadata_retrieved,
            "grid_identity_count": grid_identity_count,
            "grid_fingerprint": grid_fingerprint,
        },
        "industrial_outcome_or_thematic_magnitudes_opened": False,
        "site_temperature_magnitudes_opened": False,
        "relationship_computed": False,
        "fuzzy_identity_repair_used": False,
        "unofficial_mirror_used": False,
        "authentication_bypass_used": False,
        "post_execution_rescue_used": False,
        "raw_source_bytes_persisted": False,
        "incremental_monetary_cost_usd": 0,
    }
    (OUT / "STAGING_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "gate": gate,
        "site_ids": len(all_ids),
        "qualified_site_ids": len(qualified_ids),
        "coordinate_rate": coord_rate,
        "countries": len(qualified_countries),
        "conflicts": len(conflicting_ids),
        "era5_semantic_pass": era5_semantic_pass,
        "credential_blocked": credential_blocked,
        "industrial_outcomes_opened": False,
        "site_temperature_magnitudes_opened": False,
        "relationship_computed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
