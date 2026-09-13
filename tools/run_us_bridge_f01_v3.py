#!/usr/bin/env python3
"""Source-route + legacy State-Code padding compatibility wrapper for US-BRIDGE-F01.

Scientific contract, thresholds, outcome-blind slices, and gate logic are inherited
from run_us_bridge_f01.py. This wrapper changes only pre-outcome transport/parser
compatibility proven necessary by official archive generations and observed 2018
legacy State-Code padding.
"""
from pathlib import Path

path = Path(__file__).with_name("run_us_bridge_f01.py")
src = path.read_text(encoding="utf-8")

old_route = '''    # Frozen route: fixed-width/no-delimiter, all highway bridges, national one-file.\n    marker = f"{year}hwybronefile"\n    hits = []\n    for href, text in items:\n        low = href.lower()\n        if "disclaim.cfm" in low and marker in low and f"{marker}del" not in low:\n            hits.append(href)\n'''
new_route = '''    # Frozen route: fixed-width/no-delimiter, all highway bridges, national one-file.\n    # FHWA archive naming varies by generation; the invariant official route token\n    # is the year plus `onefilenodel`.\n    hits = []\n    for href, text in items:\n        low = href.lower()\n        if "disclaim.cfm" in low and str(year) in low and "onefilenodel" in low:\n            hits.append(href)\n'''

old_state = '''                state3 = line[0:3].decode("ascii", errors="strict")\n                if not re.fullmatch(r"\\d{3}", state3): raise RuntimeError(f"{year}: invalid state code {state3!r}")\n                sf = state3[:2]\n'''
new_state = '''                state3 = line[0:3].decode("ascii", errors="strict")\n                # FHWA Item 1: first two chars are State FIPS; third is a historical\n                # FHWA-region position and may be blank in legacy territory rows.\n                if not re.fullmatch(r"\\d{2}", state3[:2]): raise RuntimeError(f"{year}: invalid State-FIPS prefix {state3!r}")\n                sf = state3[:2]\n'''

if src.count(old_route) != 1:
    raise RuntimeError("frozen resolver block not found exactly once")
if src.count(old_state) != 1:
    raise RuntimeError("frozen state parser block not found exactly once")
patched = src.replace(old_route, new_route, 1).replace(old_state, new_state, 1)
ns = {"__name__": "__main__", "__file__": str(path)}
exec(compile(patched, str(path) + "[route-state-v3]", "exec"), ns, ns)
