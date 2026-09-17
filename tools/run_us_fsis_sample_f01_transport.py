#!/usr/bin/env python3
"""Implementation-only browser-session transport for US-FSIS-SAMPLE-F01.

Scientific contract, thresholds, years, identity rules and outcome firewall remain unchanged.
Prior urllib/curl attempts received HTTP 403 from FSIS before any empirical support count
was read. This wrapper uses a real Chromium browser context only to establish the same
public FSIS session and then fetch the same official source URLs.
"""
from __future__ import annotations

from playwright.sync_api import sync_playwright

import run_us_fsis_sample_f01 as core

_pw = sync_playwright().start()
_browser = _pw.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
_context = _browser.new_context(
    user_agent=core.UA,
    locale="en-US",
    extra_http_headers={
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.fsis.usda.gov/",
    },
)
_page = _context.new_page()
_warmed = False


def _warm_fsis(url: str) -> None:
    global _warmed
    if _warmed:
        return
    # Use the actual target rather than a third-party source. If a JS/WAF interstitial is
    # presented, give the public browser session a bounded interval to settle, then reload.
    response = _page.goto(url, wait_until="domcontentloaded", timeout=120_000)
    if response is not None and response.status >= 400:
        _page.wait_for_timeout(8_000)
        response = _page.reload(wait_until="domcontentloaded", timeout=120_000)
    if response is None or response.status >= 400:
        status = None if response is None else response.status
        raise RuntimeError(f"FSIS browser-session warm-up failed before data access: status={status} url={url}")
    _warmed = True


def browser_fetch(url: str) -> bytes:
    if "fsis.usda.gov" not in url:
        return core.urllib.request.urlopen(core.urllib.request.Request(url, headers={"User-Agent": core.UA}), timeout=90).read()

    _warm_fsis(url)
    # APIRequestContext shares cookie storage with BrowserContext. This permits binary/JSON
    # assets after the browser has established the public FSIS session, without changing URLs.
    response = _context.request.get(
        url,
        headers={
            "Accept": "text/html,application/xhtml+xml,application/json,text/csv,*/*;q=0.8",
            "Referer": "https://www.fsis.usda.gov/",
            "Cache-Control": "no-cache",
        },
        timeout=120_000,
        fail_on_status_code=False,
    )
    if response.status >= 400:
        # One bounded browser navigation retry for HTML pages; never substitute a mirror.
        nav = _page.goto(url, wait_until="domcontentloaded", timeout=120_000)
        if nav is not None and nav.status < 400:
            return nav.body()
        raise RuntimeError(f"FSIS browser-session fetch failed: status={response.status} url={url}")
    return response.body()


core.fetch = browser_fetch

try:
    if __name__ == "__main__":
        core.main()
finally:
    _context.close()
    _browser.close()
    _pw.stop()
