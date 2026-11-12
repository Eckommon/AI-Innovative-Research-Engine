#!/usr/bin/env python3
"""Q11 source-native GEOID-only DBF/PRJ meta support with Q10 raw SHA lock.

No .shp/.shx member body is read, no non-GEOID DBF column is interpreted,
and no individual county identifier or raw WKT is persisted.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import struct
from tempfile import TemporaryFile
from urllib.request import Request, build_opener
import zipfile

from tools import qualify_source_census_usda_q10 as q10

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research/SOURCE-REGISTRY-S01/qualifications"
OUT = BASE / "CENSUS-USDA-Q11/evidence/attempt-01.json"
CONTRACT_COMMIT = "a5163a861a23538cd48e3d635acb0fe31be67ecd"
SOURCES = q10.SOURCES.copy()
ORIGINALS = {
    "2023": {"bytes": 83451409,
             "sha256": "692e12c30c83adcaabdbac0d3954fafa55e1c89a24b36d95e72e02dff938652e"},
    "2024": {"bytes": 83913260,
             "sha256": "04e668d3502757c837c13444730547cd967f28a2c49aeffb873d1792ab2cb97b"},
}
MAX_DBF = 2 * 1024 * 1024
MAX_PRJ = 2 * 1024
MIN_KEYS = 3000
MAX_KEYS = 3500
MIN_OVERLAP = 3000
MIN_SHARE = 0.95
MIN_PREFIXES = 50
ISLAND_PREFIXES = ("60", "66", "69", "78")
PASS = "PASS_Q11_TIGER_DBF_GEOID_AND_PRJ_CRS_SUPPORT_ONLY__POLYGON_UNOPENED"
HOLD = "HOLD_Q11_ORIGINAL_SHA_OR_SOURCE"


def verify_context(root=ROOT):
    cp = json.loads((root / "context/checkpoint.json").read_text(encoding="utf-8"))
    if (cp.get("checkpoint_id") != "CHK-20261020-SOURCE-REGISTRY-S01-ACTIVE"
        or cp.get("active_issue") != 244 or cp.get("last_completed_issue") != 203
        or cp.get("last_decision") != "DEC-324"):
        raise RuntimeError("Q11 context mismatch")
    base = root / "research/SOURCE-REGISTRY-S01/qualifications"
    contract = base / "CENSUS-USDA-Q11/CONTRACT.md"
    if not contract.is_file() or "FROZEN_BEFORE_FIRST_Q11_MEMBER_PAYLOAD_READ" not in contract.read_text(encoding="utf-8"):
        raise RuntimeError("Q11 independent contract missing")
    if not (base / "CENSUS-USDA-Q10/RESULT.md").is_file():
        raise RuntimeError("Q10 terminal Result missing")
    q10_evidence = json.loads((base / "CENSUS-USDA-Q10/evidence/attempt-01.json").read_text(encoding="utf-8"))
    if (q10_evidence.get("disposition") != q10.PASS
        or q10_evidence.get("archive_members_decompressed") is not False
        or q10_evidence.get("geographic_boundary_equivalence_verified") is not False
        or q10_evidence.get("science_f01_authorized") is not False
        or q10_evidence.get("github_run_id") != "43135875832"):
        raise RuntimeError("Q10 exact prior D2 source receipt failed")
    for year in ("2023", "2024"):
        prior = (q10_evidence.get("source_receipts") or {}).get(year) or {}
        if (prior.get("official_original_url") != SOURCES[year]
            or prior.get("original_zip_bytes") != ORIGINALS[year]["bytes"]
            or prior.get("original_zip_sha256") != ORIGINALS[year]["sha256"]
            or prior.get("member_count") != 7
            or prior.get("member_payloads_read") is not False
            or len(prior.get("member_inventory_sha256", "")) != 64):
            raise RuntimeError("Q10 source SHA/member expectation changed")
    if (base / "CENSUS-USDA-Q11/evidence/attempt-01.json").exists():
        raise RuntimeError("Q11 original immutable attempt already exists")
    return q10_evidence


def parse_dbf_geoid_only(raw):
    """Parse dBase III headers and one GEOID 5-byte column; no other value extraction."""
    if len(raw) < 33 or raw[0] != 0x03:
        raise ValueError("unsupported DBF version/header")
    count = struct.unpack_from("<I", raw, 4)[0]
    header_bytes, record_bytes = struct.unpack_from("<HH", raw, 8)
    if not MIN_KEYS <= count <= MAX_KEYS:
        raise ValueError("DBF record count out of prospectively frozen bounds")
    if (header_bytes < 65 or record_bytes < 6
        or header_bytes > 8192 or record_bytes > 4096
        or (header_bytes-33) % 32 or len(raw) < header_bytes
        or raw[header_bytes-1] != 0x0D):
        raise ValueError("invalid DBF field descriptor structure")
    field_count = (header_bytes-33)//32
    field_offset = 1  # first byte in record is active/deletion marker
    geoid_field = None
    seen_names = set()
    for i in range(field_count):
        desc = raw[32+i*32:32+(i+1)*32]
        name_bytes = desc[:11].split(b"\x00", 1)[0].strip()
        name = name_bytes.decode("ascii", errors="strict")
        field_type = chr(desc[11])
        width = int(desc[16])
        if not name or name in seen_names or width <= 0:
            raise ValueError("invalid or duplicate DBF descriptor")
        seen_names.add(name)
        if name == "GEOID":
            if field_type != "C" or width != 5 or geoid_field is not None:
                raise ValueError("source-native GEOID not exact five-character field")
            geoid_field = field_offset
        field_offset += width
    if geoid_field is None or field_offset != record_bytes:
        raise ValueError("GEOID field absent or DBF record size mismatch")
    extent = header_bytes + count*record_bytes
    if len(raw) < extent or raw[extent:] not in (b"", b"\x1a"):
        raise ValueError("DBF record body truncated or unexpected trailing bytes")
    ids = set()
    for i in range(count):
        start = header_bytes+i*record_bytes
        if raw[start] != 0x20:
            raise ValueError("deleted or invalid record marker")
        geoid = raw[start+geoid_field:start+geoid_field+5]
        if not re.fullmatch(rb"[0-9]{5}", geoid):
            raise ValueError("invalid 5-digit GEOID")
        if geoid in ids:
            raise ValueError("duplicate GEOID")
        ids.add(geoid)
    return ids, {"declared_record_count": count, "unique_geoid_count": len(ids),
                 "geoid_field_type": "C", "geoid_field_length": 5,
                 "other_dbf_value_columns_interpreted": False}


def prj_receipt(raw):
    if not 1 <= len(raw) <= MAX_PRJ:
        raise ValueError("PRJ original bytes exceed cap")
    wkt = raw.decode("ascii", errors="strict")
    if ("\n" in wkt.strip() or "\r" in wkt.strip()
        or not wkt.startswith("GEOGCS[")
        or "DATUM[" not in wkt or "UNIT[" not in wkt):
        raise ValueError("unsupported PRJ WKT")
    return {"prj_bytes":len(raw),
            "prj_sha256": hashlib.sha256(raw).hexdigest(),
            "prj_wkt_syntax_verified": True,
            "prj_wkt_text_emitted": False}


def fetch_source(year, previous, opener=None):
    if year not in SOURCES:
        raise ValueError("year not frozen")
    url = SOURCES[year]
    expect = ORIGINALS[year]
    client = opener or build_opener(q10.RejectRedirect())
    request = Request(url, method="GET", headers={
        "User-Agent":"S01-Q11-GEOID-PRJ-source-qualification/1.0",
        "Accept-Encoding":"identity",
    })
    with client.open(request, timeout=q10.TIMEOUT) as response:
        if response.status != 200 or response.geturl() != url:
            raise ValueError("Q11 unapproved HTTP/redirect")
        declared = response.headers.get("Content-Length") if response.headers else None
        if declared is not None and (not declared.isdecimal() or int(declared) > q10.LIMIT
                                     or int(declared) != expect["bytes"]):
            raise ValueError("Q11 compressed source size diverged from Q10")
        if response.headers and response.headers.get("Content-Encoding", "identity").lower() != "identity":
            raise ValueError("Q11 response encoding unapproved")
        hasher = hashlib.sha256()
        size = 0
        with TemporaryFile(mode="w+b") as temp:
            while True:
                chunk = response.read(q10.CHUNK)
                if not chunk:
                    break
                size += len(chunk)
                if size > q10.LIMIT or size > expect["bytes"]:
                    raise ValueError("Q11 original compressed source size over limit")
                hasher.update(chunk)
                temp.write(chunk)
            if size != expect["bytes"] or hasher.hexdigest() != expect["sha256"]:
                raise ValueError("Q11 Q10 exact original SHA or bytes mismatch")
            temp.seek(0)
            with zipfile.ZipFile(temp, "r") as zf:
                manifest = q10.check_manifest(year, zf.infolist())
                if manifest["member_inventory_sha256"] != previous["member_inventory_sha256"]:
                    raise ValueError("Q11 exact Q10 archive inventory drift")
                dbf_name = f"tl_{year}_us_county.dbf"
                prj_name = f"tl_{year}_us_county.prj"
                if (zf.getinfo(dbf_name).file_size > MAX_DBF or
                    zf.getinfo(prj_name).file_size > MAX_PRJ):
                    raise ValueError("Q11 permitted member uncompressed-size limit")
                # These TWO members only. No SHP, SHX, XML, CPG member bodies.
                dbf_bytes = zf.read(dbf_name)
                prj_bytes = zf.read(prj_name)
    ids, dbf_stats = parse_dbf_geoid_only(dbf_bytes)
    wkt = prj_receipt(prj_bytes)
    return ({
        "official_original_url":url,
        "http_status":200,
        "original_zip_bytes_verified":size,
        "original_zip_sha256_verified":hasher.hexdigest(),
        "q10_original_source_sha_and_manifest_matched":True,
        "observed_utc":datetime.now(timezone.utc).isoformat(),
        "dbf_projection":dbf_stats,
        "prj":wkt,
        "dbf_non_geoid_columns_parsed":False,
        "shp_shx_or_polygon_payload_read":False,
    }, ids, hashlib.sha256(prj_bytes).hexdigest())


def support_receipt(ids23, ids24):
    n23 = len(ids23)
    n24 = len(ids24)
    overlap = ids23 & ids24
    prefixes23 = {v[:2] for v in ids23}
    prefixes24 = {v[:2] for v in ids24}
    result = {
        "unique_2023_geoid": n23,
        "unique_2024_geoid": n24,
        "distinct_geoid_overlap": len(overlap),
        "only_2023_geoid_count": len(ids23 - ids24),
        "only_2024_geoid_count": len(ids24 - ids23),
        "overlap_share_smaller_vintage": len(overlap)/min(n23,n24) if min(n23,n24) else 0,
        "shared_jurisdiction_prefix_count": len(prefixes23 & prefixes24),
        "island_areas_2023_group_total": sum(x[:2] in ISLAND_PREFIXES for x in ids23),
        "island_areas_2024_group_total": sum(x[:2] in ISLAND_PREFIXES for x in ids24),
        "raw_individual_geoid_emitted": False,
    }
    if not (MIN_KEYS <= n23 <= MAX_KEYS and MIN_KEYS <= n24 <= MAX_KEYS
            and result["distinct_geoid_overlap"] >= MIN_OVERLAP
            and result["overlap_share_smaller_vintage"] >= MIN_SHARE
            and result["shared_jurisdiction_prefix_count"] >= MIN_PREFIXES):
        raise ValueError("source-native GEOID support below prospective thresholds")
    return result


def run(fetch=fetch_source, out=OUT, context=verify_context):
    if out.exists():
        raise RuntimeError("Q11 immutable receipt already exists")
    prior = context()
    result = {
        "qualification": "CENSUS-USDA-Q11", "parent_issue": 244,
        "contract_commit": CONTRACT_COMMIT, "github_run_id": os.getenv("GITHUB_RUN_ID"),
        "observed_utc":datetime.now(timezone.utc).isoformat(),
        "disposition":None, "failure_type":None, "source_receipts":{},
        "aggregate_geoid_support":None, "crs_exact_wkt_sha_equal":False,
        "dbf_non_geoid_columns_parsed":False, "shp_shx_or_polygon_payload_read":False,
        "geographic_boundary_equivalence_verified":False,
        "source_case_rows_emitted":False, "individual_identifiers_emitted":False,
        "future_outcome_values_emitted":False, "science_f01_authorized":False,
        "incremental_monetary_cost_usd":0,
    }
    try:
        receipts = {}
        keys = {}
        crs = {}
        for year in ("2023","2024"):
            safe, keyset, prj_sha = fetch(year, prior["source_receipts"][year])
            receipts[year] = safe
            keys[year] = keyset
            crs[year] = prj_sha
            result["source_receipts"][year] = safe
        result["aggregate_geoid_support"] = support_receipt(keys["2023"], keys["2024"])
        result["crs_exact_wkt_sha_equal"] = crs["2023"] == crs["2024"]
        if not result["crs_exact_wkt_sha_equal"]:
            raise ValueError("two-year PRJ WKT mismatch")
        result["disposition"] = PASS
    except Exception as exc:
        result["disposition"] = HOLD
        result["failure_type"] = type(exc).__name__
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    out.with_suffix(".md").write_text(
        "# Q11 source-native TIGER DBF GEOID + PRJ CRS only / 원본 식별자·좌표계만\n\n"
        f"- Disposition / 판정: {result['disposition']}\n"
        f"- Safe receipts: {json.dumps(result['source_receipts'],sort_keys=True)}\n"
        f"- Aggregate key support: {json.dumps(result['aggregate_geoid_support'],sort_keys=True)}\n"
        f"- Exact two-vintage PRJ WKT byte SHA equal: {result['crs_exact_wkt_sha_equal']}\n"
        f"- Failure class only: {result['failure_type']}\n"
        "- DBF GEOID projection only; no county rows emitted or other value columns parsed.\n"
        "- No SHP/SHX polygon records, geometry equality, USDA rurality or F01. 0 USD.\n",
        encoding="utf-8")
    print("CENSUS_USDA_Q11", result["disposition"], "YEARS", len(result["source_receipts"]),
          "FAILURE_CLASS", result["failure_type"])
    return result


if __name__ == "__main__":
    run()
