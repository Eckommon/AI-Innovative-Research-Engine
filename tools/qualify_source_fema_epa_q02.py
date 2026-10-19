#!/usr/bin/env python3
"""Independent Q02: frozen EPA 2024 annual concentration monitor ZIP, header only.

Reuses Q01 FEMA D2 fingerprint but DOES NOT rescue Q01's separate AQI schema HOLD.
No row values, no inferred county support, no research or E01 outcomes.
"""
from __future__ import annotations
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, HTTPRedirectHandler, build_opener
import zipfile

ROOT = Path(__file__).resolve().parents[1]
Q02 = ROOT / "research/SOURCE-REGISTRY-S01/qualifications/FEMA-EPA-Q02"
OUT = Q02 / "evidence/source-qualification-01.json"
Q01 = ROOT / "research/SOURCE-REGISTRY-S01/qualifications/FEMA-EPA-Q01"
EPA_URL = "https://aqs.epa.gov/aqsweb/airdata/annual_conc_by_monitor_2024.zip"
EPA_MEMBER = "annual_conc_by_monitor_2024.csv"
MAX_BYTES = 16 * 1024 * 1024
MAX_HEADER = 16384
REQUIRED = frozenset(("State Code", "County Code", "Site Num", "Parameter Code",
                      "Year", "Pollutant Standard", "Event Type"))
FEMA_SHA = "0c51c72b0fd4f616afeb01bb1f7e95f6b7f1349832f7b3be9d12e7dd7e5aaa30"
CONTRACT_COMMIT = "5afdbf003d5fc423c0bc9fa78b5b4461f4d41f38"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def verify_existing_q01():
    original = (Q01 / "RESULT.md").read_text(encoding="utf-8")
    if "HOLD_SOURCE_ACCESS_OR_SCHEMA" not in original:
        raise RuntimeError("Q01 terminal HOLD must remain unchanged")
    doc = json.loads((Q01 / "evidence/source-qualification-01.json").read_text(encoding="utf-8"))
    if (doc["disposition"] != "HOLD_SOURCE_ACCESS_OR_SCHEMA"
        or doc["sources"]["FEMA_v2_full_CSV"]["sha256"] != FEMA_SHA
        or doc["sources"]["FEMA_v2_full_CSV"]["county_fields_documented"] is not True
        or doc["sources"]["EPA_2024_county_annual_AQI_ZIP"]["county_fields_documented"] is not False):
        raise RuntimeError("Cannot safely reference immutable Q01 FEMA D2 evidence")
    return {"fema_original_sha256": FEMA_SHA,
            "fema_existing_receipt": "FEMA-EPA-Q01/evidence/source-qualification-01.json",
            "fema_source_grain": "declaration with FIPS state/county exceptions",
            "fema_original_q01_holding_preserved": True}


def download(url=EPA_URL, max_bytes=MAX_BYTES, opener=None):
    if url != EPA_URL or max_bytes != MAX_BYTES:
        raise ValueError("Q02 exact URL/size lock prevents alternate product or mirror")
    opener = opener or build_opener(NoRedirect())
    request = Request(url, method="GET", headers={
        "User-Agent": "AI-Innovative-Research-Engine-S01-Q02/1.0 (header-only-inspection)",
        "Accept": "application/zip",
    })
    with opener.open(request, timeout=55) as response:
        if response.geturl() != EPA_URL or response.status != 200:
            raise RuntimeError("redirect/non-200 rejected")
        raw = response.read(max_bytes + 1)
        if not raw or len(raw) > max_bytes:
            raise ValueError("original ZIP empty or exceeds frozen bound")
        return raw, {
            "http_status": 200, "method": "GET", "url": EPA_URL,
            "zip_byte_count": len(raw),
            "zip_sha256": hashlib.sha256(raw).hexdigest(),
            "observed_utc": datetime.now(timezone.utc).isoformat(),
            "content_type": response.headers.get("Content-Type"),
            "last_modified_transport": response.headers.get("Last-Modified"),
            "etag_transport": response.headers.get("ETag"),
            "first_publication_verified": False,
            "case_rows_parsed": False,
        }


