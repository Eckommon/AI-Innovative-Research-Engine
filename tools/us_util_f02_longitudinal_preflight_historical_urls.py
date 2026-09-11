#!/usr/bin/env python3
"""Execution-only source/schema resolver for US-UTIL-F02.

The scientific F02 contract is unchanged. This wrapper:
1) resolves official historical EIA-861 ZIP paths; and
2) fixes outcome-blind worksheet/header selection discovered from diagnostic Run
   34553361343, before any Reliability or AMI magnitude is parsed.
"""

import us_util_f02_longitudinal_preflight as base


def official_eia_url(year: int) -> str:
    if year == 2024:
        return "https://www.eia.gov/electricity/data/eia861/zip/f8612024.zip"
    if 2019 <= year <= 2023:
        return f"https://www.eia.gov/electricity/data/eia861/archive/zip/f861{year}.zip"
    raise ValueError(f"Unsupported frozen F02 year: {year}")


def largest_identity_sheet(wb):
    """Choose the Utility-ID worksheet by identity cardinality only."""
    candidates = []
    for ws in wb.worksheets:
        try:
            header_row = base.find_header_row(ws)
        except Exception:
            continue
        ucol = base.exact_col(ws, header_row, "Utility Number") or base.exact_col(ws, header_row, "Utility ID")
        if not ucol:
            continue
        ids = set()
        for row in ws.iter_rows(
            min_row=header_row + 1,
            min_col=ucol,
            max_col=ucol,
            values_only=True,
        ):
            uid = base.utility_id(row[0])
            if uid and uid.lower() not in {"total", "none", "nan"}:
                ids.add(uid)
        candidates.append((len(ids), -header_row, ws.title, header_row))
    if not candidates:
        raise RuntimeError("No worksheet with a usable Utility Number/ID identity column")
    _, _, title, header_row = max(candidates)
    return wb[title], header_row


def primary_ieee_with_med_columns(labels):
    """Resolve full/all-events IEEE with-MED SAIDI/SAIFI, excluding LOS variants."""
    saidi = []
    saifi = []
    for idx, label in enumerate(labels, start=1):
        n = base.norm_header(label)
        if "ieee" not in n:
            continue
        if any(token in n for token in ("without", "excluding", "excl", "minuslos", "lossofsupplyremoved")):
            continue
        with_med = (
            "withmed" in n
            or "withmajorevent" in n
            or "majoreventdays" in n
            or "allevents" in n
        )
        if not with_med:
            continue
        if "saidi" in n:
            saidi.append(idx)
        if "saifi" in n:
            saifi.append(idx)
    return (
        saidi[0] if len(saidi) == 1 else None,
        saifi[0] if len(saifi) == 1 else None,
        [labels[i - 1] for i in sorted(set(saidi + saifi))],
    )


base.eia_url = official_eia_url
base.choose_sheet_with_utility = largest_identity_sheet
base.classify_ieee_with_med_columns = primary_ieee_with_med_columns


if __name__ == "__main__":
    base.main()
