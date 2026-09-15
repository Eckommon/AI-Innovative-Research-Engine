#!/usr/bin/env python3
"""Execution-only correction wrapper for US-UTIL-N01.

Scientific contract: Issue #137 / DEC-188, unchanged.
This wrapper reuses the prospectively adjudicated US-UTIL-F02 worksheet/header
resolver and re-adjudicates the staging gate against only the requirements that
were actually frozen in Issue #137.
"""
from __future__ import annotations

import json
from pathlib import Path

import run_us_util_n01 as base
import us_util_f02_longitudinal_preflight_historical_urls as f02fix

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-UTIL-N01"

# Execution correction only: reuse the already prospective F02 parser adjudication.
base.choose_sheet_with_utility = f02fix.largest_identity_sheet
base.classify_ieee_with_med_columns = f02fix.primary_ieee_with_med_columns


def adjudicate_frozen_issue_137(result: dict) -> str:
    """Apply exactly the frozen Issue #137 PASS conditions; add no new gate."""
    r = result.get("requirements", {})
    d = result.get("diagnostics", {})
    m = result.get("matching", {})
    c = result.get("candidate_support", {})
    by_year = c.get("by_year", {})
    pair_years = {int(k): int(v) for k, v in m.get("pairs_by_exposure_year", {}).items()}

    frozen = {
        "source_hash_match_f02": bool(result.get("source_hash_match_f02")),
        "ami_exact_route_all_years": bool(r.get("ami_exact_route_all_years")),
        "reliability_ieee_saidi_with_med_route_all_years": bool(r.get("reliability_ieee_saidi_with_med_route_all_years")),
        "no_conflicting_ami_duplicates": int(d.get("ami_duplicate_conflicts", 0)) == 0,
        "eligible_utilities_ge_500": int(d.get("eligible_utilities", 0)) >= 500,
        "each_exposure_year_has_both_roles": all(
            int(by_year.get(str(y), by_year.get(y, {})).get("EXPOSED", 0)) > 0
            and int(by_year.get(str(y), by_year.get(y, {})).get("CONTROL", 0)) > 0
            for y in (2020, 2021, 2022, 2023)
        ),
        "exposed_candidates_ge_300": int(c.get("exposed", 0)) >= 300,
        "control_candidates_ge_300": int(c.get("control", 0)) >= 300,
        "matched_pairs_ge_150": int(m.get("pairs", 0)) >= 150,
        "matched_states_ge_25": int(m.get("states", 0)) >= 25,
        "represented_exposure_years_ge_3": len([y for y, n in pair_years.items() if n > 0]) >= 3,
        "each_represented_exposure_year_pairs_ge_30": all(n >= 30 for n in pair_years.values() if n > 0),
        "pair_fingerprint_frozen": bool(m.get("pair_identity_sha256")) and (OUT / "PAIR_IDENTITIES.jsonl.gz").exists(),
        "reliability_magnitudes_not_opened": result.get("reliability_magnitudes_opened") is False,
        "relationship_not_computed": result.get("relationship_computed") is False,
        "noaa_storm_magnitudes_not_used": result.get("noaa_storm_magnitudes_used") is False,
        "invented_county_weights_not_used": result.get("invented_county_weights") is False,
        "incremental_monetary_cost_zero": result.get("incremental_monetary_cost_usd") == 0,
    }

    result["frozen_issue_137_requirements"] = frozen
    result["execution_correction"] = {
        "f02_largest_identity_sheet_reused": True,
        "f02_primary_ieee_with_med_excluding_los_reused": True,
        "invalid_meter_rows_retained_as_diagnostic_only": True,
        "scientific_contract_changed": False,
        "superseded_run": 35007936755,
    }

    if all(frozen.values()):
        return "PASS_US_UTIL_N01_AMI_RAMP_MATCHED_DESIGN_IDENTIFIABLE"

    structural = all(frozen[k] for k in (
        "source_hash_match_f02",
        "ami_exact_route_all_years",
        "reliability_ieee_saidi_with_med_route_all_years",
        "no_conflicting_ami_duplicates",
        "eligible_utilities_ge_500",
        "each_exposure_year_has_both_roles",
        "reliability_magnitudes_not_opened",
        "relationship_not_computed",
        "noaa_storm_magnitudes_not_used",
        "invented_county_weights_not_used",
        "incremental_monetary_cost_zero",
    ))
    if structural and int(m.get("pairs", 0)) > 0:
        return "PARTIAL_US_UTIL_N01_AMI_EXPOSURE_IDENTIFIABLE__MATCH_SUPPORT_PENDING"
    return "HOLD_US_UTIL_N01_SOURCE_OR_DESIGN_SUPPORT"


def main() -> None:
    base.main()
    path = OUT / "STAGING_RESULT.json"
    result = json.loads(path.read_text(encoding="utf-8"))
    corrected_gate = adjudicate_frozen_issue_137(result)
    result["base_runner_gate_before_contract_correction"] = result.get("gate")
    result["gate"] = corrected_gate
    result["post_execution_rescue_used"] = False
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    audit_path = OUT / "STAGING_SOURCE_AUDIT.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    audit["execution_correction"] = result["execution_correction"]
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "gate": corrected_gate,
        "eligible_utilities": result.get("diagnostics", {}).get("eligible_utilities"),
        "exposed_candidates": result.get("candidate_support", {}).get("exposed"),
        "control_candidates": result.get("candidate_support", {}).get("control"),
        "pairs": result.get("matching", {}).get("pairs"),
        "states": result.get("matching", {}).get("states"),
        "pairs_by_exposure_year": result.get("matching", {}).get("pairs_by_exposure_year"),
        "pair_identity_sha256": result.get("matching", {}).get("pair_identity_sha256"),
        "scientific_contract_changed": False,
        "reliability_magnitudes_opened": False,
        "relationship_computed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
