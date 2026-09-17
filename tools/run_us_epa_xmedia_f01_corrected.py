#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

import run_us_epa_xmedia_f01 as base

CORRECTED_OUT = base.OUTDIR / "STAGING_RESULT_CORRECTED.json"


def parse_year_strict(value: str) -> int | None:
    """Mechanical correction only: reject malformed/out-of-range parsed years.

    The frozen F01 contract, source set, identity rules, thresholds, and outcome
    firewall are unchanged. A structural permit date is treated as valid only
    when its parsed calendar year is in [1900, 2100].
    """
    s = base.norm(value)
    if not s:
        return None
    m = re.search(r"(?<!\d)((?:19|20)\d{2})(?!\d)", s)
    if m:
        y = int(m.group(1))
        return y if 1900 <= y <= 2100 else None
    for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%d-%b-%Y", "%d-%b-%y", "%m/%d/%y"):
        try:
            y = datetime.strptime(s, fmt).year
            return y if 1900 <= y <= 2100 else None
        except ValueError:
            pass
    return None


def main() -> None:
    original = base.OUTDIR / "STAGING_RESULT.json"
    assert original.exists(), "original immutable staging result must be preserved"
    original_result = json.loads(original.read_text(encoding="utf-8"))
    assert original_result["contract_commit"] == "86a7a01ba3b64160ee21a7ea821536d3d1adbb14"
    assert original_result["effluent_violation_rows_opened"] is False
    assert original_result["dmr_outcome_rows_opened"] is False
    assert original_result["relationship_computed"] is False
    assert not CORRECTED_OUT.exists(), "corrected immutable staging result already exists"

    base.parse_year = parse_year_strict
    base.OUT = CORRECTED_OUT
    base.main()

    corrected = json.loads(CORRECTED_OUT.read_text(encoding="utf-8"))
    corrected["implementation_correction"] = {
        "kind": "DATE_PARSER_VALID_YEAR_RANGE",
        "preserves_original_staging": "research/US-EPA-XMEDIA-F01/STAGING_RESULT.json",
        "reason": "Original fallback date parser could admit malformed/out-of-range years; corrected parser accepts only calendar years 1900-2100.",
        "contract_changed": False,
        "sources_changed": False,
        "thresholds_changed": False,
        "identity_rules_changed": False,
        "outcome_firewall_changed": False,
    }
    CORRECTED_OUT.write_text(json.dumps(corrected, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"gate": corrected["gate"], "requirements": f"{corrected['requirements_passed']}/{corrected['requirements_total']}", "corrected_output": str(CORRECTED_OUT)}, sort_keys=True))


if __name__ == "__main__":
    main()
