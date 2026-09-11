#!/usr/bin/env python3
"""Execution-only DOM stability wrapper for US-WATERWAY-E01 Stage A.

Preserves the frozen Stage A scientific contract. Oracle APEX renders a fixed-
header clone at the canonical table id and the actual paginated rows in the
same id suffixed ``_orig``. This wrapper selects that data table and makes
header discovery consistent with the successful structural probe. No scientific
variable, support threshold, identity rule, annual cell semantics, or outcome
boundary changes.
"""
from __future__ import annotations

import time

from selenium.webdriver.common.by import By

import us_waterway_e01_stage_a as stage_a

_original_table_headers = stage_a.table_headers
_original_find_individual_table = stage_a.find_individual_table


def find_data_table(driver):
    """Prefer APEX's actual row-bearing ``_orig`` table over fixed-header clone."""
    data_id = stage_a.INDIVIDUAL_TABLE_ID + "_orig"
    found = driver.find_elements(By.ID, data_id)
    if found:
        return found[0]
    return _original_find_individual_table(driver)


def _required_present(headers):
    normalized = [" ".join(h.upper().split()) for h in headers]
    required = ("DISTRICT", "RIVER", "LOCK", "USAGE TYPE")
    return bool(headers) and all(
        any(x == r or x.startswith(r + " ") or x.startswith(r + "SORT") for x in normalized)
        for r in required
    )


def stable_table_headers(table):
    """Retry transient reads and fall back from ``thead th`` to table ``th``."""
    last = []
    for attempt in range(20):
        try:
            headers = _original_table_headers(table)
            if _required_present(headers):
                return headers
            fallback = [stage_a.text_content(x) for x in table.find_elements(By.TAG_NAME, "th")]
            last = fallback or headers
            if _required_present(fallback):
                return fallback
        except Exception:
            pass
        time.sleep(0.25 + 0.05 * attempt)
    return last


stage_a.find_individual_table = find_data_table
stage_a.table_headers = stable_table_headers

if __name__ == "__main__":
    stage_a.main()
