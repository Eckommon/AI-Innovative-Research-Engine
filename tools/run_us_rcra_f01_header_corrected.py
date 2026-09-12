#!/usr/bin/env python3
"""Execute US-RCRA-F01 with audited source-encoding/network corrections only.

Scientific/source/join/cardinality thresholds are unchanged.

Correction 1: EPA's file-structure table spells the evaluation flag as
FOUND_VOLATION, while the detailed dictionary and live CSV use FOUND_VIOLATION.

Correction 2: OPERATING_TSDF is a six-position code in the live CSV. Missing
sub-universe positions are encoded with '-' (for example ----T-, ---S--,
LIBST-). The base probe incorrectly rejected '-' as an invalid character.
Allowing '-' preserves the documented meaning: a valid operating TSDF still
must contain at least one of L/I/B/S/T; H alone remains excluded.

Correction 3: ECHO ArcGIS exact-ID batch queries can transiently time out.
Reduce batch size and add bounded retries/backoff without changing identifiers,
join semantics, thresholds, geography, or the no-outcome boundary.

Fail closed unless each expected source fragment is present at the expected
cardinality before substitution. No disaster-linked compliance outcome is
opened here.
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

# Harden only the ArcGIS POST helper; same URL, payload and exact-ID semantics.
old_post = '''def post_form(url: str, params: dict[str, str]) -> dict:
    body = urllib.parse.urlencode(params).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "User-Agent": UA,
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)
'''
new_post = '''def post_form(url: str, params: dict[str, str]) -> dict:
    body = urllib.parse.urlencode(params).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "User-Agent": UA,
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    last_exc = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as exc:
            last_exc = exc
            if attempt == 3:
                raise
            __import__("time").sleep(2 ** attempt)
    raise last_exc
'''
post_count = corrected.count(old_post)
if post_count != 1:
    raise SystemExit(
        f"Unexpected ArcGIS helper correction cardinality: target occurs "
        f"{post_count} times, expected 1"
    )
corrected = corrected.replace(old_post, new_post)

old_batch = "    batch_size = 75"
new_batch = "    batch_size = 25"
batch_count = corrected.count(old_batch)
if batch_count != 1:
    raise SystemExit(
        f"Unexpected ArcGIS batch correction cardinality: target occurs "
        f"{batch_count} times, expected 1"
    )
corrected = corrected.replace(old_batch, new_batch)

namespace = {"__name__": "__main__", "__file__": str(source_path)}
exec(
    compile(
        corrected,
        str(source_path)
        + "[FOUND_VIOLATION+TSDF-positional+GIS-retry-corrected]",
        "exec",
    ),
    namespace,
)
