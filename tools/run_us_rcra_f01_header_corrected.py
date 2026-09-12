#!/usr/bin/env python3
"""Execute US-RCRA-F01 with the documented EPA evaluation-header typo corrected.

Scientific/source/join/cardinality contract is unchanged. The original probe used
FOUND_VOLATION because EPA's file-structure table spells it that way; EPA's detailed
definition and actual CSV use FOUND_VIOLATION. Fail closed unless the expected two
source references are exactly present before substitution.
"""
from pathlib import Path

source_path = Path(__file__).with_name("run_us_rcra_f01.py")
source = source_path.read_text(encoding="utf-8")
old = "FOUND_VOLATION"
new = "FOUND_VIOLATION"
count = source.count(old)
if count != 2:
    raise SystemExit(f"Unexpected technical-correction cardinality: {old} occurs {count} times, expected 2")
corrected = source.replace(old, new)
namespace = {"__name__": "__main__", "__file__": str(source_path)}
exec(compile(corrected, str(source_path) + "[FOUND_VIOLATION-corrected]", "exec"), namespace)
