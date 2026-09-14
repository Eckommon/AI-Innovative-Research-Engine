#!/usr/bin/env python3
"""US-BRIDGE-E01 preregistered matched-pair outcome runner.

Fail-closed ordering:
1) validate exact N01 compressed pair artifact and uncompressed pair fingerprint;
2) validate frozen pair counts/classes;
3) only then download the frozen NBI archives;
4) verify ZIP/member source hashes before slicing any condition field;
5) extract only the exact frozen pair endpoints;
6) compute the frozen deterioration indicators and exact paired test once.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import math
import os
import re
import tempfile
import time
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import date
from decimal import Decimal, localcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-BRIDGE-E01"
OUT.mkdir(parents=True, exist_ok=True)
TMP = Path(os.environ.get("RUNNER_TEMP", tempfile.gettempdir())) / "us-bridge-e01"
TMP.mkdir(parents=True, exist_ok=True)

PAIR_GZ = ROOT / "research" / "US-BRIDGE-N01" / "PAIR_IDENTITIES.jsonl.gz"
N01_SOURCE_MANIFEST = ROOT / "research" / "US-BRIDGE-N01" / "SOURCE_MANIFEST.json"
N01_DESIGN_RESULT = ROOT / "research" / "US-BRIDGE-N01" / "DESIGN_RESULT.json"

EXPECTED_PAIR_COUNT = 89800
EXPECTED_PAIR_SHA = "a35d38c8219de527a72c5d4975c6f6c2fed63e92711632fd5adc4b16056269b9"
EXPECTED_GZ_SHA = "4de3b8cbc7152725f72e4a93a0990a26e92579607cca8ecfe3390eba5d69e6e3"
EXPECTED_CLASS_COUNTS = {"CULVERT": 15245, "NON_CULVERT": 74555}
EXPECTED_N01_GATE = "PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE"
UA = "AI-Innovative-Research-Engine/US-BRIDGE-E01 preregistered outcome test"

# One-based official legacy-NBI positions -> zero-based Python byte slices.
# Items 58/59/60/62 occupy positions 259/260/261/263.
COND_SLICES = {
    "58": (258, 259),
    "59": (259, 260),
    "60": (260, 261),
    "62": (262, 263),
}
INSPECT_SLICE = (286, 290)  # Item 90, positions 287-290.

ALLOWED_DISPOSITIONS = {
    "PASS_POSITIVE_MATERIAL_US_BRIDGE_E01_RELATIONSHIP",
    "POSITIVE_BELOW_MATERIALITY_US_BRIDGE_E01_RELATIONSHIP",
    "NO_PREREGISTERED_POSITIVE_US_BRIDGE_E01_RELATIONSHIP",
}


def fail(stage: str, detail: str) -> None:
    payload = {
        "research_id": "US-BRIDGE-E01",
        "issue": 132,
        "gate": "HOLD_US_BRIDGE_E01_FAIL_CLOSED",
        "failure_stage": stage,
        "failure_detail": detail,
        "condition_values_opened": False,
        "relationship_computed": False,
        "incremental_monetary_cost_usd": 0,
    }
    (OUT / "STAGING_RESULT.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    raise RuntimeError(f"{stage}: {detail}")


def parse_mm_yy(raw: bytes) -> str | None:
    s = raw.decode("ascii", errors="strict").strip()
    if not re.fullmatch(r"\d{4}", s):
        return None
    mm, yy = int(s[:2]), int(s[2:])
    if not 1 <= mm <= 12:
        return None
    yyyy = 1900 + yy if yy >= 50 else 2000 + yy
    return date(yyyy, mm, 1).isoformat()


def numeric_grade(raw: bytes) -> int | None:
    s = raw.decode("ascii", errors="strict").strip()
    return int(s) if re.fullmatch(r"[0-9]", s) else None


def download(url: str, path: Path) -> tuple[int, str]:
    last: Exception | None = None
    for attempt in range(5):
        h = hashlib.sha256()
        total = 0
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=300) as r, open(path, "wb") as f:
                while True:
                    chunk = r.read(1024 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
                    h.update(chunk)
                    total += len(chunk)
            return total, h.hexdigest()
        except Exception as exc:
            last = exc
            path.unlink(missing_ok=True)
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)
    assert last is not None
    raise last


def exact_two_sided_binomial(discordant_exposed_only: int, discordant_control_only: int) -> dict:
    b = int(discordant_exposed_only)
    c = int(discordant_control_only)
    n = b + c
    if n == 0:
        return {"discordant_n": 0, "tail_k": 0, "p_value": 1.0, "p_decimal_50": "1", "p_less_than_0_05_exact": False}
    k = min(b, c)
    comb = 1
    tail_num = 1
    for i in range(k):
        comb = comb * (n - i) // (i + 1)
        tail_num += comb
    den = 1 << n
    num = min(den, 2 * tail_num)
    with localcontext() as ctx:
        ctx.prec = 50
        p_dec = Decimal(num) / Decimal(den)
    return {
        "discordant_n": n,
        "tail_k": k,
        "p_value": float(p_dec),
        "p_decimal_50": format(p_dec, "f"),
        "p_less_than_0_05_exact": (num * 20 < den),
    }


def interval_deterioration(bridge_class: str, pre_vals: dict[str, int | None], post_vals: dict[str, int | None]):
    if bridge_class == "CULVERT":
        pre = pre_vals["62"]
        post = post_vals["62"]
        if pre is None or post is None:
            return None, {"components": []}
        return int(post <= pre - 1), {"components": ["62"], "pre_score": pre, "post_score": post}
    if bridge_class != "NON_CULVERT":
        raise RuntimeError(f"unknown bridge class {bridge_class!r}")
    common = [item for item in ("58", "59", "60") if pre_vals[item] is not None and post_vals[item] is not None]
    if len(common) < 2:
        return None, {"components": common}
    pre_score = min(pre_vals[item] for item in common if pre_vals[item] is not None)
    post_score = min(post_vals[item] for item in common if post_vals[item] is not None)
    return int(post_score <= pre_score - 1), {
        "components": common,
        "pre_score": pre_score,
        "post_score": post_score,
    }


# 1. PRE-OUTCOME: validate exact N01 pair artifact before any condition slicing.
if not PAIR_GZ.exists():
    fail("PAIR_ARTIFACT", "N01 pair gzip missing")
compressed = PAIR_GZ.read_bytes()
compressed_sha = hashlib.sha256(compressed).hexdigest()
if compressed_sha != EXPECTED_GZ_SHA:
    fail("PAIR_ARTIFACT", f"compressed SHA mismatch {compressed_sha}")

design = json.loads(N01_DESIGN_RESULT.read_text(encoding="utf-8"))
if design.get("gate") != EXPECTED_N01_GATE:
    fail("PAIR_ARTIFACT", f"N01 gate mismatch {design.get('gate')!r}")
if design.get("pair_identity_sha256") != EXPECTED_PAIR_SHA:
    fail("PAIR_ARTIFACT", "N01 DESIGN_RESULT pair SHA mismatch")

pair_hasher = hashlib.sha256()
pairs = []
class_counts = Counter()
targets_by_year: dict[int, dict[str, str]] = defaultdict(dict)

with gzip.open(PAIR_GZ, "rb") as f:
    for raw_line in f:
        if not raw_line.endswith(b"\n"):
            fail("PAIR_ARTIFACT", "pair JSONL line lacks newline")
        pair_hasher.update(raw_line)
        pair = json.loads(raw_line)
        pairs.append(pair)
        bclass = pair["class"]
        class_counts[bclass] += 1
        for arm in ("exp", "ctl"):
            bridge = pair[f"{arm}_bridge"]
            for endpoint in ("pre", "post"):
                archive = int(pair[f"{arm}_{endpoint}_archive"])
                inspect_date = pair[f"{arm}_{endpoint}"]
                prior = targets_by_year[archive].get(bridge)
                if prior is not None and prior != inspect_date:
                    fail("PAIR_ARTIFACT", f"multiple target dates for {bridge} in archive {archive}")
                targets_by_year[archive][bridge] = inspect_date

pair_sha = pair_hasher.hexdigest()
if len(pairs) != EXPECTED_PAIR_COUNT:
    fail("PAIR_ARTIFACT", f"pair count mismatch {len(pairs)}")
if pair_sha != EXPECTED_PAIR_SHA:
    fail("PAIR_ARTIFACT", f"pair identity SHA mismatch {pair_sha}")
if dict(sorted(class_counts.items())) != EXPECTED_CLASS_COUNTS:
    fail("PAIR_ARTIFACT", f"class count mismatch {dict(class_counts)}")

identity_pass = True
print(json.dumps({
    "stage": "PAIR_IDENTITY_PASS",
    "pair_count": len(pairs),
    "pair_identity_sha256": pair_sha,
    "compressed_sha256": compressed_sha,
    "class_counts": dict(sorted(class_counts.items())),
}, sort_keys=True), flush=True)

# 2. OUTCOME ACCESS AUTHORIZED only after identity PASS.
#    Each exact NBI source hash is verified before its condition positions are sliced.
source_manifest = json.loads(N01_SOURCE_MANIFEST.read_text(encoding="utf-8"))
source_by_year = {int(x["year"]): x for x in source_manifest["annual_sources"]}
needed_years = sorted(targets_by_year)
if not needed_years or any(y not in source_by_year for y in needed_years):
    fail("SOURCE_SUPPORT", f"needed years unsupported: {needed_years}")

outcomes: dict[tuple[int, str, str], dict[str, int | None]] = {}
source_audit = []
condition_values_opened = False
condition_row_bytes_sliced = False

for year in needed_years:
    meta = source_by_year[year]
    zpath = TMP / f"nbi-{year}.zip"
    print(f"US-BRIDGE-E01 source {year}", flush=True)
    zip_bytes, zip_sha = download(meta["resolved_data_url"], zpath)
    if zip_sha != meta["zip_sha256"] or zip_bytes != int(meta["zip_bytes"]):
        fail("SOURCE_SUPPORT", f"{year}: ZIP drift bytes={zip_bytes} sha={zip_sha}")
    if not zipfile.is_zipfile(zpath):
        fail("SOURCE_SUPPORT", f"{year}: not ZIP")

    with zipfile.ZipFile(zpath) as z:
        names = {i.filename: i for i in z.infolist() if not i.is_dir()}
        member_name = meta["member_name"]
        if member_name not in names:
            fail("SOURCE_SUPPORT", f"{year}: frozen member missing")
        member_sha = hashlib.sha256()
        member_bytes = 0
        with z.open(member_name) as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                member_sha.update(chunk)
                member_bytes += len(chunk)
        member_hex = member_sha.hexdigest()
        if member_hex != meta["member_sha256"] or member_bytes != int(meta["member_bytes"]):
            fail("SOURCE_SUPPORT", f"{year}: member drift bytes={member_bytes} sha={member_hex}")

        # Only now, after pair identity + exact source hash PASS, slice outcomes.
        wanted = targets_by_year[year]
        seen = Counter()
        with z.open(member_name) as f:
            for raw_line in f:
                line = raw_line.rstrip(b"\r\n")
                if len(line) < 291:
                    continue
                state3 = line[0:3].decode("ascii", errors="strict")
                if not re.fullmatch(r"\d{2}", state3[:2]):
                    continue
                structure = line[3:18].decode("ascii", errors="replace").strip()
                if not structure:
                    continue
                bridge = state3[:2] + "|" + structure
                expected_date = wanted.get(bridge)
                if expected_date is None:
                    continue
                inspect_date = parse_mm_yy(line[INSPECT_SLICE[0]:INSPECT_SLICE[1]])
                if inspect_date != expected_date:
                    continue
                seen[bridge] += 1
                if seen[bridge] > 1:
                    fail("SOURCE_SUPPORT", f"{year}: duplicate exact endpoint for {bridge}")
                vals = {
                    item: numeric_grade(line[a:b])
                    for item, (a, b) in COND_SLICES.items()
                }
                condition_row_bytes_sliced = True
                condition_values_opened = True
                outcomes[(year, bridge, inspect_date)] = vals

        missing = sorted(set(wanted) - set(seen))
        if missing:
            fail("SOURCE_SUPPORT", f"{year}: {len(missing)} frozen endpoints missing; first={missing[:3]}")
        source_audit.append({
            "year": year,
            "resolved_data_url": meta["resolved_data_url"],
            "zip_bytes": zip_bytes,
            "zip_sha256": zip_sha,
            "member_name": member_name,
            "member_bytes": member_bytes,
            "member_sha256": member_hex,
            "target_bridge_endpoints": len(wanted),
            "matched_endpoint_rows": sum(seen.values()),
            "source_hash_matches_n01": True,
        })
    zpath.unlink(missing_ok=True)

# 3. Frozen deterioration + complete matched-pair exact test.
pair_cells = Counter()
analyzable_class = Counter()
missing_arm_class = Counter()
exp_det = 0
ctl_det = 0
component_patterns = Counter()

for pair in pairs:
    bclass = pair["class"]

    def arm_det(arm: str):
        pre_key = (int(pair[f"{arm}_pre_archive"]), pair[f"{arm}_bridge"], pair[f"{arm}_pre"])
        post_key = (int(pair[f"{arm}_post_archive"]), pair[f"{arm}_bridge"], pair[f"{arm}_post"])
        pre_vals = outcomes[pre_key]
        post_vals = outcomes[post_key]
        return interval_deterioration(bclass, pre_vals, post_vals)

    e, emeta = arm_det("exp")
    c, cmeta = arm_det("ctl")
    if e is None or c is None:
        missing_arm_class[bclass] += 1
        continue
    analyzable_class[bclass] += 1
    exp_det += e
    ctl_det += c
    pair_cells[(e, c)] += 1
    component_patterns[(bclass, tuple(emeta["components"]), tuple(cmeta["components"]))] += 1

n = sum(pair_cells.values())
if n == 0:
    fail("ANALYSIS_SUPPORT", "no complete analyzable matched pairs")
exp_risk = exp_det / n
ctl_risk = ctl_det / n
rd = exp_risk - ctl_risk

n00 = pair_cells[(0, 0)]
n10 = pair_cells[(1, 0)]  # exposed deteriorates only
n01 = pair_cells[(0, 1)]  # control deteriorates only
n11 = pair_cells[(1, 1)]
exact = exact_two_sided_binomial(n10, n01)
p = exact["p_value"]
significant = exact["p_less_than_0_05_exact"]

if rd >= 0.05 and significant:
    disposition = "PASS_POSITIVE_MATERIAL_US_BRIDGE_E01_RELATIONSHIP"
elif 0 < rd < 0.05 and significant:
    disposition = "POSITIVE_BELOW_MATERIALITY_US_BRIDGE_E01_RELATIONSHIP"
else:
    disposition = "NO_PREREGISTERED_POSITIVE_US_BRIDGE_E01_RELATIONSHIP"
assert disposition in ALLOWED_DISPOSITIONS

result = {
    "research_id": "US-BRIDGE-E01",
    "issue": 132,
    "gate": disposition,
    "pair_identity_revalidated_before_outcome_access": identity_pass,
    "n01_pair_count": len(pairs),
    "n01_pair_identity_sha256": pair_sha,
    "n01_pair_artifact_gzip_sha256": compressed_sha,
    "n01_class_counts": dict(sorted(class_counts.items())),
    "condition_values_opened": condition_values_opened,
    "condition_row_bytes_sliced": condition_row_bytes_sliced,
    "condition_access_after_pair_identity_pass": True,
    "nbi_source_hashes_match_n01": all(x["source_hash_matches_n01"] for x in source_audit),
    "complete_analyzable_pairs": n,
    "complete_pair_rate": n / len(pairs),
    "analyzable_class_counts": dict(sorted(analyzable_class.items())),
    "incomplete_pair_class_counts": dict(sorted(missing_arm_class.items())),
    "exposed_deterioration_count": exp_det,
    "control_deterioration_count": ctl_det,
    "exposed_deterioration_risk": exp_risk,
    "control_deterioration_risk": ctl_risk,
    "risk_difference": rd,
    "risk_difference_percentage_points": rd * 100.0,
    "paired_cells": {
        "neither_00": n00,
        "exposed_only_10": n10,
        "control_only_01": n01,
        "both_11": n11,
    },
    "exact_two_sided_mcnemar_binomial": exact,
    "frozen_significance_threshold": 0.05,
    "frozen_positive_materiality_rd": 0.05,
    "relationship_computed": True,
    "post_value_rescue_used": False,
    "negative_rd_protective_interpretation_authorized": False,
    "causal_claim_authorized": False,
    "raw_source_bytes_persisted": False,
    "incremental_monetary_cost_usd": 0,
}

audit = {
    "research_id": "US-BRIDGE-E01",
    "issue": 132,
    "pair_validation": {
        "expected_pair_count": EXPECTED_PAIR_COUNT,
        "observed_pair_count": len(pairs),
        "expected_pair_identity_sha256": EXPECTED_PAIR_SHA,
        "observed_pair_identity_sha256": pair_sha,
        "expected_compressed_sha256": EXPECTED_GZ_SHA,
        "observed_compressed_sha256": compressed_sha,
        "expected_class_counts": EXPECTED_CLASS_COUNTS,
        "observed_class_counts": dict(sorted(class_counts.items())),
        "passed_before_outcome_access": True,
    },
    "condition_byte_slices_zero_based": COND_SLICES,
    "source_audit": source_audit,
    "outcome_contract": {
        "CULVERT": "Item 62 numeric 0-9 both endpoints; deterioration iff post <= pre-1",
        "NON_CULVERT": "Items 58/59/60; same common numeric set at both endpoints; >=2 components; score=min; deterioration iff post <= pre-1",
        "primary_pair_rule": "both exposed and control analyzable",
        "estimand": "RD = exposed deterioration risk - control deterioration risk",
        "test": "exact two-sided McNemar/binomial on discordant pairs",
        "significance": "p < 0.05",
        "positive_materiality": "RD >= +0.05",
    },
    "component_pattern_count": len(component_patterns),
    "raw_source_bytes_persisted": False,
    "incremental_monetary_cost_usd": 0,
}

(OUT / "STAGING_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
(OUT / "STAGING_SOURCE_AUDIT.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")

md = f"""# US-BRIDGE-E01 staging result

