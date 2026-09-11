#!/usr/bin/env python3
"""Outcome-blind source-route diagnostic for US-WATERWAY-F01.

This script does not parse delay magnitudes or hydrology magnitudes. It only tests
public authoritative routes, metadata/schema text, identifiers, date-window labels,
and lock cardinality needed to decide whether the frozen F01 can proceed.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-WATERWAY-F01"
UA = "AI-Innovative-Research-Engine/US-WATERWAY-F01-source-route-diagnostic"

CORPS_HOME = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home"
ANNUAL_USAGE = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/annual-usage-report"
NDC_LOCKS = "https://www.iwr.usace.army.mil/About/Technical-Centers/NDC-Navigation-and-Civil-Works-Decision-Support/NDC-Locks/"
CONTENTDM_SEARCH = "https://usace.contentdm.oclc.org/digital/api/search/collection/p16021coll2/searchterm/lock%20usage/field/title/maxRecords/100"
CONTENTDM_ITEM_2958 = "https://usace.contentdm.oclc.org/digital/api/singleitem/collection/p16021coll2/id/2958"
LOCK_LAYER = "https://services7.arcgis.com/n1YM8pTrFmm7L4hs/ArcGIS/rest/services/Locks/FeatureServer/0"
LOCK_QUERY = LOCK_LAYER + "/query?where=1%3D1&outFields=*&returnGeometry=true&f=json&outSR=4326"


def fetch(url: str, *, timeout: int = 90) -> tuple[bytes, int, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
        return data, getattr(r, "status", 200), r.geturl(), r.headers.get("content-type", "")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_text(data: bytes) -> str:
    return data.decode("utf-8", errors="replace")


def html_signals(text: str) -> dict[str, object]:
    low = text.lower()
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', text, flags=re.I)
    labels = {
        "annual_usage": "annual usage" in low,
        "average_delay": "average delay" in low,
        "delay": "delay" in low,
        "processing_time": "processing time" in low,
        "2016": "2016" in low,
        "2025": "2025" in low,
        "xlsx": ".xlsx" in low,
        "csv": ".csv" in low,
        "download": "download" in low,
        "apex": "apex" in low or "wwv_flow" in low,
    }
    relevant = []
    for h in hrefs:
        hl = h.lower()
        if any(tok in hl for tok in ("usage", "lock", "xlsx", "csv", "download", "export", "ords")):
            relevant.append(h)
    return {"signals": labels, "relevant_hrefs": sorted(set(relevant))[:100]}


def fetch_record(name: str, url: str) -> dict[str, object]:
    try:
        data, status, final, ctype = fetch(url)
        rec = {
            "name": name,
            "url": url,
            "status": status,
            "final_url": final,
            "content_type": ctype,
            "bytes": len(data),
            "sha256": sha(data),
        }
        if "text" in ctype.lower() or "html" in ctype.lower() or data[:1] in {b"{", b"["}:
            rec.update(html_signals(safe_text(data)))
        return rec
    except Exception as exc:
        return {"name": name, "url": url, "error": f"{type(exc).__name__}: {exc}"}


def contentdm_diagnostic() -> dict[str, object]:
    out: dict[str, object] = {"search_url": CONTENTDM_SEARCH}
    try:
        data, status, final, ctype = fetch(CONTENTDM_SEARCH)
        obj = json.loads(safe_text(data))
        items = obj.get("items", []) if isinstance(obj, dict) else []
        reduced = []
        for item in items:
            title = str(item.get("title", ""))
            date = str(item.get("date", ""))
            item_id = item.get("itemLink") or item.get("item") or item.get("item_id") or item.get("pointer")
            reduced.append({"title": title, "date": date, "item_ref": item_id})
        out.update({"status": status, "final_url": final, "content_type": ctype, "bytes": len(data), "sha256": sha(data), "totalResults": obj.get("totalResults"), "items": reduced[:100]})
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    try:
        data, status, final, ctype = fetch(CONTENTDM_ITEM_2958)
        obj = json.loads(safe_text(data))
        out["known_item_2958"] = {
            "status": status,
            "title": obj.get("title"),
            "date": obj.get("date"),
            "find": obj.get("find"),
            "filename": obj.get("filename"),
            "format": obj.get("format"),
            "resource": obj.get("resource"),
            "type": obj.get("type"),
            "fullrsEnabled": obj.get("fullrsEnabled"),
        }
    except Exception as exc:
        out["known_item_2958_error"] = f"{type(exc).__name__}: {exc}"
    return out


def lock_layer_diagnostic() -> dict[str, object]:
    out: dict[str, object] = {"layer": LOCK_LAYER}
    try:
        meta_data, status, final, ctype = fetch(LOCK_LAYER + "?f=json")
        meta = json.loads(safe_text(meta_data))
        fields = [{"name": f.get("name"), "alias": f.get("alias"), "type": f.get("type")} for f in meta.get("fields", [])]
        out.update({"metadata_status": status, "name": meta.get("name"), "object_id_field": meta.get("objectIdField"), "max_record_count": meta.get("maxRecordCount"), "fields": fields})
    except Exception as exc:
        out["metadata_error"] = f"{type(exc).__name__}: {exc}"
    try:
        qdata, status, final, ctype = fetch(LOCK_QUERY)
        qobj = json.loads(safe_text(qdata))
        feats = qobj.get("features", [])
        out["query_status"] = status
        out["feature_count"] = len(feats)
        # Persist identity/schema support only. Never persist operational/delay magnitudes.
        sample_attrs = []
        for f in feats[:5]:
            attrs = f.get("attributes", {})
            safe = {k: v for k, v in attrs.items() if any(tok in k.lower() for tok in ("id", "name", "river", "water", "state", "district", "division", "pms"))}
            sample_attrs.append(safe)
        out["identity_samples"] = sample_attrs
        out["geometry_nonnull_count"] = sum(1 for f in feats if f.get("geometry"))
    except Exception as exc:
        out["query_error"] = f"{type(exc).__name__}: {exc}"
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    routes = [
        fetch_record("NDC_LOCKS", NDC_LOCKS),
        fetch_record("CORPS_HOME", CORPS_HOME),
        fetch_record("ANNUAL_USAGE", ANNUAL_USAGE),
    ]
    contentdm = contentdm_diagnostic()
    locks = lock_layer_diagnostic()

    result = {
        "boundary": {
            "delay_magnitudes_parsed": False,
            "hydrology_magnitudes_parsed": False,
            "relationship_computed": False,
            "incremental_monetary_cost_usd": 0,
        },
        "routes": routes,
        "contentdm": contentdm,
        "lock_layer": locks,
    }
    (OUT / "SOURCE_ROUTE_DIAGNOSTIC.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# US-WATERWAY-F01 Source Route Diagnostic",
        "",
        "Outcome-blind diagnostic only. No delay or hydrology magnitudes were parsed.",
        "",
        "## Current routes",
    ]
    for r in routes:
        lines.append(f"- {r.get('name')}: HTTP={r.get('status', 'ERROR')} final=`{r.get('final_url', '')}` bytes={r.get('bytes', '')} error=`{r.get('error', '')}` signals={r.get('signals', {})}")
    lines += [
        "",
        "## Digital Library search",
        f"- totalResults: {contentdm.get('totalResults')}",
        f"- known item 2958: {contentdm.get('known_item_2958', contentdm.get('known_item_2958_error'))}",
        "- matched titles: " + " | ".join(str(x.get('title')) for x in contentdm.get('items', [])[:20]),
        "",
        "## National Lock Characteristics layer",
        f"- layer name: {locks.get('name')}",
        f"- feature count returned: {locks.get('feature_count')}",
        f"- non-null geometry count: {locks.get('geometry_nonnull_count')}",
        f"- metadata/query errors: {locks.get('metadata_error', '')} {locks.get('query_error', '')}",
        "",
        "This diagnostic is not a PASS/HOLD decision. It only resolves the current public source routes for the next bounded F01 step.",
        "",
        "Incremental monetary cost: **0 USD**.",
    ]
    (OUT / "SOURCE_ROUTE_DIAGNOSTIC.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"routes": routes, "contentdm_total": contentdm.get("totalResults"), "lock_count": locks.get("feature_count")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
