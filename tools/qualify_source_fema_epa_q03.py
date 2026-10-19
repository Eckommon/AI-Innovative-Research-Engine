#!/usr/bin/env python3
"""Prospectively frozen Q03 structural support only; no FEMA/EPA outcome columns."""
from __future__ import annotations
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
from urllib.request import Request, build_opener, HTTPRedirectHandler
import zipfile

ROOT = Path(__file__).resolve().parents[1]
Q01 = ROOT / "research/SOURCE-REGISTRY-S01/qualifications/FEMA-EPA-Q01"
Q02 = ROOT / "research/SOURCE-REGISTRY-S01/qualifications/FEMA-EPA-Q02"
Q03 = ROOT / "research/SOURCE-REGISTRY-S01/qualifications/FEMA-EPA-Q03"
OUT = Q03 / "evidence/source-structure-01.json"
FEMA_URL = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries.csv"
EPA_URL = "https://aqs.epa.gov/aqsweb/airdata/annual_conc_by_monitor_2024.zip"
EPA_MEMBER = "annual_conc_by_monitor_2024.csv"
SOURCES = {
    FEMA_URL: (64 * 1024 * 1024, "0c51c72b0fd4f616afeb01bb1f7e95f6b7f1349832f7b3be9d12e7dd7e5aaa30"),
    EPA_URL: (16 * 1024 * 1024, "8af92d1ec8ac9271babc84e3512cb2068e6a8849af438448c4170fd9e99ea5bb"),
}
FEMA_FIELDS = ("fipsStateCode", "fipsCountyCode", "incidentBeginDate")
EPA_FIELDS = ("State Code", "County Code", "Site Num", "Parameter Code", "POC",
              "Sample Duration", "Pollutant Standard", "Event Type", "Year")
CONTRACT_COMMIT = "TO_BE_FILLED_FROM_MERGED_Q03_CONTRACT"
MIN_EPA_COUNTIES = 100
MIN_SHARED_COUNTIES = 100
MIN_SHARED_STATES = 15
MIN_EPA_OVERLAP = 0.20

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def locked_fetch(url, opener=None):
    if url not in SOURCES:
        raise ValueError("not an exact frozen source URL")
    limit, expected = SOURCES[url]
    opener = opener or build_opener(NoRedirect())
    req = Request(url, method="GET", headers={
        "User-Agent": "AI-Innovative-Research-Engine-Q03/1.0 (source-key-only)",
        "Accept": "*/*",
    })
    with opener.open(req, timeout=55) as response:
        if response.geturl() != url or response.status != 200:
            raise RuntimeError("redirect/non-200 official source blocked")
        raw = response.read(limit + 1)
        if not raw or len(raw) > limit:
            raise ValueError("source size/empty bound violated")
        observed = hashlib.sha256(raw).hexdigest()
        if observed != expected:
            raise ValueError("HOLD_Q03_SOURCE_VINTAGE_CHANGED")
        return raw, {
            "url": url, "http_status": 200,
            "full_sha256": observed, "byte_count": len(raw),
            "observed_utc": datetime.now(timezone.utc).isoformat(),
            "raw_transport_last_modified": response.headers.get("Last-Modified"),
            "first_publication_date_proven": False,
            "source_blob_matches_frozen_original": True,
        }

def verify_priors():
    old = json.loads((Q01 / "evidence/source-qualification-01.json").read_text())
    new = json.loads((Q02 / "evidence/source-qualification-01.json").read_text())
    assert old["disposition"] == "HOLD_SOURCE_ACCESS_OR_SCHEMA"
    assert old["sources"]["FEMA_v2_full_CSV"]["sha256"] == SOURCES[FEMA_URL][1]
    assert new["disposition"] == "DUAL_D2_SOURCE_HEADERS_ONLY_Q02"
    assert new["epa_separate_monitor_product"]["zip_sha256"] == SOURCES[EPA_URL][1]
    assert new["science_f01_authorized"] is False

