#!/usr/bin/env python3
"""Execute US-RCRA-F01 with audited source-encoding corrections only.

Scientific/source/join/cardinality thresholds are unchanged.

Correction 1: EPA's file-structure table spells the evaluation flag as
FOUND_VOLATION, while the detailed dictionary and live CSV use FOUND_VIOLATION.

Correction 2: OPERATING_TSDF is a six-position code in the live CSV. Missing
sub-universe positions are encoded with '-' (for example ----T-, ---S--,
LIBST-). The base probe incorrectly rejected '-' as an invalid character.
Allowing '-' preserves the documented meaning: a valid operating TSDF still
must contain at least one of L/I/B/S/T; H alone remains excluded.

Fail closed unless the expected source fragments are present exactly once/twice
before substitution. No disaster-linked compliance outcome is opened here.
"""
from pathlib import Path

source_path = Path(__file__).with_name("run_us_rcra_f01.py")
source = source_path.read_text(encoding="utf-8")

# EPA evaluation-header typo correction.
old_header = "FOUND_VOLATION"
new_header = "FOUND_VIOLATION"
header_count = source.count(old_header)
if header_count != 2:
    raise SystemExit(
        f"Unexpected header-correction cardinality: {old_header} occurs "
        f"{header_count} times, expected 2"
    )
corrected = source.replace(old_header, new_header)

# Six-position OPERATING_TSDF encoding correction: '-' is a placeholder.
old_tsdf = 'valid_chars = set(code) <= set("LIBSTH")'
new_tsdf = 'valid_chars = set(code) <= set("LIBSTH-")'
tsdf_count = corrected.count(old_tsdf)
if tsdf_count != 1:
    raise SystemExit(
        f"Unexpected TSDF-correction cardinality: target occurs {tsdf_count} "
        "times, expected 1"
    )
corrected = corrected.replace(old_tsdf, new_tsdf)

namespace = {"__name__": "__main__", "__file__": str(source_path)}
exec(
    compile(
        corrected,
        str(source_path) + "[FOUND_VIOLATION+TSDF-positional-corrected]",
        "exec",
    ),
    namespace,
)
