#!/usr/bin/env python3
"""Outcome-blind US-AIR-F01 full-year identity, mapping, and NOAA DATE support."""

from __future__ import annotations

import csv
import hashlib
import html
import http.cookiejar
import io
import math
import re
import time
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path

YEAR = 2025
CAP_KM = 10.0
TIE_KM = 0.001
MIN_AIRPORTS = 50
MIN_STATIONS = 40
UA = "AI-Innovative-Research-Engine/US-AIR-F01 support-runner"
BASE = "https://transtats.bts.gov"
MASTER = (
    "https://transtats.bts.gov/DL_SelectFields.aspx?"
    "QO_fu146_anzr=N8vn6v10+f722146+gnoyr5&gnoyr_VQ=FLL"
)
NOAA_LIST = (
    "https://www.ncei.noaa.gov/oa/local-climatological-data/v2/doc/"
    "lcdv2-station-list.txt"
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-AIR-F01"
SEQ_MAP = OUT / "DERIVED_AIRPORT_SEQ_STATION_MAP.csv"
AIRPORT_SUPPORT = OUT / "DERIVED_AIRPORT_SUPPORT.csv"
DATE_SUPPORT = OUT / "DERIVED_NOAA_DATE_SUPPORT.csv"
FINAL_SUPPORT = OUT / "FINAL_SUPPORT_AIRPORTS.csv"
SUMMARY = OUT / "FULL_YEAR_DATE_SUPPORT.md"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def get(url, timeout=240, attempts=3):
    err = None
    for n in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), getattr(r, "status", 200), dict(r.headers), r.geturl()
        except Exception as exc:
            err = exc
            if n + 1 < attempts:
                time.sleep(1.5 * (n + 1))
    raise err


def norm(value):
    return re.sub(r"[^a-z0-9]+", "", str(value).casefold())


def parse_day(value):
    text = str(value).strip()
    if not text:
        return None
    for fmt in (
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%m/%d/%Y",
        "%m/%d/%Y %H:%M:%S",
        "%m/%d/%Y %I:%M:%S %p",
        "%m/%d/%Y %I:%M %p",
    ):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", text)
    if m:
        try:
            return datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            return None
    return None


def true_flag(value):
    return str(value).strip().upper() in {"1", "1.0", "1.00", "Y", "YES", "TRUE"}


def known_flag(value):
    return str(value).strip().upper() in {
        "", "0", "0.0", "0.00", "N", "NO", "FALSE",
        "1", "1.0", "1.00", "Y", "YES", "TRUE",
    }


def haversine(lat1, lon1, lat2, lon2):
    r = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(min(1.0, math.sqrt(a)))


def expected_dates():
    d = date(YEAR, 1, 1)
    stop = date(YEAR + 1, 1, 1)
    out = []
    while d < stop:
        out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def bts_url(month):
    name = (
        "On_Time_Marketing_Carrier_On_Time_Performance_"
        f"Beginning_January_2018_{YEAR}_{month}.zip"
    )
    return f"{BASE}/PREZIP/{name}"


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "input":
            self.inputs.append(dict(attrs))


