#!/usr/bin/env python3
"""Outcome-blind identity/hydrology support preflight for US-WATERWAY-F01.

No lock delay metric values and no USGS hydrologic observation values are parsed.
The script inspects Annual Usage identity UI structure, national lock identity/
geometry, and modern USGS monitoring-location/time-series metadata only.
"""

from __future__ import annotations

import hashlib
import html
import http.cookiejar
import json
import math
import re
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-WATERWAY-F01"
UA = "AI-Innovative-Research-Engine/US-WATERWAY-F01-identity-hydrology"
HOME = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home"
ANNUAL = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/annual-usage-report"
LOCK_QUERY = "https://services7.arcgis.com/n1YM8pTrFmm7L4hs/ArcGIS/rest/services/Locks/FeatureServer/0/query?where=1%3D1&outFields=ID,NDCCODE,RIVERCD,LOCKCD,PMSDATA,PMSNAME,RIVER,STATE,DISTRICT&returnGeometry=true&f=json&outSR=4326"
USGS_LOC = "https://api.waterdata.usgs.gov/ogcapi/v0/collections/monitoring-locations/items"
USGS_TS = "https://api.waterdata.usgs.gov/ogcapi/v0/collections/time-series-metadata/items"
TARGET_START = "2018-01-01"
TARGET_END = "2020-12-31"
TARGET_MATCHES = 25


def fetch(url: str, opener=None, referer: str | None = None, attempts: int = 3):
    op = opener or urllib.request.build_opener()
    headers = {"User-Agent": UA, "Accept": "application/json,text/html;q=0.9,*/*;q=0.8"}
    if referer:
        headers["Referer"] = referer
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=headers)
            with op.open(req, timeout=90) as r:
                return r.read(), getattr(r, "status", 200), r.geturl(), dict(r.headers.items())
        except Exception as exc:
            last = exc
            if i + 1 < attempts:
                time.sleep(1.5 * (i + 1))
    raise last


class SelectParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.selects = []
        self.current = None
        self.in_option = False
        self.option_text = []
        self.option_value = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag.lower() == "select":
            self.current = {"id": a.get("id"), "name": a.get("name"), "options": []}
            self.selects.append(self.current)
        elif tag.lower() == "option" and self.current is not None:
            self.in_option = True
            self.option_text = []
            self.option_value = a.get("value")

    def handle_data(self, data):
        if self.in_option:
            self.option_text.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "option" and self.in_option and self.current is not None:
            text = html.unescape("".join(self.option_text)).strip()
            self.current["options"].append({"value": self.option_value, "text": text})
            self.in_option = False
        elif tag.lower() == "select":
            self.current = None


def norm(s: object) -> str:
    t = str(s or "").upper().replace("&", " AND ")
    t = re.sub(r"[^A-Z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def river_match(river: str, site_name: str) -> bool:
    r = norm(river)
    s = norm(site_name)
    if not r or not s:
        return False
    # Conservative textual identity: full reported river/waterbody name must occur,
    # with a small set of explicit generic suffix transformations.
    variants = {r}
    if not r.endswith(" RIVER"):
        variants.add(r + " RIVER")
    if r.endswith(" WATERWAY"):
        variants.add(r[:-9].strip() + " RIVER")
    if r.endswith(" RIV"):
        variants.add(r[:-4].strip() + " RIVER")
    return any(len(v) >= 5 and v in s for v in variants)


def parse_date(s: object) -> str:
    text = str(s or "")
    return text[:10] if len(text) >= 10 else text


def date_covers(start: object, end: object) -> bool:
    a, b = parse_date(start), parse_date(end)
    return bool(a and b and a <= TARGET_START and b >= TARGET_END)


def hav_km(lat1, lon1, lat2, lon2):
    r = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2-lat1); dl = math.radians(lon2-lon1)
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*r*math.asin(math.sqrt(a))


