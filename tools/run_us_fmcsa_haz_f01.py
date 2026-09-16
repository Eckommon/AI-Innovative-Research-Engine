#!/usr/bin/env python3
"""US-FMCSA-HAZ-F01 outcome-blind structural feasibility runner.

Only the preregistered official DOT/FMCSA and PHMSA routes are used. The runner
persists aggregate source/schema/identity/time support only. It never persists a
carrier-level FMCSA↔PHMSA joined membership table and never computes incident
occurrence/rates by any inspection-derived profile.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-FMCSA-HAZ-F01"
UA = "AI-Innovative-Research-Engine/US-FMCSA-HAZ-F01 outcome-blind"

FMCSA_INSPECTION_ID = "fx4q-ay7w"
FMCSA_VIOLATION_ID = "876r-jsdb"
URLS = {
    "fmcsa_docs": "https://www.fmcsa.dot.gov/registration/fmcsa-data-dissemination-program",
    "fmcsa_inspection_catalog": "https://catalog.data.gov/dataset/vehicle-inspection-file",
    "fmcsa_inspection_schema": f"https://data.transportation.gov/api/views/{FMCSA_INSPECTION_ID}/columns.json",
    "fmcsa_inspection_csv": f"https://data.transportation.gov/api/v3/views/{FMCSA_INSPECTION_ID}/export.csv?accessType=DOWNLOAD",
    "fmcsa_violation_catalog": "https://catalog.data.gov/dataset/vehicle-inspections-and-violations",
    "fmcsa_violation_schema": f"https://data.transportation.gov/api/views/{FMCSA_VIOLATION_ID}/columns.json",
    "fmcsa_violation_csv": f"https://data.transportation.gov/api/v3/views/{FMCSA_VIOLATION_ID}/export.csv?accessType=DOWNLOAD",
    "phmsa_catalog": "https://catalog.data.gov/dataset/hazmat-incident-reports-data-mining-tool",
    "phmsa_stats": "https://www.phmsa.dot.gov/hazmat-program-management-data-and-statistics/data-operations/incident-statistics",
    "phmsa_dictionary": "https://portal.phmsa.dot.gov/HIP_Help/DataDictionary.pdf",
    "phmsa_search": "https://portalpublic.phmsa.dot.gov/analytics/saw.dll?Portal%3FPortalPath=%2Fshared%2FPublic+Website+Pages%2F_portal%2FHazmat+Incident+Report+Search",
}

PASS = "PASS_US_FMCSA_HAZ_F01_CARRIER_TIME_JOIN_READY"
PARTIAL = "PARTIAL_US_FMCSA_HAZ_F01_SOURCE_SEMANTICS_READY__PHMSA_EXPORT_ACCESS_BLOCKED"
HOLD = "HOLD_US_FMCSA_HAZ_F01_SOURCE_SCHEMA_OR_IDENTITY"
INVALID = "IMPLEMENTATION_OR_SOURCE_PARSE_NOT_VALID_FOR_GATE"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def request(url: str, timeout: int = 60, max_bytes: int | None = None) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "application/json,text/csv,text/plain,text/html,application/pdf,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read() if max_bytes is None else r.read(max_bytes)
            return {
                "ok": True,
                "http": getattr(r, "status", 200),
                "url": url,
                "final_url": r.geturl(),
                "headers": dict(r.headers),
                "data": data,
                "error": None,
            }
    except urllib.error.HTTPError as e:
        try:
            body = e.read(32768)
        except Exception:
            body = b""
        return {
            "ok": False,
            "http": e.code,
            "url": url,
            "final_url": getattr(e, "url", url),
            "headers": dict(e.headers or {}),
            "data": body,
            "error": "HTTPError",
        }
    except Exception as e:
        return {
            "ok": False,
            "http": None,
            "url": url,
            "final_url": url,
            "headers": {},
            "data": b"",
            "error": type(e).__name__,
        }


def retry(url: str, attempts: int = 3, timeout: int = 60, max_bytes: int | None = None) -> dict:
    last = None
    for _ in range(attempts):
        last = request(url, timeout=timeout, max_bytes=max_bytes)
        if last["ok"]:
            return last
    assert last is not None
    return last


def audit(resp: dict, include_sha: bool = True) -> dict:
    return {
        "url": resp["url"],
        "final_url": resp["final_url"],
        "http": resp["http"],
        "bytes": len(resp["data"]),
        "sha256": sha256(resp["data"]) if include_sha else None,
        "content_type": resp["headers"].get("Content-Type", ""),
        "content_disposition": resp["headers"].get("Content-Disposition", ""),
        "error": resp["error"],
    }


def norm_name(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(s or "").lower())


def choose_col(cols: list[dict], aliases: list[str], contains: list[list[str]] | None = None) -> dict | None:
    aliases_n = {norm_name(x) for x in aliases}
    for c in cols:
        values = [str(c.get("fieldName") or ""), str(c.get("name") or "")]
        if any(norm_name(v) in aliases_n for v in values):
            return c
    for tokens in contains or []:
        for c in cols:
            n = norm_name((c.get("fieldName") or "") + " " + (c.get("name") or ""))
            if all(norm_name(t) in n for t in tokens):
                return c
    return None


def field(c: dict | None) -> str | None:
    return str(c.get("fieldName")) if c and c.get("fieldName") else None


def socrata_query(dataset_id: str, params: dict, timeout: int = 90) -> tuple[list[dict], dict]:
    base = f"https://data.transportation.gov/resource/{dataset_id}.json"
    url = base + "?" + urllib.parse.urlencode(params)
    resp = retry(url, attempts=3, timeout=timeout)
    if not resp["ok"]:
        raise RuntimeError(f"Socrata query failed {dataset_id}: http={resp['http']} error={resp['error']}")
    try:
        obj = json.loads(resp["data"].decode("utf-8"))
    except Exception as e:
        raise RuntimeError(f"Socrata JSON parse failed {dataset_id}: {e}") from e
    if not isinstance(obj, list):
        raise RuntimeError(f"Socrata query not list for {dataset_id}")
    a = audit(resp)
    a["query_params"] = params
    return obj, a


def canonical_id(v) -> str | None:
    s = str(v or "").strip()
    if not re.fullmatch(r"\d+", s):
        return None
    try:
        n = int(s)
    except Exception:
        return None
    return str(n) if n > 0 else None


def fingerprint(values: set[str]) -> str | None:
    if not values:
        return None
    return sha256(("\n".join(sorted(values, key=lambda x: (len(x), x))) + "\n").encode("utf-8"))


def group_carriers(dataset_id: str, carrier_field: str) -> tuple[set[str], int, int, int, list[dict]]:
    carriers: set[str] = set()
    repeated = 0
    max_rows = 0
    total_valid_rows = 0
    query_audits = []
    offset = 0
    page = 50000
    while True:
        rows, a = socrata_query(dataset_id, {
            "$select": f"{carrier_field}, count(*) as n",
            "$where": f"{carrier_field} is not null",
            "$group": carrier_field,
            "$order": carrier_field,
            "$limit": page,
            "$offset": offset,
        })
        query_audits.append(a)
        if not rows:
            break
        for row in rows:
            cid = canonical_id(row.get(carrier_field))
            if cid is None:
                continue
            try:
                n = int(float(row.get("n", 0)))
            except Exception:
                n = 0
            carriers.add(cid)
            total_valid_rows += n
            if n > 1:
                repeated += 1
            max_rows = max(max_rows, n)
        if len(rows) < page:
            break
        offset += page
        if offset > 2_000_000:
            raise RuntimeError("carrier pagination safety bound exceeded")
    return carriers, repeated, max_rows, total_valid_rows, query_audits


def scalar_count(dataset_id: str, where: str | None = None, expr: str = "count(*) as n") -> tuple[int, dict]:
    params = {"$select": expr}
    if where:
        params["$where"] = where
    rows, a = socrata_query(dataset_id, params)
    if not rows:
        return 0, a
    value = rows[0].get("n")
    try:
        return int(float(value)), a
    except Exception as e:
        raise RuntimeError(f"scalar count parse failed: {value!r}") from e


def date_support(dataset_id: str, carrier_field: str, date_field: str, date_type: str) -> tuple[dict, list[dict]]:
    audits: list[dict] = []
    total, a = scalar_count(dataset_id, f"{carrier_field} is not null")
    audits.append(a)
    dated, a = scalar_count(dataset_id, f"{carrier_field} is not null AND {date_field} is not null")
    audits.append(a)
    years: list[int] = []
    # Socrata fixed/floating timestamps support date_extract_y().
    if "date" in date_type.lower() or "calendar" in date_type.lower() or "timestamp" in date_type.lower():
        rows, a = socrata_query(dataset_id, {
            "$select": f"date_extract_y({date_field}) as y, count(*) as n",
            "$where": f"{carrier_field} is not null AND {date_field} is not null",
            "$group": "y",
            "$order": "y",
            "$limit": 100,
        })
        audits.append(a)
        for row in rows:
            try:
                y = int(float(row.get("y")))
            except Exception:
                continue
            if 1900 <= y <= 2100:
                years.append(y)
    return {
        "valid_carrier_rows": total,
        "dated_valid_carrier_rows": dated,
        "date_parse_rate": (dated / total) if total else 0.0,
        "date_years": sorted(set(years)),
        "distinct_date_years": len(set(years)),
        "date_field_type": date_type,
    }, audits


def html_text(data: bytes) -> str:
    raw = data.decode("utf-8", errors="replace")
    raw = re.sub(r"<script\b[^>]*>.*?</script>", " ", raw, flags=re.I | re.S)
    raw = re.sub(r"<style\b[^>]*>.*?</style>", " ", raw, flags=re.I | re.S)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", unescape(raw)).strip()


class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows: list[list[str]] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "tr":
            self._row = []
        elif tag.lower() in {"td", "th"} and self._row is not None:
            self._cell = []

    def handle_data(self, data):
        if self._cell is not None:
            self._cell.append(data)

    def handle_endtag(self, tag):
        if tag.lower() in {"td", "th"} and self._cell is not None and self._row is not None:
            self._row.append(re.sub(r"\s+", " ", "".join(self._cell)).strip())
            self._cell = None
        elif tag.lower() == "tr" and self._row is not None:
            if self._row:
                self.rows.append(self._row)
            self._row = None


def parse_tabular_export(data: bytes, content_type: str) -> tuple[list[str], list[list[str]], str] | None:
    head = data[:4096].lower()
    if b"<html" in head or b"<table" in head:
        p = TableParser()
        p.feed(data.decode("utf-8", errors="replace"))
        if len(p.rows) >= 2:
            return p.rows[0], p.rows[1:], "html-table"
        return None
    text = None
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            text = data.decode(enc)
            break
        except Exception:
            pass
    if text is None:
        return None
    sample = text[:65536]
    delim = "\t" if sample.count("\t") >= sample.count(",") else ","
    r = csv.reader(io.StringIO(text), delimiter=delim)
    rows = list(r)
    if len(rows) < 2:
        return None
    return rows[0], rows[1:], "tsv" if delim == "\t" else "csv"


def phmsa_export_candidates(search_resp: dict) -> list[str]:
    if not search_resp["ok"]:
        return []
    raw = search_resp["data"].decode("utf-8", errors="replace")
    hrefs = re.findall(r'''href\s*=\s*["']([^"']+)["']''', raw, flags=re.I)
    out = []
    for h in hrefs:
        u = urllib.parse.urljoin(URLS["phmsa_search"], unescape(h))
        p = urllib.parse.urlparse(u)
        host = (p.hostname or "").lower()
        low = u.lower()
        if host.endswith("phmsa.dot.gov") and any(k in low for k in ("download", "export", "csv", "txt", "excel")):
            if u not in out:
                out.append(u)
    return out[:20]


def find_header(headers: list[str], aliases: list[str], contains: list[list[str]] | None = None) -> int | None:
    ns = [norm_name(h) for h in headers]
    aset = {norm_name(a) for a in aliases}
    for i, n in enumerate(ns):
        if n in aset:
            return i
    for tokens in contains or []:
        nt = [norm_name(t) for t in tokens]
        for i, n in enumerate(ns):
            if all(t in n for t in nt):
                return i
    return None


def parse_date_year(s: str) -> int | None:
    s = str(s or "").strip()
    if not s:
        return None
    m = re.search(r"\b(19|20)\d{2}\b", s)
    if not m:
        return None
    y = int(m.group(0))
    return y if 1900 <= y <= 2100 else None


def parse_phmsa_export(data: bytes, ctype: str) -> dict | None:
    parsed = parse_tabular_export(data, ctype)
    if not parsed:
        return None
    headers, rows, fmt = parsed
    i_report = find_header(headers, ["Report Number"], [["report", "number"]])
    i_date = find_header(headers, ["Date of Incident"], [["date", "incident"]])
    i_mode = find_header(headers, ["Mode of Transportation"], [["mode", "transport"]])
    i_dot = find_header(headers, ["Carrier/Reporter FED DOT ID"], [["carrier", "reporter", "fed", "dot", "id"]])
    schema = all(i is not None for i in (i_report, i_date, i_mode, i_dot))
    if not schema:
        return {
            "schema_complete": False,
            "headers": headers,
            "format": fmt,
        }
    carriers: set[str] = set()
    years: list[int] = []
    dated = 0
    eligible = 0
    reports: set[str] = set()
    row_mult: defaultdict[str, int] = defaultdict(int)
    for row in rows:
        if max(i_report, i_date, i_mode, i_dot) >= len(row):
            continue
        mode = str(row[i_mode] or "").strip().lower()
        if mode != "highway":
            continue
        cid = canonical_id(row[i_dot])
        if cid is None:
            continue
        eligible += 1
        carriers.add(cid)
        y = parse_date_year(row[i_date])
        if y is not None:
            dated += 1
            years.append(y)
        rep = str(row[i_report] or "").strip()
        if rep:
            reports.add(rep)
            row_mult[rep] += 1
    return {
        "schema_complete": True,
        "headers": headers,
        "format": fmt,
        "highway_rows_with_valid_fed_dot_id": eligible,
        "distinct_highway_fed_dot_ids": len(carriers),
        "carriers": carriers,
        "date_parse_rate": (dated / eligible) if eligible else 0.0,
        "date_years": sorted(set(years)),
        "distinct_date_years": len(set(years)),
        "distinct_report_numbers": len(reports),
        "reports_with_multiple_rows": sum(1 for n in row_mult.values() if n > 1),
        "max_rows_per_report": max(row_mult.values(), default=0),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    audits: dict = {
        "raw_source_bytes_persisted": False,
        "carrier_level_join_membership_persisted": False,
        "unofficial_mirror_used": False,
        "authentication_bypass_used": False,
    }

    # Official docs and metadata.
    small_docs = {}
    for k in ("fmcsa_docs", "fmcsa_inspection_catalog", "fmcsa_violation_catalog", "phmsa_catalog", "phmsa_stats", "phmsa_dictionary", "phmsa_search"):
        r = retry(URLS[k], attempts=2, timeout=60, max_bytes=8_000_000)
        small_docs[k] = r
        audits[k] = audit(r)

    insp_schema_resp = retry(URLS["fmcsa_inspection_schema"], attempts=3, timeout=60, max_bytes=4_000_000)
    viol_schema_resp = retry(URLS["fmcsa_violation_schema"], attempts=3, timeout=60, max_bytes=4_000_000)
    audits["fmcsa_inspection_schema"] = audit(insp_schema_resp)
    audits["fmcsa_violation_schema"] = audit(viol_schema_resp)

    implementation_error = None
    fmcsa = {
        "schema_complete": False,
        "violation_linkage_ready": False,
        "distinct_valid_usdot_carriers": 0,
        "repeated_inspection_carriers": 0,
        "max_inspections_per_carrier": 0,
        "carrier_fingerprint": None,
    }
    fmcsa_carriers: set[str] = set()
    query_audits: list[dict] = []

    try:
        if not (insp_schema_resp["ok"] and viol_schema_resp["ok"]):
            raise RuntimeError("FMCSA schema metadata unavailable")
        insp_cols = json.loads(insp_schema_resp["data"].decode("utf-8"))
        viol_cols = json.loads(viol_schema_resp["data"].decode("utf-8"))
        if not isinstance(insp_cols, list) or not isinstance(viol_cols, list):
            raise RuntimeError("FMCSA schema metadata not column lists")

        c_usdot = choose_col(insp_cols, ["USDOT_NUM", "USDOT_NUMBER", "US_DOT_NUM", "US DOT NUMBER", "U.S. DOT#"], [["usdot"]])
        c_iid = choose_col(insp_cols, ["INSPECTION_ID", "Inspection ID"], [["inspection", "id"]])
        c_date = choose_col(insp_cols, ["INSPECTION_DATE", "Inspection Date", "INSP_DATE"], [["inspection", "date"]])
        v_iid = choose_col(viol_cols, ["INSPECTION_ID", "Inspection ID"], [["inspection", "id"]])
        v_oos = choose_col(viol_cols, ["OUT_OF_SERVICE", "OOS", "OOS_IND", "Out-of-Service"], [["out", "service"], ["oos"]])

        f_usdot, f_iid, f_date, f_viid = map(field, (c_usdot, c_iid, c_date, v_iid))
        f_oos = field(v_oos)
        fmcsa["field_map"] = {
            "usdot": f_usdot,
            "inspection_id": f_iid,
            "inspection_date": f_date,
            "violation_inspection_id": f_viid,
            "violation_oos": f_oos,
        }
        fmcsa["inspection_schema_column_count"] = len(insp_cols)
        fmcsa["violation_schema_column_count"] = len(viol_cols)
        fmcsa["schema_complete"] = all((f_usdot, f_iid, f_date, f_viid, f_oos))
        if not fmcsa["schema_complete"]:
            raise RuntimeError(f"FMCSA required field mapping incomplete: {fmcsa['field_map']}")

        fmcsa_carriers, repeated, max_rows, valid_rows, qa = group_carriers(FMCSA_INSPECTION_ID, f_usdot)
        query_audits.extend(qa)
        fmcsa["distinct_valid_usdot_carriers"] = len(fmcsa_carriers)
        fmcsa["repeated_inspection_carriers"] = repeated
        fmcsa["max_inspections_per_carrier"] = max_rows
        fmcsa["valid_usdot_inspection_rows"] = valid_rows
        fmcsa["carrier_fingerprint"] = fingerprint(fmcsa_carriers)

        ds, qa = date_support(FMCSA_INSPECTION_ID, f_usdot, f_date, str(c_date.get("dataTypeName") or ""))
        fmcsa.update(ds)
        query_audits.extend(qa)

        distinct_iids, a = scalar_count(FMCSA_INSPECTION_ID, f"{f_iid} is not null", f"count(distinct {f_iid}) as n")
        query_audits.append(a)
        fmcsa["distinct_inspection_ids"] = distinct_iids

        viol_total, a = scalar_count(FMCSA_VIOLATION_ID)
        query_audits.append(a)
        viol_linked, a = scalar_count(FMCSA_VIOLATION_ID, f"{f_viid} is not null")
        query_audits.append(a)
        viol_distinct, a = scalar_count(FMCSA_VIOLATION_ID, f"{f_viid} is not null", f"count(distinct {f_viid}) as n")
        query_audits.append(a)
        mult_rows, a = socrata_query(FMCSA_VIOLATION_ID, {
            "$select": f"{f_viid}, count(*) as n",
            "$where": f"{f_viid} is not null",
            "$group": f_viid,
            "$order": "n DESC",
            "$limit": 1,
        })
        query_audits.append(a)
        max_viol = int(float(mult_rows[0].get("n", 0))) if mult_rows else 0
        fmcsa["violation_rows"] = viol_total
        fmcsa["violation_rows_with_inspection_id"] = viol_linked
        fmcsa["violation_inspection_id_nonnull_rate"] = (viol_linked / viol_total) if viol_total else 0.0
        fmcsa["distinct_violation_inspection_ids"] = viol_distinct
        fmcsa["max_violation_rows_per_inspection_id"] = max_viol
        fmcsa["violation_linkage_ready"] = bool(f_viid and f_oos and viol_linked > 0 and viol_distinct > 0)
    except Exception as e:
        implementation_error = f"{type(e).__name__}: {e}"

    audits["fmcsa_query_audits"] = query_audits

    # Official PHMSA public-export semantics are preregistered from these current sources.
    phmsa_docs_ready = all(small_docs[k]["ok"] for k in ("phmsa_catalog", "phmsa_dictionary", "phmsa_search"))
    catalog_text = html_text(small_docs["phmsa_catalog"]["data"]).lower() if small_docs["phmsa_catalog"]["ok"] else ""
    search_text = html_text(small_docs["phmsa_search"]["data"]).lower() if small_docs["phmsa_search"]["ok"] else ""
    phmsa_export_semantics = (
        "export" in catalog_text and "text file" in catalog_text
    ) or (
        "incident detailed report" in search_text and ("download" in search_text or "export" in search_text)
    )

    phmsa_export = None
    export_attempts = []
    candidates = phmsa_export_candidates(small_docs["phmsa_search"])
    audits["phmsa_discovered_export_candidate_count"] = len(candidates)
    audits["phmsa_discovered_export_candidates"] = candidates
    for u in candidates:
        r = retry(u, attempts=1, timeout=120, max_bytes=250_000_000)
        a = audit(r)
        export_attempts.append(a)
        if not r["ok"]:
            continue
        ct = (r["headers"].get("Content-Type", "") or "").lower()
        cd = (r["headers"].get("Content-Disposition", "") or "").lower()
        # Reject landing/navigation HTML unless it actually contains a parsable result table.
        parsed = parse_phmsa_export(r["data"], ct)
        if parsed and ("attachment" in cd or any(x in ct for x in ("csv", "text", "excel", "html"))):
            evald = parse_phmsa_export(r["data"], ct)
            if evald and evald.get("schema_complete"):
                phmsa_export = {"url": u, "response": r, "eval": evald}
                break
    audits["phmsa_export_attempts"] = export_attempts

    phmsa = {
        "docs_reachable": phmsa_docs_ready,
        "public_export_semantics_documented": phmsa_export_semantics,
        "export_bytes_accessible": phmsa_export is not None,
        "required_schema_present": False,
        "distinct_highway_fed_dot_ids": None,
        "date_parse_rate": None,
        "date_years": None,
        "distinct_date_years": None,
        "carrier_fingerprint": None,
    }
    phmsa_carriers: set[str] = set()
    if phmsa_export is not None:
        ev = phmsa_export["eval"]
        phmsa["required_schema_present"] = bool(ev.get("schema_complete"))
        phmsa["format"] = ev.get("format")
        phmsa["headers"] = ev.get("headers")
        phmsa["highway_rows_with_valid_fed_dot_id"] = ev.get("highway_rows_with_valid_fed_dot_id")
        phmsa["distinct_highway_fed_dot_ids"] = ev.get("distinct_highway_fed_dot_ids")
        phmsa["date_parse_rate"] = ev.get("date_parse_rate")
        phmsa["date_years"] = ev.get("date_years")
        phmsa["distinct_date_years"] = ev.get("distinct_date_years")
        phmsa["distinct_report_numbers"] = ev.get("distinct_report_numbers")
        phmsa["reports_with_multiple_rows"] = ev.get("reports_with_multiple_rows")
        phmsa["max_rows_per_report"] = ev.get("max_rows_per_report")
        phmsa_carriers = set(ev.get("carriers") or set())
        phmsa["carrier_fingerprint"] = fingerprint(phmsa_carriers)
        audits["phmsa_selected_export"] = audit(phmsa_export["response"])

    intersection = fmcsa_carriers & phmsa_carriers if phmsa_export is not None else set()

    docs_req = all(small_docs[k]["ok"] for k in ("fmcsa_docs", "fmcsa_inspection_catalog", "fmcsa_violation_catalog", "phmsa_catalog", "phmsa_dictionary"))
    req = {
        "official_metadata_documentation_reachable_fingerprinted": docs_req,
        "fmcsa_inspection_machine_readable": implementation_error is None and bool(fmcsa.get("schema_complete")),
        "fmcsa_violation_machine_readable": implementation_error is None and bool(fmcsa.get("violation_linkage_ready")),
        "fmcsa_required_native_fields_present": bool(fmcsa.get("schema_complete")),
        "fmcsa_distinct_usdot_ge_50000": int(fmcsa.get("distinct_valid_usdot_carriers") or 0) >= 50000,
        "fmcsa_date_support_ge_3_years_and_95pct": float(fmcsa.get("date_parse_rate") or 0) >= 0.95 and int(fmcsa.get("distinct_date_years") or 0) >= 3,
        "phmsa_detailed_export_publicly_executable": phmsa_export is not None,
        "phmsa_required_fields_present": bool(phmsa.get("required_schema_present")),
        "phmsa_highway_fed_dot_ids_ge_500": int(phmsa.get("distinct_highway_fed_dot_ids") or 0) >= 500,
        "phmsa_date_support_ge_10_years_and_95pct": float(phmsa.get("date_parse_rate") or 0) >= 0.95 and int(phmsa.get("distinct_date_years") or 0) >= 10,
        "exact_carrier_intersection_ge_300": len(intersection) >= 300,
        "fmcsa_violation_oos_linkage_deterministic": bool(fmcsa.get("violation_linkage_ready")),
        "three_identity_fingerprints_persisted": bool(fmcsa.get("carrier_fingerprint") and phmsa.get("carrier_fingerprint") and fingerprint(intersection)),
        "public_cohort_boundary_preserved": True,
        "outcome_boundary_preserved": True,
        "carrier_level_join_membership_not_persisted": True,
        "relationship_prediction_causality_closed": True,
        "zero_cost_no_bypass": True,
    }

    fm_empirical_for_partial = all(req[k] for k in (
        "official_metadata_documentation_reachable_fingerprinted",
        "fmcsa_inspection_machine_readable",
        "fmcsa_violation_machine_readable",
        "fmcsa_required_native_fields_present",
        "fmcsa_distinct_usdot_ge_50000",
        "fmcsa_date_support_ge_3_years_and_95pct",
        "fmcsa_violation_oos_linkage_deterministic",
    ))

    if implementation_error is not None:
        gate = INVALID
        valid_execution = False
    elif all(req.values()):
        gate = PASS
        valid_execution = True
    elif (
        fm_empirical_for_partial
        and phmsa_docs_ready
        and phmsa_export_semantics
        and phmsa_export is None
    ):
        gate = PARTIAL
        valid_execution = True
    else:
        gate = HOLD
        valid_execution = True

    result = {
        "research_id": "US-FMCSA-HAZ-F01",
        "issue": 145,
        "gate": gate,
        "valid_execution": valid_execution,
        "implementation_error": implementation_error,
        "fmcsa": fmcsa,
        "phmsa": phmsa,
        "aggregate_exact_carrier_intersection": len(intersection) if phmsa_export is not None else None,
        "fingerprints": {
            "fmcsa_usdot_carriers": fmcsa.get("carrier_fingerprint"),
            "phmsa_highway_fed_dot_ids": phmsa.get("carrier_fingerprint"),
            "intersection": fingerprint(intersection) if phmsa_export is not None else None,
        },
        "requirements": req,
        "phmsa_export_access_only_partial_condition": {
            "fmcsa_empirical_requirements_pass": fm_empirical_for_partial,
            "phmsa_docs_reachable": phmsa_docs_ready,
            "phmsa_public_export_semantics_documented": phmsa_export_semantics,
            "phmsa_export_bytes_accessible": phmsa_export is not None,
        },
        "hazmat_incident_occurrence_by_inspection_profile_opened": False,
        "future_incident_membership_conditioned_on_fmcsa_opened": False,
        "carrier_level_join_membership_persisted": False,
        "relationship_computed": False,
        "predictive_metric_computed": False,
        "causal_claim_made": False,
        "federal_safety_rating_claim_made": False,
        "unofficial_mirror_used": False,
        "authentication_bypass_used": False,
        "post_execution_rescue_used": False,
        "incremental_monetary_cost_usd": 0,
    }

    audits["source_boundary"] = {
        "fmcsa_dataset_ids": [FMCSA_INSPECTION_ID, FMCSA_VIOLATION_ID],
        "phmsa_source": "Form 5800.1 official public Incident Detailed Report/export only",
        "no_unofficial_mirror": True,
        "no_authentication_bypass": True,
        "raw_source_bytes_persisted": False,
        "carrier_level_join_membership_persisted": False,
    }

    (OUT / "STAGING_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "STAGING_SOURCE_AUDIT.json").write_text(json.dumps(audits, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "gate": gate,
        "valid_execution": valid_execution,
        "fmcsa_carriers": fmcsa.get("distinct_valid_usdot_carriers"),
        "fmcsa_years": fmcsa.get("distinct_date_years"),
        "phmsa_export_accessible": phmsa.get("export_bytes_accessible"),
        "phmsa_carriers": phmsa.get("distinct_highway_fed_dot_ids"),
        "intersection": len(intersection) if phmsa_export is not None else None,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