def parse_bts():
    seq = {}
    airport_months = defaultdict(set)
    source = {}
    status_vocab = {"Cancelled": Counter(), "Diverted": Counter(), "Duplicate": Counter()}
    total_rows = 0
    date_errors = 0
    header_ref = None
    header_same = True

    fields = [
        "FlightDate", "OriginAirportID", "OriginAirportSeqID", "Origin",
        "Cancelled", "Diverted", "Duplicate", "DepDelayMinutes",
    ]

    for month in range(1, 13):
        payload, http, _, final = get(bts_url(month))
        z = zipfile.ZipFile(io.BytesIO(payload))
        members = [n for n in z.namelist() if n.lower().endswith(".csv") and "readme" not in n.lower()]
        member = max(members, key=lambda n: z.getinfo(n).file_size)
        month_rows = 0
        month_airports, month_seqids = set(), set()

        with z.open(member) as raw:
            reader = csv.reader(io.TextIOWrapper(raw, encoding="utf-8-sig", newline="", errors="replace"))
            header = next(reader)
            hm = {str(x).strip(): i for i, x in enumerate(header)}
            missing = [x for x in fields if x not in hm]
            if missing:
                raise RuntimeError(f"BTS month {month} missing {missing}")
            if header_ref is None:
                header_ref = header
            elif header != header_ref:
                header_same = False
            idx = {x: hm[x] for x in fields}
            mx = max(idx.values())

            for row in reader:
                total_rows += 1
                month_rows += 1
                if len(row) <= mx:
                    continue
                aid = row[idx["OriginAirportID"]].strip()
                sid = row[idx["OriginAirportSeqID"]].strip()
                code = row[idx["Origin"]].strip()
                if not aid or not sid:
                    continue
                day = parse_day(row[idx["FlightDate"]])
                if day is None:
                    date_errors += 1
                key = (aid, sid)
                rec = seq.setdefault(
                    key,
                    {
                        "airport_id": aid,
                        "seq_id": sid,
                        "code": code,
                        "first": None,
                        "last": None,
                        "months": set(),
                        "rows": 0,
                        "cancelled": 0,
                        "diverted": 0,
                        "duplicate": 0,
                        "status_unknown": 0,
                        "delay_nonblank": 0,
                        "delay_blank": 0,
                    },
                )
                if rec["code"] != code:
                    raise RuntimeError(f"Origin code conflict for {aid}/{sid}")
                rec["rows"] += 1
                rec["months"].add(month)
                airport_months[aid].add(month)
                month_airports.add(aid)
                month_seqids.add(sid)
                if day is not None:
                    rec["first"] = day if rec["first"] is None or day < rec["first"] else rec["first"]
                    rec["last"] = day if rec["last"] is None or day > rec["last"] else rec["last"]

                for field in ("Cancelled", "Diverted", "Duplicate"):
                    rawv = row[idx[field]].strip()
                    status_vocab[field][rawv] += 1
                    if not known_flag(rawv):
                        rec["status_unknown"] += 1
                if true_flag(row[idx["Cancelled"]]):
                    rec["cancelled"] += 1
                if true_flag(row[idx["Diverted"]]):
                    rec["diverted"] += 1
                if true_flag(row[idx["Duplicate"]]):
                    rec["duplicate"] += 1
                if row[idx["DepDelayMinutes"]].strip():
                    rec["delay_nonblank"] += 1
                else:
                    rec["delay_blank"] += 1

        source[month] = {
            "url": bts_url(month),
            "http": http,
            "final": final,
            "bytes": len(payload),
            "sha256": sha(payload),
            "member": member,
            "rows": month_rows,
            "airports": len(month_airports),
            "seqids": len(month_seqids),
        }

    diag = {
        "total_rows": total_rows,
        "airports": len(airport_months),
        "all12": sum(len(v) == 12 for v in airport_months.values()),
        "seq_pairs": len(seq),
        "seqids": len({sid for _, sid in seq}),
        "date_errors": date_errors,
        "header_same": header_same,
        "status_vocab": {k: dict(v) for k, v in status_vocab.items()},
        "source": source,
    }
    return seq, airport_months, diag