- gate: **`{disposition}`**
- N01 pair identity revalidated before outcome access: **YES**
- frozen pair count: **{len(pairs):,}**
- complete analyzable pairs: **{n:,}** ({n/len(pairs):.4%})
- exposed deterioration: **{exp_det:,} / {n:,} = {exp_risk:.6%}**
- control deterioration: **{ctl_det:,} / {n:,} = {ctl_risk:.6%}**
- RD (exposed - control): **{rd:+.6%} ({rd*100:+.4f} pp)**
- paired cells `(exp, ctl)`: 00={n00:,}, 10={n10:,}, 01={n01:,}, 11={n11:,}
- exact two-sided McNemar/binomial p: **{exact['p_decimal_50']}**
- frozen positive materiality: RD >= +5pp
- significance: p < 0.05
- post-value rescue: **NO**
- protective interpretation for negative RD: **NOT AUTHORIZED**
- causal claim: **NOT AUTHORIZED**
- incremental monetary cost: **0 USD**

This is staging evidence. Canonical claim/decision/status finalization occurs only after the workflow result is independently read back.
"""
(OUT / "STAGING_RESULT.md").write_text(md, encoding="utf-8")

print(json.dumps({
    "gate": disposition,
    "complete_pairs": n,
    "exposed_risk": exp_risk,
    "control_risk": ctl_risk,
    "rd": rd,
    "rd_pp": rd * 100.0,
    "n10_exposed_only": n10,
    "n01_control_only": n01,
    "p": exact["p_decimal_50"],
    "condition_opened": condition_values_opened,
    "pair_identity_revalidated_first": True,
}, sort_keys=True), flush=True)
