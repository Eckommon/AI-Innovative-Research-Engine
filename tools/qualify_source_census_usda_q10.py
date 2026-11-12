#!/usr/bin/env python3
"""Q10 source-only official TIGER ZIP-byte fingerprint and central-directory receipt.

This code NEVER reads/decompresses archive member bodies or polygon/DBF content.
Scientific and geometry access require an independent later preregistration.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat
from tempfile import TemporaryFile
from urllib.request import build_opener, Request, HTTPRedirectHandler
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research/SOURCE-REGISTRY-S01/qualifications"
OUT = BASE / "CENSUS-USDA-Q10/evidence/attempt-01.json"
CONTRACT_COMMIT = "2a9575dbad00c95325f52f437493df9dce5fcef7"
SOURCES = {
    "2023": "https://www2.census.gov/geo/tiger/TIGER2023/COUNTY/tl_2023_us_county.zip",
    "2024": "https://www2.census.gov/geo/tiger/TIGER2024/COUNTY/tl_2024_us_county.zip",
}
LIMIT = 100 * 1024 * 1024
CHUNK = 1024 * 1024
TIMEOUT = 180
MAX_MEMBERS = 32
MAX_MEMBER_SIZE = 1536 * 1024 * 1024
MAX_TOTAL_SIZE = 2 * 1024 * 1024 * 1024
CORE_SUFFIXES = {".shp", ".shx", ".dbf", ".prj"}
OPTIONAL_SUFFIXES = {".cpg", ".shp.xml", ".shp.iso.xml", ".shp.ea.iso.xml"}
ALLOWED_SUFFIXES = CORE_SUFFIXES | OPTIONAL_SUFFIXES
PASS = "PASS_Q10_DUAL_OFFICIAL_TIGER_ZIP_BYTES_AND_MANIFEST_ONLY__GEOMETRY_UNOPENED"
HOLD = "HOLD_Q10_SOURCE_OR_TRANSPORT"


class RejectRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def verify_context(root=ROOT):
    cp = json.loads((root / "context/checkpoint.json").read_text(encoding="utf-8"))
    if (cp.get("checkpoint_id") != "CHK-20261020-SOURCE-REGISTRY-S01-ACTIVE"
        or cp.get("active_issue") != 244
        or cp.get("active_research") != "SOURCE-REGISTRY-S01"
        or cp.get("last_completed_issue") != 203
        or cp.get("last_decision") != "DEC-324"):
        raise RuntimeError("canonical checkpoint changed")
    if not (root / "research/US-CMS-NPI-E01/RESULT.md").is_file():
        raise RuntimeError("original terminal E01 missing")
    if "INCONCLUSIVE_US_CMS_NPI_E01" not in (
        root / "research/US-CMS-NPI-E01/RESULT.md"
    ).read_text(encoding="utf-8"):
        raise RuntimeError("E01 science terminal disposition changed")
    contract = root / "research/SOURCE-REGISTRY-S01/qualifications/CENSUS-USDA-Q10/CONTRACT.md"
    if not contract.is_file() or "FROZEN_BEFORE_Q10_ORIGINAL_ARCHIVE_GET" not in contract.read_text(encoding="utf-8"):
        raise RuntimeError("preregistered source contract missing")
    base = root / "research/SOURCE-REGISTRY-S01/qualifications"
    if not (base / "CENSUS-USDA-Q08/RESULT.md").is_file() or not (base / "CENSUS-USDA-Q09/RESULT.md").is_file():
        raise RuntimeError("Q08/Q09 source-native terminal results missing")
    q09 = json.loads((base / "CENSUS-USDA-Q09/evidence/attempt-01.json").read_text(encoding="utf-8"))
    if (q09.get("disposition") !=
        "PASS_Q09_OFFICIAL_TIGER_2023_2024_COUNTY_ARCHIVES_LISTED__GEOMETRY_UNOPENED"
        or q09.get("archive_bodies_opened") is not False
        or q09.get("science_f01_authorized") is not False):
        raise RuntimeError("Q09 source catalog not independently confirmed")
    for year, url in SOURCES.items():
        entry = (q09.get("source_catalog_receipts") or {}).get(year) or {}
        if (entry.get("official_listing_url") != url.rsplit("/", 1)[0] + "/"
            or entry.get("required_archive_basename") != url.rsplit("/", 1)[1]
            or entry.get("exact_relative_href_count") != 1):
            raise RuntimeError("Q09 exact source URL not preregistered")
    if (base / "CENSUS-USDA-Q10/evidence/attempt-01.json").exists():
        raise RuntimeError("immutable Q10 source attempt already exists")


def check_manifest(year, infos):
    """Validate ZIP central-directory entries only; never call ZipFile.open/read/extract."""
    if year not in SOURCES:
        raise ValueError("year not preselected")
    if not 4 <= len(infos) <= MAX_MEMBERS:
        raise ValueError("unexpected archive member count")
    stem = f"tl_{year}_us_county"
    seen = set()
    required = set()
    manifest = []
    uncompressed_total = 0
    for info in infos:
        name = info.filename
        if (not isinstance(name, str) or not name.isascii() or
            "/" in name or "\\" in name or ".." in name or
            not name.startswith(stem + ".") or name in seen or info.is_dir()):
            raise ValueError("unsafe member path/family/duplicate")
        suffix = name[len(stem):]
        if suffix not in ALLOWED_SUFFIXES:
            raise ValueError("unexpected archive component")
        seen.add(name)
        if suffix in CORE_SUFFIXES:
            required.add(suffix)
        mode = (info.external_attr >> 16) & 0xFFFF
        if stat.S_IFMT(mode) == stat.S_IFLNK or info.flag_bits & 1:
            raise ValueError("symlink or encrypted member forbidden")
        if (info.file_size < 0 or info.compress_size < 0
            or info.file_size > MAX_MEMBER_SIZE or
            (info.file_size and not info.compress_size)):
            raise ValueError("unsafe advertised member size")
        uncompressed_total += info.file_size
        if uncompressed_total > MAX_TOTAL_SIZE:
            raise ValueError("unsafe total archive expansion")
        manifest.append({
            "basename": name,
            "compressed_bytes_advertised": info.compress_size,
            "uncompressed_bytes_advertised": info.file_size,
            "crc32_advertised": f"{info.CRC:08x}",
        })
    if required != CORE_SUFFIXES:
        raise ValueError("required shapefile components missing")
    manifest.sort(key=lambda item: item["basename"])
    packed = json.dumps(manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    return {
        "member_count": len(manifest),
        "member_inventory": manifest,
        "member_inventory_sha256": hashlib.sha256(packed).hexdigest(),
        "total_uncompressed_bytes_advertised": uncompressed_total,
        "member_payloads_decompressed": False,
        "member_payloads_read": False,
    }


def fetch_source(year, opener=None):
    """One bounded first-party GET; full raw SHA before reading ZIP directory."""
    if year not in SOURCES:
        raise ValueError("year not frozen")
    url = SOURCES[year]
    client = opener or build_opener(RejectRedirect())
    req = Request(url, method="GET", headers={
        "User-Agent": "S01-Q10-official-source-evidence/1.0",
        "Accept-Encoding": "identity",
    })
    with client.open(req, timeout=TIMEOUT) as resp:
        if resp.status != 200 or resp.geturl() != url:
            raise ValueError("official URL non-200/redirect")
        declared = resp.headers.get("Content-Length") if resp.headers else None
        if declared is not None:
            if not declared.isdecimal() or int(declared) > LIMIT:
                raise ValueError("Content-Length outside frozen limit")
        if resp.headers and resp.headers.get("Content-Encoding", "identity").lower() != "identity":
            raise ValueError("compressed HTTP transfer encoding unsupported")
        hasher = hashlib.sha256()
        size = 0
        with TemporaryFile(mode="w+b") as tmp:
            while True:
                chunk = resp.read(CHUNK)
                if not chunk:
                    break
                size += len(chunk)
                if size > LIMIT:
                    raise ValueError("actual original source exceeds cap")
                hasher.update(chunk)
                tmp.write(chunk)
            if not size or (declared is not None and size != int(declared)):
                raise ValueError("empty or truncated original source")
            tmp.seek(0)
            if tmp.read(4) != b"PK\x03\x04":
                raise ValueError("not a supported original ZIP")
            tmp.seek(0)
            # ZIP central directory inspection only. NO .open/.read/.extract.
            with zipfile.ZipFile(tmp, mode="r") as zf:
                manifest = check_manifest(year, zf.infolist())
    return {
        "official_original_url": url,
        "http_status": 200,
        "observed_utc": datetime.now(timezone.utc).isoformat(),
        "original_zip_bytes": size,
        "original_zip_sha256": hasher.hexdigest(),
        "original_zip_bytes_sha_verified_before_manifest": True,
        "first_publication_time_verified": False,
        "geometry_read": False,
        **manifest,
    }


def run(fetch=fetch_source, out=OUT, context=verify_context):
    if out.exists():
        raise RuntimeError("Q10 original receipt already exists")
    context()
    result = {
        "qualification": "CENSUS-USDA-Q10",
        "parent_issue": 244,
        "contract_commit": CONTRACT_COMMIT,
        "github_run_id": os.getenv("GITHUB_RUN_ID"),
        "observed_utc": datetime.now(timezone.utc).isoformat(),
        "source_receipts": {},
        "disposition": None,
        "failure_type": None,
        "archive_original_bytes_fetched": False,
        "archive_members_decompressed": False,
        "geographic_boundary_equivalence_verified": False,
        "source_case_rows_emitted": False,
        "individual_identifiers_emitted": False,
        "future_outcome_values_emitted": False,
        "science_f01_authorized": False,
        "incremental_monetary_cost_usd": 0,
    }
    try:
        for year in ("2023", "2024"):
            receipt = fetch(year)
            result["source_receipts"][year] = receipt
            result["archive_original_bytes_fetched"] = True
        result["disposition"] = PASS
    except Exception as exc:
        result["disposition"] = HOLD
        # No source exception messages, names, GEOIDs or arbitrary response data.
        result["failure_type"] = type(exc).__name__
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    report = (
        "# Q10 original TIGER archive byte/manifest-only proof / ZIP 원본·목록 검증\n\n"
        f"- Disposition / 판정: \`{result['disposition']}\`\n"
        f"- First-party receipts (ZIP compressed SHA and central directory only): "
        f"\`{json.dumps(result['source_receipts'], sort_keys=True)}\`\n"
        f"- Safe failure type only: \`{result['failure_type']}\`\n"
        "- No member bodies decompressed; no DBF rows, CRS contents, polygons, rurality "
        "or F01/causality. Independently review actual CI and immutable receipt before terminal grade.\n"
        "- Next: distinct Q11 prospectively frozen member/geometry method. Monetary cost: 0 USD.\n"
    )
    out.with_suffix(".md").write_text(report, encoding="utf-8")
    print("CENSUS_USDA_Q10", result["disposition"],
          "SOURCE_RECEIPTS", len(result["source_receipts"]),
          "FAILURE_CLASS", result["failure_type"])
    return result


if __name__ == "__main__":
    run()
