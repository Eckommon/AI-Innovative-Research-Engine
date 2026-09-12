#!/usr/bin/env python3
"""US-RCRA-E01 Pass 2 v3: resolve frozen selected CEI source duplicates outcome-independently.

Scientific contract is unchanged. Frozen selected identity is
(ID_NUMBER, CEI date, EVALUATION_IDENTIFIER). For duplicate source rows:
- code every duplicate's FOUND_VIOLATION using the preregistered Y/N/U/missing rule;
- if all duplicate rows agree on one coded class, use it;
- if they disagree, treat that selected CEI as DUPLICATE_CONFLICT_MISSING.
Agency sensitivity is restricted to pairs whose pre/post selected identities each
have exactly one nonblank agency and the same agency. Multi-agency identities are
reported but cannot rescue the primary result.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import os
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-RCRA-E01"
TMP = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "us-rcra-e01-v3"
TMP.mkdir(parents=True, exist_ok=True)
RCRA_URL = "https://echo.epa.gov/files/echodownloads/rcra_downloads.zip"
UA = "AI-Innovative-Research-Engine/US-RCRA-E01 frozen-pair outcome pass v3"


def iso_date(s: str | None) -> str:
    s = (s or "").strip()
    for fmt, n in (("%m/%d/%Y", 10), ("%Y-%m-%d", 10), ("%Y-%m-%dT%H:%M:%S", 19)):
        try:
            return datetime.strptime(s[:n], fmt).date().isoformat()
        except ValueError:
            pass
    return ""


def outcome_class(v: str | None) -> str:
    u = (v or "").strip().upper()
    if u in {"Y", "N", "U"}:
        return u
    return "BLANK_OTHER"


def exact_mcnemar_p(ny: int, yn: int) -> float | None:
    m = ny + yn
    if m == 0:
        return None
    lo = min(ny, yn)
    tail = sum(math.comb(m, k) for k in range(lo + 1)) / (2**m)
    return min(1.0, 2.0 * tail)


pair_manifest = json.loads((OUT / "PAIR_MANIFEST.json").read_text(encoding="utf-8"))
audit = json.loads((OUT / "DUPLICATE_IDENTITY_AUDIT.json").read_text(encoding="utf-8"))
assert pair_manifest["issue"] == 125
assert pair_manifest["pair_count"] == 297
assert pair_manifest["state_territory_fips_count"] == 43
assert pair_manifest["pair_identity_sha256"] == "d648d242e6adcddcac44dba7a61cab0ac9da2c4a5aa80e9d123d725aa7dfed73"
assert audit["outcome_field_read"] is False and audit["outcome_field_persisted"] is False
assert audit["duplicate_identity_count"] == 32
assert audit["nonoutcome_differing_column_counts"] == {"EVALUATION_AGENCY": 32}

pairs = pair_manifest["pairs"]
canonical = json.dumps(pairs, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
fingerprint = hashlib.sha256(canonical).hexdigest()
assert fingerprint == pair_manifest["pair_identity_sha256"]

selected: set[tuple[str, str, str]] = set()
for p in pairs:
    selected.add((p["id_number"], p["pre_cei_date"], p["pre_evaluation_identifier"]))
    selected.add((p["id_number"], p["post_cei_date"], p["post_evaluation_identifier"]))
assert len(selected) == 594

zip_path = TMP / "rcra_downloads.zip"
req = urllib.request.Request(RCRA_URL, headers={"User-Agent": UA, "Accept": "*/*"})
h = hashlib.sha256()
total = 0
with urllib.request.urlopen(req, timeout=300) as r, open(zip_path, "wb") as f:
    while True:
        chunk = r.read(1024 * 1024)
        if not chunk:
            break
        f.write(chunk)
        h.update(chunk)
        total += len(chunk)
if not zipfile.is_zipfile(zip_path):
    raise RuntimeError("RCRA source is not a ZIP")

source_rows: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
with zipfile.ZipFile(zip_path) as z:
    hits = [n for n in z.namelist() if n.rsplit("/", 1)[-1].casefold() == "rcra_evaluations.csv"]
    if len(hits) != 1:
        raise RuntimeError(f"evaluation member drift: {hits}")
    reader = csv.DictReader(io.TextIOWrapper(z.open(hits[0]), encoding="utf-8-sig", errors="replace", newline=""))
    required = {
        "ID_NUMBER",
        "EVALUATION_IDENTIFIER",
        "EVALUATION_TYPE",
        "EVALUATION_START_DATE",
        "EVALUATION_AGENCY",
        "FOUND_VIOLATION",
    }
    missing = sorted(required - set(reader.fieldnames or []))
    if missing:
        raise RuntimeError(f"missing evaluation headers: {missing}")
    for r in reader:
        rid = (r.get("ID_NUMBER") or "").strip().upper()
        d = iso_date(r.get("EVALUATION_START_DATE"))
        eid = (r.get("EVALUATION_IDENTIFIER") or "").strip()
        key = (rid, d, eid)
        if key in selected and (r.get("EVALUATION_TYPE") or "").strip().upper() == "CEI":
            source_rows[key].append(
                {
                    "agency": (r.get("EVALUATION_AGENCY") or "").strip().upper(),
                    "outcome": outcome_class(r.get("FOUND_VIOLATION")),
                }
            )
try:
    zip_path.unlink()
except FileNotFoundError:
    pass

if set(source_rows) != selected:
    missing_ids = sorted(selected - set(source_rows))
    extra_ids = sorted(set(source_rows) - selected)
    raise RuntimeError(f"frozen selected identity coverage drift missing={len(missing_ids)} extra={len(extra_ids)}")

resolved_outcome: dict[tuple[str, str, str], str] = {}
agency_sets: dict[tuple[str, str, str], tuple[str, ...]] = {}
duplicate_identity_count = 0
duplicate_agree_count = 0
duplicate_conflict_count = 0
multiagency_identity_count = 0
for key, rows in source_rows.items():
    if len(rows) > 1:
        duplicate_identity_count += 1
    classes = {r["outcome"] for r in rows}
    if len(classes) == 1:
        resolved_outcome[key] = next(iter(classes))
        if len(rows) > 1:
            duplicate_agree_count += 1
    else:
        resolved_outcome[key] = "DUPLICATE_CONFLICT_MISSING"
        duplicate_conflict_count += 1
    agencies = tuple(sorted({r["agency"] for r in rows if r["agency"]}))
    agency_sets[key] = agencies
    if len(agencies) > 1:
        multiagency_identity_count += 1

pre_counts = Counter()
post_counts = Counter()
contingency = Counter()
pre_days: list[int] = []
post_days: list[int] = []
hazard_ct: dict[str, Counter] = defaultdict(Counter)
same_agency_ct = Counter()
same_agency_candidate_pairs = 0
agency_status_counts = Counter()

for p in pairs:
    pre_key = (p["id_number"], p["pre_cei_date"], p["pre_evaluation_identifier"])
    post_key = (p["id_number"], p["post_cei_date"], p["post_evaluation_identifier"])
    a = resolved_outcome[pre_key]
    b = resolved_outcome[post_key]
    pre_counts[a] += 1
    post_counts[b] += 1

    pre_ag = agency_sets[pre_key]
    post_ag = agency_sets[post_key]
    if len(pre_ag) == 1 and len(post_ag) == 1:
        if pre_ag[0] == post_ag[0]:
            agency_status = "SINGLE_AGENCY_SAME"
        else:
            agency_status = "SINGLE_AGENCY_CHANGED"
    else:
        agency_status = "MULTI_OR_MISSING_AGENCY_AMBIGUOUS"
    agency_status_counts[agency_status] += 1

    idx = date.fromisoformat(p["index_date"])
    pred = date.fromisoformat(p["pre_cei_date"])
    postd = date.fromisoformat(p["post_cei_date"])
    pre_days.append((idx - pred).days)
    post_days.append((postd - idx).days)

    analyzable = a in {"Y", "N"} and b in {"Y", "N"}
    if analyzable:
        contingency[a + b] += 1
        hazard_ct[p["index_incident_type"]][a + b] += 1
        if agency_status == "SINGLE_AGENCY_SAME":
            same_agency_candidate_pairs += 1
            same_agency_ct[a + b] += 1

nn = contingency["NN"]
ny = contingency["NY"]
yn = contingency["YN"]
yy = contingency["YY"]
n = nn + ny + yn + yy
discordant = ny + yn
p_exact = exact_mcnemar_p(ny, yn)
rd = None if n == 0 else (ny - yn) / n

if n < 100 or discordant < 20:
    gate = "HOLD_US_RCRA_E01_INSUFFICIENT_OUTCOME_SUPPORT"
elif rd is not None and rd >= 0.05 and p_exact is not None and p_exact < 0.05:
    gate = "PASS_POSITIVE_MATERIAL_US_RCRA_E01_RELATIONSHIP"
elif rd is not None and 0 < rd < 0.05 and p_exact is not None and p_exact < 0.05:
    gate = "POSITIVE_BELOW_MATERIALITY_US_RCRA_E01_RELATIONSHIP"
else:
    gate = "NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP"

same_n = sum(same_agency_ct.values())
same_disc = same_agency_ct["NY"] + same_agency_ct["YN"]
same_diag: dict[str, object] = {
    "eligible_analyzable_pairs": same_n,
    "discordant_pairs": same_disc,
    "minimum_analyzable_for_sensitivity": 50,
    "minimum_discordant_for_sensitivity": 10,
}
if same_n >= 50 and same_disc >= 10:
    same_diag.update(
        {
            "n_NN": same_agency_ct["NN"],
            "n_NY": same_agency_ct["NY"],
            "n_YN": same_agency_ct["YN"],
            "n_YY": same_agency_ct["YY"],
            "pre_risk": (same_agency_ct["YY"] + same_agency_ct["YN"]) / same_n,
            "post_risk": (same_agency_ct["YY"] + same_agency_ct["NY"]) / same_n,
            "risk_difference": (same_agency_ct["NY"] - same_agency_ct["YN"]) / same_n,
            "p_exact_two_sided_mcnemar": exact_mcnemar_p(same_agency_ct["NY"], same_agency_ct["YN"]),
        }
    )

result = {
    "id": "US-RCRA-E01-EXECUTION-RESULT",
    "issue": 125,
    "gate": gate,
    "pair_identity_sha256": fingerprint,
    "pair_count_frozen": 297,
    "state_territory_fips_count_frozen": 43,
    "pair_identity_drift": False,
    "selected_outcomes_opened": True,
    "relationship_computed": n >= 100 and discordant >= 20,
    "source": {
        "rcra_url": RCRA_URL,
        "bytes_transient": total,
        "sha256": h.hexdigest(),
        "raw_source_bytes_persisted": False,
    },
    "outcome_coding": {
        "Y": 1,
        "N": 0,
        "U": "missing",
        "blank_or_other": "missing",
        "duplicate_conflict": "missing",
    },
    "duplicate_resolution": {
        "frozen_rule": "all duplicate source rows must agree on preregistered coded class; disagreement => missing",
        "selected_identity_count": len(selected),
        "duplicate_identity_count": duplicate_identity_count,
        "duplicate_agree_count": duplicate_agree_count,
        "duplicate_conflict_count": duplicate_conflict_count,
        "multiagency_identity_count": multiagency_identity_count,
        "audit_file": "research/US-RCRA-E01/DUPLICATE_IDENTITY_AUDIT.json",
    },
    "value_counts": {"pre": dict(pre_counts), "post": dict(post_counts)},
    "primary_support": {
        "analyzable_pairs": n,
        "discordant_pairs": discordant,
        "minimum_analyzable": 100,
        "minimum_discordant": 20,
    },
    "primary": {
        "n_NN": nn,
        "n_NY": ny,
        "n_YN": yn,
        "n_YY": yy,
        "pre_risk": None if n == 0 else (yy + yn) / n,
        "post_risk": None if n == 0 else (yy + ny) / n,
        "risk_difference": rd,
        "p_exact_two_sided_mcnemar": p_exact,
        "materiality_floor": 0.05,
    },
    "diagnostics_non_rescuing": {
        "agency_status_pair_counts": dict(agency_status_counts),
        "same_single_agency_subset": same_diag,
        "pre_cei_distance_days": {
            "min": min(pre_days),
            "max": max(pre_days),
            "mean": sum(pre_days) / len(pre_days),
        },
        "post_cei_distance_days": {
            "min": min(post_days),
            "max": max(post_days),
            "mean": sum(post_days) / len(post_days),
        },
        "hazard_contingencies": {k: dict(v) for k, v in sorted(hazard_ct.items())},
    },
    "execution_integrity": {
        "prior_failed_pass2_note": "An earlier implementation projected selected FOUND_VIOLATION fields into memory but failed before any value/statistic was surfaced, persisted, aggregated, or used to tune the contract; see Issue #125 integrity comment.",
        "scientific_contract_changed_after_value_access": False,
    },
    "claim_boundary": "non-causal monitoring/compliance association; FOUND_VIOLATION is an inspection-result field",
    "incremental_monetary_cost_usd": 0,
}
(OUT / "EXECUTION_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"gate": gate, "analyzable": n, "discordant": discordant, "RD": rd, "p": p_exact, "duplicate_conflicts": duplicate_conflict_count}, indent=2))
