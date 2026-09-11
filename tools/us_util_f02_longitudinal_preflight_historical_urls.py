#!/usr/bin/env python3
"""Execution-only URL resolver for US-UTIL-F02.

The scientific F02 contract is unchanged. This wrapper corrects the historical
EIA-861 final ZIP route discovered after Run 34553100100: 2024 is under /zip/,
while 2019-2023 are under /archive/zip/.
"""

from tools import us_util_f02_longitudinal_preflight as base


def official_eia_url(year: int) -> str:
    if year == 2024:
        return "https://www.eia.gov/electricity/data/eia861/zip/f8612024.zip"
    if 2019 <= year <= 2023:
        return f"https://www.eia.gov/electricity/data/eia861/archive/zip/f861{year}.zip"
    raise ValueError(f"Unsupported frozen F02 year: {year}")


base.eia_url = official_eia_url


if __name__ == "__main__":
    base.main()