def materialize_master():
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    req = urllib.request.Request(MASTER, headers={"User-Agent": UA})
    with opener.open(req, timeout=120) as r:
        page = r.read()
        page_http = getattr(r, "status", 200)

    parser = FormParser()
    parser.feed(page.decode("utf-8", errors="replace"))
    hidden, by_name = {}, {}
    for attrs in parser.inputs:
        name = attrs.get("name")
        if not name:
            continue
        by_name[name] = attrs
        if str(attrs.get("type", "")).lower() == "hidden":
            hidden[name] = html.unescape(str(attrs.get("value", "")))

    def fval(name):
        return html.unescape(str(by_name.get(name, {}).get("value", "on"))) or "on"

    body = dict(hidden)
    body.update(
        {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__LASTFOCUS": "",
            "txtSearch": "",
            "btnDownload": "Download",
            "cboGeography": "All",
            "cboYear": "All",
            "cboPeriod": "All",
        }
    )
    wanted = [
        "AIRPORT_SEQ_ID", "AIRPORT_ID", "AIRPORT",
        "AIRPORT_COUNTRY_CODE_ISO", "LATITUDE", "LONGITUDE",
        "UTC_LOCAL_TIME_VARIATION", "AIRPORT_START_DATE", "AIRPORT_THRU_DATE",
        "AIRPORT_IS_CLOSED", "AIRPORT_IS_LATEST",
    ]
    for name in wanted:
        if name in by_name:
            body[name] = fval(name)

    post = urllib.request.Request(
        MASTER,
        data=urllib.parse.urlencode(body).encode(),
        headers={
            "User-Agent": UA,
            "Referer": MASTER,
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    with opener.open(post, timeout=240) as r:
        payload = r.read()
        post_http = getattr(r, "status", 200)
        final = r.geturl()

    if payload[:2] != b"PK":
        text = payload.decode("utf-8", errors="replace")
        links = re.findall(
            r'(?:https?://[^"\x27<>\s]+\.zip|/?ftproot/TranStatsData/[^"\x27<>\s]+\.zip)',
            text,
            re.I,
        )
        if not links:
            raise RuntimeError("Master Coordinate POST produced no ZIP")
        link = html.unescape(links[0])
        if link.startswith("/"):
            link = BASE + link
        elif link.lower().startswith("ftproot/"):
            link = BASE + "/" + link
        payload, post_http, _, final = get(link)

    z = zipfile.ZipFile(io.BytesIO(payload))
    members = [
        n for n in z.namelist()
        if n.lower().endswith(".csv")
        and "documentation" not in n.lower()
        and "readme" not in n.lower()
    ]
    member = max(members, key=lambda n: z.getinfo(n).file_size)
    rows, conflicts, count = {}, 0, 0

    with z.open(member) as raw:
        reader = csv.reader(io.TextIOWrapper(raw, encoding="utf-8-sig", newline="", errors="replace"))
        header = next(reader)
        hm = {norm(x): i for i, x in enumerate(header)}

        def pick(*names):
            for name in names:
                if norm(name) in hm:
                    return hm[norm(name)]
            return None

        cols = {
            "seq": pick("AirportSeqID", "AIRPORT_SEQ_ID"),
            "id": pick("AirportID", "AIRPORT_ID"),
            "code": pick("Airport", "AIRPORT"),
            "lat": pick("Latitude", "LATITUDE"),
            "lon": pick("Longitude", "LONGITUDE"),
            "tz": pick("UTCLocalTimeVariation", "UTC_LOCAL_TIME_VARIATION"),
            "start": pick("AirportStartDate", "AIRPORT_START_DATE"),
            "thru": pick("AirportThruDate", "AIRPORT_THRU_DATE"),
            "country": pick("AirportCountryCodeISO", "AIRPORT_COUNTRY_CODE_ISO"),
        }
        if any(cols[k] is None for k in ("seq", "id", "lat", "lon")):
            raise RuntimeError(f"Master Coordinate required columns missing: {header}")

        for row in reader:
            count += 1

            def val(key):
                i = cols[key]
                return row[i].strip() if i is not None and i < len(row) else ""

            rec = {
                "seq": val("seq"),
                "id": val("id"),
                "code": val("code"),
                "lat": val("lat"),
                "lon": val("lon"),
                "tz": val("tz"),
                "start": val("start"),
                "thru": val("thru"),
                "country": val("country"),
            }
            if not rec["seq"]:
                continue
            if rec["seq"] in rows and rows[rec["seq"]] != rec:
                conflicts += 1
            else:
                rows[rec["seq"]] = rec

    diag = {
        "page_http": page_http,
        "http": post_http,
        "final": final,
        "bytes": len(payload),
        "sha256": sha(payload),
        "member": member,
        "rows": count,
        "seqids": len(rows),
        "conflicts": conflicts,
    }
    return rows, diag


def load_stations():
    payload, http, _, final = get(NOAA_LIST)
    stations = []
    for line in payload.decode("utf-8", errors="replace").splitlines():
        p = line.split(maxsplit=4)
        if len(p) < 5 or not p[0].startswith("US"):
            continue
        try:
            stations.append((p[0], float(p[1]), float(p[2]), p[4]))
        except ValueError:
            pass
    return stations, {
        "http": http,
        "final": final,
        "bytes": len(payload),
        "sha256": sha(payload),
        "stations": len(stations),
    }


def validate_master(obs, master):
    if obs["airport_id"] != master["id"]:
        return False, "AIRPORT_ID_MISMATCH"
    if obs["first"] is None or obs["last"] is None:
        return False, "OBSERVED_DATE_UNPARSED"
    start, thru = parse_day(master["start"]), parse_day(master["thru"])
    if master["start"] and start is None:
        return False, "MASTER_START_UNPARSED"
    if master["thru"] and thru is None:
        return False, "MASTER_THRU_UNPARSED"
    if start is not None and obs["first"] < start:
        return False, "BEFORE_MASTER_START"
    if thru is not None and obs["last"] > thru:
        return False, "AFTER_MASTER_THRU"
    return True, "PASS"


def nearest(lat, lon, stations):
    values = sorted(
        (haversine(lat, lon, slat, slon), sid, name)
        for sid, slat, slon, name in stations
    )
    if len(values) > 1 and abs(values[1][0] - values[0][0]) <= TIE_KM:
        return "", "", values[0][0], "AMBIGUOUS_TIE"
    d, sid, name = values[0]
    if d > CAP_KM:
        return sid, name, d, "OVER_10KM"
    return sid, name, d, "PASS"


def build_mapping(seq, airport_months, masters, stations):
    OUT.mkdir(parents=True, exist_ok=True)
    seq_rows, by_airport = [], defaultdict(list)

    for (aid, sid), obs in sorted(seq.items()):
        master = masters.get(sid)
        status = "NO_MASTER_SEQID"
        valid = False
        station_id = station_name = ""
        distance = ""
        m = {k: "" for k in ("id", "code", "lat", "lon", "tz", "start", "thru")}

        if master is not None:
            m = master
            valid, reason = validate_master(obs, master)
            try:
                lat, lon = float(master["lat"]), float(master["lon"])
            except ValueError:
                status = "INVALID_COORDINATE"
            else:
                station_id, station_name, d, spatial = nearest(lat, lon, stations)
                distance = f"{d:.6f}"
                status = spatial if valid else "TIME_INVALID:" + reason

        row = {
            "airport_id": aid,
            "airport_seq_id": sid,
            "origin_code": obs["code"],
            "first_flight_date": obs["first"].isoformat() if obs["first"] else "",
            "last_flight_date": obs["last"].isoformat() if obs["last"] else "",
            "months_present": "|".join(map(str, sorted(obs["months"]))),
            "identity_rows": obs["rows"],
            "cancelled_rows": obs["cancelled"],
            "diverted_rows": obs["diverted"],
            "duplicate_rows": obs["duplicate"],
            "status_unknown_rows": obs["status_unknown"],
            "dep_delay_nonblank_rows": obs["delay_nonblank"],
            "dep_delay_blank_rows": obs["delay_blank"],
            "master_airport_id": m["id"],
            "master_airport_code": m["code"],
            "master_start_date": m["start"],
            "master_thru_date": m["thru"],
            "master_time_valid": valid,
            "utc_local_time_variation": m["tz"],
            "latitude": m["lat"],
            "longitude": m["lon"],
            "noaa_station_id": station_id,
            "noaa_station_name": station_name,
            "distance_km": distance,
            "mapping_status": status,
        }
        seq_rows.append(row)
        by_airport[aid].append(row)

    with SEQ_MAP.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(seq_rows[0]))
        w.writeheader()
        w.writerows(seq_rows)

    airport_rows, info = [], {}
    for aid in sorted(airport_months):
        records = by_airport[aid]
        codes = sorted({r["origin_code"] for r in records if r["origin_code"]})
        station_ids = sorted({r["noaa_station_id"] for r in records if r["mapping_status"] == "PASS"})
        all12 = len(airport_months[aid]) == 12
        all_seq_pass = bool(records) and all(r["mapping_status"] == "PASS" for r in records)
        spatial = all12 and all_seq_pass
        row = {
            "airport_id": aid,
            "origin_codes": "|".join(codes),
            "months_present": "|".join(map(str, sorted(airport_months[aid]))),
            "all_12_months": all12,
            "observed_seq_count": len(records),
            "all_seq_mapping_pass": all_seq_pass,
            "station_ids": "|".join(station_ids),
            "unique_station_count": len(station_ids),
            "spatial_qualified": spatial,
        }
        airport_rows.append(row)
        info[aid] = row

    with AIRPORT_SUPPORT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(airport_rows[0]))
        w.writeheader()
        w.writerows(airport_rows)

    spatial_airports = [r for r in airport_rows if str(r["spatial_qualified"]) == "True"]
    spatial_stations = {
        sid
        for r in spatial_airports
        for sid in str(r["station_ids"]).split("|")
        if sid
    }
    return info, {
        "seq_rows": len(seq_rows),
        "status_counts": dict(Counter(r["mapping_status"] for r in seq_rows)),
        "all12_airports": sum(str(r["all_12_months"]) == "True" for r in airport_rows),
        "spatial_airports": len(spatial_airports),
        "spatial_stations": len(spatial_stations),
    }


