#!/usr/bin/env python3
"""Network-resilient launcher for US-RCRA-N01.

Scientific contract is unchanged. This wrapper only makes FEMA OpenFEMA GETs
retry after transient chunked-transfer / incomplete-read failures, buffering one
FEMA page before handing it to the frozen N01 runner. RCRA/ECHO routes remain
untouched.
"""
from __future__ import annotations

import io
import time
import urllib.request
from pathlib import Path
import runpy

_ORIGINAL_URLOPEN = urllib.request.urlopen
FEMA_HOST_FRAGMENT = "www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"


class _BufferedResponse(io.BytesIO):
    def __init__(self, payload: bytes, headers=None, url: str | None = None, status: int = 200):
        super().__init__(payload)
        self.headers = headers
        self.url = url
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False

    def getcode(self):
        return self.status


def _url_value(req) -> str:
    if isinstance(req, urllib.request.Request):
        return req.full_url
    return str(req)


def resilient_urlopen(req, *args, **kwargs):
    url = _url_value(req)
    if FEMA_HOST_FRAGMENT not in url:
        return _ORIGINAL_URLOPEN(req, *args, **kwargs)

    last_exc: Exception | None = None
    for attempt in range(5):
        try:
            with _ORIGINAL_URLOPEN(req, *args, **kwargs) as response:
                payload = response.read()
                return _BufferedResponse(
                    payload,
                    headers=getattr(response, "headers", None),
                    url=getattr(response, "url", url),
                    status=getattr(response, "status", 200),
                )
        except Exception as exc:  # transport-only retry; no scientific branching
            last_exc = exc
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)
    assert last_exc is not None
    raise last_exc


urllib.request.urlopen = resilient_urlopen
runpy.run_path(str(Path(__file__).with_name("run_us_rcra_n01.py")), run_name="__main__")