def json_get(url: str):
    data, status, final, headers = fetch(url)
    return json.loads(data.decode("utf-8", errors="replace")), {"status": status, "final_url": final, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    # Annual Usage UI: parse only select/option identity labels, never metric cells.
    jar = http.cookiejar.CookieJar(); opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    hb, hs, hf, _ = fetch(HOME, opener)
    ab, ast, af, _ = fetch(ANNUAL, opener, hf)
    at = ab.decode("utf-8", errors="replace")
    sp = SelectParser(); sp.feed(at)
    select_diag = []
    annual_lock_labels = set()
    for sel in sp.selects:
        opts = sel["options"]
        texts = [norm(o.get("text")) for o in opts if norm(o.get("text"))]
        years = [x for x in texts if re.fullmatch(r"20(?:1[6-9]|2[0-5])", x)]
        # Lock selectors generally contain many named options and are not year selectors.
        if len(texts) >= 30 and len(years) < 10:
            for x in texts:
                if not re.fullmatch(r"20\d{2}", x) and x not in {"ALL", "SELECT", "SELECT LOCK", "ALL LOCKS"}:
                    annual_lock_labels.add(x)
        select_diag.append({"id": sel.get("id"), "name": sel.get("name"), "option_count": len(opts), "year_options": years, "sample_options": texts[:12]})

    lock_obj, lock_src = json_get(LOCK_QUERY)
    features = lock_obj.get("features", [])
    locks = []
    for f in features:
        a = f.get("attributes", {}) or {}; g = f.get("geometry", {}) or {}
        if str(a.get("PMSDATA", "")).upper() != "Y":
            continue
        x, y = g.get("x"), g.get("y")
        if x is None or y is None:
            continue
        locks.append({"id": a.get("ID"), "ndccode": a.get("NDCCODE"), "rivercd": a.get("RIVERCD"), "lockcd": a.get("LOCKCD"), "name": a.get("PMSNAME"), "river": a.get("RIVER"), "state": a.get("STATE"), "district": a.get("DISTRICT"), "lon": float(x), "lat": float(y)})

    matches = []
    attempted = 0
    usgs_requests = 0
    errors = []
    # Use increasing search radii conservatively; require river identity in station name.
    for lock in locks:
        if len(matches) >= TARGET_MATCHES:
            break
        if not lock["river"]:
            continue
        attempted += 1
        found = None
        for deg in (0.08, 0.18, 0.30):
            bbox = f"{lock['lon']-deg:.6f},{lock['lat']-deg:.6f},{lock['lon']+deg:.6f},{lock['lat']+deg:.6f}"
            url = USGS_LOC + "?" + urllib.parse.urlencode({"f":"json", "bbox":bbox, "limit":100})
            try:
                obj, _src = json_get(url); usgs_requests += 1
            except Exception as exc:
                errors.append(f"location:{lock['id']}:{type(exc).__name__}:{exc}")
                continue
            cands = []
            for feat in obj.get("features", []):
                p = feat.get("properties", {}) or {}; gg = feat.get("geometry", {}) or {}; coords = gg.get("coordinates") or []
                mid = feat.get("id") or p.get("id") or p.get("monitoring_location_id")
                name = p.get("monitoring_location_name") or p.get("name") or ""
                agency = p.get("agency_code") or ""
                if agency != "USGS" or not mid or not river_match(str(lock["river"]), str(name)) or len(coords) < 2:
                    continue
                dist = hav_km(lock["lat"], lock["lon"], float(coords[1]), float(coords[0]))
                cands.append((dist, str(mid), str(name), float(coords[1]), float(coords[0])))
            for dist, mid, name, slat, slon in sorted(cands):
                # Query metadata only: no observations/values endpoint.
                ts_url = USGS_TS + "?" + urllib.parse.urlencode({"f":"json", "monitoring_location_id":mid, "limit":100})
                try:
                    ts_obj, _ts_src = json_get(ts_url); usgs_requests += 1
                except Exception as exc:
                    errors.append(f"ts:{mid}:{type(exc).__name__}:{exc}")
                    continue
                qualifying = []
                for ts in ts_obj.get("features", []):
                    p = ts.get("properties", {}) or {}
                    if str(p.get("parameter_code")) not in {"00060", "00065"}:
                        continue
                    if str(p.get("computation_period_identifier", "")).lower() != "daily":
                        continue
                    if date_covers(p.get("begin_utc") or p.get("begin"), p.get("end_utc") or p.get("end")):
                        qualifying.append({"parameter_code": p.get("parameter_code"), "statistic_id": p.get("statistic_id"), "start": parse_date(p.get("begin_utc") or p.get("begin")), "end": parse_date(p.get("end_utc") or p.get("end"))})
                if qualifying:
                    found = {"lock_id": lock["id"], "lock_name": lock["name"], "river": lock["river"], "state": lock["state"], "usgs_monitoring_location_id": mid, "usgs_name": name, "distance_km": round(dist, 3), "daily_metadata_support": qualifying[:10]}
                    break
            if found:
                break
        if found:
            matches.append(found)
        time.sleep(0.05)

    result = {
        "boundary": {"delay_magnitudes_parsed": False, "hydrology_observation_values_parsed": False, "relationship_computed": False, "incremental_monetary_cost_usd": 0},
        "target_overlap": {"start": TARGET_START, "end": TARGET_END},
        "annual_usage": {"status": ast, "final_url": af, "bytes": len(ab), "sha256": hashlib.sha256(ab).hexdigest(), "contains_average_delay_label": "average delay" in at.lower(), "selects": select_diag, "candidate_lock_option_labels": len(annual_lock_labels)},
        "national_locks": {"source": lock_src, "all_features": len(features), "pmsdata_y_with_geometry": len(locks)},
        "usgs": {"locks_attempted_until_stop": attempted, "requests": usgs_requests, "qualified_matches": len(matches), "errors": errors[:50]},
        "matches": matches,
    }
    (OUT / "IDENTITY_HYDROLOGY_PREFLIGHT.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md = [
        "# US-WATERWAY-F01 Identity + Hydrology Metadata Preflight",
        "",
        "Outcome-blind: no lock-delay metric values or USGS hydrologic observation values were parsed.",
        "",
        "## Annual Usage identity support",
        f"- HTTP: **{ast}**; final route `{af}`",
        f"- `Average Delay` schema label present: **{'average delay' in at.lower()}**",
        f"- candidate lock option labels discovered: **{len(annual_lock_labels)}**",
        "",
        "## National lock identity",
        f"- FeatureServer rows: **{len(features)}**",
        f"- `PMSDATA=Y` with geometry: **{len(locks)}**",
        "",
        "## USGS modern metadata match",
        f"- target overlap: **{TARGET_START} through {TARGET_END}**",
        f"- locks attempted before stop: **{attempted}**",
        f"- qualified lock↔USGS matches: **{len(matches)}** / required {TARGET_MATCHES}",
        f"- USGS metadata requests: **{usgs_requests}**",
        "",
        "A qualified USGS match requires coordinates plus the full reported lock river/waterbody identity to occur in the USGS monitoring-location name, plus a Daily time-series metadata record for parameter `00060` (discharge) and/or `00065` (gage height) spanning the full 2018–2020 target interval.",
        "",
        "## Qualified identities",
    ]
    for m in matches:
        params = ",".join(sorted(set(str(x["parameter_code"]) for x in m["daily_metadata_support"])))
        md.append(f"- lock `{m['lock_id']}` {m['lock_name']} / {m['river']} ↔ `{m['usgs_monitoring_location_id']}` {m['usgs_name']} — {m['distance_km']} km; daily parameters {params}")
    md += ["", "This is a source/identity/date-support preflight only; no relationship is tested.", "", "Incremental monetary cost: **0 USD**."]
    (OUT / "IDENTITY_HYDROLOGY_PREFLIGHT.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"annual_lock_options": len(annual_lock_labels), "pms_locks": len(locks), "qualified_usgs_matches": len(matches), "attempted": attempted, "errors": len(errors)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