def station_date_support(station_id):
    url = (
        "https://www.ncei.noaa.gov/oa/local-climatological-data/v2/access/"
        f"{YEAR}/LCD_{station_id}_{YEAR}.csv"
    )
    exp = expected_dates()
    try:
        payload, http, _, final = get(url, timeout=180, attempts=3)
    except Exception as exc:
        return {
            "station_id": station_id, "url": url, "http": "ERROR", "final_url": "",
            "bytes": 0, "sha256": "", "header_valid": False, "rows": 0,
            "station_mismatch_rows": 0, "date_parse_error_rows": 0,
            "outside_year_rows": 0, "unique_2025_dates": 0,
            "first_date": "", "last_date": "", "missing_date_count": len(exp),
            "missing_dates": "|".join(exp), "complete_365": False,
            "error": f"{type(exc).__name__}:{exc}",
        }

    lines = payload.decode("utf-8-sig", errors="replace").splitlines()
    header = lines[0].split(",") if lines else []
    header_valid = (
        len(header) >= 2
        and header[0].strip().strip('"') == "STATION"
        and header[1].strip().strip('"') == "DATE"
    )
    dates = set()
    rows = mismatch = parse_errors = outside = 0
    for line in lines[1:]:
        if not line.strip():
            continue
        rows += 1
        p = line.split(",", 2)
        if len(p) < 2:
            parse_errors += 1
            continue
        sid = p[0].strip().strip('"')
        stamp = p[1].strip().strip('"')
        if sid != station_id:
            mismatch += 1
        m = re.match(r"^(\d{4}-\d{2}-\d{2})", stamp)
        if not m:
            parse_errors += 1
            continue
        day = m.group(1)
        if day.startswith(f"{YEAR}-"):
            dates.add(day)
        else:
            outside += 1

    missing = [d for d in exp if d not in dates]
    ordered = sorted(dates)
    complete = (
        header_valid
        and len(dates) == len(exp)
        and not missing
        and mismatch == 0
        and parse_errors == 0
    )
    return {
        "station_id": station_id, "url": url, "http": http, "final_url": final,
        "bytes": len(payload), "sha256": sha(payload), "header_valid": header_valid,
        "rows": rows, "station_mismatch_rows": mismatch,
        "date_parse_error_rows": parse_errors, "outside_year_rows": outside,
        "unique_2025_dates": len(dates), "first_date": ordered[0] if ordered else "",
        "last_date": ordered[-1] if ordered else "",
        "missing_date_count": len(missing), "missing_dates": "|".join(missing),
        "complete_365": complete, "error": "",
    }


