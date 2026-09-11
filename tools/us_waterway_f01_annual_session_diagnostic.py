#!/usr/bin/env python3
"""Session-aware outcome-blind diagnostic for the Corps Locks Annual Usage report.

Creates a normal public HTTP cookie session from the Corps Locks home page and
then follows the published Annual Usage link. It records page/schema/export/date
signals only; it does not parse or persist delay magnitudes.
"""

from __future__ import annotations

import hashlib
import html
import http.cookiejar
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-WATERWAY-F01"
UA = "Mozilla/5.0 AI-Innovative-Research-Engine/US-WATERWAY-F01"
HOME = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home"


def get(opener, url: str, referer: str | None = None):
    headers = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8"}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    with opener.open(req, timeout=90) as r:
        data = r.read()
        return data, getattr(r, "status", 200), r.geturl(), dict(r.headers.items())


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    home_bytes, home_status, home_final, _ = get(opener, HOME)
    text = home_bytes.decode("utf-8", errors="replace")

    hrefs = [html.unescape(h) for h in re.findall(r'href=["\']([^"\']+)["\']', text, flags=re.I)]
    annual_hrefs = [h for h in hrefs if "annual-usage-report" in h.lower()]
    if not annual_hrefs:
        raise RuntimeError("published Annual Usage href not found on public home page")
    annual_url = urllib.parse.urljoin(home_final, annual_hrefs[0])
    annual_bytes, annual_status, annual_final, annual_headers = get(opener, annual_url, referer=home_final)
    annual_text = annual_bytes.decode("utf-8", errors="replace")
    low = annual_text.lower()

    # only metadata/schema labels; never extract table cell magnitudes
    labels = sorted(set(re.findall(r"[^<>\n]{0,80}(?:average\s+delay|delay\s+minutes|average\s+processing|percent\s+vessels\s+delayed|lock\s+usage|usage\s+metrics)[^<>\n]{0,80}", annual_text, flags=re.I)))[:100]
    years = sorted(set(re.findall(r"\b(?:201[6-9]|202[0-5])\b", annual_text)))
    all_hrefs = [html.unescape(h) for h in re.findall(r'href=["\']([^"\']+)["\']', annual_text, flags=re.I)]
    export_hrefs = sorted(set(h for h in all_hrefs if any(t in h.lower() for t in ("csv", "xlsx", "download", "export"))))[:100]
    buttons = sorted(set(re.findall(r"[^<>\n]{0,60}(?:download|export|csv|excel|xlsx)[^<>\n]{0,60}", annual_text, flags=re.I)))[:100]

    result = {
        "boundary": {"delay_magnitudes_parsed": False, "hydrology_magnitudes_parsed": False, "relationship_computed": False},
        "home": {"status": home_status, "final_url": home_final, "bytes": len(home_bytes), "sha256": hashlib.sha256(home_bytes).hexdigest()},
        "cookies_created": [{"name": c.name, "domain": c.domain, "path": c.path} for c in jar],
        "published_annual_href": annual_hrefs[0],
        "annual": {
            "requested_url": annual_url,
            "status": annual_status,
            "final_url": annual_final,
            "bytes": len(annual_bytes),
            "sha256": hashlib.sha256(annual_bytes).hexdigest(),
            "title": (re.search(r"<title[^>]*>(.*?)</title>", annual_text, flags=re.I | re.S).group(1).strip() if re.search(r"<title[^>]*>(.*?)</title>", annual_text, flags=re.I | re.S) else None),
            "contains_average_delay_label": "average delay" in low,
            "contains_processing_label": "processing time" in low or "average processing" in low,
            "contains_delay_label": "delay" in low,
            "year_labels_2016_2025": years,
            "schema_label_contexts": labels,
            "export_hrefs": export_hrefs,
            "export_button_contexts": buttons,
            "contains_apex_region": "a-region" in low or "apex" in low,
        },
    }
    (OUT / "ANNUAL_USAGE_SESSION_DIAGNOSTIC.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md = [
        "# Corps Locks Annual Usage — Session-aware Diagnostic",
        "",
        "Outcome-blind: no delay or hydrology magnitudes parsed.",
        "",
        f"- home HTTP: **{home_status}**",
        f"- published Annual Usage href: `{annual_hrefs[0]}`",
        f"- Annual Usage HTTP: **{annual_status}**",
        f"- Annual final URL: `{annual_final}`",
        f"- Annual page bytes: **{len(annual_bytes)}**",
        f"- year labels found: **{', '.join(years) if years else 'none'}**",
        f"- `Average Delay` label present: **{'average delay' in low}**",
        f"- processing-time label present: **{'processing time' in low or 'average processing' in low}**",
        f"- generic delay label present: **{'delay' in low}**",
        f"- export links found: **{len(export_hrefs)}**",
        "",
        "Schema-label contexts: " + (" | ".join(labels) if labels else "none"),
        "",
        "Export/button contexts: " + (" | ".join(buttons) if buttons else "none"),
        "",
        "This diagnostic does not itself declare PASS/HOLD.",
        "",
        "Incremental monetary cost: **0 USD**.",
    ]
    (OUT / "ANNUAL_USAGE_SESSION_DIAGNOSTIC.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps(result["annual"], ensure_ascii=False))


if __name__ == "__main__":
    main()
