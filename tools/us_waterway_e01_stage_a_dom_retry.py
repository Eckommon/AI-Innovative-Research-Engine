#!/usr/bin/env python3
"""Execution-only DOM stability wrapper for US-WATERWAY-E01 Stage A.

Preserves the frozen Stage A scientific contract. It only retries reading the
same table headers while Oracle APEX replaces the paginated table DOM.
"""
from __future__ import annotations

import time

import us_waterway_e01_stage_a as stage_a

_original_table_headers = stage_a.table_headers


def stable_table_headers(table):
    """Retry transient empty/stale header reads; never alter parsed content."""
    last = []
    for attempt in range(20):
        try:
            headers = _original_table_headers(table)
            last = headers
            normalized = [" ".join(h.upper().split()) for h in headers]
            required = ("DISTRICT", "RIVER", "LOCK", "USAGE TYPE")
            if headers and all(any(x == r or x.startswith(r + " ") or x.startswith(r + "SORT") for x in normalized) for r in required):
                return headers
        except Exception:
            pass
        time.sleep(0.25 + 0.05 * attempt)
    return last


stage_a.table_headers = stable_table_headers

if __name__ == "__main__":
    stage_a.main()
