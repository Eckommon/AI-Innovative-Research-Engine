#!/usr/bin/env python3
"""Metadata-only CMS NPI E01 first qualifying V2 weekly source watch.

Never downloads a ZIP, opens provider rows, mutates the preregistered experiment,
or activates its Issue marker. Commits evidence only for the first observed candidate.
"""
from __future__ import annotations

from datetime import date, datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
URL = "https://download.cms.gov/nppes/NPI_Files.html"
CONTRACT = "48843c9979336dcd10fdff984f458277062d6f20"
ANCHOR = "100526_101126"
BASELINE = date(2026, 10, 12)
EVIDENCE = ROOT / "research/US-CMS-NPI-E01/evidence"
OUTPUT_JSON = EVIDENCE / "source-candidate-01.json"
OUTPUT_MD = EVIDENCE / "source-candidate-01.md"
TOKEN = re.compile(r"(?<!\d)(\d{6}_\d{6})(?!\d)")


class Anchors(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            self.current = {"href": dict(attrs).get("href", ""), "text": ""}

    def handle_data(self, data):
        if self.current is not None:
            self.current["text"] += data

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self.current is not None:
            self.links.append(self.current)
            self.current = None


def date_range(token):
    if not re.fullmatch(r"\d{6}_\d{6}", token):
        return None
    try:
        a, b = token.split("_")
        start, end = datetime.strptime(a, "%m%d%y").date(), datetime.strptime(b, "%m%d%y").date()
    except ValueError:
        return None
    return (start, end) if start <= end else None


def classify_html(html: str, final_url: str):
    if final_url != URL:
        raise ValueError("Unexpected CMS listing redirect")
    parser = Anchors()
    parser.feed(html)
    by_token = {}
    for a in parser.links:
        label, href = " ".join(a["text"].split()), a["href"]
        combined = label + " " + href
        # Require BOTH a V2 signifier and weekly context. Monthly bodies are excluded.
        if "weekly" not in combined.lower():
            continue
        if not re.search(r"(?:v\.?2\b|version\s*2\b)", combined, flags=re.I):
            continue
        match = TOKEN.search(combined)
        if not match:
            continue
        token = match.group(1)
        dates = date_range(token)
        if dates is None:
            raise ValueError("Malformed official weekly covered-date token: " + token)
        uri = urljoin(final_url, href)
        u = urlparse(uri)
        if (u.scheme, u.hostname) != ("https", "download.cms.gov") or not u.path.startswith("/nppes/") or not u.path.lower().endswith(".zip"):
            raise ValueError("Official weekly listing references unexpected ZIP host/path")
        record = {
            "token": token, "start": dates[0].isoformat(), "end": dates[1].isoformat(),
            "label": label, "href": uri
        }
        if token in by_token and by_token[token] != record:
            raise ValueError("Ambiguous duplicate official weekly token: " + token)
        by_token[token] = record
    weekly = sorted(by_token.values(), key=lambda x: (x["start"], x["end"], x["token"]))
    if not weekly:
        raise ValueError("No independently identifiable official V2 weekly listing")
    qualified = [x for x in weekly
                 if date.fromisoformat(x["start"]) >= BASELINE
                 and date.fromisoformat(x["end"]) > BASELINE]
    return {
        "weekly_listings": weekly, "qualifying_count": len(qualified),
        "earliest_observed_qualifying": qualified[0] if qualified else None,
        "historical_anchor_still_visible": ANCHOR in by_token,
    }


def check_prior():
    cp = json.loads((ROOT / "context/checkpoint.json").read_text(encoding="utf-8"))
    if not (cp.get("checkpoint_id") == "CHK-20261013-US-CMS-NPI-E01-ACTIVE"
            and cp.get("active_issue") == 203 and cp.get("active_research") == "US-CMS-NPI-E01"
            and cp.get("last_decision") == "DEC-318"):
        raise RuntimeError("E01 active checkpoint mismatch")
    pf = json.loads((EVIDENCE / "source-preflight-03.json").read_text(encoding="utf-8"))
    if not (pf.get("contract_sha") == CONTRACT
            and pf.get("anchor_present") is True and pf.get("anchor_token") == ANCHOR
            and pf.get("metadata_only") is True
            and pf.get("zip_body_opened") is False
            and pf.get("future_membership_opened") is False
            and pf.get("disposition") == "WAIT_SOURCE_US_CMS_NPI_E01"):
        raise RuntimeError("Immutable official historical anchor not established")
    if (EVIDENCE / "attempt-01.json").exists():
        raise RuntimeError("E01 experiment attempt exists; watcher must not run")
    return pf["source_page"]["sha256"]


def fetch_html():
    req = Request(URL, headers={
        "User-Agent": "AI-Innovative-Research-Engine/1.0 (official-CMS-listing-metadata-only)",
        "Cache-Control": "no-cache",
    })
    with urlopen(req, timeout=60) as response:
        meta = {
            "url": response.geturl(), "http_status": response.status,
            "content_type": response.headers.get("Content-Type"),
            "etag": response.headers.get("ETag"),
            "last_modified": response.headers.get("Last-Modified"),
            "http_date": response.headers.get("Date"),
        }
        raw = response.read(512_001)
    if meta["http_status"] != 200 or len(raw) > 512_000:
        raise RuntimeError("Unusable CMS listing response")
    if not (meta["content_type"] or "").lower().startswith("text/html"):
        raise RuntimeError("CMS listing is not text/html")
    meta["byte_count"] = len(raw)
    meta["sha256"] = hashlib.sha256(raw).hexdigest()
    return raw.decode("utf-8-sig"), meta


def main():
    if OUTPUT_JSON.exists() or OUTPUT_MD.exists():
        print("SOURCE_CANDIDATE_ALREADY_LOCKED_US_CMS_NPI_E01")
        return
    previous_hash = check_prior()
    html, source = fetch_html()
    parsed = classify_html(html, source["url"])
    candidate = parsed["earliest_observed_qualifying"]
    if candidate is None:
        print("WAIT_SOURCE_US_CMS_NPI_E01",
              "qualifying=0", "source_sha256=" + source["sha256"],
              "unchanged_since_preflight03=" + str(source["sha256"] == previous_hash))
        return
    evidence = {
        "research": "US-CMS-NPI-E01",
        "type": "FIRST_OBSERVED_SOURCE_CANDIDATE_METADATA_ONLY",
        "contract_sha": CONTRACT,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_page": source,
        "immutable_anchor": ANCHOR,
        "historical_anchor_confirmed_by_preflight03": True,
        **parsed,
        "disposition": "SOURCE_CANDIDATE_OBSERVED_US_CMS_NPI_E01",
        "scientific_first_published_weekly_adjudicated": False,
        "requires_explicit_issue_marker_before_experiment": True,
        "zip_body_opened": False,
        "future_membership_opened": False,
        "incremental_monetary_cost_usd": 0,
    }
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(evidence, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(
        "# US-CMS-NPI-E01 — first observed source candidate / 최초 관측 적격 소스 후보\n\n"
        "**State / 상태:** \`SOURCE_CANDIDATE_OBSERVED_US_CMS_NPI_E01\`\n\n"
        f"- Observed at UTC / 확인: \`{evidence['checked_at_utc']}\`\n"
        f"- Official page SHA-256 / 공식 페이지: \`{source['sha256']}\`\n"
        f"- Earliest visible qualified weekly / 확인한 후보: \`{candidate['token']}\` "
        f"({candidate['start']}..{candidate['end']})\n"
        "- Prior official historical anchor: immutable Preflight 03 / 과거 공식 근거 유지\n"
        "- ZIP/provider outcomes opened: **no / 아니오**\n"
        "- Scientific first-publication rule not yet adjudicated / 최초 공개 여부 최종 판정 전\n"
        "- Experiment Issue execution marker added: **no / 아니오**\n"
        "- Cost / 비용: **0 USD**\n\n"
        "Explicitly verify first-qualifying-source integrity before editing Issue #203. "
        "Do not substitute later updates or a monthly body.\n",
        encoding="utf-8",
    )
    print("SOURCE_CANDIDATE_OBSERVED_US_CMS_NPI_E01", candidate["token"])


if __name__ == "__main__":
    main()
