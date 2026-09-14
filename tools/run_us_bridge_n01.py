#!/usr/bin/env python3
"""US-BRIDGE-N01 outcome-blind matched inspection-interval design runner.

CRITICAL OUTCOME-BLIND BOUNDARY
-------------------------------
NBI legacy condition Items 58/59/60/62 are never sliced, decoded, parsed,
persisted, summarized, ranked, compared, or tested. This runner accesses only
pre-registered identity/design fields: Items 1, 8, 3, 27, 43B, 90, 91, 106.

Raw NBI/FEMA bytes are transient. Durable outputs contain source hashes/counts,
outcome-blind design diagnostics, exact matched-pair identities and a fingerprint.
"""
from __future__ import annotations

import bisect
import hashlib
import html.parser
import json
import os
import re
import sqlite3
import tempfile
import time
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-BRIDGE-N01"
OUT.mkdir(parents=True, exist_ok=True)
TMP = Path(os.environ.get("RUNNER_TEMP", tempfile.gettempdir())) / "us-bridge-n01"
TMP.mkdir(parents=True, exist_ok=True)
DB_PATH = TMP / "design.sqlite3"
UA = "AI-Innovative-Research-Engine/US-BRIDGE-N01 outcome-blind design"
YEARS = list(range(2015, 2026))
FEMA_URL = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
FEMA_START = date(2015, 1, 1)
FEMA_END = date(2024, 12, 31)
MIN_INTERVAL_DAYS = 180
MAX_INTERVAL_DAYS = 1095

PHYSICAL_HAZARDS = {
    "Coastal Storm", "Dam/Levee Break", "Earthquake", "Fire", "Flood",
    "Hurricane", "Mud/Landslide", "Severe Ice Storm", "Severe Storm",
    "Snowstorm", "Straight-Line Winds", "Tornado", "Tropical Storm",
    "Typhoon", "Volcanic Eruption", "Winter Storm",
}
ALLOWED_GATES = {
    "PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE",
    "PARTIAL_US_BRIDGE_N01_INTERVAL_DESIGN_READY_MATCH_SUPPORT_PENDING",
    "HOLD_US_BRIDGE_N01_DESIGN_NOT_IDENTIFIABLE",
}

# One-based FHWA positions documented for the only fields this runner may access.
# CONDITION POSITIONS ARE INTENTIONALLY ABSENT FROM THE INDEXING MAP.
FIELD_POSITIONS = {
    "STATE_CODE_001": [1, 3],
    "STRUCTURE_NUMBER_008": [4, 18],
    "COUNTY_CODE_003": [30, 32],
    "YEAR_BUILT_027": [157, 160],
    "STRUCTURE_TYPE_043B": [203, 204],
    "DATE_OF_INSPECT_090": [287, 290],
    "INSPECTION_FREQ_091": [291, 292],
    "YEAR_RECONSTRUCTED_106": [362, 365],
}
FORBIDDEN_CONDITION_FIELDS = ["DECK_COND_058", "SUPERSTRUCTURE_COND_059", "SUBSTRUCTURE_COND_060", "CULVERT_COND_062"]


def fetch_bytes(url: str, *, tries: int = 5, timeout: int = 180) -> bytes:
    last: Exception | None = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as exc:
            last = exc
            if attempt == tries - 1:
                raise
            time.sleep(2 ** attempt)
    assert last is not None
    raise last


class Anchors(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.items: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self._href is not None:
            self.items.append((self._href, " ".join(self._text).strip()))
            self._href = None
            self._text = []


def anchors(url: str) -> list[tuple[str, str]]:
    body = fetch_bytes(url).decode("utf-8", errors="replace")
    p = Anchors()
    p.feed(body)
    return p.items


def resolve_nbi_zip(year: int) -> tuple[str, str, str]:
    page = f"https://www.fhwa.dot.gov/bridge/nbi/ascii{year}.cfm"
    hits: list[str] = []
    for href, _text in anchors(page):
        low = href.lower()
        if "disclaim.cfm" in low and str(year) in low and "onefilenodel" in low:
            hits.append(href)
    if len(hits) != 1:
        raise RuntimeError(f"{year}: expected one official fixed-width onefilenodel route, got {hits}")
    disclaimer = urllib.parse.urljoin(page, hits[0])
    proceed = [(h, t) for h, t in anchors(disclaimer) if "proceed to data" in t.lower()]
    if len(proceed) != 1:
        raise RuntimeError(f"{year}: expected one Proceed to Data link, got {proceed}")
    return page, disclaimer, urllib.parse.urljoin(disclaimer, proceed[0][0])


def download(url: str, path: Path) -> tuple[int, str]:
    last: Exception | None = None
    for attempt in range(5):
        h = hashlib.sha256()
        total = 0
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=300) as r, open(path, "wb") as f:
                while True:
                    chunk = r.read(1024 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
                    h.update(chunk)
                    total += len(chunk)
            return total, h.hexdigest()
        except Exception as exc:
            last = exc
            try:
                path.unlink()
            except FileNotFoundError:
                pass
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)
    assert last is not None
    raise last


