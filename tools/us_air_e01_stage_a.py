#!/usr/bin/env python3
"""US-AIR-E01 Stage A: outcome-blind DailyPrecipitation quality/support gate."""

from __future__ import annotations

import csv
import hashlib
import io
import re
import time
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta
from pathlib import Path

YEAR = 2025
MIN_USABLE_DAYS = 330
MIN_MONTH_DAYS = 20
MIN_AIRPORTS = 120
MIN_STATIONS = 120
UA = "AI-Innovative-Research-Engine/US-AIR-E01-stage-a"

ROOT = Path(__file__).resolve().parents[1]
F01 = ROOT / "research" / "US-AIR-F01"
OUT = ROOT / "research" / "US-AIR-E01"

SEQ_MAP = F01 / "DERIVED_AIRPORT_SEQ_STATION_MAP.csv"
FINAL_F01 = F01 / "FINAL_SUPPORT_AIRPORTS.csv"
F01_DATE_SUPPORT = F01 / "DERIVED_NOAA_DATE_SUPPORT.csv"

STATION_MANIFEST = OUT / "STAGE_A_STATION_MANIFEST.csv"
AIRPORT_QUALITY = OUT / "STAGE_A_AIRPORT_QUALITY.csv"
AIRPORT_DATE_WEATHER = OUT / "STAGE_A_AIRPORT_DATE_WEATHER.csv"
RESULT = OUT / "STAGE_A_RESULT.md"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def get(url: str, timeout: int = 180, attempts: int = 3):
    last = None
    for n in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return (
                    response.read(),
                    getattr(response, "status", 200),
                    response.geturl(),
                )
        except Exception as exc:
            last = exc
            if n + 1 < attempts:
                time.sleep(1.5 * (n + 1))
    raise last


def parse_day(text: str):
    value = str(text).strip()
    if not value:
        return None
    for fmt in (
        "%m/%d/%Y %I:%M:%S %p",
        "%m/%d/%Y",
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
    ):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", value)
    if m:
        return datetime.strptime(m.group(1), "%Y-%m-%d").date()
    return None


def year_dates():
    current = date(YEAR, 1, 1)
    stop = date(YEAR + 1, 1, 1)
    values = []
    while current < stop:
        values.append(current)
        current += timedelta(days=1)
    return values


def bool_text(value: str) -> bool:
    return str(value).strip().lower() == "true"


def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_f01_inputs():
    final_rows = read_csv(FINAL_F01)
    final_airports = {
        row["airport_id"]: row
        for row in final_rows
        if bool_text(row.get("final_date_supported", ""))
    }

    seq_rows = [
        row
        for row in read_csv(SEQ_MAP)
        if row.get("airport_id") in final_airports
        and row.get("mapping_status") == "PASS"
        and row.get("noaa_station_id")
    ]

    prior_hashes = {}
    for row in read_csv(F01_DATE_SUPPORT):
        sid = row.get("station_id", "")
        if sid:
            prior_hashes[sid] = row.get("sha256", "")

    return final_airports, seq_rows, prior_hashes


def build_assignments(final_airports, seq_rows):
    by_airport = defaultdict(list)
    for row in seq_rows:
        start = parse_day(row.get("master_start_date", "")) or date(1900, 1, 1)
        thru = parse_day(row.get("master_thru_date", "")) or date(9999, 12, 31)
        by_airport[row["airport_id"]].append(
            {
                "seq_id": row["airport_seq_id"],
                "station_id": row["noaa_station_id"],
                "start": start,
                "thru": thru,
            }
        )

    assignments = {}
    assignment_counts = Counter()
    for aid in sorted(final_airports):
        for day in year_dates():
            candidates = [
                row for row in by_airport.get(aid, [])
                if row["start"] <= day <= row["thru"]
            ]
            if not candidates:
                assignments[(aid, day.isoformat())] = ("", "", "UNASSIGNED")
                assignment_counts["UNASSIGNED"] += 1
                continue
            stations = sorted({row["station_id"] for row in candidates})
            seqids = sorted({row["seq_id"] for row in candidates})
            if len(stations) != 1:
                assignments[(aid, day.isoformat())] = (
                    "|".join(seqids),
                    "|".join(stations),
                    "AMBIGUOUS_STATION",
                )
                assignment_counts["AMBIGUOUS_STATION"] += 1
                continue
            assignments[(aid, day.isoformat())] = (
                "|".join(seqids),
                stations[0],
                "PASS",
            )
            assignment_counts["PASS"] += 1

    return assignments, assignment_counts


