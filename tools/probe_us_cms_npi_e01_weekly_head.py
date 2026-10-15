#!/usr/bin/env python3
"""Manual HEAD-only CMS first-week hypothetical URL availability *hint*.

No GET/ZIP, no redirect following, no weekly release authorization or E01 execution.
"""
from __future__ import annotations
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, HTTPRedirectHandler
import json

WEEK_END_EXCLUSIVE = datetime(2026, 10, 19, tzinfo=timezone.utc)
URL = "https://download.cms.gov/nppes/NPPES_Data_Dissemination_101226_101826_Weekly_V2.zip"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def allowed(now, url):
    if now.tzinfo is None or now.astimezone(timezone.utc) < WEEK_END_EXCLUSIVE:
        raise ValueError("Coverage week unfinished: before 2026-10-19 UTC")
    if url != URL:
        raise ValueError("Only exact hypothetical official CMS V2 weekly URL allowed")


def classify(status, headers):
    return {
        "method": "HEAD",
        "hypothetical_uri": URL,
        "http_status": status,
        "content_length_header": headers.get("Content-Length"),
        "last_modified_header": headers.get("Last-Modified"),
        "etag_header": headers.get("ETag"),
        "signal": "POSSIBLE_PUBLIC_OBJECT_METADATA_ONLY" if status == 200 else "NOT_ESTABLISHED",
        "official_listing_confirmed": False,
        "first_publication_adjudicated": False,
        "candidate_commit_authorized": False,
        "e01_experiment_authorized": False,
        "zip_body_opened": False,
        "provider_outcomes_opened": False,
        "incremental_monetary_cost_usd": 0,
    }


def probe(now=None, opener=None):
    now = now or datetime.now(timezone.utc)
    allowed(now, URL)
    opener = opener or build_opener(NoRedirect())
    req = Request(URL, method="HEAD", headers={
        "User-Agent": "AI-Innovative-Research-Engine/1.0 (metadata-only-CMS-HEAD)",
        "Cache-Control": "no-cache",
    })
    try:
        with opener.open(req, timeout=25) as res:
            if res.geturl() != URL:
                raise RuntimeError("Unexpected redirect; refusing source inference")
            return classify(res.status, res.headers)
    except HTTPError as exc:
        return classify(exc.code, exc.headers)
    except URLError as exc:
        raise RuntimeError("HEAD transport failure; no negative source inference") from exc


def main():
    print(json.dumps(probe(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
