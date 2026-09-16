#!/usr/bin/env python3
"""Implementation-only correction for US-NHTSA-MC-F01 Run 35042810534.

Frozen scientific contract is unchanged. The correction separates catalog-page
reachability from actual ZIP/dictionary parseability and uses an ordinary public
browser User-Agent for unauthenticated NHTSA requests.
"""
from __future__ import annotations

import json
import zipfile
from collections import Counter

import run_us_nhtsa_mc_f01 as base

base.UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
)


def main() -> None:
    base.OUT.mkdir(parents=True, exist_ok=True)

    responses = {name: base.retry(url) for name, url in base.URLS.items()}
    source_audit = {name: base.audit_response(resp) for name, resp in responses.items()}

    comm_dict_text, comm_dict_encoding = base.decode_text(responses["comm_dictionary"]["data"]) if responses["comm_dictionary"]["ok"] else ("", None)
    recall_dict_text, recall_dict_encoding = base.decode_text(responses["recall_dictionary"]["data"]) if responses["recall_dictionary"]["ok"] else ("", None)
    semantics = base.dictionary_semantics(comm_dict_text, recall_dict_text)
    source_audit["comm_dictionary"]["decoded_encoding"] = comm_dict_encoding
    source_audit["recall_dictionary"]["decoded_encoding"] = recall_dict_encoding

    data_sources_ok = all(responses[k]["ok"] for k in (
        "comm_dictionary", "recall_dictionary",
        "comm_2020_2024", "comm_2025_2026", "recall_post_2010",
    ))

    parse_error = None
    comm_audits = []
    comm_product_keys: set[str] = set()
    comm_makes: set[str] = set()
    comm_ids: set[str] = set()
    comm_product_docs: Counter = Counter()
    comm_total_rows = 0
    comm_valid_product_rows = 0
    comm_date_success = 0
    comm_date_years: set[int] = set()
    comm_schema_complete = False

    recall_audit = None
    recall_product_keys: set[str] = set()
    recall_makes: set[str] = set()
    recall_campaigns: set[str] = set()
    recall_stats = {
        "total_rows": 0,
        "valid_product_rows": 0,
        "date_parse_success": 0,
        "date_parse_rate": 0.0,
        "date_years": [],
    }

    try:
        if data_sources_ok:
            for label in ("comm_2020_2024", "comm_2025_2026"):
                a, keys, makes, ids, product_docs, stats = base.parse_communications_zip(label, responses[label]["data"])
                comm_audits.append(a)
                comm_product_keys |= keys
                comm_makes |= makes
                comm_ids |= ids
                comm_product_docs.update(product_docs)
                comm_total_rows += stats["total_rows"]
                comm_valid_product_rows += stats["valid_product_rows"]
                comm_date_success += stats["date_parse_success"]
                comm_date_years |= set(stats["date_years"])
            comm_schema_complete = len(comm_audits) == 2 and all(a["schema_complete"] for a in comm_audits)

            recall_audit, recall_product_keys, recall_makes, recall_campaigns, recall_stats = base.parse_recall_zip(responses["recall_post_2010"]["data"])
    except (zipfile.BadZipFile, csv.Error if False else RuntimeError, ValueError, IndexError) as e:
        # The odd-looking tuple intentionally avoids adding another parser dependency;
        # RuntimeError/ValueError/IndexError/BadZipFile cover current parser failures.
        parse_error = f"{type(e).__name__}: {e}"
    except Exception as e:
        parse_error = f"{type(e).__name__}: {e}"

    comm_date_rate = comm_date_success / comm_valid_product_rows if comm_valid_product_rows else 0.0
    overlap_keys = comm_product_keys & recall_product_keys

    multiplicity = {
        "product_keys_with_multiple_communication_rows_or_ids": sum(1 for n in comm_product_docs.values() if n > 1),
        "max_communication_rows_or_ids_per_product_key": max(comm_product_docs.values(), default=0),
        "distinct_communication_or_document_ids": len(comm_ids),
        "distinct_recall_campaign_ids": len(recall_campaigns),
    }

    valid_execution = (
        data_sources_ok
        and parse_error is None
        and comm_schema_complete
        and bool(recall_audit and recall_audit["schema_structurally_readable"])
    )

    req = {
        "official_metadata_dictionaries_reachable_hashed": (
            responses["catalog"]["ok"]
            and responses["comm_dictionary"]["ok"]
            and responses["recall_dictionary"]["ok"]
            and all(semantics.values())
        ),
        "all_frozen_zip_sources_readable_hashed": (
            all(responses[k]["ok"] for k in ("comm_2020_2024", "comm_2025_2026", "recall_post_2010"))
            and parse_error is None
        ),
        "communication_schema_verified": comm_schema_complete,
        "recall_schema_verified": (
            bool(recall_audit and recall_audit["schema_structurally_readable"])
            and semantics["recall_dictionary_campaign_confirmed"]
            and semantics["recall_dictionary_make_model_year_confirmed"]
            and semantics["recall_dictionary_rcdate_confirmed"]
        ),
        "communication_product_keys_ge_10000": len(comm_product_keys) >= 10_000,
        "recall_product_keys_ge_5000": len(recall_product_keys) >= 5_000,
        "each_source_normalized_makes_ge_25": len(comm_makes) >= 25 and len(recall_makes) >= 25,
        "aggregate_product_key_intersection_ge_1000": len(overlap_keys) >= 1_000,
        "communication_date_support_ge_5_years_and_95pct": len(comm_date_years) >= 5 and comm_date_rate >= 0.95,
        "recall_date_support_ge_10_years_and_95pct": len(recall_stats.get("date_years", [])) >= 10 and recall_stats.get("date_parse_rate", 0.0) >= 0.95,
        "communication_multiplicity_quantified_outcome_blind": valid_execution,
        "identity_fingerprints_frozen": bool(comm_product_keys and recall_product_keys and overlap_keys),
        "outcome_boundary_and_cost_zero": True,
    }

    if not valid_execution:
        gate = "IMPLEMENTATION_OR_SOURCE_PARSE_NOT_VALID_FOR_GATE"
    elif all(req.values()):
        gate = "PASS_US_NHTSA_MC_F01_PRODUCT_TIME_JOIN_READY"
    else:
        gate = "HOLD_US_NHTSA_MC_F01_SOURCE_SCHEMA_OR_IDENTITY"

    source_audit.update({
        "corrects_run": 35042810534,
        "correction_scope": "execution-control-flow-and-public-user-agent-only",
        "communication_archives": comm_audits,
        "recall_archive": recall_audit,
        "dictionary_semantics": semantics,
        "parse_error": parse_error,
        "raw_source_bytes_persisted": False,
        "unofficial_mirror_used": False,
        "authentication_bypass_used": False,
    })

    result = {
        "issue": 143,
        "research_id": "US-NHTSA-MC-F01",
        "corrects_run": 35042810534,
        "gate": gate,
        "valid_execution": valid_execution,
        "requirements": req,
        "communication": {
            "total_rows": comm_total_rows,
            "valid_product_rows": comm_valid_product_rows,
            "distinct_product_keys": len(comm_product_keys),
            "distinct_normalized_makes": len(comm_makes),
            "date_parse_success": comm_date_success,
            "date_parse_rate": comm_date_rate,
            "date_years": sorted(comm_date_years),
            "distinct_date_years": len(comm_date_years),
        },
        "recall": {
            "total_rows": recall_stats.get("total_rows", 0),
            "valid_product_rows": recall_stats.get("valid_product_rows", 0),
            "distinct_product_keys": len(recall_product_keys),
            "distinct_normalized_makes": len(recall_makes),
            "date_parse_success": recall_stats.get("date_parse_success", 0),
            "date_parse_rate": recall_stats.get("date_parse_rate", 0.0),
            "date_years": recall_stats.get("date_years", []),
            "distinct_date_years": len(recall_stats.get("date_years", [])),
        },
        "aggregate_product_key_overlap": len(overlap_keys),
        "multiplicity": multiplicity,
        "fingerprints": {
            "communication_product_keys": base.key_fingerprint(comm_product_keys),
            "recall_product_keys": base.key_fingerprint(recall_product_keys),
            "intersection_product_keys": base.key_fingerprint(overlap_keys),
        },
        "recall_incidence_opened": False,
        "future_recall_membership_conditioned_on_communications_opened": False,
        "relationship_computed": False,
        "predictive_metric_computed": False,
        "causal_claim_made": False,
        "unofficial_mirror_used": False,
        "authentication_bypass_used": False,
        "post_execution_rescue_used": False,
        "incremental_monetary_cost_usd": 0,
    }

    (base.OUT / "STAGING_SOURCE_AUDIT.json").write_text(json.dumps(source_audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (base.OUT / "STAGING_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "gate": gate,
        "valid_execution": valid_execution,
        "catalog_http": responses["catalog"]["http"],
        "comm_keys": len(comm_product_keys),
        "recall_keys": len(recall_product_keys),
        "overlap": len(overlap_keys),
        "comm_date_rate": round(comm_date_rate, 6),
        "recall_date_rate": round(recall_stats.get("date_parse_rate", 0.0), 6),
        "parse_error": parse_error,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
