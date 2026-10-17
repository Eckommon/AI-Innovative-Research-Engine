#!/usr/bin/env python3
"""R58 read-only official source transport + field-layout preflight, NO candidate event rows.

One-time, exact-whitelist, no redirect-follow, no event/body extraction.
"""
from __future__ import annotations
import datetime as dt
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research/PORTFOLIO-R58/evidence/source-endpoint-preflight-01.json"
CONTRACT = "86f2bf09b4fd2c38dbd89608eb80a368a428c7e5"
SOURCES = {
    "NHTSA_campaign_zip": ("https://static.nhtsa.gov/odi/ffdd/rcl/FLAT_RCL_POST_2010.zip", "zip"),
    "NHTSA_quarterly_zip": ("https://static.nhtsa.gov/odi/ffdd/rcl/FLAT_RCL_Qrtly_Rpts.zip", "zip"),
    "NHTSA_campaign_dictionary": ("https://static.nhtsa.gov/odi/ffdd/rcl/RCL.txt", "text_dictionary"),
    "NHTSA_quarterly_dictionary": ("https://static.nhtsa.gov/odi/ffdd/rcl/RCL_Qtrly_Rpts.txt", "text_dictionary"),
    "Census_CBP_2023_county_zip": ("https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip", "zip"),
    "BLS_QCEW_2024_county_csv_header": ("https://data.bls.gov/cew/data/api/2024/1/area/01001.csv", "csv_header"),
    "NOAA_StormEvents_2023_gzip": ("https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2023_c20260323.csv.gz", "gzip"),
}
MAGIC = {"zip": ("504b0304", "504b0506", "504b0708"), "gzip": ("1f8b",)}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def inspect(url, kind, opener=None):
    if (url, kind) not in SOURCES.values():
        raise ValueError("not an exact prospective first-party source and method")
    opener = opener or urllib.request.build_opener(NoRedirect())
    req = urllib.request.Request(url, method="GET", headers={
        "User-Agent": "AI-Innovative-Research-Engine/1.0 (R58-preregistered-metadata-only)",
        "Accept": "*/*",
    })
    r = {
        "url": url, "method": "GET", "kind": kind, "http_status": None,
        "content_type": None, "content_length_header": None,
        "last_modified_header": None, "redirect_location": None,
        "content_prefix_hex": None, "bytes_read": 0, "prefix_format_verified": False,
        "dictionary_prefix_sha256": None, "csv_header": None,
        "outcome_or_case_rows_parsed": False,
        "status": "UNVERIFIED",
    }
    try:
        with opener.open(req, timeout=22) as res:
            r["http_status"] = res.status
            r["content_type"] = res.headers.get("Content-Type")
            r["content_length_header"] = res.headers.get("Content-Length")
            r["last_modified_header"] = res.headers.get("Last-Modified")
            r["redirect_location"] = res.headers.get("Location")
            if res.geturl() != url:
                raise RuntimeError("unexpected redirect in read-only probe")
            if kind in MAGIC:
                n = 4 if kind == "zip" else 2
                prefix = res.read(n)
                r["bytes_read"] = len(prefix)
                r["content_prefix_hex"] = prefix.hex()
                r["prefix_format_verified"] = prefix.hex() in MAGIC[kind]
                r["status"] = ("PREFIX_MATCH_BODY_UNINSPECTED" if r["prefix_format_verified"]
                               else "PREFIX_MISMATCH_NOT_SOURCE_BODY_PROOF")
            elif kind == "text_dictionary":
                buf = res.read(12000)
                r["bytes_read"] = len(buf)
                r["dictionary_prefix_sha256"] = hashlib.sha256(buf).hexdigest()
                # Text is a source field dictionary, NEVER candidate event records.
                r["status"] = ("DICTIONARY_PREFIX_ACCESSED_ONLY" if buf and b"<html" not in buf[:128].lower() and "html" not in (r["content_type"] or "").lower() else "DICTIONARY_FORMAT_NOT_VERIFIED")
            elif kind == "csv_header":
                # Consume only the first CSV header line. Do not touch an outcome record.
                chars = bytearray()
                while len(chars) < 2048:
                    c = res.read(1)
                    if not c or c == b"\n":
                        break
                    chars.extend(c)
                r["bytes_read"] = len(chars) + (1 if c == b"\n" else 0)
                r["csv_header"] = chars.decode("utf-8-sig", errors="replace").strip("\r")
                r["status"] = ("CSV_HEADER_ONLY_ACCESSED" if all(field in r["csv_header"] for field in ("area_fips", "industry_code", "year")) else "CSV_HEADER_FORMAT_NOT_VERIFIED")
    except urllib.error.HTTPError as ex:
        r["http_status"] = ex.code
        r["content_type"] = ex.headers.get("Content-Type")
        r["content_length_header"] = ex.headers.get("Content-Length")
        r["redirect_location"] = ex.headers.get("Location")
        r["status"] = "HTTP_UNVERIFIED_NOT_ABSENCE"
    except (urllib.error.URLError, TimeoutError, OSError) as ex:
        r["status"] = "TRANSPORT_INCONCLUSIVE"
        r["error_type"] = type(ex).__name__
    return r