def csv_projection(blob, names):
    # This CSV parser necessarily tokenizes each row, but never indexes,
    # derives, saves or reports any non-allowed field value.
    reader = csv.reader(io.StringIO(blob.decode("utf-8-sig", errors="strict"), newline=""))
    header = next(reader)
    if len(header) != len(set(header)) or not set(names).issubset(header):
        raise ValueError("required source-native columns missing/duplicated")
    positions = tuple(header.index(n) for n in names)
    for row in reader:
        if len(row) != len(header):
            raise ValueError("malformed source CSV record")
        yield tuple(row[i] for i in positions)

def key(state, county):
    if (not re.fullmatch(r"[0-9]{2}", state)
        or not re.fullmatch(r"[0-9]{3}", county)
        or state == "00" or county in {"000", "999"}):
        return None
    return state + county

def historical_window(text):
    # No FEMA year 2024+ event attributes inspected.
    if not re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}(?:T|$)", text):
        return False
    try:
        day = datetime.strptime(text[:10], "%Y-%m-%d").date()
    except ValueError:
        return False
    return 2019 <= day.year <= 2023

def fema_keys(raw):
    counties = set()
    rejected = Counter()
    for state, county, incident in csv_projection(raw, FEMA_FIELDS):
        # Only historical baseline exposure location + time fields accessed.
        if not historical_window(incident):
            rejected["outside_historical_window_or_invalid_date"] += 1
            continue
        k = key(state, county)
        if k is None:
            rejected["invalid_or_noncounty_fips_syntax"] += 1
            continue
        counties.add(k)
    return counties, dict(rejected)

def epa_keys(raw):
    if not raw.startswith(b"PK\x03\x04"):
        raise ValueError("EPA original ZIP signature invalid")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        members = [i for i in archive.infolist() if not i.is_dir()]
        if (len(members) != 1 or members[0].filename != EPA_MEMBER
            or members[0].flag_bits & 1
            or members[0].file_size > 256 * 1024 * 1024):
            raise ValueError("EPA exact nonencrypted single CSV member required")
        csvbytes = archive.read(members[0])
    counties = set()
    monitor_ids = set()
    strata_ids = set()
    rejected = Counter()
    valid_summary_rows = 0
    for state, county, site, parameter, poc, duration, standard, events, year in csv_projection(csvbytes, EPA_FIELDS):
        if year != "2024":
            raise ValueError("EPA annual source includes invalid year")
        k = key(state, county)
        if k is None:
            rejected["invalid_or_noncounty_fips_syntax"] += 1
            continue
        if (not site or not parameter or not poc):
            rejected["incomplete_source_monitor_identity"] += 1
            continue
        counties.add(k)
        monitor = (k, site, parameter, poc)
        monitor_ids.add(monitor)
        strata_ids.add((monitor, duration, standard, events))
        valid_summary_rows += 1
    return counties, {
        "distinct_monitors_all_parameters": len(monitor_ids),
        "distinct_monitor_duration_standard_event_signatures": len(strata_ids),
        "valid_summary_record_count_structural_only": valid_summary_rows,
        "monitor_signature_multiplicity": valid_summary_rows - len(monitor_ids),
        "invalid_or_excluded": dict(rejected),
    }

def metrics(fema, epa, epa_detail):
    common = fema & epa
    denom = len(epa)
    support = {
        "fema_historical_2019_2023_distinct_syntax_counties": len(fema),
        "epa_2024_distinct_monitored_syntax_counties": denom,
        "overlap_distinct_syntax_counties": len(common),
        "overlap_share_of_epa_monitored_counties": round(len(common) / denom, 8) if denom else 0.0,
        "epa_monitored_counties_not_in_historical_fema": len(epa - fema),
        "overlap_distinct_states": len({k[:2] for k in common}),
        **epa_detail,
    }
    meets = (
        denom >= MIN_EPA_COUNTIES
        and len(common) >= MIN_SHARED_COUNTIES
        and support["overlap_distinct_states"] >= MIN_SHARED_STATES
        and (len(common) / denom if denom else 0) >= MIN_EPA_OVERLAP
    )
    return support, ("PASS_Q03_SYNTAX_SUPPORT_ONLY__F01_NOT_AUTHORIZED" if meets
                     else "HOLD_Q03_INSUFFICIENT_SOURCE_NATIVE_KEY_SUPPORT")

