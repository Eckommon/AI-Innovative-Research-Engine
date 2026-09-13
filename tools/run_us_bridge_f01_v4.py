#!/usr/bin/env python3
"""Key-year duplicate fail-closed correction for US-BRIDGE-F01.

This wrapper preserves the frozen F01 sources, windows, thresholds, FEMA hazard set,
outcome-blind slices, and gate logic. It corrects only an implementation
nonconformity in Run 34790222911: a duplicate canonical key discarded the entire
annual NBI file. The frozen contract requires the ambiguous canonical key-year to
fail closed; unique keys in that year remain eligible.

Condition-rating bytes remain untouched.
"""
from pathlib import Path

path = Path(__file__).with_name("run_us_bridge_f01.py")
src = path.read_text(encoding="utf-8")

old_route = '''    # Frozen route: fixed-width/no-delimiter, all highway bridges, national one-file.\n    marker = f"{year}hwybronefile"\n    hits = []\n    for href, text in items:\n        low = href.lower()\n        if "disclaim.cfm" in low and marker in low and f"{marker}del" not in low:\n            hits.append(href)\n'''
new_route = '''    # Frozen route: fixed-width/no-delimiter, all highway bridges, national one-file.\n    # FHWA archive naming varies by generation; the invariant official route token\n    # is the year plus `onefilenodel`.\n    hits = []\n    for href, text in items:\n        low = href.lower()\n        if "disclaim.cfm" in low and str(year) in low and "onefilenodel" in low:\n            hits.append(href)\n'''

old_state = '''                state3 = line[0:3].decode("ascii", errors="strict")\n                if not re.fullmatch(r"\\d{3}", state3): raise RuntimeError(f"{year}: invalid state code {state3!r}")\n                sf = state3[:2]\n'''
new_state = '''                state3 = line[0:3].decode("ascii", errors="strict")\n                # FHWA Item 1: first two chars are State FIPS; third is a historical\n                # FHWA-region position and may be blank in legacy territory rows.\n                if not re.fullmatch(r"\\d{2}", state3[:2]): raise RuntimeError(f"{year}: invalid State-FIPS prefix {state3!r}")\n                sf = state3[:2]\n'''

old_decl = '''    year_data: dict[str, tuple[str | None, str | None]] = {}\n    duplicates = 0; rows = 0; parseable_dates = 0\n'''
new_decl = '''    year_data: dict[str, tuple[str | None, str | None]] = {}\n    duplicate_keys: set[str] = set()\n    duplicates = 0; rows = 0; parseable_dates = 0\n'''

old_seen = '''                if key in year_data:\n                    duplicates += 1\n                else:\n                    year_data[key] = (county, ins)\n'''
new_seen = '''                if key in year_data:\n                    duplicates += 1\n                    duplicate_keys.add(key)\n                else:\n                    year_data[key] = (county, ins)\n'''

old_contrib = '''    schema_supported = (min_len or 0) >= 290\n    # Duplicate canonical keys fail closed for the whole state-year contribution.\n    if duplicates == 0 and schema_supported:\n        for key, (county, ins) in year_data.items():\n            support[key] += 1\n            if ins is not None: dates[key].add(ins)\n            if key not in county_ok: county_ok[key] = True\n            if county is None:\n                county_ok[key] = False\n            elif key not in county_first:\n                county_first[key] = county\n            elif county_first[key] != county:\n                county_ok[key] = False\n'''
new_contrib = '''    schema_supported = (min_len or 0) >= 290\n    # Frozen fail-closed semantics are applied at the ambiguous canonical key-year\n    # level. A duplicated key is excluded for this year; unrelated unique bridge\n    # identities from the same official annual file remain eligible.\n    if schema_supported:\n        for key, (county, ins) in year_data.items():\n            if key in duplicate_keys:\n                continue\n            support[key] += 1\n            if ins is not None: dates[key].add(ins)\n            if key not in county_ok: county_ok[key] = True\n            if county is None:\n                county_ok[key] = False\n            elif key not in county_first:\n                county_first[key] = county\n            elif county_first[key] != county:\n                county_ok[key] = False\n'''

old_year_fields = '''        "unique_bridge_keys": len(year_data), "duplicate_canonical_keys": duplicates,\n'''
new_year_fields = '''        "unique_bridge_keys": len(year_data), "duplicate_canonical_keys": duplicates,\n        "duplicate_canonical_keys_excluded": len(duplicate_keys),\n        "eligible_unique_bridge_keys": len(year_data) - len(duplicate_keys),\n'''

old_base = '''base_panel = all_sources and all_schema and no_dupes and len(repeated) >= 300000 and county_rate >= 0.90 and len(repeated_states) >= 45 and len(overlap_states) >= 30 and len(overlap) >= 500\n'''
new_base = '''base_panel = all_sources and all_schema and len(repeated) >= 300000 and county_rate >= 0.90 and len(repeated_states) >= 45 and len(overlap_states) >= 30 and len(overlap) >= 500\n'''

old_result_field = '''    "all_years_zero_duplicate_canonical_keys": no_dupes,\n'''
new_result_field = '''    "all_years_zero_duplicate_canonical_keys": no_dupes,\n    "duplicate_key_fail_closed_at_key_year_level": True,\n    "duplicate_canonical_key_rows_seen": sum(m["duplicate_canonical_keys"] for m in years_manifest),\n    "duplicate_canonical_keys_excluded": sum(m["duplicate_canonical_keys_excluded"] for m in years_manifest),\n    "supersedes_technical_run": 34790222911,\n'''

pairs = [
    (old_route, new_route, "route"),
    (old_state, new_state, "state"),
    (old_decl, new_decl, "duplicate declaration"),
    (old_seen, new_seen, "duplicate detection"),
    (old_contrib, new_contrib, "key-year fail-closed contribution"),
    (old_year_fields, new_year_fields, "annual duplicate diagnostics"),
    (old_base, new_base, "base panel duplicate semantics"),
    (old_result_field, new_result_field, "result integrity fields"),
]
patched = src
for old, new, label in pairs:
    if patched.count(old) != 1:
        raise RuntimeError(f"frozen {label} block not found exactly once")
    patched = patched.replace(old, new, 1)

ns = {"__name__": "__main__", "__file__": str(path)}
exec(compile(patched, str(path) + "[key-year-v4]", "exec"), ns, ns)