def assess(results):
    # Metadata-only access is NOT validated row-body access, joins, or F01 authorization.
    ok = {k: v["status"] for k, v in results.items()}
    return {
        "NHTSA": ("METADATA_PREFIX_READY_NO_JOIN_PROOF" if all(
            ok[k] in {"PREFIX_MATCH_BODY_UNINSPECTED", "DICTIONARY_PREFIX_ACCESSED_ONLY"}
            for k in ("NHTSA_campaign_zip", "NHTSA_quarterly_zip",
                      "NHTSA_campaign_dictionary", "NHTSA_quarterly_dictionary"))
                  else "HOLD_TRANSPORT_OR_FORMAT"),
        "CBP_QCEW": ("METADATA_ACCESS_ONLY_NO_JOIN_PROOF" if
                     ok["Census_CBP_2023_county_zip"] == "PREFIX_MATCH_BODY_UNINSPECTED" and
                     ok["BLS_QCEW_2024_county_csv_header"] == "CSV_HEADER_ONLY_ACCESSED"
                     else "HOLD_TRANSPORT_OR_FORMAT"),
        "NOAA_QCEW": ("METADATA_ACCESS_ONLY_NO_JOIN_PROOF" if
                      ok["NOAA_StormEvents_2023_gzip"] == "PREFIX_MATCH_BODY_UNINSPECTED" and
                      ok["BLS_QCEW_2024_county_csv_header"] == "CSV_HEADER_ONLY_ACCESSED"
                      else "HOLD_TRANSPORT_OR_FORMAT"),
    }

def run():
    if OUT.exists():
        raise RuntimeError("R58 initial immutable source endpoint evidence already exists")
    reports = {key: inspect(url, kind) for key, (url, kind) in SOURCES.items()}
    record = {
        "research": "PORTFOLIO-R58", "issue": 226, "frozen_contract_commit": CONTRACT,
        "observed_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "checked_urls": SOURCES,
        "reports": reports, "candidate_conditions": assess(reports),
        "scientific_stage": "PRE_SCORE_TRANSPORT_AND_DICTIONARY_ONLY",
        "candidate_event_rows_opened": False, "future_outcomes_opened": False,
        "row_level_joins_computed": False, "scores_assigned": False,
        "no_f01_authorization": True, "incremental_monetary_cost_usd": 0,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# R58 — official source metadata preflight / 공식 자료 메타데이터 실측", "",
        f"- UTC: \`{record['observed_utc']}\`",
        "- Scientific stage: **PRE-SCORE; NO OUTCOME ROWS OPENED** / 결과행 미개봉",
        "", "| Exact official file | HTTP | Read bytes | Preflight interpretation |",
        "|---|---:|---:|---|",
    ]
    for name, r in reports.items():
        lines.append(f"| \`{name}\` | {r['http_status']} | {r['bytes_read']} | \`{r['status']}\` |")
    lines += ["", "Only ZIP/gzip signatures, published dictionaries and a single CSV header are inspected. This is not a binary full-body download nor a source-native exact join; a 200 response is never scientific evidence of a relationship. / 본문·결과변수·정확조인 미검증.",
              "", "**Candidate access dispositions / 후보별:**"]
    lines += [f"- \`{k}\`: \`{v}\`" for k, v in record["candidate_conditions"].items()]
    lines += ["", "Incremental cost / 추가비용: **0 USD**.", ""]
    OUT.with_suffix(".md").write_text("\n".join(lines), encoding="utf-8")
    print("R58_OFFICIAL_SOURCE_PREFLIGHT", record["candidate_conditions"])
    print("file_statuses", {k: (v["http_status"], v["status"]) for k, v in reports.items()})

if __name__ == "__main__":
    run()
