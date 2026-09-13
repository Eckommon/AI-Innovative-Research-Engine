#!/usr/bin/env python3
"""Transport/source-route compatibility wrapper for US-BRIDGE-F01.

Scientific contract and all parsing/gates remain byte-for-byte inherited from
run_us_bridge_f01.py. Only the pre-outcome FHWA disclaimer-link naming resolver
is generalized across legacy/current annual page naming generations.
"""
from pathlib import Path

path = Path(__file__).with_name("run_us_bridge_f01.py")
src = path.read_text(encoding="utf-8")
old = '''    # Frozen route: fixed-width/no-delimiter, all highway bridges, national one-file.\n    marker = f"{year}hwybronefile"\n    hits = []\n    for href, text in items:\n        low = href.lower()\n        if "disclaim.cfm" in low and marker in low and f"{marker}del" not in low:\n            hits.append(href)\n'''
new = '''    # Frozen route: fixed-width/no-delimiter, all highway bridges, national one-file.\n    # FHWA naming varies by archive generation (e.g. 2015onefilenodel vs\n    # 2025hwybronefilenodel). The invariant official route token is the year\n    # plus `onefilenodel`; delimited routes use a different suffix.\n    hits = []\n    for href, text in items:\n        low = href.lower()\n        if "disclaim.cfm" in low and str(year) in low and "onefilenodel" in low:\n            hits.append(href)\n'''
if src.count(old) != 1:
    raise RuntimeError("frozen resolver block not found exactly once")
patched = src.replace(old, new, 1)
ns = {"__name__": "__main__", "__file__": str(path)}
exec(compile(patched, str(path) + "[route-v2]", "exec"), ns, ns)
