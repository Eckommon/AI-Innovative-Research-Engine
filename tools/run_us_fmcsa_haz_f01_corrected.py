#!/usr/bin/env python3
"""Corrected execution wrapper for US-FMCSA-HAZ-F01.

Corrections are limited to the implementation defects durably recorded in
SUPERSEDED_RUN_35045639924.md: the observed native FMCSA `dot_number` alias and
proper separation of PHMSA documentation semantics from Oracle export access.
The preregistered source identities, thresholds, exact join, outcomes and cost
boundary are unchanged.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from tools import run_us_fmcsa_haz_f01 as b

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-FMCSA-HAZ-F01"
CORRECTS_RUN = 35045639924


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    audits: dict = {
        "corrects_run": CORRECTS_RUN,
        "correction_scope": "native-dot-number-alias-and-documentation-vs-export-access-control-flow-only",
        "raw_source_bytes_persisted": False,
        "carrier_level_join_membership_persisted": False,
        "unofficial_mirror_used": False,
        "authentication_bypass_used": False,
    }

    small_docs = {}
    for k in (
        "fmcsa_docs",
        "fmcsa_inspection_catalog",
        "fmcsa_violation_catalog",
        "phmsa_catalog",
        "phmsa_stats",
        "phmsa_dictionary",
        "phmsa_search",
    ):
        r = b.retry(b.URLS[k], attempts=2, timeout=60, max_bytes=8_000_000)
        small_docs[k] = r
        audits[k] = b.audit(r)

    insp_schema_resp = b.retry(b.URLS["fmcsa_inspection_schema"], attempts=3, timeout=60, max_bytes=4_000_000)
    viol_schema_resp = b.retry(b.URLS["fmcsa_violation_schema"], attempts=3, timeout=60, max_bytes=4_000_000)
    audits["fmcsa_inspection_schema"] = b.audit(insp_schema_resp)
    audits["fmcsa_violation_schema"] = b.audit(viol_schema_resp)

    implementation_error = None
    fmcsa = {
        "schema_complete": False,
        "violation_linkage_ready": False,
        "distinct_valid_usdot_carriers": 0,
        "repeated_inspection_carriers": 0,
        "max_inspections_per_carrier": 0,
        "carrier_fingerprint": None,
    }
    fmcsa_carriers: set[str] = set()
    query_audits: list[dict] = []

    try:
        if not (insp_schema_resp["ok"] and viol_schema_resp["ok"]):
            raise RuntimeError("FMCSA schema metadata unavailable")
        insp_cols = json.loads(insp_schema_resp["data"].decode("utf-8"))
        viol_cols = json.loads(viol_schema_resp["data"].decode("utf-8"))
        if not isinstance(insp_cols, list) or not isinstance(viol_cols, list):
            raise RuntimeError("FMCSA schema metadata not column lists")

        # `dot_number` is the current native field observed in the official
        # fx4q-ay7w schema. It is an alias of the preregistered USDOT identity,
        # not a different identifier or source.
        c_usdot = b.choose_col(
            insp_cols,
            ["DOT_NUMBER", "DOT_NUM", "USDOT_NUM", "USDOT_NUMBER", "US_DOT_NUM", "US DOT NUMBER", "U.S. DOT#"],
            [["dot", "number"], ["usdot"]],
        )
        c_iid = b.choose_col(insp_cols, ["INSPECTION_ID", "Inspection ID"], [["inspection", "id"]])
        c_date = b.choose_col(insp_cols, ["INSPECTION_DATE", "Inspection Date", "INSP_DATE"], [["inspection", "date"], ["insp", "date"]])
        v_iid = b.choose_col(viol_cols, ["INSPECTION_ID", "Inspection ID"], [["inspection", "id"]])
        v_oos = b.choose_col(viol_cols, ["OUT_OF_SERVICE", "OOS", "OOS_IND", "Out-of-Service"], [["out", "service"], ["oos"]])

        f_usdot, f_iid, f_date, f_viid = map(b.field, (c_usdot, c_iid, c_date, v_iid))
        f_oos = b.field(v_oos)
        fmcsa["field_map"] = {
            "usdot": f_usdot,
            "inspection_id": f_iid,
            "inspection_date": f_date,
            "violation_inspection_id": f_viid,
            "violation_oos": f_oos,
        }
        fmcsa["inspection_schema_column_count"] = len(insp_cols)
        fmcsa["violation_schema_column_count"] = len(viol_cols)
        fmcsa["inspection_schema_fields"] = [str(c.get("fieldName") or "") for c in insp_cols]
        fmcsa["violation_schema_fields"] = [str(c.get("fieldName") or "") for c in viol_cols]
        fmcsa["schema_complete"] = all((f_usdot, f_iid, f_date, f_viid, f_oos))
        if not fmcsa["schema_complete"]:
            raise RuntimeError(f"FMCSA required field mapping incomplete: {fmcsa['field_map']}")

        fmcsa_carriers, repeated, max_rows, valid_rows, qa = b.group_carriers(b.FMCSA_INSPECTION_ID, f_usdot)
        query_audits.extend(qa)
        fmcsa["distinct_valid_usdot_carriers"] = len(fmcsa_carriers)
        fmcsa["repeated_inspection_carriers"] = repeated
        fmcsa["max_inspections_per_carrier"] = max_rows
        fmcsa["valid_usdot_inspection_rows"] = valid_rows
        fmcsa["carrier_fingerprint"] = b.fingerprint(fmcsa_carriers)

        ds, qa = b.date_support(
            b.FMCSA_INSPECTION_ID,
            f_usdot,
            f_date,
            str(c_date.get("dataTypeName") or ""),
        )
        fmcsa.update(ds)
        query_audits.extend(qa)

        distinct_iids, a = b.scalar_count(
            b.FMCSA_INSPECTION_ID,
            f"{f_iid} is not null",
            f"count(distinct {f_iid}) as n",
        )
        query_audits.append(a)
        fmcsa["distinct_inspection_ids"] = distinct_iids

        viol_total, a = b.scalar_count(b.FMCSA_VIOLATION_ID)
        query_audits.append(a)
        viol_linked, a = b.scalar_count(b.FMCSA_VIOLATION_ID, f"{f_viid} is not null")
        query_audits.append(a)
        viol_distinct, a = b.scalar_count(
            b.FMCSA_VIOLATION_ID,
            f"{f_viid} is not null",
            f"count(distinct {f_viid}) as n",
        )
        query_audits.append(a)
        mult_rows, a = b.socrata_query(
            b.FMCSA_VIOLATION_ID,
            {
                "$select": f"{f_viid}, count(*) as n",
                "$where": f"{f_viid} is not null",
                "$group": f_viid,
                "$order": "n DESC",
                "$limit": 1,
            },
        )
        query_audits.append(a)
        max_viol = int(float(mult_rows[0].get("n", 0))) if mult_rows else 0
        fmcsa["violation_rows"] = viol_total
        fmcsa["violation_rows_with_inspection_id"] = viol_linked
        fmcsa["violation_inspection_id_nonnull_rate"] = (viol_linked / viol_total) if viol_total else 0.0
        fmcsa["distinct_violation_inspection_ids"] = viol_distinct
        fmcsa["max_violation_rows_per_inspection_id"] = max_viol
        fmcsa["violation_linkage_ready"] = bool(f_viid and f_oos and viol_linked > 0 and viol_distinct > 0)
    except Exception as e:
        implementation_error = f"{type(e).__name__}: {e}"

    audits["fmcsa_query_audits"] = query_audits

    # The preregistered PARTIAL distinguishes documented PHMSA semantics from
    # inability to retrieve the Oracle detailed export. Thus the search/export
    # route itself is not required to be reachable for `docs_reachable`.
    phmsa_docs_ready = all(small_docs[k]["ok"] for k in ("phmsa_catalog", "phmsa_dictionary"))
    catalog_text = b.html_text(small_docs["phmsa_catalog"]["data"]).lower() if small_docs["phmsa_catalog"]["ok"] else ""
    search_text = b.html_text(small_docs["phmsa_search"]["data"]).lower() if small_docs["phmsa_search"]["ok"] else ""
    phmsa_export_semantics = (
        "export" in catalog_text and "text file" in catalog_text
    ) or (
        "incident detailed report" in search_text and ("download" in search_text or "export" in search_text)
    )

    phmsa_export = None
    export_attempts = []
    candidates = b.phmsa_export_candidates(small_docs["phmsa_search"])
    audits["phmsa_discovered_export_candidate_count"] = len(candidates)
    audits["phmsa_discovered_export_candidates"] = candidates
    for u in candidates:
        r = b.retry(u, attempts=1, timeout=120, max_bytes=250_000_000)
        export_attempts.append(b.audit(r))
        if not r["ok"]:
            continue
        ct = (r["headers"].get("Content-Type", "") or "").lower()
        cd = (r["headers"].get("Content-Disposition", "") or "").lower()
        ev = b.parse_phmsa_export(r["data"], ct)
        if ev and ev.get("schema_complete") and ("attachment" in cd or any(x in ct for x in ("csv", "text", "excel", "html"))):
            phmsa_export = {"url": u, "response": r, "eval": ev}
            break
    audits["phmsa_export_attempts"] = export_attempts

    phmsa = {
        "docs_reachable": phmsa_docs_ready,
        "public_export_semantics_documented": phmsa_export_semantics,
        "export_bytes_accessible": phmsa_export is not None,
        "required_schema_present": False,
        "distinct_highway_fed_dot_ids": None,
        "date_parse_rate": None,
        "date_years": None,
        "distinct_date_years": None,
        "carrier_fingerprint": None,
    }
    phmsa_carriers: set[str] = set()
    if phmsa_export is not None:
        ev = phmsa_export["eval"]
        phmsa["required_schema_present"] = bool(ev.get("schema_complete"))
        for k in (
            "format",
            "headers",
            "highway_rows_with_valid_fed_dot_id",
            "distinct_highway_fed_dot_ids",
            "date_parse_rate",
            "date_years",
            "distinct_date_years",
            "distinct_report_numbers",
            "reports_with_multiple_rows",
            "max_rows_per_report",
        ):
            phmsa[k] = ev.get(k)
        phmsa_carriers = set(ev.get("carriers") or set())
        phmsa["carrier_fingerprint"] = b.fingerprint(phmsa_carriers)
        audits["phmsa_selected_export"] = b.audit(phmsa_export["response"])

    intersection = fmcsa_carriers & phmsa_carriers if phmsa_export is not None else set()

    # Authoritative machine-readable metadata for F01 are the official DOT
    # Data.gov catalogs + schema endpoints and the official PHMSA catalog +
    # dictionary. Bot-blocked agency prose pages remain audited but are not the
    # sole source of required semantics.
    docs_req = all((
        small_docs["fmcsa_inspection_catalog"]["ok"],
        small_docs["fmcsa_violation_catalog"]["ok"],
        insp_schema_resp["ok"],
        viol_schema_resp["ok"],
        small_docs["phmsa_catalog"]["ok"],
        small_docs["phmsa_dictionary"]["ok"],
    ))

    req = {
        "official_metadata_documentation_reachable_fingerprinted": docs_req,
        "fmcsa_inspection_machine_readable": implementation_error is None and bool(fmcsa.get("schema_complete")),
        "fmcsa_violation_machine_readable": implementation_error is None and bool(fmcsa.get("violation_linkage_ready")),
        "fmcsa_required_native_fields_present": bool(fmcsa.get("schema_complete")),
        "fmcsa_distinct_usdot_ge_50000": int(fmcsa.get("distinct_valid_usdot_carriers") or 0) >= 50000,
        "fmcsa_date_support_ge_3_years_and_95pct": float(fmcsa.get("date_parse_rate") or 0) >= 0.95 and int(fmcsa.get("distinct_date_years") or 0) >= 3,
        "phmsa_detailed_export_publicly_executable": phmsa_export is not None,
        "phmsa_required_fields_present": bool(phmsa.get("required_schema_present")),
        "phmsa_highway_fed_dot_ids_ge_500": int(phmsa.get("distinct_highway_fed_dot_ids") or 0) >= 500,
        "phmsa_date_support_ge_10_years_and_95pct": float(phmsa.get("date_parse_rate") or 0) >= 0.95 and int(phmsa.get("distinct_date_years") or 0) >= 10,
        "exact_carrier_intersection_ge_300": len(intersection) >= 300,
        "fmcsa_violation_oos_linkage_deterministic": bool(fmcsa.get("violation_linkage_ready")),
        "three_identity_fingerprints_persisted": bool(fmcsa.get("carrier_fingerprint") and phmsa.get("carrier_fingerprint") and b.fingerprint(intersection)),
        "public_cohort_boundary_preserved": True,
        "outcome_boundary_preserved": True,
        "carrier_level_join_membership_not_persisted": True,
        "relationship_prediction_causality_closed": True,
        "zero_cost_no_bypass": True,
    }

    fm_empirical_for_partial = all(req[k] for k in (
        "official_metadata_documentation_reachable_fingerprinted",
        "fmcsa_inspection_machine_readable",
        "fmcsa_violation_machine_readable",
        "fmcsa_required_native_fields_present",
        "fmcsa_distinct_usdot_ge_50000",
        "fmcsa_date_support_ge_3_years_and_95pct",
        "fmcsa_violation_oos_linkage_deterministic",
    ))

    if implementation_error is not None:
        gate = b.INVALID
        valid_execution = False
    elif all(req.values()):
        gate = b.PASS
        valid_execution = True
    elif fm_empirical_for_partial and phmsa_docs_ready and phmsa_export_semantics and phmsa_export is None:
        gate = b.PARTIAL
        valid_execution = True
    else:
        gate = b.HOLD
        valid_execution = True

    result = {
        "research_id": "US-FMCSA-HAZ-F01",
        "issue": 145,
        "corrects_run": CORRECTS_RUN,
        "gate": gate,
        "valid_execution": valid_execution,
        "implementation_error": implementation_error,
        "fmcsa": fmcsa,
        "phmsa": phmsa,
        "aggregate_exact_carrier_intersection": len(intersection) if phmsa_export is not None else None,
        "fingerprints": {
            "fmcsa_usdot_carriers": fmcsa.get("carrier_fingerprint"),
            "phmsa_highway_fed_dot_ids": phmsa.get("carrier_fingerprint"),
            "intersection": b.fingerprint(intersection) if phmsa_export is not None else None,
        },
        "requirements": req,
        "phmsa_export_access_only_partial_condition": {
            "fmcsa_empirical_requirements_pass": fm_empirical_for_partial,
            "phmsa_docs_reachable": phmsa_docs_ready,
            "phmsa_public_export_semantics_documented": phmsa_export_semantics,
            "phmsa_export_bytes_accessible": phmsa_export is not None,
        },
        "hazmat_incident_occurrence_by_inspection_profile_opened": False,
        "future_incident_membership_conditioned_on_fmcsa_opened": False,
        "carrier_level_join_membership_persisted": False,
        "relationship_computed": False,
        "predictive_metric_computed": False,
        "causal_claim_made": False,
        "federal_safety_rating_claim_made": False,
        "unofficial_mirror_used": False,
        "authentication_bypass_used": False,
        "post_execution_rescue_used": False,
        "incremental_monetary_cost_usd": 0,
    }

    audits["source_boundary"] = {
        "fmcsa_dataset_ids": [b.FMCSA_INSPECTION_ID, b.FMCSA_VIOLATION_ID],
        "phmsa_source": "Form 5800.1 official public Incident Detailed Report/export only",
        "no_unofficial_mirror": True,
        "no_authentication_bypass": True,
        "raw_source_bytes_persisted": False,
        "carrier_level_join_membership_persisted": False,
    }

    (OUT / "STAGING_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "STAGING_SOURCE_AUDIT.json").write_text(json.dumps(audits, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "corrects_run": CORRECTS_RUN,
        "gate": gate,
        "valid_execution": valid_execution,
        "fmcsa_carriers": fmcsa.get("distinct_valid_usdot_carriers"),
        "fmcsa_years": fmcsa.get("distinct_date_years"),
        "phmsa_export_accessible": phmsa.get("export_bytes_accessible"),
        "phmsa_carriers": phmsa.get("distinct_highway_fed_dot_ids"),
        "intersection": len(intersection) if phmsa_export is not None else None,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