def run_dates(airport_info):
    spatial_airports = [r for r in airport_info.values() if str(r["spatial_qualified"]) == "True"]
    station_ids = sorted({
        sid
        for r in spatial_airports
        for sid in str(r["station_ids"]).split("|")
        if sid
    })

    results = {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(station_date_support, sid): sid for sid in station_ids}
        for future in as_completed(futures):
            results[futures[future]] = future.result()

    fields = list(next(iter(results.values()))) if results else []
    with DATE_SUPPORT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for sid in sorted(results):
            w.writerow(results[sid])

    final_rows = []
    for r in sorted(spatial_airports, key=lambda x: str(x["airport_id"])):
        ids = [x for x in str(r["station_ids"]).split("|") if x]
        complete = bool(ids) and all(str(results[x]["complete_365"]) == "True" for x in ids)
        final_rows.append({
            "airport_id": r["airport_id"],
            "origin_codes": r["origin_codes"],
            "observed_seq_count": r["observed_seq_count"],
            "station_ids": r["station_ids"],
            "unique_station_count": r["unique_station_count"],
            "spatial_qualified": r["spatial_qualified"],
            "all_station_dates_complete_365": complete,
            "final_date_supported": complete,
        })

    with FINAL_SUPPORT.open("w", encoding="utf-8", newline="") as f:
        if final_rows:
            w = csv.DictWriter(f, fieldnames=list(final_rows[0]))
            w.writeheader()
            w.writerows(final_rows)

    final_airports = [r for r in final_rows if str(r["final_date_supported"]) == "True"]
    final_stations = {
        sid
        for r in final_airports
        for sid in str(r["station_ids"]).split("|")
        if sid
    }
    return results, {
        "requested_stations": len(station_ids),
        "complete_stations": sum(str(r["complete_365"]) == "True" for r in results.values()),
        "fetch_errors": sum(bool(r["error"]) for r in results.values()),
        "missing_date_stations": sum(int(r["missing_date_count"]) > 0 for r in results.values()),
        "final_airports": len(final_airports),
        "final_stations": len(final_stations),
        "station_day_keys": len(final_stations) * len(expected_dates()),
    }


