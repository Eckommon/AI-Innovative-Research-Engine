#!/usr/bin/env python3
"""Implementation-only transport correction for US-FAA-AIP-F01.

The frozen scientific contract is unchanged. The original runner's landing-page
fetch is replaced with direct official FAA workbook URLs because the FAA year
landing pages return HTTP 403 to GitHub-hosted Actions runners while the linked
official XLSX assets remain public and machine-readable.
"""
from pathlib import Path

src_path = Path("tools/run_us_faa_aip_f01.py")
src = src_path.read_text(encoding="utf-8")
start = src.index("def parse_aip(year: int):")
end = src.index("\ndef parse_lid():", start)

replacement = r'''def parse_aip(year: int):
    direct = {
        2021: "https://www.faa.gov/sites/faa.gov/files/2023-07/FY2021-AIP-grants.xlsx",
        2022: "https://www.faa.gov/sites/faa.gov/files/2022-12/FY2022-AIP-grants.xlsx",
        2023: "https://www.faa.gov/sites/faa.gov/files/2023-10/FY2023-AIP-grants.xlsx",
        2024: "https://www.faa.gov/sites/faa.gov/files/2024-10/FY2024-AIP-grants.xlsx",
        2025: "https://www.faa.gov/sites/faa.gov/files/2025-11/FY_2025_AIP_Grants.xlsx",
    }
    xlsx = direct[year]
    r = get(xlsx)
    wb = load_workbook(io.BytesIO(r.content), read_only=True, data_only=True)
    rows_out = []
    detected = None
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        header_i = None
        headers = None
        for i, row in enumerate(rows[:25]):
            hh = [clean_header(x) for x in row]
            if "LocID" in hh and "State" in hh and any(x in hh for x in ("Project Summary", "Grant Number")):
                header_i, headers = i, hh
                break
        if header_i is None:
            continue
        idx = {h: j for j, h in enumerate(headers) if h}
        if not {"State", "LocID"}.issubset(idx):
            continue
        project_col = "Project Summary" if "Project Summary" in idx else None
        grant_col = "Grant Number" if "Grant Number" in idx else None
        if not (project_col or grant_col):
            continue
        detected = {"sheet": ws.title, "header_row_1based": header_i + 1, "headers": headers}
        for row in rows[header_i + 1 :]:
            code = norm(row[idx["LocID"]] if idx["LocID"] < len(row) else "")
            state = norm(row[idx["State"]] if idx["State"] < len(row) else "")
            project = str(row[idx[project_col]] if project_col and idx[project_col] < len(row) and row[idx[project_col]] is not None else "").strip()
            grant = str(row[idx[grant_col]] if grant_col and idx[grant_col] < len(row) and row[idx[grant_col]] is not None else "").strip()
            if not (code or state or project or grant):
                continue
            rows_out.append({"year": year, "code": code, "state": state, "project_nonblank": bool(project or grant)})
        break
    if detected is None:
        raise RuntimeError(f"No usable AIP schema in FY{year}")
    return rows_out, {"year": year, "url": xlsx, "bytes": len(r.content), "sha256": sha256(r.content), "schema": detected}
'''

patched = src[:start] + replacement + src[end:]
code = compile(patched, str(src_path), "exec")
exec(code, {"__name__": "__main__", "__file__": str(src_path)})
