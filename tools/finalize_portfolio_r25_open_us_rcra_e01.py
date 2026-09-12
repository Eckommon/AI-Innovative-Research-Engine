#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
claim_log_p = ROOT / "registry" / "CLAIM_LEDGER.md"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
claim_p = ROOT / "registry" / "CLM-165.md"
dec_sel_p = ROOT / "registry" / "DEC-172.md"
dec_auth_p = ROOT / "registry" / "DEC-173.md"
portfolio_dir = ROOT / "research" / "PORTFOLIO-R25"
e01_dir = ROOT / "research" / "US-RCRA-E01"
portfolio_dir.mkdir(parents=True, exist_ok=True)
e01_dir.mkdir(parents=True, exist_ok=True)

status = status_p.read_text(encoding="utf-8")
assert "active_issue: none" in status
assert "last_completed_issue: 123" in status
assert "last_decision: DEC-171" in status
for p in (claim_p, dec_sel_p, dec_auth_p):
    assert not p.exists(), p

(portfolio_dir / "RESULT.md").write_text("""---
id: PORTFOLIO-R25-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-13
issue: 124
state: COMPLETED_SELECT
selected_candidate: US-RCRA-E01
selected_gate: US-RCRA-E01
next_issue: 125
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R25 Result — Select US-RCRA-E01

**`SELECT_US_RCRA_E01_PAIRED_CEI_RELATIONSHIP_TEST`**

US-RCRA-E01 is selected outcome-blind after N01 fixed 297 same-facility CEI pairs across 43 state/territory FIPS with selected-pair `FOUND_VIOLATION` still unopened.

## Mission-ROI comparison

0–5 each; /45. Scores are portfolio-control judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-RCRA-E01 paired CEI test** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | **42** | **SELECT** |
| US-MINE-001 operational stress → injury | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_OVERLAP |
| US-UTIL post-F02 descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 2 | **38** | HOLD_HIGH_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_OVERLAP |
| C-EU-004 industrial-site climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE |

## Why E01 leads now

F01 removed source/join/time uncertainty and N01 removed pair-identifiability/surveillance-type uncertainty. The remaining bounded question is a single preregistered paired inspection-result comparison. Its information gain is therefore higher than opening a new source-feasibility branch now.

Overlap remains material: RCRA inspection/compliance and hazardous-site hazard vulnerability are established research areas. The only bounded contribution is the preregistered national same-facility paired-CEI FEMA-disaster monitoring/compliance test. Novelty is not proven.

## Exact authorization boundary

Issue #125 is authorized exactly as preregistered. Before outcome access, it must reconstruct N01's 297 pairs and persist a deterministic pair fingerprint. Only then may it read selected rows' `FOUND_VIOLATION` values. Primary coding is Y=1, N=0, U/blank/other=missing; >=100 analyzable pairs and >=20 discordant pairs are required. Primary inference is an exact two-sided McNemar/binomial test with a +5 percentage-point materiality floor. Diagnostics are non-rescuing.

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

(e01_dir / "README.md").write_text("""---
id: US-RCRA-E01
issue: 125
state: ACTIVE_PREREGISTERED_PAIRED_EXPERIMENT
selection_decision: DEC-172
authorization_decision: DEC-173
selected_pair_outcomes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-RCRA-E01 — Preregistered Paired CEI Disaster Compliance-Monitoring Test

Canonical contract is Issue #125. Before outcome access, reconstruct exactly the N01-selected 297 pair structure and verify the 43-state/territory support. Then, and only then, read selected rows' `FOUND_VIOLATION` values and execute the frozen Y/N complete-pair exact McNemar test. `U`/blank/other are missing, not recoded. Minimum support: 100 analyzable pairs and 20 discordant pairs. Materiality floor: +5 percentage points. All diagnostics are non-rescuing. Claim boundary is non-causal monitoring/compliance association. Cost: **0 USD**.
""", encoding="utf-8")

claim_p.write_text("""---
id: CLM-165
type: claim
created: 2026-09-13
issue: 124
status: active
---

# CLM-165 — N01 PASS makes one bounded preregistered paired-CEI outcome test the highest-value next gate

With 297 outcome-blind same-facility CEI pairs across 43 state/territory FIPS and deterministic source/pair identity, the remaining US-RCRA uncertainty is concentrated in one bounded paired inspection-result relationship. This raises US-RCRA-E01's immediate information value relative to opening another source-feasibility branch.

This is a portfolio-control claim, not evidence of a disaster-compliance relationship, causality, prediction, or novelty. Selected-pair `FOUND_VIOLATION` values remain unopened at selection. Cost: **0 USD**.
""", encoding="utf-8")

dec_sel_p.write_text("""---
id: DEC-172
type: decision
created: 2026-09-13
issue: 124
status: accepted
---

# DEC-172 — PORTFOLIO-R25 selects US-RCRA-E01 at 42/45

Select US-RCRA-E01 as the next bounded gate. N01 fixed 297 paired CEIs outcome-blind, so a one-shot preregistered paired inspection-result test has higher marginal information value than the preserved independent alternatives. Overlap/novelty remains penalized and no novelty claim is authorized. Cost remains **0 USD**.
""", encoding="utf-8")

dec_auth_p.write_text("""---
id: DEC-173
type: decision
created: 2026-09-13
issue: 125
status: accepted
---

# DEC-173 — Authorize only the preregistered US-RCRA-E01 paired test

Authorize Issue #125 exactly as written. Pair reconstruction and fingerprinting must occur before outcome access. Primary outcome coding is Y=1, N=0, U/blank/other=missing; require >=100 analyzable and >=20 discordant pairs. Primary inference is exact two-sided McNemar/binomial with paired risk difference and +5pp materiality floor. Agency-change and other diagnostics are non-rescuing. No post-value window, disaster, inspection-type, missingness, model, or threshold tuning. Claim boundary is non-causal monitoring/compliance. Cost remains **0 USD**.
""", encoding="utf-8")

claim_log = claim_log_p.read_text(encoding="utf-8")
assert "`CLM-165`" not in claim_log
claim_log += "\n\n| `CLM-165` | N01 PASS concentrates the remaining US-RCRA uncertainty into one bounded preregistered paired-CEI outcome test, making E01 the highest-value next gate while selected outcomes remain unopened. / N01 PASS 후 E01 paired test가 최고 정보가치 다음 gate다. | `DERIVED` | `V2_PORTFOLIO_CONTROL` | US-RCRA-N01; PORTFOLIO-R25; Issue #124 | 2026-09-13 | active |\n"
claim_log_p.write_text(claim_log, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
assert "`DEC-172`" not in dec_log and "`DEC-173`" not in dec_log
dec_log += "\n\n| `DEC-172` | 2026-09-13 | PORTFOLIO-R25 selects US-RCRA-E01 at 42/45. / R25에서 US-RCRA-E01 선정. | N01 fixed 297 outcome-blind paired CEIs; a one-shot paired test now has highest marginal information value. | Issue #124; `CLM-165`; `research/PORTFOLIO-R25/RESULT.md` | active |\n"
dec_log += "| `DEC-173` | 2026-09-13 | Authorize Issue #125 exactly as preregistered; reconstruct/fingerprint pairs before opening selected outcomes. / E01 사전등록 그대로 승인. | Prevent post-value pair/outcome/test/threshold tuning. | Issue #125; `research/US-RCRA-E01/README.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

status_p.write_text("""---
checkpoint_id: CHK-20260913-US-RCRA-E01-ACTIVE
active_issue: 125
active_research: US-RCRA-E01
last_completed_issue: 124
last_completed_research: PORTFOLIO-R25
last_decision: DEC-173
updated: 2026-09-13
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R25_SELECTED_US_RCRA_E01__US_RCRA_E01_ACTIVE`

PORTFOLIO-R25 selected **US-RCRA-E01** at **42/45**. Issue #125 is the only active research gate. N01's 297 selected CEI pairs remain outcome-blind until E01 first reproduces the exact pair structure and fingerprint.

## Exact next action / 정확한 다음 행동

Execute Issue #125 in two passes: (1) reconstruct and fingerprint the exact 297 N01 pairs without reading `FOUND_VIOLATION`; stop on identity drift, then (2) only if identical, open only selected pre/post `FOUND_VIOLATION` values and execute the frozen Y/N exact McNemar test with the preregistered support/materiality gates. No post-value tuning.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text("""---
checkpoint_id: CHK-20260913-US-RCRA-E01-ACTIVE
active_issue: 125
active_research: US-RCRA-E01
last_completed_issue: 124
last_completed_research: PORTFOLIO-R25
last_decision: DEC-173
updated: 2026-09-13
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R25 selected US-RCRA-E01 at 42/45 and authorized Issue #125 under DEC-173. N01 fixed 297 same-facility CEI pairs across 43 state/territory FIPS; selected-pair `FOUND_VIOLATION` remains unopened at authorization.

Exact restart: two-pass E01. Pass 1 reconstructs the frozen N01 pair identities and must reproduce exactly 297 pairs / 43 state-territory FIPS, then persists a pair fingerprint. Pass 2 may read only those selected rows' `FOUND_VIOLATION`: Y=1, N=0, U/blank/other missing; require >=100 analyzable and >=20 discordant pairs; exact two-sided McNemar; RD materiality +5pp. Diagnostics cannot rescue. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": "CHK-20260913-US-RCRA-E01-ACTIVE",
    "active_issue": 125,
    "active_research": "US-RCRA-E01",
    "last_completed_issue": 124,
    "last_completed_research": "PORTFOLIO-R25",
    "last_decision": "DEC-173",
    "updated": "2026-09-13"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