def run():
    if OUT.exists():
        raise RuntimeError("immutable Q03 already present; forbidden second attempt")
    verify_priors()
    receipts, raws = {}, {}
    error = None
    try:
        # Exactly one GET per source; no re-download/repair even on SHA rotation.
        for url in (FEMA_URL, EPA_URL):
            raw, receipt = locked_fetch(url)
            receipts["FEMA" if url == FEMA_URL else "EPA"] = receipt
            raws[url] = raw
        fema, fema_excluded = fema_keys(raws[FEMA_URL])
        epa, epa_detail = epa_keys(raws[EPA_URL])
        summary, disposition = metrics(fema, epa, epa_detail)
        summary["fema_historical_excluded"] = fema_excluded
    except Exception as exc:
        msg = str(exc)
        disposition = ("HOLD_Q03_SOURCE_VINTAGE_CHANGED" if msg == "HOLD_Q03_SOURCE_VINTAGE_CHANGED"
                       else "HOLD_Q03_SOURCE_ACCESS_OR_SCHEMA")
        error = {"type": type(exc).__name__, "classification": disposition}
        summary = None
    result = {
        "id": "SOURCE-QUAL-FEMA-EPA-Q03-ATTEMPT-01",
        "parent_issue": 244,
        "contract_commit": CONTRACT_COMMIT,
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "transport": receipts,
        "provenance_only": True,
        "frozen_thresholds": {"min_epa_counties": MIN_EPA_COUNTIES,
                              "min_overlap_counties": MIN_SHARED_COUNTIES,
                              "min_overlap_states": MIN_SHARED_STATES,
                              "min_epa_overlap_share": MIN_EPA_OVERLAP},
        "aggregated_source_native_identity_support": summary,
        "disposition": disposition, "operational_error": error,
        "original_q01_held": True, "q02_source_receipt_not_overwritten": True,
        "geography_codebook_or_2024_vintage_verified": False,
        "same_county_semantics_independently_verified": False,
        "epa_pollutant_specific_support_verified": False,
        "epa_monitor_coverage_random": False,
        "county_outcome_aggregation_authorized": False,
        "new_scientific_f01_authorized": False,
        "data_values_used": {"epa_concentrations": False, "epa_aqi": False,
                             "fema_incident_severity_or_counts": False,
                             "future_cms_npi_deactivation": False},
        "no_individual_county_or_site_ids_persisted": True,
        "incremental_monetary_cost_usd": 0,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    brief = [
        "# Q03 source-key preflight / Q03 정부원천 식별자 구조 판정",
        "", f"- Verdict / 판정: `{disposition}`",
        f"- Contract: `{CONTRACT_COMMIT}`",
        f"- Full-byte source SHA and vintage lock valid: `{error is None}`",
        f"- Aggregated key-only support / 식별자 통계: `{json.dumps(summary, sort_keys=True)}`",
        f"- Error category if any: `{error}`", "",
        "FIPS **syntax** overlap only; county codebook/vintage, event-exposure comparability,",
        "parameter-specific EPA coverage and statistical/causal science remain unverified.",
        "고유 군 코드의 형식 연결만 확인하며 지역 연혁·측정소 편향·인과 추론은 미승인.",
        "No county IDs, outcome values or source rows persisted. / 개별 식별자·결과값 미공개.",
        "**F01/E01 not authorized**; **incremental cost 0 USD**.",
    ]
    OUT.with_suffix(".md").write_text("\n".join(brief) + "\n", encoding="utf-8")
    print("FEMA_EPA_Q03", disposition, "OVERLAP", summary["overlap_distinct_syntax_counties"] if summary else None,
          "ERROR", error)

if __name__ == "__main__":
    run()
