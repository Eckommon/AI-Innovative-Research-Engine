#!/usr/bin/env python3
"""Second implementation-only correction for US-NHTSA-MC-F01.

This version recognizes the frozen Manufacturer Communications CSV as a valid
product/document table even though it lacks the richer flat-file date fields.
That absence is evaluated as a frozen scientific/source-schema requirement,
not misclassified as parser invalidity.
"""
from __future__ import annotations

import csv
import io
import json
import zipfile
from collections import Counter

import run_us_nhtsa_mc_f01 as base

base.UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
)


def parse_comm_product_table(label: str, data: bytes):
    z = zipfile.ZipFile(io.BytesIO(data))
    member = base.choose_zip_member(z, prefer_csv=True)
    if member is None:
        raise RuntimeError(f"{label}: no parseable member")
    raw = z.read(member)
    text, encoding = base.decode_text(raw)
    delim = base.detect_delimiter(text)
    reader = csv.DictReader(io.StringIO(text), delimiter=delim)
    fieldnames = [str(x or "") for x in (reader.fieldnames or [])]
    hmap = base.find_header_map(fieldnames)

    structural_readable = all(hmap.get(k) for k in ("document_id", "make", "model", "year"))
    date_field_present = bool(hmap.get("mfr_date") or hmap.get("file_date"))
    nhtsa_id_present = bool(hmap.get("nhtsa_id"))
    full_frozen_required_schema = structural_readable and date_field_present

    product_keys: set[str] = set()
    makes: set[str] = set()
    doc_ids: set[str] = set()
    product_doc_counts: Counter = Counter()
    total_rows = 0
    valid_product_rows = 0
    date_parse_success = 0
    date_years: set[int] = set()
    exact_rows_seen: set[tuple[str, str]] = set()
    exact_duplicate_rows = 0

    if structural_readable:
        for row in reader:
            total_rows += 1
            key = base.product_key(
                row.get(hmap["year"] or ""),
                row.get(hmap["make"] or ""),
                row.get(hmap["model"] or ""),
            )
            if not key:
                continue
            valid_product_rows += 1
            product_keys.add(key)
            makes.add(key.split("|", 2)[1])
            doc_id = base.norm_text(row.get(hmap["document_id"] or ""))
            if doc_id:
                doc_ids.add(doc_id)
                structural = (doc_id, key)
                if structural in exact_rows_seen:
                    exact_duplicate_rows += 1
                else:
                    exact_rows_seen.add(structural)
                product_doc_counts[key] += 1

            raw_date = ""
            if hmap.get("mfr_date"):
                raw_date = row.get(hmap["mfr_date"] or "")
            if not str(raw_date or "").strip() and hmap.get("file_date"):
                raw_date = row.get(hmap["file_date"] or "")
            dt = base.parse_date(raw_date)
            if dt is not None:
                date_parse_success += 1
                date_years.add(dt.year)

    audit = {
        "label": label,
        "zip_members": z.namelist(),
        "selected_member": member,
        "selected_member_bytes": len(raw),
        "selected_member_sha256": base.sha256(raw),
        "encoding": encoding,
        "delimiter": "TAB" if delim == "\t" else delim,
        "fieldnames": fieldnames,
        "field_map": hmap,
        "structural_product_document_schema_readable": structural_readable,
        "communication_date_field_present": date_field_present,
        "nhtsa_id_field_present": nhtsa_id_present,
        "full_frozen_required_schema_present": full_frozen_required_schema,
    }
    stats = {
        "total_rows": total_rows,
        "valid_product_rows": valid_product_rows,
        "date_parse_success": date_parse_success,
        "date_parse_rate": (date_parse_success / valid_product_rows if valid_product_rows else 0.0),
        "date_years": sorted(date_years),
        "exact_duplicate_rows": exact_duplicate_rows,
    }
    return audit, product_keys, makes, doc_ids, product_doc_counts, stats


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
    comm_doc_ids: set[str] = set()
    comm_product_docs: Counter = Counter()
    comm_total_rows = 0
    comm_valid_product_rows = 0
    comm_date_success = 0
    comm_date_years: set[int] = set()
    comm_structurally_readable = False
    comm_full_required_schema = False

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
                a, keys, makes, docs, product_docs, stats = parse_comm_product_table(label, responses[label]["data"])
                comm_audits.append(a)
                comm_product_keys |= keys
                comm_makes |= makes
                comm_doc_ids |= docs
                comm_product_docs.update(product_docs)
                comm_total_rows += stats["total_rows"]
                comm_valid_product_rows += stats["valid_product_rows"]
                comm_date_success += stats["date_parse_success"]
                comm_date_years |= set(stats["date_years"])
            comm_structurally_readable = len(comm_audits) == 2 and all(a["structural_product_document_schema_readable"] for a in comm_audits)
            comm_full_required_schema = len(comm_audits) == 2 and all(a["full_frozen_required_schema_present"] for a in comm_audits)
            recall_audit, recall_product_keys, recall_makes, recall_campaigns, recall_stats = base.parse_recall_zip(responses["recall_post_2010"]["data"])
    except Exception as e:
        parse_error = f"{type(e).__name__}: {e}"

    comm_date_rate = comm_date_success / comm_valid_product_rows if comm_valid_product_rows else 0.0
    overlap_keys = comm_product_keys & recall_product_keys

    multiplicity = {
        "product_keys_with_multiple_communication_documents": sum(1 for n in comm_product_docs.values() if n > 1),
        "max_communication_documents_per_product_key": max(comm_product_docs.values(), default=0),
        "distinct_communication_document_ids": len(comm_doc_ids),
        "distinct_recall_campaign_ids": len(recall_campaigns),
    }

    valid_execution = (
        data_sources_ok
        and parse_error is None
        and comm_structurally_readable
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
        "communication_schema_verified": comm_full_required_schema,
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
        "corrects_runs": [35042810534, 35042957163],
        "correction_scope": "classify-readable-csv-separately-from-missing-frozen-date-schema",
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
        "corrects_runs": [35042810534, 35042957163],
        "gate": gate,
        "valid_execution": valid_execution,
        "requirements": req,
        "communication": {
            "structural_product_document_schema_readable": comm_structurally_readable,
            "full_frozen_required_schema_present": comm_full_required_schema,
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
