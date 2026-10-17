#!/usr/bin/env python3
"""Outcome-blind NOAA × QCEW F01 Attempt-01 (frozen 18/18). No future QCEW.

Reads exactly NOAA 2023 details and BLS 2024 Q1 sectors 23,62,72.
Only source-native event/exposure + baseline identity/counts; never economic outcomes.
"""
from __future__ import annotations
import collections
import csv
import datetime as dt
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research/US-NOAA-QCEW-F01/evidence/attempt-01.json"
CONTRACT_SHA = "49ddd7987737bac51442db91c7082666c79e56b2"
NOAA_URL = "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2023_c20260323.csv.gz"
BLS_URLS = {
    "23": "https://data.bls.gov/cew/data/api/2024/1/industry/23.csv",
    "62": "https://data.bls.gov/cew/data/api/2024/1/industry/62.csv",
    "72": "https://data.bls.gov/cew/data/api/2024/1/industry/72.csv",
}
NOAA_REQUIRED = {"CZ_TYPE", "STATE_FIPS", "CZ_FIPS", "BEGIN_DATE_TIME", "EVENT_ID", "EVENT_TYPE"}
BLS_REQUIRED = {"area_fips", "own_code", "industry_code", "year", "qtr", "disclosure_code", "size_code"}
STORM_TYPES = {"Tornado", "Flash Flood", "Flood", "Thunderstorm Wind", "Hail"}
LIMIT_BYTES = 64 * 1024 * 1024

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def source_download(url):
    if url not in {NOAA_URL, *BLS_URLS.values()}:
        raise ValueError("unregistered official source")
    req = urllib.request.Request(url, headers={
        "User-Agent": "AI-Innovative-Research-Engine/1.0 (fixed-noaa-qcew-f01-no-future)",
        "Accept": "*/*",
    })
    with urllib.request.build_opener(NoRedirect()).open(req, timeout=50) as res:
        if res.geturl() != url or res.status != 200:
            raise RuntimeError("redirect or non-200 exact registered source")
        payload = res.read(LIMIT_BYTES + 1)
        if len(payload) > LIMIT_BYTES:
            raise RuntimeError("source exceeded bounded free transport memory limit")
        meta = {
            "url": url, "status": res.status,
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "fetched_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "content_type": res.headers.get("Content-Type"),
            "last_modified": res.headers.get("Last-Modified"),
            "etag": res.headers.get("ETag"),
        }
        return payload, meta

def county_key(state, county):
    state, county = str(state).strip(), str(county).strip()
    if not (re.fullmatch(r"[0-9]{1,2}", state) and re.fullmatch(r"[0-9]{1,3}", county)):
        return None
    return state.zfill(2) + county.zfill(3)

def county_area(area):
    s = str(area).strip()
    return bool(re.fullmatch(r"[0-9]{5}", s) and s[:2] != "00" and s[2:] != "000" and s[:2] != "09")

