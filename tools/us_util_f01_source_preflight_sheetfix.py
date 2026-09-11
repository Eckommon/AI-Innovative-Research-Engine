#!/usr/bin/env python3
"""Parser retry for US-UTIL-F01: prefer substantive data sheets over tiny territory lookup sheets."""

from __future__ import annotations

import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import us_util_f01_source_preflight as base  # noqa: E402


def choose_sheet(wb, needs: set[str]):
    candidates = []
    errors = []
    for ws in wb.worksheets:
        try:
            header_row, cols, headers = base.locate_header(ws, needs)
            # All candidates already satisfy the required identity headers.
            # Prefer the substantive data surface by observed worksheet row count;
            # tiny *_Territories lookup/notes sheets must not win lexicographically.
            candidates.append(
                (
                    int(ws.max_row or 0),
                    int(ws.max_column or 0),
                    -int(header_row),
                    ws.title,
                    header_row,
                    cols,
                    headers,
                )
            )
        except Exception as exc:
            errors.append(f"{ws.title}:{exc}")
    if not candidates:
        raise RuntimeError("No qualifying worksheet; " + " | ".join(errors))
    chosen = max(candidates)
    return wb[chosen[3]], chosen[4], chosen[5], chosen[6]


base.choose_sheet = choose_sheet

if __name__ == "__main__":
    # Same frozen #94 scientific gate; this retry changes parser sheet selection only.
    base.main()
