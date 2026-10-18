#!/usr/bin/env python3
"""Outcome-sealed Q01 cross-agency original full bytes and source-header verification.

Only source SHA/header are persisted. Never parse or emit case-level values.
"""
from __future__ import annotations
import csv
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "research/SOURCE-REGISTRY-S01/qualifications/FEMA-EPA-Q01"
OUT = DIR / "evidence/source-qualification-01.json"
CONTRACT = "73adb0a35e143d7871b243a64a94aea8132c40ed"
FEMA = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries.csv"
EPA = "https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_county_2024.zip"
SOURCES = {"FEMA_v2_full_CSV": (FEMA, 64 * 1024 * 1024),
           "EPA_2024_county_annual_AQI_ZIP": (EPA, 8 * 1024 * 1024)}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def fetch(url, max_bytes, opener=None):
    if (url, max_bytes) not in SOURCES.values():
        raise ValueError("not a frozen first-party URL and size boundary")
    opener = opener or urllib.request.build_opener(NoRedirect())
    request = urllib.request.Request(url, method="GET", headers={
        "User-Agent": "AI-Innovative-Research-Engine-S01/1.0 (original-bytes-no-row-inspection)",
        "Accept": "*/*",
    })
    with opener.open(request, timeout=55) as response:
        if response.geturl() != url or response.status != 200:
            raise RuntimeError("unexpected redirect or HTTP non-200")
        raw = response.read(max_bytes + 1)
        if len(raw) > max_bytes:
            raise ValueError("bounded full official source size exceeded")
        if not raw:
            raise ValueError("empty source body")
        return raw, {
            "method": "GET", "official_url": url, "http_status": response.status,
            "byte_count": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
            "observed_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "content_type": response.headers.get("Content-Type"),
            "last_modified_transport": response.headers.get("Last-Modified"),
            "etag_transport": response.headers.get("ETag"),
            "publication_timestamp_verified": False,
            "case_or_outcome_rows_parsed": False,
        }

def fema_header(raw):
    # Source dictionary/header only, no body rows, no declaration membership.
    first = raw.split(b"\n", 1)[0]
    if len(first) > 16384:
        raise ValueError("FEMA CSV header too long")
    fields = next(csv.reader([first.decode("utf-8-sig", errors="strict").strip("\r")]))
    present = {"fipsStateCode", "fipsCountyCode"}.issubset(fields)
    return {"field_count": len(fields), "county_fields_documented": present,
            "schema": "fipsStateCode+fipsCountyCode",
            "full_first_header_sha256": hashlib.sha256(first).hexdigest(),
            "parsed_case_rows": 0}

def epa_header(raw):
    if not raw.startswith(b"PK\x03\x04"):
        raise ValueError("Not an EPA ZIP signature")
    with zipfile.ZipFile(io.BytesIO(raw), "r") as archive:
        members = [z for z in archive.infolist() if not z.is_dir()]
        if (len(members) != 1 or not members[0].filename.lower().endswith(".csv")
                or "/" in members[0].filename or "\\" in members[0].filename
                or members[0].flag_bits & 0x1):
            raise ValueError("EPA unambiguous safe CSV member not verified")
        # Explicitly read a single CSV header line from this ZIP member only.
        with archive.open(members[0]) as fp:
            header = fp.readline(16385)
        if len(header) > 16384:
            raise ValueError("EPA CSV header exceeds limit")
    fields = next(csv.reader([header.decode("utf-8-sig", errors="strict").strip("\r\n")]))
    present = {"State Code", "County Code"}.issubset(fields)
    return {"field_count": len(fields), "county_fields_documented": present,
            "schema": "State Code+County Code",
            "full_first_header_sha256": hashlib.sha256(header).hexdigest(),
            "archive_csv_member": members[0].filename,
            "parsed_case_rows": 0}

def classify(report):
    return ("D2_PAIR_READY_KEYS_DOCUMENTED_ONLY" if
            set(report) == set(SOURCES) and
            all(x["http_status"] == 200 and len(x["sha256"]) == 64 and x["byte_count"] > 0
                and x["county_fields_documented"] and x["parsed_case_rows"] == 0
                for x in report.values())
            else "HOLD_SOURCE_ACCESS_OR_SCHEMA")

def run():
    if OUT.exists():
        raise RuntimeError("immutable Q01 original attempt already exists")
    report = {}
    error = None
    for name, (url, limit) in SOURCES.items():
        try:
            raw, meta = fetch(url, limit)
            check = fema_header(raw) if name.startswith("FEMA") else epa_header(raw)
            report[name] = {**meta, **check}
        except Exception as ex:
            # Fail closed, never fallback to mirror, guess other URL or retry.
            error = {"source": name, "type": type(ex).__name__,
                     "reason_category": ("HTTP_UNVERIFIED_NOT_ABSENT" if isinstance(ex, urllib.error.HTTPError)
                                         else "SOURCE_TRANSPORT_OR_SCHEMA_BLOCKED"),
                     "http_status": ex.code if isinstance(ex, urllib.error.HTTPError) else None}
            break
    decision = classify(report) if error is None else "HOLD_SOURCE_ACCESS_OR_SCHEMA"
    result = {
        "research": "SOURCE-QUAL-FEMA-EPA-Q01", "parent_issue": 244,
        "preregistered_contract_commit": CONTRACT,
        "checked_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "sources": report, "unverified_source": error,
        "disposition": decision,
        "source_grading_only": True,
        "key_bridge_state": "DOCUMENTED_ONLY_NEVER_ROW_JOIN_VERIFIED",
        "original_s01_registry_modified": False,
        "first_publication_date_proven": False,
        "source_case_rows_inspected": False, "future_outcome_rows_inspected": False,
        "association_or_event_count_computed": False,
        "third_issue_opened": False, "science_f01_authorized": False,
        "cms_e01_still_reserved": True,
        "incremental_monetary_cost_usd": 0,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    rows = ["# Q01 — FEMA×EPA paired official source qualification / FEMA·EPA 공식 출처",
            "", "- Verdict / 판정: " + decision,
            "- Source key: FEMA fipsStateCode+fipsCountyCode vs EPA State Code+County Code",
            "- Actual exact county join / 실측 조인: **NOT EXECUTED**",
            "- Case/event/AQI data rows / 사건·대기질 값: **NOT OPENED**", "",
            "| Original agency | Official body bytes | Full SHA256 | Exact header semantics |",
            "|---|---:|---|---|"]
    for name, r in report.items():
        rows.append(f"| {name} | {r['byte_count']} | {r['sha256']} | {r['schema']} |")
    if error:
        rows += ["",f"- Unverified source / 미확인: {error['source']}; {error['type']}; HTTP {error['http_status']}"]
    rows += ["", "Never substitute a differently dated source or claim an F01 PASS from D2 original bytes. / 원본 확보는 과학적 인과 또는 F01 승인이 아닙니다.", "", "Incremental monetary cost **0 USD**."]
    (OUT.with_suffix(".md")).write_text("\n".join(rows) + "\n", encoding="utf-8")
    print("FEMA_EPA_Q01", decision, {k:(v["byte_count"],v["county_fields_documented"]) for k,v in report.items()}, "error", error)

if __name__ == "__main__":
    run()