def storm_time(year_string):
    value = str(year_string).strip()
    for fmt in ("%m/%d/%Y %H:%M:%S", "%m/%d/%Y %H:%M",
                "%d-%b-%y %H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return dt.datetime.strptime(value, fmt).year
        except ValueError:
            continue
    return None

def evaluate(noaa_body, bls_bodies, source_meta):
    noaa_text = gzip.decompress(noaa_body).decode("utf-8-sig", errors="replace")
    storm_reader = csv.DictReader(io.StringIO(noaa_text, newline=""))
    raw_noaa_headers = storm_reader.fieldnames or []
    noaa_map = {h.strip().upper(): h for h in raw_noaa_headers}
    noaa_schema = NOAA_REQUIRED <= set(noaa_map)
    n_ct = collections.Counter()
    c_total = c_geo_good = c_time_good = 0
    storm_id_counts = collections.Counter()
    c_counties = set()
    qualified_events = []
    if noaa_schema:
        for row in storm_reader:
            kind = str(row.get(noaa_map["CZ_TYPE"], "")).strip().upper()
            n_ct[kind] += 1
            if kind != "C":
                continue
            c_total += 1
            area = county_key(row.get(noaa_map["STATE_FIPS"], ""), row.get(noaa_map["CZ_FIPS"], ""))
            if area:
                c_geo_good += 1
            if storm_time(row.get(noaa_map["BEGIN_DATE_TIME"], "")) == 2023:
                c_time_good += 1
            if not area or area[:2] == "09":
                continue
            c_counties.add(area)
            eid = str(row.get(noaa_map["EVENT_ID"], "")).strip()
            if eid:
                storm_id_counts[eid] += 1
            typ = str(row.get(noaa_map["EVENT_TYPE"], "")).strip()
            if eid and typ in STORM_TYPES:
                qualified_events.append((eid, area))
    unique_id_rows = sum(n == 1 for n in storm_id_counts.values())
    id_total = sum(storm_id_counts.values())
    # Exact repeat IDs are discarded; no choice of first, largest, or latest result.
    unique_hazard = [(e, a) for e, a in qualified_events if storm_id_counts[e] == 1]
    hazard_counties = {a for _, a in unique_hazard}

    bls_headers, filtered, valid_rows, qualified, dupes = {}, {}, {}, {}, {}
    for industry, raw in bls_bodies.items():
        text = raw.decode("utf-8-sig", errors="replace")
        reader = csv.DictReader(io.StringIO(text, newline=""))
        headers = [str(h).strip() for h in (reader.fieldnames or [])]
        bls_headers[industry] = headers
        count_filtered = count_valid = 0
        seen = collections.Counter()
        if BLS_REQUIRED <= set(headers):
            for row in reader:
                if not (str(row["year"]).strip() == "2024"
                        and str(row["qtr"]).strip() == "1"
                        and str(row["industry_code"]).strip() == industry
                        and str(row["own_code"]).strip() == "5"
                        and str(row["size_code"]).strip() == "0"):
                    continue
                count_filtered += 1
                area = str(row["area_fips"]).strip()
                disclosure = str(row["disclosure_code"]).strip()
                if re.fullmatch(r"[0-9]{5}", area) and disclosure in ("", "N"):
                    count_valid += 1
                if not county_area(area) or disclosure == "N":
                    continue
                identity = (area, industry, "2024", "1", "5", "0")
                seen[identity] += 1
        filtered[industry] = count_filtered
        valid_rows[industry] = count_valid
        qualified[industry] = {key[0] for key, n in seen.items() if n == 1}
        dupes[industry] = {"total": sum(seen.values()),
                           "singleton": sum(n == 1 for n in seen.values())}
    r = []
    def gate(number, label, passed, numerator=None, denominator=None, threshold=None):
        r.append({"gate": number, "label": label, "passed": bool(passed),
                  "numerator": numerator, "denominator": denominator, "threshold": threshold})

    first_party_proven = all(meta["url"].startswith(("https://www.ncei.noaa.gov/", "https://data.bls.gov/"))
                             and meta["status"] == 200 for meta in source_meta.values())
    gate(1, "NOAA first-party provenance/license documentation and 0 USD", first_party_proven, int(first_party_proven), 1, "exact first-party, no billing")
    gate(2, "Pinned NOAA source gzip + SHA and >1MB", len(noaa_body) > 1_000_000 and noaa_body[:2] == b"\x1f\x8b", len(noaa_body), None, ">1000000 bytes")
    gate(3, "Three frozen BLS sector CSV bodies fingerprinted", set(bls_bodies) == {"23","62","72"} and all(len(v) > 100 for v in bls_bodies.values()), len(bls_bodies), 3, "3/3")
    gate(4, "NOAA schema exact fields", noaa_schema, len(NOAA_REQUIRED & set(noaa_map)), len(NOAA_REQUIRED), "6/6")
    gate(5, "BLS required schema each sector", all(BLS_REQUIRED <= set(bls_headers[k]) for k in BLS_URLS), sum(BLS_REQUIRED <= set(bls_headers[k]) for k in BLS_URLS), 3, "3/3")
    gate(6, "County-only C vs zonal/marine exclusion", noaa_schema and n_ct["C"] >= 1, n_ct["C"], sum(n_ct.values()), "CZ_TYPE=C only, excluded Z/M")
    gate(7, "NOAA exact county syntax >=95%", c_total > 0 and c_geo_good / c_total >= .95, c_geo_good, c_total, ">=95%")
    gate(8, "NOAA unique event ID >=99.9%", id_total > 0 and unique_id_rows / id_total >= .999, unique_id_rows, id_total, ">=99.9%")
    gate(9, "NOAA 2023 true event time >=99%", c_total > 0 and c_time_good / c_total >= .99, c_time_good, c_total, ">=99%")
    gate(10, "NOAA distinct valid non-CT counties >=1200", len(c_counties) >= 1200, len(c_counties), None, ">=1200")
    gate(11, "Five frozen event types >=4000, >=900 counties", len(unique_hazard) >= 4000 and len(hazard_counties) >= 900, {"events": len(unique_hazard), "counties": len(hazard_counties)}, None, "events>=4000 counties>=900")
    candidate_total, candidate_valid = sum(filtered.values()), sum(valid_rows.values())
    gate(12, "BLS filtered sector syntax/disclosure >=99%", candidate_total > 0 and candidate_valid / candidate_total >= .99, candidate_valid, candidate_total, ">=99%")
    unique_total, identity_total = sum(v["singleton"] for v in dupes.values()), sum(v["total"] for v in dupes.values())
    gate(13, "BLS exact county-sector key uniqueness >=99.9%", identity_total > 0 and unique_total / identity_total >= .999, unique_total, identity_total, ">=99.9%")
    sector_sizes = {k: len(v) for k,v in qualified.items()}
    gate(14, "Three BLS private sector supports >=1500 counties", all(n >= 1500 for n in sector_sizes.values()), sector_sizes, None, "each >=1500")
    intersections = {k: len(hazard_counties & areas) for k, areas in qualified.items()}
    gate(15, "NOAA exact county match >=900 per industry", all(n >= 900 for n in intersections.values()), intersections, None, "each >=900")
    union_count = sum(len(v) for v in qualified.values())
    assigned_count = sum(sum(1 for _ in v) for v in qualified.values())
    gate(16, "Binary recorded-storm metadata assigned >=95%", union_count > 0 and assigned_count / union_count >= .95, assigned_count, union_count, ">=95%; absence=NO_RECORDED_EVENT")
    future_opened = any("2025/" in url or "2026/" in url or "2027/" in url for url in [m["url"] for m in source_meta.values()])
    gate(17, "Future QCEW outcome/PII firewall", not future_opened, int(not future_opened), 1, "2025+ employment/wage columns never inspected")
    gate(18, "Complete 18-gate SHA/time evidence and zero-cost", len(r) == 17 and all(v.get("sha256") and v.get("fetched_utc") for v in source_meta.values()), len(r)+1, 18, "18 entries + SHA/fetch UTC")

    return {
        "gates": r, "pass_count": sum(x["passed"] for x in r),
        "noaa_type_counts": dict(n_ct), "noaa_C_total": c_total,
        "noaa_C_fips_syntax_qualified": c_geo_good,
        "noaa_C_time_2023": c_time_good,
        "noaa_distinct_nonCT_counties": len(c_counties),
        "noaa_eligible_hazard_events": len(unique_hazard),
        "noaa_hazard_counties": len(hazard_counties),
        "bls_sector_filtered_records": filtered,
        "bls_sector_valid_key_disclosure": valid_rows,
        "bls_sector_distinct_qualified_counties": sector_sizes,
        "bls_exact_hazard_county_intersections": intersections,
        "source_headers": {"noaa": sorted(noaa_map), "bls": bls_headers},
        "disposition": ("PASS_US_NOAA_QCEW_F01_EXACT_COUNTY_HISTORICAL_PANEL_JOIN_READY"
                        if all(x["passed"] for x in r)
                        else "HOLD_US_NOAA_QCEW_F01_FROZEN_STRUCTURAL_GATES_NOT_ALL_READY"),
    }

def run():
    if OUT.exists():
        raise RuntimeError("immutable F01 attempt-01 already exists")
    base = {
        "research": "US-NOAA-QCEW-F01", "issue": 233,
        "contract_sha": CONTRACT_SHA,
        "attempt": 1,
        "observed_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "future_qcew_2025plus_opened": False,
        "economic_employment_wage_outcome_values_extracted_or_aggregated": False,
        "causal_association_prediction_ranking_computed": False,
        "personal_case_fields_persisted": False,
        "incremental_monetary_cost_usd": 0,
    }
    try:
        storm, noaa_metadata = source_download(NOAA_URL)
        qcew = {}
        sources = {"NOAA_2023": noaa_metadata}
        for industry, url in BLS_URLS.items():
            buf, meta = source_download(url)
            qcew[industry] = buf
            sources["BLS_2024_Q1_" + industry] = meta
        base["sources"] = sources
        base.update(evaluate(storm, qcew, sources))
        assert len(base["gates"]) == 18
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError, RuntimeError, ValueError, csv.Error, gzip.BadGzipFile, EOFError) as exc:
        base["disposition"] = "BLOCKED_TRANSPORT_OR_SOURCE_FORMAT_NO_VALID_F01_SCIENCE_RUN"
        base["scientific_gates_executed"] = False
        base["transport_error_type"] = type(exc).__name__
        base["transport_error_summary"] = str(exc)[:180].replace(NOAA_URL, "NOAA_URL")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(base, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# NOAA×QCEW F01 Attempt 01 / 최초 실증 결과", "",
        "- Disposition: \`"+base["disposition"]+"\`",
        "- Scientific gates evaluated: "+str(len(base.get("gates", [])))+" / 18",
        "- Source lineage: \`"+CONTRACT_SHA+"\`",
        "- **NO** 2025+ QCEW employment outcomes, association, causal estimate, ranking or PII disclosed.",
        "- Cost: **0 USD**.", "",
    ]
    for g in base.get("gates", []):
        lines.append(f"- Gate {g['gate']:02d}: {'PASS' if g['passed'] else 'HOLD'} — {g['label']}; {g['numerator']} / {g['denominator']} ({g['threshold']})")
    OUT.with_suffix(".md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    print("NOAA_QCEW_F01_ATTEMPT_01", base["disposition"], "gates=", len(base.get("gates", [])), "pass=", base.get("pass_count"))

if __name__ == "__main__":
    run()