def parse_precip_raw(raw: str):
    value = str(raw).strip()
    if value == "":
        return None, False, "MISSING"

    upper = value.upper()
    if "*" in value:
        return None, False, "ERRONEOUS"
    if "S" in upper and upper != "T":
        return None, False, "SUSPECT"
    if upper == "T":
        return 0.0, True, "USABLE_TRACE"

    try:
        numeric = float(value)
    except ValueError:
        return None, False, "UNPARSED"

    if numeric < 0:
        return None, False, "UNPARSED"
    return numeric, False, "USABLE_NUMERIC"


def adjudicate_raw_values(raw_values):
    nonblank = [str(x).strip() for x in raw_values if str(x).strip() != ""]
    if not nonblank:
        return None, False, "MISSING", ""

    parsed = [parse_precip_raw(raw) for raw in nonblank]
    signatures = {(x[0], x[1], x[2]) for x in parsed}
    if len(signatures) != 1:
        return None, False, "AMBIGUOUS_DAILY_VALUE", "|".join(sorted(set(nonblank)))

    numeric, trace, status = parsed[0]
    return numeric, trace, status, "|".join(sorted(set(nonblank)))


def fetch_station(station_id: str, prior_hash: str):
    url = (
        "https://www.ncei.noaa.gov/oa/local-climatological-data/v2/access/"
        f"{YEAR}/LCD_{station_id}_{YEAR}.csv"
    )
    try:
        payload, http, final_url = get(url)
    except Exception as exc:
        return {
            "station_id": station_id,
            "url": url,
            "http": "ERROR",
            "final_url": "",
            "bytes": 0,
            "sha256": "",
            "f01_sha256": prior_hash,
            "same_as_f01_snapshot": False,
            "daily_precipitation_column": False,
            "usable_days": 0,
            "numeric_days": 0,
            "trace_days": 0,
            "missing_days": 365,
            "suspect_days": 0,
            "erroneous_days": 0,
            "ambiguous_days": 0,
            "unparsed_days": 0,
            "error": f"{type(exc).__name__}:{exc}",
            "daily": {d.isoformat(): (None, False, "FETCH_ERROR", "") for d in year_dates()},
        }

    text = io.StringIO(payload.decode("utf-8-sig", errors="replace"))
    reader = csv.DictReader(text)
    has_col = "DailyPrecipitation" in (reader.fieldnames or [])
    by_date = defaultdict(list)

    if has_col:
        for row in reader:
            stamp = str(row.get("DATE", "")).strip()
            m = re.match(r"^(\d{4}-\d{2}-\d{2})", stamp)
            if not m or not m.group(1).startswith(f"{YEAR}-"):
                continue
            by_date[m.group(1)].append(row.get("DailyPrecipitation", ""))

    daily = {}
    counts = Counter()
    for d in year_dates():
        key = d.isoformat()
        if not has_col:
            result = (None, False, "COLUMN_MISSING", "")
        else:
            result = adjudicate_raw_values(by_date.get(key, []))
        daily[key] = result
        counts[result[2]] += 1

    usable = counts["USABLE_NUMERIC"] + counts["USABLE_TRACE"]
    current_hash = sha256(payload)
    return {
        "station_id": station_id,
        "url": url,
        "http": http,
        "final_url": final_url,
        "bytes": len(payload),
        "sha256": current_hash,
        "f01_sha256": prior_hash,
        "same_as_f01_snapshot": bool(prior_hash) and current_hash == prior_hash,
        "daily_precipitation_column": has_col,
        "usable_days": usable,
        "numeric_days": counts["USABLE_NUMERIC"],
        "trace_days": counts["USABLE_TRACE"],
        "missing_days": counts["MISSING"] + counts["COLUMN_MISSING"] + counts["FETCH_ERROR"],
        "suspect_days": counts["SUSPECT"],
        "erroneous_days": counts["ERRONEOUS"],
        "ambiguous_days": counts["AMBIGUOUS_DAILY_VALUE"],
        "unparsed_days": counts["UNPARSED"],
        "error": "",
        "daily": daily,
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    final_airports, seq_rows, prior_hashes = load_f01_inputs()
    assignments, assignment_counts = build_assignments(final_airports, seq_rows)

    station_ids = sorted({
        station_id
        for (_aid, _day), (_seqid, station_id, status) in assignments.items()
        if status == "PASS" and station_id
    })

    station_results = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {
            pool.submit(fetch_station, sid, prior_hashes.get(sid, "")): sid
            for sid in station_ids
        }
        for future in as_completed(futures):
            sid = futures[future]
            station_results[sid] = future.result()

    station_fields = [
        "station_id", "url", "http", "final_url", "bytes", "sha256",
        "f01_sha256", "same_as_f01_snapshot", "daily_precipitation_column",
        "usable_days", "numeric_days", "trace_days", "missing_days",
        "suspect_days", "erroneous_days", "ambiguous_days", "unparsed_days", "error",
    ]
    with STATION_MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=station_fields)
        writer.writeheader()
        for sid in station_ids:
            writer.writerow({k: station_results[sid][k] for k in station_fields})

    airport_day_rows = []
    airport_stats = {}
    for aid in sorted(final_airports):
        monthly = Counter()
        status_counts = Counter()
        stations_used = set()
        usable_days = 0
        assignment_gap_days = 0
        assignment_ambiguous_days = 0
        staged_rows = []

        for day in year_dates():
            day_text = day.isoformat()
            seqid, station_id, assignment_status = assignments[(aid, day_text)]
            precip = None
            trace = False
            weather_status = "NO_ASSIGNMENT"
            raw = ""

            if assignment_status == "PASS":
                stations_used.add(station_id)
                station = station_results.get(station_id)
                if station is not None:
                    precip, trace, weather_status, raw = station["daily"][day_text]
            elif assignment_status == "UNASSIGNED":
                assignment_gap_days += 1
            else:
                assignment_ambiguous_days += 1

            usable = weather_status in {"USABLE_NUMERIC", "USABLE_TRACE"}
            if usable:
                usable_days += 1
                monthly[day.month] += 1
            status_counts[weather_status] += 1

            staged_rows.append({
                "airport_id": aid,
                "origin_codes": final_airports[aid].get("origin_codes", ""),
                "date": day_text,
                "airport_seq_id": seqid,
                "station_id": station_id,
                "assignment_status": assignment_status,
                "daily_precipitation_raw": raw,
                "daily_precipitation_mm": "" if precip is None else f"{precip:.6f}",
                "trace_flag": trace,
                "weather_quality_status": weather_status,
                "usable_primary": usable,
            })

        month_min = min(monthly[m] for m in range(1, 13))
        qualified = (
            usable_days >= MIN_USABLE_DAYS
            and all(monthly[m] >= MIN_MONTH_DAYS for m in range(1, 13))
            and assignment_gap_days == 0
            and assignment_ambiguous_days == 0
        )

        for row in staged_rows:
            row["stage_a_airport_qualified"] = qualified
            airport_day_rows.append(row)

        airport_stats[aid] = {
            "airport_id": aid,
            "origin_codes": final_airports[aid].get("origin_codes", ""),
            "station_ids": "|".join(sorted(stations_used)),
            "unique_station_count": len(stations_used),
            "usable_assigned_days": usable_days,
            "minimum_month_usable_days": month_min,
            "assignment_gap_days": assignment_gap_days,
            "assignment_ambiguous_days": assignment_ambiguous_days,
            "weather_missing_days": status_counts["MISSING"] + status_counts["COLUMN_MISSING"] + status_counts["FETCH_ERROR"],
            "weather_suspect_days": status_counts["SUSPECT"],
            "weather_erroneous_days": status_counts["ERRONEOUS"],
            "weather_ambiguous_days": status_counts["AMBIGUOUS_DAILY_VALUE"],
            "weather_unparsed_days": status_counts["UNPARSED"],
            **{f"usable_m{m:02d}": monthly[m] for m in range(1, 13)},
            "stage_a_qualified": qualified,
        }

    airport_quality_fields = list(next(iter(airport_stats.values())).keys())
    with AIRPORT_QUALITY.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=airport_quality_fields)
        writer.writeheader()
        for aid in sorted(airport_stats):
            writer.writerow(airport_stats[aid])

    airport_day_fields = list(airport_day_rows[0].keys())
    with AIRPORT_DATE_WEATHER.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=airport_day_fields)
        writer.writeheader()
        writer.writerows(airport_day_rows)

    qualified_airports = {
        aid for aid, row in airport_stats.items()
        if row["stage_a_qualified"]
    }
    qualified_stations = {
        row["station_id"]
        for row in airport_day_rows
        if row["airport_id"] in qualified_airports
        and row["usable_primary"]
        and row["station_id"]
    }
    qualified_usable_keys = sum(
        1 for row in airport_day_rows
        if row["airport_id"] in qualified_airports and row["usable_primary"]
    )

    changed_sources = sum(
        not station_results[sid]["same_as_f01_snapshot"] for sid in station_ids
    )
    fetch_errors = sum(bool(station_results[sid]["error"]) for sid in station_ids)
    column_missing = sum(
        not station_results[sid]["daily_precipitation_column"] for sid in station_ids
    )

    gate_pass = (
        len(qualified_airports) >= MIN_AIRPORTS
        and len(qualified_stations) >= MIN_STATIONS
    )
    gate = (
        "PASS_US_AIR_E01_STAGE_A_PRECIPITATION_QUALITY"
        if gate_pass
        else "HOLD_US_AIR_E01_PRECIPITATION_SOURCE_QUALITY"
    )

    result_lines = [
        "---",
        "id: US-AIR-E01-STAGE-A-RESULT",
        "type: outcome-blind-weather-quality-result",
        "created: 2026-09-10",
        "issue: 90",
        f"gate: {gate}",
        "delay_magnitudes_parsed: false",
        "weather_delay_relationship_computed: false",
        "incremental_monetary_cost_usd: 0",
        "---",
        "",
        "# US-AIR-E01 Stage A — DailyPrecipitation Quality",
        "# US-AIR-E01 Stage A — DailyPrecipitation 품질",
        "",
        "## Exposure boundary / 노출 경계",
        "",
        "- Primary variable was frozen before this execution: NOAA LCDv2 DailyPrecipitation.",
        "- This stage parsed the frozen weather variable and quality syntax only.",
        "- No BTS DepDelayMinutes magnitude was loaded or summarized.",
        "- No weather-delay relationship, airport ranking, threshold or lag was computed.",
        "",
        "## Source cohort / source cohort",
        "",
        f"- F01 final airports entering Stage A: **{len(final_airports)}**",
        f"- deterministic station identities required by 2025 assignment: **{len(station_ids)}**",
        f"- source fetch errors: **{fetch_errors}**",
        f"- station files missing DailyPrecipitation column: **{column_missing}**",
        f"- current station-year files whose SHA-256 differs from the F01 DATE-support snapshot: **{changed_sources}/{len(station_ids)}**",
        "",
        "A changed hash is disclosed as source revision/snapshot drift; it is not selected by weather or delay results.",
        "",
        "## Deterministic airport-date assignment / 결정론적 공항-일 배정",
        "",
        f"- PASS assignments: **{assignment_counts['PASS']:,}**",
        f"- unassigned airport-dates: **{assignment_counts['UNASSIGNED']:,}**",
        f"- ambiguous-station airport-dates: **{assignment_counts['AMBIGUOUS_STATION']:,}**",
        "",
        "## Frozen quality gate / 고정 품질 gate",
        "",
        f"Per-airport requirement: >= {MIN_USABLE_DAYS} usable assigned days and >= {MIN_MONTH_DAYS} usable days in every month.",
        "",
        f"- qualified origin airports: **{len(qualified_airports)}**",
        f"- unique NOAA stations represented by qualified usable airport-days: **{len(qualified_stations)}**",
        f"- qualified usable airport-date weather keys: **{qualified_usable_keys:,}**",
        f"- >= {MIN_AIRPORTS} airport threshold: **{len(qualified_airports) >= MIN_AIRPORTS}**",
        f"- >= {MIN_STATIONS} station threshold: **{len(qualified_stations) >= MIN_STATIONS}**",
        "",
        "## Gate / 판정",
        "",
        f"**{gate}**",
        "",
        "If PASS, Stage B may be separately executed under the already frozen outcome/model contract. If HOLD, do not substitute another weather variable inside E01; return to Stage 0.",
        "",
        "## Durable derived artifacts / 영속 파생 산출물",
        "",
        "- research/US-AIR-E01/STAGE_A_STATION_MANIFEST.csv",
        "- research/US-AIR-E01/STAGE_A_AIRPORT_QUALITY.csv",
        "- research/US-AIR-E01/STAGE_A_AIRPORT_DATE_WEATHER.csv",
        "",
        "Raw NOAA station-year CSV files are transient and are not persisted.",
        "",
        "Incremental monetary cost remains **0 USD**.",
    ]
    RESULT.write_text("\n".join(result_lines) + "\n", encoding="utf-8")

    print(
        f"{gate};"
        f"qualified_airports={len(qualified_airports)};"
        f"qualified_stations={len(qualified_stations)};"
        f"qualified_keys={qualified_usable_keys};"
        f"fetch_errors={fetch_errors};"
        f"changed_sources={changed_sources}"
    )


if __name__ == "__main__":
    main()