def inspect_header_only(raw):
    if not raw.startswith(b"PK\x03\x04"):
        raise ValueError("EPA ZIP magic not verified")
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        entries = [info for info in z.infolist() if not info.is_dir()]
        if (len(entries) != 1 or entries[0].filename != EPA_MEMBER
            or entries[0].flag_bits & 1
            or entries[0].file_size > 256 * 1024 * 1024):
            raise ValueError("invalid unique unencrypted CSV member")
        with z.open(entries[0]) as f:
            header = f.readline(MAX_HEADER + 1)
    if not header or len(header) > MAX_HEADER or not header.endswith(b"\n"):
        raise ValueError("missing or overlong first header")
    fields = next(csv.reader([header.decode("utf-8-sig").rstrip("\r\n")]))
    return {
        "csv_member": EPA_MEMBER,
        "csv_header_sha256": hashlib.sha256(header).hexdigest(),
        "header_field_count": len(fields),
        "required_exact_fields_confirmed": REQUIRED.issubset(fields),
        "missing_required_field_names": sorted(REQUIRED.difference(fields)),
        "actual_case_rows_parsed": 0,
    }


def classify(header):
    if header["required_exact_fields_confirmed"] and header["actual_case_rows_parsed"] == 0:
        return "DUAL_D2_SOURCE_HEADERS_ONLY_Q02"
    return "HOLD_SOURCE_ACCESS_OR_SCHEMA_Q02"


def run():
    if OUT.exists():
        raise RuntimeError("Q02 attempt already committed: refusing repeat")
    fema = verify_existing_q01()  # before ANY new network access
    metadata = {}
    error = None
    try:
        raw, transport = download()
        metadata.update(transport)
        metadata.update(inspect_header_only(raw))
        disposition = classify(metadata)
    except Exception as exc:
        disposition = ("HOLD_SOURCE_TRANSPORT_Q02" if isinstance(exc, HTTPError)
                       else "HOLD_SOURCE_ACCESS_OR_SCHEMA_Q02")
        error = {"type": type(exc).__name__,
                 "http_status": exc.code if isinstance(exc, HTTPError) else None}
    result = {
        "research": "SOURCE-QUAL-FEMA-EPA-Q02",
        "parent_issue": 244,
        "preregistered_contract_commit": CONTRACT_COMMIT,
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "q01_original_disposition_preserved": "HOLD_SOURCE_ACCESS_OR_SCHEMA",
        "fema_existing_d2_reference": fema,
        "epa_separate_monitor_product": metadata,
        "epa_original_zip_fully_fingerprinted": bool(metadata.get("zip_sha256")),
        "epa_source_grain": "MONITOR_X_PARAMETER_X_DURATION_X_STANDARD_X_EVENT_TYPE",
        "source_native_bridge": "COUNTY_FIPS_SCHEMA_ONLY_NO_JOIN_SUPPORT",
        "exact_join_cardinality_verified": False,
        "monitor_to_county_aggregation_authorized": False,
        "temporal_2024_alignment_verified": False,
        "nonrandom_monitor_coverage_handled": False,
        "disposition": disposition,
        "source_outcome_rows_opened": False,
        "future_cms_outcomes_opened": False,
        "science_f01_authorized": False,
        "original_s01_registry_modified": False,
        "incremental_monetary_cost_usd": 0,
        "error": error,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
                   encoding="utf-8")
    md = [
        "# Q02 result — independent FEMA×EPA monitor-source proof / 별도 원천 사전검증",
        "",
        f"- Verdict / 판정: `{disposition}`",
        f"- FEMA reused immutable original SHA: `{FEMA_SHA}`",
        f"- EPA official product: `{EPA_URL}`",
        f"- EPA ZIP bytes / 원본: `{metadata.get('zip_byte_count')}`",
        f"- EPA SHA256: `{metadata.get('zip_sha256')}`",
        f"- EPA HTTP: `{metadata.get('http_status', error['http_status'] if error else None)}`",
        f"- EPA CSV first-header hash: `{metadata.get('csv_header_sha256')}`",
        f"- Required literal EPA fields present: `{metadata.get('required_exact_fields_confirmed')}`",
        f"- Missing fields: `{metadata.get('missing_required_field_names')}`",
        f"- Transport/schema error type: `{error['type'] if error else None}`",
        "",
        "**Q01 remains terminal HOLD; Q02 is monitor-grain, not county-grain and not joined.**",
        "Q01 기존 HOLD 유지. Q02는 측정소 단위 자료로 군 단위 조인을 검증하지 않았습니다.",
        "No case/outcome rows opened, no support/cardinality or science, no F01 approval.",
        "개별 관측값·재난 건수·상관관계·인과·F01 실행 없음.",
        "",
        "Cost / 추가비용: **0 USD**.",
    ]
    OUT.with_suffix(".md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("Q02", disposition, "EPA_HEADER_EXACT", metadata.get("required_exact_fields_confirmed"),
          "BYTES", metadata.get("zip_byte_count"), "ERROR", error)


if __name__ == "__main__":
    run()