def write_summary(bts, master, noaa, mapping, dates):
    monthly = []
    for month in range(1, 13):
        r = bts["source"][month]
        monthly.append(
            f"| {month} | {r['bytes']} | {r['sha256']} | {r['rows']} | "
            f"{r['airports']} | {r['seqids']} |"
        )

    structural_pass = (
        mapping["spatial_airports"] >= MIN_AIRPORTS
        and mapping["spatial_stations"] >= MIN_STATIONS
        and dates["final_airports"] >= MIN_AIRPORTS
        and dates["final_stations"] >= MIN_STATIONS
        and master["conflicts"] == 0
        and bts["date_errors"] == 0
    )

    lines = [
        "---",
        "id: US-AIR-F01-FULL-YEAR-DATE-SUPPORT",
        "type: outcome-blind-full-year-support",
        "created: 2026-09-08",
        "issue: 88",
        "frozen_distance_cap_km: 10.0",
        "relationship_outcome_computed: false",
        "weather_values_parsed: false",
        "delay_magnitudes_parsed: false",
        "incremental_monetary_cost_usd: 0",
        "---",
        "",
        "# US-AIR-F01 Full-Year Identity x NOAA DATE Support",
        "# US-AIR-F01 연중 식별자 x NOAA DATE 지원도",
        "",
        "## Exposure boundary / 노출 경계",
        "",
        "- BTS delay magnitudes were not parsed or summarized.",
        "- DepDelayMinutes was inspected only as blank/nonblank structure under the frozen eligibility contract.",
        "- NOAA station-year payloads were inspected only for the STATION and DATE prefixes; weather measurement columns were not interpreted.",
        "- Raw BTS and NOAA payloads were temporary and were not persisted.",
        "",
        "## A. BTS 2025 identity source",
        "",
        "| Month | ZIP bytes | SHA-256 | rows | Origin AirportID | Origin AirportSeqID |",
        "|---:|---:|---|---:|---:|---:|",
        *monthly,
        "",
        f"- total identity rows: **{bts['total_rows']:,}**",
        f"- union Origin AirportIDs: **{bts['airports']}**",
        f"- AirportIDs present in all 12 months: **{bts['all12']}**",
        f"- unique AirportID/SeqID pairs: **{bts['seq_pairs']}**",
        f"- unique Origin AirportSeqIDs: **{bts['seqids']}**",
        f"- monthly header consistency: **{bts['header_same']}**",
        f"- FlightDate parse errors: **{bts['date_errors']}**",
        "",
        "### Structural status vocabulary",
        "",
        f"- Cancelled: {bts['status_vocab']['Cancelled']}",
        f"- Diverted: {bts['status_vocab']['Diverted']}",
        f"- Duplicate: {bts['status_vocab']['Duplicate']}",
        "- Frozen eligibility: exclude Duplicate; exclude Cancelled for continuous DepDelayMinutes; retain non-cancelled Diverted rows when DepDelayMinutes is nonblank.",
        "",
        "## B. Master Coordinate full-year identity",
        "",
        f"- materialized ZIP bytes: **{master['bytes']:,}**",
        f"- SHA-256: {master['sha256']}",
        f"- CSV member: {master['member']}",
        f"- CSV rows: **{master['rows']:,}**",
        f"- distinct AirportSeqIDs: **{master['seqids']:,}**",
        f"- conflicting duplicate AirportSeqIDs: **{master['conflicts']}**",
        "",
        "## C. Frozen 10 km full-year mapping",
        "",
        f"- derived AirportID/SeqID mapping rows: **{mapping['seq_rows']}**",
        f"- all-12-month airports: **{mapping['all12_airports']}**",
        f"- spatial-qualified airports requiring every observed SeqID to pass: **{mapping['spatial_airports']}**",
        f"- unique NOAA stations used by spatial-qualified airports: **{mapping['spatial_stations']}**",
        f"- mapping status counts: {mapping['status_counts']}",
        f"- >=50 airport spatial threshold: **{mapping['spatial_airports'] >= MIN_AIRPORTS}**",
        f"- >=40 station spatial threshold: **{mapping['spatial_stations'] >= MIN_STATIONS}**",
        "",
        "## D. NOAA 2025 DATE-only support",
        "",
        f"- station-year files requested: **{dates['requested_stations']}**",
        f"- stations with complete 365 DATE labels: **{dates['complete_stations']}**",
        f"- fetch errors: **{dates['fetch_errors']}**",
        f"- stations with missing 2025 DATE labels: **{dates['missing_date_stations']}**",
        f"- final date-supported airports: **{dates['final_airports']}**",
        f"- final unique NOAA stations: **{dates['final_stations']}**",
        f"- source-supported station x calendar-date keys: **{dates['station_day_keys']:,}**",
        f"- >=50 airport DATE-support threshold: **{dates['final_airports'] >= MIN_AIRPORTS}**",
        f"- >=40 station DATE-support threshold: **{dates['final_stations'] >= MIN_STATIONS}**",
        "",
        "DATE presence is source support only. It does not prove usable weather-variable completeness, quality, statistical independence, or an effect.",
        "",
        "## E. Reusable derived manifests",
        "",
        "- research/US-AIR-F01/DERIVED_AIRPORT_SEQ_STATION_MAP.csv",
        "- research/US-AIR-F01/DERIVED_AIRPORT_SUPPORT.csv",
        "- research/US-AIR-F01/DERIVED_NOAA_DATE_SUPPORT.csv",
        "- research/US-AIR-F01/FINAL_SUPPORT_AIRPORTS.csv",
        "",
        "No raw BTS ZIP/CSV or NOAA station-year CSV is persisted.",
        "",
        "## Structural/date gate",
        "",
        (
            "**PASS_US_AIR_F01_FULL_YEAR_IDENTITY_DATE_SUPPORT**"
            if structural_pass
            else "**HOLD_US_AIR_F01_FULL_YEAR_IDENTITY_DATE_SUPPORT**"
        ),
        "",
        "This is not the final F01 research gate. Final adjudication must separately resolve NOAA LST DATE-window versus BTS local civil-date semantics.",
        "",
        "Incremental monetary cost remains **0 USD**.",
    ]
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    seq, airport_months, bts = parse_bts()
    masters, master = materialize_master()
    stations, noaa = load_stations()
    airport_info, mapping = build_mapping(seq, airport_months, masters, stations)
    _, dates = run_dates(airport_info)
    write_summary(bts, master, noaa, mapping, dates)
    print(
        "US_AIR_F01_SUPPORT_COMPLETE;"
        f"spatial_airports={mapping['spatial_airports']};"
        f"spatial_stations={mapping['spatial_stations']};"
        f"date_airports={dates['final_airports']};"
        f"date_stations={dates['final_stations']};"
        f"station_days={dates['station_day_keys']}"
    )


if __name__ == "__main__":
    main()
