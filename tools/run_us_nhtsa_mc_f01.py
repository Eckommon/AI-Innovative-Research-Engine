#!/usr/bin/env python3
"""US-NHTSA-MC-F01 outcome-blind source/schema/product-time feasibility gate.

Only frozen official NHTSA sources are used. This runner never derives recall
incidence by communication-derived groups and never derives future-recall
membership conditional on communication history.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import unicodedata
import urllib.error
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-NHTSA-MC-F01"
UA = "AI-Innovative-Research-Engine/US-NHTSA-MC-F01 outcome-blind"

URLS = {
    "catalog": "https://www.nhtsa.gov/nhtsa-datasets-and-apis",
    "comm_dictionary": "https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS.txt",
    "recall_dictionary": "https://static.nhtsa.gov/odi/ffdd/rcl/RCL.txt",
    "comm_2020_2024": "https://static.nhtsa.gov/odi/ffdd/tsbs/MFR_COMMS_RECEIVED_2020-2024.zip",
    "comm_2025_2026": "https://static.nhtsa.gov/odi/ffdd/tsbs/MFR_COMMS_RECEIVED_2025-2026.zip",
    "recall_post_2010": "https://static.nhtsa.gov/odi/ffdd/rcl/FLAT_RCL_POST_2010.zip",
}

COMM_ALIASES = {
    "nhtsa_id": {"nhtsaidnumber", "id"},
    "document_id": {"tsbdocumentid", "bulno"},
    "mfr_date": {"mfrcommunicationdate", "buldte"},
    "file_date": {"dateaddedtofile", "datee"},
    "make": {"make", "maketxt"},
    "model": {"model", "modeltxt"},
    "year": {"modelyear", "yeartxt"},
}

RECALL_MIN_FIELDS = 16
# Current/legacy official RCL flat-file positions, zero-based:
# 1 RECORD_ID, 2 CAMPNO, 3 MAKETXT, 4 MODELTXT, 5 YEARTXT, ... 16 RCDATE.
RECALL_IDX = {"campaign": 1, "make": 2, "model": 3, "year": 4, "date": 15}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def request(url: str, timeout: int = 120) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
            return {
                "ok": True,
                "http": getattr(r, "status", 200),
                "url": url,
                "final_url": r.geturl(),
                "headers": dict(r.headers),
                "data": data,
                "error": None,
            }
    except urllib.error.HTTPError as e:
        body = e.read(8192)
        return {
            "ok": False,
            "http": e.code,
            "url": url,
            "final_url": getattr(e, "url", url),
            "headers": dict(e.headers or {}),
            "data": body,
            "error": "HTTPError",
        }
    except Exception as e:
        return {
            "ok": False,
            "http": None,
            "url": url,
            "final_url": url,
            "headers": {},
            "data": b"",
            "error": type(e).__name__,
        }


def retry(url: str, attempts: int = 3, timeout: int = 120) -> dict:
    last = None
    for _ in range(attempts):
        last = request(url, timeout=timeout)
        if last["ok"]:
            return last
    assert last is not None
    return last


def audit_response(resp: dict) -> dict:
    return {
        "url": resp["url"],
        "final_url": resp["final_url"],
        "http": resp["http"],
        "bytes": len(resp["data"]),
        "sha256": sha256(resp["data"]),
        "content_type": resp["headers"].get("Content-Type", ""),
        "error": resp["error"],
    }


def decode_text(data: bytes) -> tuple[str, str]:
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return data.decode(enc), enc
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", errors="replace"), "utf-8-replace"


def header_token(value: object) -> str:
    s = unicodedata.normalize("NFKC", str(value or "")).strip().lower()
    return re.sub(r"[^a-z0-9]+", "", s)


def norm_text(value: object) -> str:
    s = unicodedata.normalize("NFKC", str(value or ""))
    s = re.sub(r"\s+", " ", s.strip())
    return s.upper()


def valid_year(value: object) -> str | None:
    s = unicodedata.normalize("NFKC", str(value or "")).strip()
    if re.fullmatch(r"\d{4}", s) and s != "9999":
        return s
    return None


def product_key(year: object, make: object, model: object) -> str | None:
    y = valid_year(year)
    mk = norm_text(make)
    md = norm_text(model)
    if not y or not mk or not md:
        return None
    return f"{y}|{mk}|{md}"


def parse_date(value: object) -> datetime | None:
    s = unicodedata.normalize("NFKC", str(value or "")).strip()
    if not s:
        return None
    candidates = [s]
    if len(s) >= 10:
        candidates.append(s[:10])
    if len(s) >= 8:
        candidates.append(s[:8])
    seen = set()
    for x in candidates:
        if x in seen:
            continue
        seen.add(x)
        for fmt in ("%Y%m%d", "%Y-%m-%d", "%m/%d/%Y", "%Y/%m/%d", "%m/%d/%y"):
            try:
                return datetime.strptime(x, fmt)
            except ValueError:
                pass
    return None


def key_fingerprint(keys: set[str]) -> str | None:
    if not keys:
        return None
    canonical = ("\n".join(sorted(keys)) + "\n").encode("utf-8")
    return sha256(canonical)


def choose_zip_member(z: zipfile.ZipFile, prefer_csv: bool) -> str | None:
    names = [n for n in z.namelist() if not n.endswith("/")]
    if prefer_csv:
        csvs = [n for n in names if n.lower().endswith(".csv")]
        if csvs:
            return max(csvs, key=lambda n: z.getinfo(n).file_size)
    texts = [n for n in names if n.lower().endswith((".txt", ".tsv", ".lst", ".csv"))]
    if texts:
        return max(texts, key=lambda n: z.getinfo(n).file_size)
    return max(names, key=lambda n: z.getinfo(n).file_size) if names else None


def detect_delimiter(sample: str) -> str:
    first = sample.splitlines()[0] if sample.splitlines() else ""
    if "\t" in first:
        return "\t"
    try:
        return csv.Sniffer().sniff(sample[:8192], delimiters=",\t|;").delimiter
    except csv.Error:
        return ","


def find_header_map(fieldnames: list[str]) -> dict[str, str | None]:
    token_to_original = {header_token(x): x for x in fieldnames}
    result: dict[str, str | None] = {}
    for logical, aliases in COMM_ALIASES.items():
        result[logical] = next((token_to_original[a] for a in aliases if a in token_to_original), None)
    return result


def parse_communications_zip(label: str, data: bytes) -> tuple[dict, set[str], set[str], set[str], Counter, dict]:
    z = zipfile.ZipFile(io.BytesIO(data))
    member = choose_zip_member(z, prefer_csv=True)
    if member is None:
        raise RuntimeError(f"{label}: no parseable file member")
    raw = z.read(member)
    text, encoding = decode_text(raw)
    delim = detect_delimiter(text)
    reader = csv.DictReader(io.StringIO(text), delimiter=delim)
    fieldnames = [str(x or "") for x in (reader.fieldnames or [])]
    hmap = find_header_map(fieldnames)
    required = ("nhtsa_id", "document_id", "make", "model", "year")
    schema_complete = all(hmap.get(k) for k in required) and bool(hmap.get("mfr_date") or hmap.get("file_date"))

    product_keys: set[str] = set()
    makes: set[str] = set()
    communication_ids: set[str] = set()
    doc_ids: set[str] = set()
    product_doc_counts: Counter = Counter()
    valid_product_rows = 0
    date_parse_success = 0
    date_years: set[int] = set()
    total_rows = 0
    exact_rows_seen: set[tuple[str, str, str]] = set()
    exact_duplicate_rows = 0

    if schema_complete:
        for row in reader:
            total_rows += 1
            key = product_key(row.get(hmap["year"] or ""), row.get(hmap["make"] or ""), row.get(hmap["model"] or ""))
            if not key:
                continue
            valid_product_rows += 1
            product_keys.add(key)
            makes.add(key.split("|", 2)[1])
            nhtsa_id = norm_text(row.get(hmap["nhtsa_id"] or ""))
            doc_id = norm_text(row.get(hmap["document_id"] or ""))
            if nhtsa_id:
                communication_ids.add(nhtsa_id)
            if doc_id:
                doc_ids.add(doc_id)
            source_id = nhtsa_id or doc_id
            if source_id:
                structural = (source_id, doc_id, key)
                if structural in exact_rows_seen:
                    exact_duplicate_rows += 1
                else:
                    exact_rows_seen.add(structural)
                product_doc_counts[key] += 1
            raw_date = row.get(hmap["mfr_date"] or "") if hmap.get("mfr_date") else ""
            if not str(raw_date or "").strip() and hmap.get("file_date"):
                raw_date = row.get(hmap["file_date"] or "")
            dt = parse_date(raw_date)
            if dt is not None:
                date_parse_success += 1
                date_years.add(dt.year)

    audit = {
        "label": label,
        "zip_members": z.namelist(),
        "selected_member": member,
        "selected_member_bytes": len(raw),
        "selected_member_sha256": sha256(raw),
        "encoding": encoding,
        "delimiter": "TAB" if delim == "\t" else delim,
        "fieldnames": fieldnames,
        "field_map": hmap,
        "schema_complete": schema_complete,
    }
    stats = {
        "total_rows": total_rows,
        "valid_product_rows": valid_product_rows,
        "date_parse_success": date_parse_success,
        "date_parse_rate": (date_parse_success / valid_product_rows if valid_product_rows else 0.0),
        "date_years": sorted(date_years),
        "exact_duplicate_rows": exact_duplicate_rows,
    }
    return audit, product_keys, makes, communication_ids | doc_ids, product_doc_counts, stats


def parse_recall_zip(data: bytes) -> tuple[dict, set[str], set[str], set[str], dict]:
    z = zipfile.ZipFile(io.BytesIO(data))
    member = choose_zip_member(z, prefer_csv=False)
    if member is None:
        raise RuntimeError("recall: no parseable file member")
    raw = z.read(member)
    text, encoding = decode_text(raw)
    lines = text.splitlines()
    product_keys: set[str] = set()
    makes: set[str] = set()
    campaigns: set[str] = set()
    date_years: set[int] = set()
    valid_product_rows = 0
    date_parse_success = 0
    total_rows = 0
    malformed_short_rows = 0
    observed_max_fields = 0

    for row in csv.reader(lines, delimiter="\t"):
        if not row or not any(str(x).strip() for x in row):
            continue
        total_rows += 1
        observed_max_fields = max(observed_max_fields, len(row))
        # Be tolerant of an unexpected header row, but never infer alternate positions.
        if header_token(row[0]) in {"recordid", "record_id"} or (len(row) > 1 and header_token(row[1]) == "campno"):
            continue
        if len(row) < RECALL_MIN_FIELDS:
            malformed_short_rows += 1
            continue
        key = product_key(row[RECALL_IDX["year"]], row[RECALL_IDX["make"]], row[RECALL_IDX["model"]])
        if not key:
            continue
        valid_product_rows += 1
        product_keys.add(key)
        makes.add(key.split("|", 2)[1])
        campaign = norm_text(row[RECALL_IDX["campaign"]])
        if campaign:
            campaigns.add(campaign)
        dt = parse_date(row[RECALL_IDX["date"]])
        if dt is not None:
            date_parse_success += 1
            date_years.add(dt.year)

    schema_structurally_readable = observed_max_fields >= RECALL_MIN_FIELDS and valid_product_rows > 0
    audit = {
        "zip_members": z.namelist(),
        "selected_member": member,
        "selected_member_bytes": len(raw),
        "selected_member_sha256": sha256(raw),
        "encoding": encoding,
        "delimiter": "TAB",
        "frozen_field_positions_zero_based": RECALL_IDX,
        "observed_max_fields": observed_max_fields,
        "schema_structurally_readable": schema_structurally_readable,
    }
    stats = {
        "total_rows": total_rows,
        "valid_product_rows": valid_product_rows,
        "date_parse_success": date_parse_success,
        "date_parse_rate": (date_parse_success / valid_product_rows if valid_product_rows else 0.0),
        "date_years": sorted(date_years),
        "malformed_short_rows": malformed_short_rows,
    }
    return audit, product_keys, makes, campaigns, stats


def dictionary_semantics(comm_text: str, recall_text: str) -> dict:
    ct = comm_text.lower()
    rt = recall_text.lower()
    return {
        "communication_dictionary_fields_confirmed": all(x in ct for x in (
            "nhtsa id number", "tsb/document id", "mfr communication date", "make", "model", "model year"
        )),
        "communication_csv_product_row_semantics_confirmed": "one record per tsb/document id per product" in ct,
        "communication_unknown_year_9999_confirmed": "9999 if unknown" in ct,
        "recall_dictionary_campaign_confirmed": "campno" in rt or "campaign" in rt,
        "recall_dictionary_make_model_year_confirmed": all(x in rt for x in ("maketxt", "modeltxt", "yeartxt")),
        "recall_dictionary_rcdate_confirmed": "rcdate" in rt,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    responses = {name: retry(url) for name, url in URLS.items()}
    source_audit = {name: audit_response(resp) for name, resp in responses.items()}
    all_sources_ok = all(resp["ok"] for resp in responses.values())

    comm_dict_text, comm_dict_encoding = decode_text(responses["comm_dictionary"]["data"]) if responses["comm_dictionary"]["ok"] else ("", None)
    recall_dict_text, recall_dict_encoding = decode_text(responses["recall_dictionary"]["data"]) if responses["recall_dictionary"]["ok"] else ("", None)
    semantics = dictionary_semantics(comm_dict_text, recall_dict_text)
    source_audit["comm_dictionary"]["decoded_encoding"] = comm_dict_encoding
    source_audit["recall_dictionary"]["decoded_encoding"] = recall_dict_encoding

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
    recall_stats = {"total_rows": 0, "valid_product_rows": 0, "date_parse_success": 0, "date_parse_rate": 0.0, "date_years": []}

    try:
        if all_sources_ok:
            for label in ("comm_2020_2024", "comm_2025_2026"):
                a, keys, makes, ids, product_docs, stats = parse_communications_zip(label, responses[label]["data"])
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

            recall_audit, recall_product_keys, recall_makes, recall_campaigns, recall_stats = parse_recall_zip(responses["recall_post_2010"]["data"])
    except (zipfile.BadZipFile, csv.Error, RuntimeError, ValueError, IndexError) as e:
        parse_error = f"{type(e).__name__}: {e}"

    comm_date_rate = comm_date_success / comm_valid_product_rows if comm_valid_product_rows else 0.0
    overlap_keys = comm_product_keys & recall_product_keys

    multiplicity = {
        "product_keys_with_multiple_communication_rows_or_ids": sum(1 for n in comm_product_docs.values() if n > 1),
        "max_communication_rows_or_ids_per_product_key": max(comm_product_docs.values(), default=0),
        "distinct_communication_or_document_ids": len(comm_ids),
        "distinct_recall_campaign_ids": len(recall_campaigns),
    }

    valid_execution = all_sources_ok and parse_error is None and comm_schema_complete and bool(recall_audit and recall_audit["schema_structurally_readable"])

    req = {
        "official_metadata_dictionaries_reachable_hashed": all(responses[k]["ok"] for k in ("catalog", "comm_dictionary", "recall_dictionary")) and all(semantics.values()),
        "all_frozen_zip_sources_readable_hashed": all(responses[k]["ok"] for k in ("comm_2020_2024", "comm_2025_2026", "recall_post_2010")) and parse_error is None,
        "communication_schema_verified": comm_schema_complete,
        "recall_schema_verified": bool(recall_audit and recall_audit["schema_structurally_readable"]) and semantics["recall_dictionary_campaign_confirmed"] and semantics["recall_dictionary_make_model_year_confirmed"] and semantics["recall_dictionary_rcdate_confirmed"],
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
            "communication_product_keys": key_fingerprint(comm_product_keys),
            "recall_product_keys": key_fingerprint(recall_product_keys),
            "intersection_product_keys": key_fingerprint(overlap_keys),
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

    (OUT / "STAGING_SOURCE_AUDIT.json").write_text(json.dumps(source_audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "STAGING_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "gate": gate,
        "valid_execution": valid_execution,
        "comm_keys": len(comm_product_keys),
        "recall_keys": len(recall_product_keys),
        "overlap": len(overlap_keys),
        "comm_date_rate": round(comm_date_rate, 6),
        "recall_date_rate": round(recall_stats.get("date_parse_rate", 0.0), 6),
        "parse_error": parse_error,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