def parse_mm_yy(raw: bytes) -> date | None:
    s = raw.decode("ascii", errors="strict").strip()
    if not re.fullmatch(r"\d{4}", s):
        return None
    mm, yy = int(s[:2]), int(s[2:])
    if not 1 <= mm <= 12:
        return None
    yyyy = 1900 + yy if yy >= 50 else 2000 + yy
    return date(yyyy, mm, 1)


def parse_year_optional(raw: bytes, *, zero_none: bool = True) -> int | None | str:
    s = raw.decode("ascii", errors="strict").strip()
    if not s:
        return None
    if zero_none and s == "0000":
        return None
    if not re.fullmatch(r"\d{4}", s):
        return "INVALID"
    value = int(s)
    if value == 0 and zero_none:
        return None
    if not 1800 <= value <= 2100:
        return "INVALID"
    return value


def parse_freq(raw: bytes) -> int | None:
    s = raw.decode("ascii", errors="strict").strip()
    if not re.fullmatch(r"\d{1,2}", s):
        return None
    v = int(s)
    return v if 0 <= v <= 48 else None


def bridge_class(raw: bytes) -> str | None:
    s = raw.decode("ascii", errors="strict").strip()
    if not re.fullmatch(r"\d{2}", s):
        return None
    return "CULVERT" if s == "19" else "NON_CULVERT"


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        PRAGMA journal_mode=WAL;
        PRAGMA synchronous=NORMAL;
        PRAGMA temp_store=FILE;
        CREATE TABLE inspections (
            bridge_key TEXT NOT NULL,
            state_fips TEXT NOT NULL,
            structure_number TEXT NOT NULL,
            county_fips TEXT,
            inspect_date TEXT NOT NULL,
            inspect_ord INTEGER NOT NULL,
            archive_year INTEGER NOT NULL,
            bridge_class TEXT,
            year_built INTEGER,
            inspection_freq INTEGER,
            recon_year INTEGER,
            recon_invalid INTEGER NOT NULL,
            PRIMARY KEY (bridge_key, inspect_date)
        );
        CREATE INDEX idx_inspections_bridge_date ON inspections(bridge_key, inspect_ord);

        CREATE TABLE exposed_units (
            bridge_key TEXT PRIMARY KEY,
            state_fips TEXT NOT NULL,
            bridge_class TEXT NOT NULL,
            county_fips TEXT NOT NULL,
            pre_date TEXT NOT NULL,
            post_date TEXT NOT NULL,
            pre_ord INTEGER NOT NULL,
            post_ord INTEGER NOT NULL,
            pre_year INTEGER NOT NULL,
            interval_days INTEGER NOT NULL,
            pre_archive_year INTEGER NOT NULL,
            post_archive_year INTEGER NOT NULL,
            pre_year_built INTEGER,
            pre_freq INTEGER,
            post_freq INTEGER,
            event_count INTEGER NOT NULL,
            event_hash TEXT NOT NULL
        );
        CREATE INDEX idx_exposed_stratum ON exposed_units(state_fips, bridge_class, pre_year, pre_ord, bridge_key);

        CREATE TABLE control_intervals (
            bridge_key TEXT NOT NULL,
            state_fips TEXT NOT NULL,
            bridge_class TEXT NOT NULL,
            county_fips TEXT NOT NULL,
            pre_date TEXT NOT NULL,
            post_date TEXT NOT NULL,
            pre_ord INTEGER NOT NULL,
            post_ord INTEGER NOT NULL,
            pre_year INTEGER NOT NULL,
            interval_days INTEGER NOT NULL,
            pre_archive_year INTEGER NOT NULL,
            post_archive_year INTEGER NOT NULL,
            pre_year_built INTEGER,
            pre_freq INTEGER,
            post_freq INTEGER
        );
        CREATE INDEX idx_control_stratum ON control_intervals(state_fips, bridge_class, pre_year, interval_days, pre_ord, bridge_key);
        CREATE INDEX idx_control_bridge ON control_intervals(bridge_key);
        """
    )


def process_nbi_year(conn: sqlite3.Connection, year: int) -> dict:
    page, disclaimer, data_url = resolve_nbi_zip(year)
    zpath = TMP / f"nbi-{year}.zip"
    zip_bytes, zip_sha = download(data_url, zpath)
    if not zipfile.is_zipfile(zpath):
        raise RuntimeError(f"{year}: source is not ZIP")

    # Per-year staging is outcome-blind and permits exact key-year duplicate exclusion.
    year_data: dict[str, tuple] = {}
    duplicate_keys: set[str] = set()
    duplicate_rows = 0
    rows = 0
    parseable_dates = 0
    min_len: int | None = None
    max_len = 0
    member_sha = hashlib.sha256()
    member_bytes = 0

    with zipfile.ZipFile(zpath) as z:
        candidates = [i for i in z.infolist() if not i.is_dir()]
        if not candidates:
            raise RuntimeError(f"{year}: empty ZIP")
        target = max(candidates, key=lambda i: i.file_size)
        with z.open(target) as f:
            for raw_line in f:
                member_sha.update(raw_line)
                member_bytes += len(raw_line)
                line = raw_line.rstrip(b"\r\n")
                if not line:
                    continue
                rows += 1
                L = len(line)
                min_len = L if min_len is None else min(min_len, L)
                max_len = max(max_len, L)
                if L < 365:
                    raise RuntimeError(f"{year}: short legacy record {L}")

                # Authorized slices only. Never access legacy condition byte positions.
                state3 = line[0:3].decode("ascii", errors="strict")
                if not re.fullmatch(r"\d{2}", state3[:2]):
                    raise RuntimeError(f"{year}: invalid State-FIPS prefix {state3!r}")
                sf = state3[:2]
                structure = line[3:18].decode("ascii", errors="replace").strip()
                if not structure:
                    continue
                key = sf + "|" + structure
                county3 = line[29:32].decode("ascii", errors="strict").strip()
                county = sf + county3 if re.fullmatch(r"\d{3}", county3) and county3 != "000" else None
                ybuilt_raw = parse_year_optional(line[156:160])
                ybuilt = ybuilt_raw if isinstance(ybuilt_raw, int) else None
                bclass = bridge_class(line[202:204])
                inspect = parse_mm_yy(line[286:290])
                freq = parse_freq(line[290:292])
                recon_raw = parse_year_optional(line[361:365])
                recon_invalid = int(recon_raw == "INVALID")
                recon = recon_raw if isinstance(recon_raw, int) else None

                if inspect is None:
                    inspect_iso = None
                    inspect_ord = None
                else:
                    inspect_iso = inspect.isoformat()
                    inspect_ord = inspect.toordinal()
                    parseable_dates += 1

                record = (sf, structure, county, inspect_iso, inspect_ord, bclass, ybuilt, freq, recon, recon_invalid)
                if key in year_data:
                    duplicate_rows += 1
                    duplicate_keys.add(key)
                else:
                    year_data[key] = record

    schema_supported = (min_len or 0) >= 365
    if not schema_supported:
        raise RuntimeError(f"{year}: required non-outcome schema unsupported")

    batch = []
    eligible_key_years = 0
    for key, rec in year_data.items():
        if key in duplicate_keys:
            continue
        sf, structure, county, inspect_iso, inspect_ord, bclass, ybuilt, freq, recon, recon_invalid = rec
        if inspect_iso is None or inspect_ord is None:
            continue
        eligible_key_years += 1
        batch.append((key, sf, structure, county, inspect_iso, inspect_ord, year, bclass, ybuilt, freq, recon, recon_invalid))
        if len(batch) >= 20000:
            conn.executemany(
                "INSERT OR IGNORE INTO inspections VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                batch,
            )
            batch.clear()
    if batch:
        conn.executemany("INSERT OR IGNORE INTO inspections VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", batch)
    conn.commit()

    try:
        zpath.unlink()
    except FileNotFoundError:
        pass

    return {
        "year": year,
        "page_url": page,
        "disclaimer_url": disclaimer,
        "resolved_data_url": data_url,
        "zip_bytes": zip_bytes,
        "zip_sha256": zip_sha,
        "member_name": target.filename,
        "member_bytes": member_bytes,
        "member_sha256": member_sha.hexdigest(),
        "rows": rows,
        "unique_bridge_keys": len(year_data),
        "duplicate_rows": duplicate_rows,
        "duplicate_key_years_excluded": len(duplicate_keys),
        "eligible_parseable_key_years": eligible_key_years,
        "parseable_inspection_rows": parseable_dates,
        "min_record_length": min_len,
        "max_record_length": max_len,
        "required_non_outcome_schema_supported": schema_supported,
        "condition_values_accessed": False,
        "condition_row_bytes_sliced": False,
    }


def parse_api_date(value) -> date | None:
    s = str(value or "").strip()
    if not s:
        return None
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def fetch_fema_events() -> tuple[dict[str, list[tuple[int, str, str, str]]], dict]:
    events: dict[str, list[tuple[int, str, str, str]]] = defaultdict(list)
    seen: set[tuple[str, str, str, str]] = set()
    top = 1000
    skip = 0
    pages = 0
    scanned = 0
    qualifying = 0
    hazards = Counter()
    while True:
        qs = urllib.parse.urlencode({"$top": top, "$skip": skip, "$format": "json"})
        data = json.loads(fetch_bytes(FEMA_URL + "?" + qs, timeout=180))
        rows = data.get("DisasterDeclarationsSummaries")
        if rows is None:
            rows = next((v for v in data.values() if isinstance(v, list)), None)
        if rows is None:
            raise RuntimeError(f"FEMA rows unavailable in keys={list(data)}")
        for r in rows:
            scanned += 1
            declaration = str(r.get("declarationType") or r.get("disasterType") or "").strip().upper()
            if declaration != "DR":
                continue
            itype = str(r.get("incidentType") or "").strip()
            if itype not in PHYSICAL_HAZARDS:
                continue
            d = parse_api_date(r.get("incidentBeginDate"))
            if d is None or not (FEMA_START <= d <= FEMA_END):
                continue
            sf = str(r.get("fipsStateCode") or "").strip().zfill(2)
            cf = str(r.get("fipsCountyCode") or "").strip().zfill(3)
            if not re.fullmatch(r"\d{2}", sf) or not re.fullmatch(r"\d{3}", cf) or cf == "000":
                continue
            dn = str(r.get("disasterNumber") or "").strip()
            if not dn:
                continue
            county = sf + cf
            key = (county, dn, d.isoformat(), itype)
            if key in seen:
                continue
            seen.add(key)
            canonical = f"{county}|{dn}|{d.isoformat()}|{itype}"
            events[county].append((d.toordinal(), dn, itype, canonical))
            hazards[itype] += 1
            qualifying += 1
        pages += 1
        if len(rows) < top:
            break
        skip += len(rows)
        if pages > 200:
            raise RuntimeError("unexpected FEMA pagination >200")
    for county in events:
        events[county].sort(key=lambda x: (x[0], x[1], x[2]))
    return events, {
        "api": FEMA_URL,
        "declaration_filter": "DR",
        "incident_window": [FEMA_START.isoformat(), FEMA_END.isoformat()],
        "pages": pages,
        "records_scanned": scanned,
        "qualifying_event_identities": qualifying,
        "qualified_counties": len(events),
        "incident_type_counts": dict(sorted(hazards.items())),
    }


def events_in_interval(events_by_county, county: str, pre_ord: int, post_ord: int):
    rows = events_by_county.get(county, [])
    ords = [x[0] for x in rows]
    lo = bisect.bisect_right(ords, pre_ord)
    hi = bisect.bisect_right(ords, post_ord)
    return rows[lo:hi]


def recon_blocks(pre_recon, pre_invalid, post_recon, post_invalid, pre_year: int, post_year: int) -> bool:
    if pre_invalid or post_invalid:
        return True
    for value in (pre_recon, post_recon):
        if value is not None and pre_year <= value <= post_year:
            return True
    return False


def build_design_units(conn: sqlite3.Connection, events_by_county) -> dict:
    eligible_bridge_count = 0
    exposed_bridge_count = 0
    control_bridge_count = 0
    excluded_unstable_county = 0
    interval_counts = Counter()
    class_counts = Counter()
    cadence_diffs = []

    cur = conn.execute(
        "SELECT bridge_key,state_fips,structure_number,county_fips,inspect_date,inspect_ord,archive_year,bridge_class,year_built,inspection_freq,recon_year,recon_invalid "
        "FROM inspections ORDER BY bridge_key, inspect_ord, archive_year"
    )

    current_key = None
    group = []

    def consume(rows):
        nonlocal eligible_bridge_count, exposed_bridge_count, control_bridge_count, excluded_unstable_county
        if len(rows) < 2:
            return
        counties = {r[3] for r in rows}
        if None in counties or len(counties) != 1:
            excluded_unstable_county += 1
            return
        county = next(iter(counties))
        eligible = []
        for a, b in zip(rows, rows[1:]):
            (
                key, sf, _structure, _county, pre_date, pre_ord, pre_archive, pre_class,
                pre_ybuilt, pre_freq, pre_recon, pre_recon_invalid,
            ) = a
            (
                _key2, _sf2, _structure2, _county2, post_date, post_ord, post_archive, post_class,
                _post_ybuilt, post_freq, post_recon, post_recon_invalid,
            ) = b
            days = post_ord - pre_ord
            if not (MIN_INTERVAL_DAYS <= days <= MAX_INTERVAL_DAYS):
                interval_counts["outside_day_window"] += 1
                continue
            if pre_class is None or post_class is None or pre_class != post_class:
                interval_counts["class_missing_or_drift"] += 1
                continue
            py = int(pre_date[:4]); qy = int(post_date[:4])
            if recon_blocks(pre_recon, pre_recon_invalid, post_recon, post_recon_invalid, py, qy):
                interval_counts["reconstruction_or_invalid_excluded"] += 1
                continue
            event_rows = events_in_interval(events_by_county, county, pre_ord, post_ord)
            event_hash = hashlib.sha256("\n".join(x[3] for x in event_rows).encode("utf-8")).hexdigest()
            if pre_freq is not None:
                cadence_diffs.append(abs(days - pre_freq * 30.4375))
            eligible.append({
                "bridge_key": key, "state_fips": sf, "bridge_class": pre_class, "county_fips": county,
                "pre_date": pre_date, "post_date": post_date, "pre_ord": pre_ord, "post_ord": post_ord,
                "pre_year": py, "interval_days": days, "pre_archive_year": pre_archive,
                "post_archive_year": post_archive, "pre_year_built": pre_ybuilt,
                "pre_freq": pre_freq, "post_freq": post_freq,
                "event_count": len(event_rows), "event_hash": event_hash,
            })
            interval_counts["eligible"] += 1
            class_counts[pre_class] += 1
        if not eligible:
            return
        eligible_bridge_count += 1
        exposed = [x for x in eligible if x["event_count"] > 0]
        if exposed:
            exposed_bridge_count += 1
            chosen = min(exposed, key=lambda x: (x["pre_date"], x["post_date"]))
            conn.execute(
                "INSERT INTO exposed_units VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    chosen["bridge_key"], chosen["state_fips"], chosen["bridge_class"], chosen["county_fips"],
                    chosen["pre_date"], chosen["post_date"], chosen["pre_ord"], chosen["post_ord"], chosen["pre_year"],
                    chosen["interval_days"], chosen["pre_archive_year"], chosen["post_archive_year"],
                    chosen["pre_year_built"], chosen["pre_freq"], chosen["post_freq"], chosen["event_count"], chosen["event_hash"],
                ),
            )
        else:
            control_bridge_count += 1
            conn.executemany(
                "INSERT INTO control_intervals VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                [(
                    x["bridge_key"], x["state_fips"], x["bridge_class"], x["county_fips"],
                    x["pre_date"], x["post_date"], x["pre_ord"], x["post_ord"], x["pre_year"], x["interval_days"],
                    x["pre_archive_year"], x["post_archive_year"], x["pre_year_built"], x["pre_freq"], x["post_freq"],
                ) for x in eligible],
            )

    for row in cur:
        if current_key is None:
            current_key = row[0]
        if row[0] != current_key:
            consume(group)
            group = []
            current_key = row[0]
        group.append(row)
    if group:
        consume(group)
    conn.commit()

    return {
        "unique_bridges_with_eligible_interval": eligible_bridge_count,
        "unique_exposed_bridges": exposed_bridge_count,
        "unique_control_candidate_bridges": control_bridge_count,
        "bridges_excluded_unstable_or_invalid_county": excluded_unstable_county,
        "interval_diagnostics": dict(sorted(interval_counts.items())),
        "eligible_interval_class_counts": dict(sorted(class_counts.items())),
        "inspection_frequency_absolute_day_deviation_mean": (sum(cadence_diffs) / len(cadence_diffs)) if cadence_diffs else None,
        "inspection_frequency_diagnostic_n": len(cadence_diffs),
    }


def nearest_unused(bucket, target_ord: int, used: set[str]):
    """Exact nearest pre-date within a fixed interval-length bucket.

    bucket is sorted by (pre_ord, bridge_key, post_date, payload...).
    Returns candidate and pre-date difference, respecting global used-control set.
    """
    if not bucket:
        return None
    probe = (target_ord, "", "")
    i = bisect.bisect_left(bucket, probe)
    left, right = i - 1, i
    best = None
    best_diff = None
    while left >= 0 or right < len(bucket):
        ld = abs(bucket[left][0] - target_ord) if left >= 0 else 10**9
        rd = abs(bucket[right][0] - target_ord) if right < len(bucket) else 10**9
        d = min(ld, rd)
        if best_diff is not None and d > best_diff:
            break
        if left >= 0 and ld == d:
            c = bucket[left]
            if c[1] not in used:
                rank = (d, c[1], c[2])
                if best is None or rank < best[0]:
                    best = (rank, c)
                    best_diff = d
            left -= 1
        if right < len(bucket) and rd == d:
            c = bucket[right]
            if c[1] not in used:
                rank = (d, c[1], c[2])
                if best is None or rank < best[0]:
                    best = (rank, c)
                    best_diff = d
            right += 1
    if best is None:
        return None
    return best[1], best[0][0]


def match_pairs(conn: sqlite3.Connection, pair_path: Path) -> dict:
    used_controls: set[str] = set()
    pair_count = 0
    class_counts = Counter()
    state_counts = Counter()
    within_365 = 0
    unmatched_exposed = 0
    fingerprint = hashlib.sha256()

    strata = conn.execute(
        "SELECT DISTINCT state_fips,bridge_class,pre_year FROM exposed_units ORDER BY state_fips,bridge_class,pre_year"
    ).fetchall()

    with open(pair_path, "w", encoding="utf-8", newline="\n") as out:
        for sf, bclass, pre_year in strata:
            controls = conn.execute(
                "SELECT pre_ord,bridge_key,post_date,pre_date,post_ord,interval_days,county_fips,pre_archive_year,post_archive_year,pre_year_built,pre_freq,post_freq "
                "FROM control_intervals WHERE state_fips=? AND bridge_class=? AND pre_year=?",
                (sf, bclass, pre_year),
            ).fetchall()
            buckets: dict[int, list[tuple]] = defaultdict(list)
            for row in controls:
                pre_ord, bridge_key, post_date, *rest = row
                interval_days = row[5]
                # tuple prefix exactly supports bisect and contract tie-breaks.
                buckets[interval_days].append((pre_ord, bridge_key, post_date, row))
            for length in buckets:
                buckets[length].sort(key=lambda x: (x[0], x[1], x[2]))

            exposures = conn.execute(
                "SELECT bridge_key,county_fips,pre_date,post_date,pre_ord,post_ord,interval_days,pre_archive_year,post_archive_year,pre_year_built,pre_freq,post_freq,event_count,event_hash "
                "FROM exposed_units WHERE state_fips=? AND bridge_class=? AND pre_year=? ORDER BY pre_ord,bridge_key,post_date",
                (sf, bclass, pre_year),
            ).fetchall()

            for exp in exposures:
                (
                    exp_key, exp_county, exp_pre, exp_post, exp_pre_ord, exp_post_ord, exp_days,
                    exp_pre_archive, exp_post_archive, exp_ybuilt, exp_pre_freq, exp_post_freq,
                    event_count, event_hash,
                ) = exp
                chosen = None
                chosen_rank = None
                max_d = max(exp_days - MIN_INTERVAL_DAYS, MAX_INTERVAL_DAYS - exp_days)
                for d in range(max_d + 1):
                    lengths = []
                    if MIN_INTERVAL_DAYS <= exp_days - d <= MAX_INTERVAL_DAYS:
                        lengths.append(exp_days - d)
                    if d and MIN_INTERVAL_DAYS <= exp_days + d <= MAX_INTERVAL_DAYS:
                        lengths.append(exp_days + d)
                    candidates = []
                    for length in lengths:
                        found = nearest_unused(buckets.get(length, []), exp_pre_ord, used_controls)
                        if found is None:
                            continue
                        candidate, pre_diff = found
                        # contract rank: interval diff, pre-date diff, bridge key, post date
                        candidates.append(((d, pre_diff, candidate[1], candidate[2]), candidate))
                    if candidates:
                        chosen_rank, chosen = min(candidates, key=lambda x: x[0])
                        break
                if chosen is None:
                    unmatched_exposed += 1
                    continue

                _ctl_pre_ord_prefix, ctl_key, ctl_post_prefix, ctl_row = chosen
                (
                    ctl_pre_ord, _ctl_key2, ctl_post, ctl_pre, ctl_post_ord, ctl_days, ctl_county,
                    ctl_pre_archive, ctl_post_archive, ctl_ybuilt, ctl_pre_freq, ctl_post_freq,
                ) = ctl_row
                used_controls.add(ctl_key)
                pair_count += 1
                class_counts[bclass] += 1
                state_counts[sf] += 1
                interval_diff = abs(exp_days - ctl_days)
                if interval_diff <= 365:
                    within_365 += 1

                pair = {
                    "i": pair_count,
                    "state": sf,
                    "class": bclass,
                    "pre_year": pre_year,
                    "exp_bridge": exp_key,
                    "exp_county": exp_county,
                    "exp_pre": exp_pre,
                    "exp_post": exp_post,
                    "exp_days": exp_days,
                    "exp_pre_archive": exp_pre_archive,
                    "exp_post_archive": exp_post_archive,
                    "exp_year_built": exp_ybuilt,
                    "exp_pre_freq": exp_pre_freq,
                    "exp_post_freq": exp_post_freq,
                    "exp_event_count": event_count,
                    "exp_event_hash": event_hash,
                    "ctl_bridge": ctl_key,
                    "ctl_county": ctl_county,
                    "ctl_pre": ctl_pre,
                    "ctl_post": ctl_post,
                    "ctl_days": ctl_days,
                    "ctl_pre_archive": ctl_pre_archive,
                    "ctl_post_archive": ctl_post_archive,
                    "ctl_year_built": ctl_ybuilt,
                    "ctl_pre_freq": ctl_pre_freq,
                    "ctl_post_freq": ctl_post_freq,
                    "interval_day_diff": interval_diff,
                }
                line = json.dumps(pair, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
                out.write(line + "\n")
                fingerprint.update(line.encode("utf-8") + b"\n")

    return {
        "matched_pairs": pair_count,
        "matched_state_fips_count": len(state_counts),
        "matched_state_counts": dict(sorted(state_counts.items())),
        "matched_class_counts": dict(sorted(class_counts.items())),
        "pairs_interval_diff_le_365": within_365,
        "pairs_interval_diff_le_365_rate": (within_365 / pair_count) if pair_count else 0.0,
        "unmatched_exposed_units": unmatched_exposed,
        "unique_control_bridges_used": len(used_controls),
        "pair_identity_sha256": fingerprint.hexdigest(),
    }


if DB_PATH.exists():
    DB_PATH.unlink()
conn = sqlite3.connect(DB_PATH)
init_db(conn)

annual = []
for year in YEARS:
    print(f"US-BRIDGE-N01 NBI {year}", flush=True)
    annual.append(process_nbi_year(conn, year))

print("US-BRIDGE-N01 FEMA", flush=True)
events_by_county, fema_meta = fetch_fema_events()

print("US-BRIDGE-N01 BUILD DESIGN UNITS", flush=True)
design = build_design_units(conn, events_by_county)

print("US-BRIDGE-N01 MATCH", flush=True)
pair_path = OUT / "PAIR_IDENTITIES.jsonl"
matching = match_pairs(conn, pair_path)
conn.close()

all_schema = len(annual) == 11 and all(x["required_non_outcome_schema_supported"] for x in annual)
base_ready = (
    all_schema
    and design["unique_bridges_with_eligible_interval"] >= 300000
    and design["unique_exposed_bridges"] >= 10000
    and design["unique_control_candidate_bridges"] >= 100000
)
match_ready = (
    matching["matched_pairs"] >= 10000
    and matching["matched_state_fips_count"] >= 30
    and matching["matched_class_counts"].get("CULVERT", 0) >= 500
    and matching["matched_class_counts"].get("NON_CULVERT", 0) >= 8000
    and matching["pairs_interval_diff_le_365_rate"] >= 0.90
)
if base_ready and match_ready:
    gate = "PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE"
elif base_ready:
    gate = "PARTIAL_US_BRIDGE_N01_INTERVAL_DESIGN_READY_MATCH_SUPPORT_PENDING"
else:
    gate = "HOLD_US_BRIDGE_N01_DESIGN_NOT_IDENTIFIABLE"
assert gate in ALLOWED_GATES

result = {
    "research_id": "US-BRIDGE-N01",
    "issue": 131,
    "gate": gate,
    "nbi_years": [2015, 2025],
    "annual_sources": 11,
    "all_years_required_non_outcome_schema_supported": all_schema,
    **design,
    **matching,
    "fema": fema_meta,
    "frozen_interval_days": [MIN_INTERVAL_DAYS, MAX_INTERVAL_DAYS],
    "frozen_exact_match_stratum": ["state_fips", "bridge_class", "pre_inspection_year"],
    "frozen_declaration_type": "DR",
    "condition_rating_values_opened": False,
    "condition_rating_row_bytes_sliced": False,
    "relationship_computed": False,
    "fuzzy_repair_used": False,
    "outcome_dependent_inclusion_used": False,
    "raw_source_bytes_persisted": False,
    "incremental_monetary_cost_usd": 0,
}
manifest = {
    "research_id": "US-BRIDGE-N01",
    "official_record_format": "https://www.fhwa.dot.gov/bridge/nbi/format.cfm",
    "authorized_field_positions": FIELD_POSITIONS,
    "forbidden_condition_fields": FORBIDDEN_CONDITION_FIELDS,
    "condition_values_accessed": False,
    "condition_row_bytes_sliced": False,
    "annual_sources": annual,
    "fema": fema_meta,
    "raw_source_bytes_persisted": False,
    "incremental_monetary_cost_usd": 0,
}
pair_manifest = {
    "research_id": "US-BRIDGE-N01",
    "issue": 131,
    "pair_file": "research/US-BRIDGE-N01/PAIR_IDENTITIES.jsonl",
    "pair_count": matching["matched_pairs"],
    "pair_identity_sha256": matching["pair_identity_sha256"],
    "ordering": "state_fips, bridge_class, pre_year, exposed pre_date, exposed bridge_key; deterministic control tie-breaks per README",
    "condition_values_accessed": False,
    "relationship_computed": False,
}

(OUT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
(OUT / "DESIGN_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
(OUT / "PAIR_MANIFEST.json").write_text(json.dumps(pair_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "gate": gate,
    "eligible_bridges": design["unique_bridges_with_eligible_interval"],
    "exposed_bridges": design["unique_exposed_bridges"],
    "control_bridges": design["unique_control_candidate_bridges"],
    "matched_pairs": matching["matched_pairs"],
    "matched_states": matching["matched_state_fips_count"],
    "matched_classes": matching["matched_class_counts"],
    "within_365_rate": matching["pairs_interval_diff_le_365_rate"],
    "pair_sha256": matching["pair_identity_sha256"],
    "condition_values_opened": False,
    "relationship_computed": False,
}, sort_keys=True), flush=True)
