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
result_json_p = ROOT / "research" / "US-RCRA-E01" / "EXECUTION_RESULT.json"
result_md_p = ROOT / "research" / "US-RCRA-E01" / "RESULT.md"
readme_p = ROOT / "research" / "US-RCRA-E01" / "README.md"
claim_p = ROOT / "registry" / "CLM-166.md"
dec_p = ROOT / "registry" / "DEC-174.md"

status = status_p.read_text(encoding="utf-8")
assert "active_issue: 125" in status
assert "active_research: US-RCRA-E01" in status
assert "last_decision: DEC-173" in status
r = json.loads(result_json_p.read_text(encoding="utf-8"))
assert r["gate"] == "NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP"
assert r["pair_identity_sha256"] == "d648d242e6adcddcac44dba7a61cab0ac9da2c4a5aa80e9d123d725aa7dfed73"
assert r["pair_identity_drift"] is False
assert r["primary_support"]["analyzable_pairs"] >= 100
assert r["primary_support"]["discordant_pairs"] >= 20
assert r["primary"]["risk_difference"] < 0
assert r["execution_integrity"]["scientific_contract_changed_after_value_access"] is False
assert r["incremental_monetary_cost_usd"] == 0
assert not claim_p.exists() and not dec_p.exists()

p = r["primary"]
dup = r["duplicate_resolution"]
diag = r["diagnostics_non_rescuing"]

result_md_p.write_text(f"""---
id: US-RCRA-E01-RESULT
type: preregistered-paired-relationship
created: 2026-09-13
issue: 125
gate: NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP
relationship_computed: true
incremental_monetary_cost_usd: 0
---

# US-RCRA-E01 Result

**`NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP`**

The frozen same-facility paired-CEI test does **not** support the preregistered positive monitoring/compliance association. This is a non-causal result and must not be reframed as evidence that disasters improve compliance.

## Frozen primary result

- Frozen pair structure: **297** facilities across **43** state/territory FIPS; pair fingerprint `{r['pair_identity_sha256']}`.
- Primary analyzable complete Y/N pairs: **{r['primary_support']['analyzable_pairs']}**; discordant pairs: **{r['primary_support']['discordant_pairs']}**.
- Contingency: `NN={p['n_NN']}`, `N→Y={p['n_NY']}`, `Y→N={p['n_YN']}`, `YY={p['n_YY']}`.
- Pre inspection violation-found risk: **{p['pre_risk']:.6%}**.
- Post inspection violation-found risk: **{p['post_risk']:.6%}**.
- Paired absolute risk difference: **{p['risk_difference']:.6%}** ({p['risk_difference']*100:+.3f} percentage points).
- Exact two-sided McNemar/binomial p-value: **{p['p_exact_two_sided_mcnemar']:.12f}**.
- Frozen positive materiality floor: **+5 percentage points**.

Because the point estimate is negative and the exact test is not significant, the positive preregistered gate fails. No reversed or alternative post-hoc hypothesis is opened.

## Duplicate-row integrity handling

The committed pair manifest reproduced the N01 structure outcome-blind at 297/43 before the primary outcome pass. A subsequent source audit found **{dup['duplicate_identity_count']}** of 594 selected CEI identities represented by multiple source rows; all differed only in `EVALUATION_AGENCY` on non-outcome fields.

Before the successful primary calculation, the resolution rule was frozen: all duplicate source rows must agree under the original Y/N/U/missing coding to supply a selected CEI outcome; otherwise the selected CEI is missing. Under that rule, **{dup['duplicate_agree_count']}** duplicate identities agreed and **{dup['duplicate_conflict_count']}** conflicted and were treated as missing. No row or agency was selected based on the outcome.

Execution-integrity note: an earlier failed Pass-2 implementation technically projected selected `FOUND_VIOLATION` fields into memory before halting on duplicate identity, but surfaced, persisted and aggregated no outcome values or statistics and did not change the scientific pair/window/test/materiality contract. The durable Issue #125 record preserves this limitation; therefore the final record does not claim uninterrupted value non-access after that failed run.

## Non-rescuing diagnostics

- Agency status across 297 pairs: {json.dumps(diag['agency_status_pair_counts'], sort_keys=True)}.
- Same-single-agency sensitivity: **{diag['same_single_agency_subset']['eligible_analyzable_pairs']}** analyzable / **{diag['same_single_agency_subset']['discordant_pairs']}** discordant; RD **{diag['same_single_agency_subset']['risk_difference']*100:+.3f}pp**, exact p **{diag['same_single_agency_subset']['p_exact_two_sided_mcnemar']:.6f}**.
- Diagnostics are descriptive/non-rescuing and do not alter the primary disposition.

## Claim boundary

`FOUND_VIOLATION` is an inspection-result field. This test is a same-facility monitoring/compliance association around FEMA-declared physical hazards, not a causal estimate of underlying hazardous-waste compliance. Surveillance, agency, response timing, disaster severity, inspection selection and concurrent policy remain potential explanations. No claim is made that disasters cause violations or reduce violations.

## Terminal decision

US-RCRA-E01 is terminal under this preregistration. Do **not** rescue it by changing the disaster set, 365-day washout, ±730-day CEI window, pair identities, Y/N/U coding, duplicate handling, inspection type, statistical test, direction or +5pp materiality threshold. Return to Stage 0 for independent-candidate comparison.

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

readme = readme_p.read_text(encoding="utf-8")
if "NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP" not in readme:
    readme += "\n## Terminal result / 최종 결과\n\n**`NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP`** — see `RESULT.md`. The preregistered positive paired association is not supported. No post-value rescue is allowed.\n"
readme_p.write_text(readme, encoding="utf-8")

claim_p.write_text(f"""---
id: CLM-166
type: claim
created: 2026-09-13
issue: 125
status: active
---

# CLM-166 — US-RCRA-E01 does not support the preregistered positive paired-CEI disaster association

Under the frozen 297-pair identity and duplicate-safe Y/N complete-pair rule, **{r['primary_support']['analyzable_pairs']}** pairs are analyzable with **{r['primary_support']['discordant_pairs']}** discordant. The paired violation-found risk changes from **{p['pre_risk']:.6%}** pre to **{p['post_risk']:.6%}** post, `RD={p['risk_difference']:.9f}`, exact two-sided McNemar `p={p['p_exact_two_sided_mcnemar']:.12f}`. The preregistered positive relationship is therefore not supported.

This is non-causal and does not establish a protective disaster effect. Duplicate source-row ambiguity was handled by a frozen outcome-independent agreement-or-missing rule; no post-value rescue is authorized. Cost: **0 USD**.
""", encoding="utf-8")

dec_p.write_text("""---
id: DEC-174
type: decision
created: 2026-09-13
issue: 125
status: accepted
---

# DEC-174 — Finalize US-RCRA-E01 as no preregistered positive relationship and return Stage 0

Finalize Issue #125 at **`NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP`**. Preserve the frozen 297-pair design, duplicate-safe outcome rule and exact McNemar result as terminal for this hypothesis. Do not reverse the hypothesis or alter pair/window/disaster/outcome/test/materiality rules after observing results.

The result is non-causal and does not establish that disasters improve compliance. Return to Stage 0 for independent-candidate comparison. Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

claim_log = claim_log_p.read_text(encoding="utf-8")
assert "`CLM-166`" not in claim_log
claim_log += f"\n\n| `CLM-166` | US-RCRA-E01 does not support the preregistered positive same-facility paired-CEI disaster association: n={r['primary_support']['analyzable_pairs']}, RD={p['risk_difference']:.6f}, exact McNemar p={p['p_exact_two_sided_mcnemar']:.6f}. / 사전등록 positive paired 관계는 지지되지 않는다. | `OBSERVED/DERIVED/VALIDATED` | `V3_PREREGISTERED_RELATIONSHIP_GATE` | Run `34722366631`; `research/US-RCRA-E01/EXECUTION_RESULT.json`; `RESULT.md` | 2026-09-13 | active |\n"
claim_log_p.write_text(claim_log, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
assert "`DEC-174`" not in dec_log
dec_log += "\n\n| `DEC-174` | 2026-09-13 | Finalize US-RCRA-E01 at `NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP`; prohibit post-value rescue and return Stage 0. / E01 positive 관계 미지지 종결·사후 구제 금지·Stage 0 복귀. | Frozen paired test gives negative RD and non-significant exact McNemar result; duplicate ambiguity handled under pre-frozen agreement-or-missing rule. | Issue #125; `CLM-166`; Run `34722366631` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

status_p.write_text("""---
checkpoint_id: CHK-20260913-US-RCRA-E01-TERMINAL-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 125
last_completed_research: US-RCRA-E01
last_decision: DEC-174
updated: 2026-09-13
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_RCRA_E01_NO_POSITIVE__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

US-RCRA-E01 completed at **`NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP`**. The frozen complete-pair test had 284 analyzable pairs and 92 discordant pairs; pre violation-found risk 41.90% vs post 39.08%, RD −2.817pp, exact McNemar p=0.4657. This is non-causal and does not establish a protective effect.

## Exact next action / 정확한 다음 행동

Return to Stage 0 and compare independent alternatives. Do not rescue US-RCRA-E01 with post-outcome changes to disaster definition, inspection pairing/window, duplicate handling, outcome coding, statistical test or materiality threshold.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text("""---
checkpoint_id: CHK-20260913-US-RCRA-E01-TERMINAL-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 125
last_completed_research: US-RCRA-E01
last_decision: DEC-174
updated: 2026-09-13
---

# Session Handoff / 세션 인수인계

US-RCRA-E01 / Issue #125 is terminal at **`NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP`**.

Frozen result: 297 structural pairs; 284 analyzable Y/N pairs; 92 discordant; NN=123, N→Y=42, Y→N=50, YY=69; pre risk 41.9014%, post risk 39.0845%; RD −2.8169pp; exact two-sided McNemar p=0.465707. 32 selected identities had duplicate source rows differing only in agency; 25 outcome classes agreed, 7 conflicted and were treated as missing under the pre-frozen agreement-or-missing rule. Same-single-agency sensitivity was also negative/non-significant and is non-rescuing.

Execution-integrity limitation: an earlier failed Pass-2 technically projected selected outcome fields before duplicate failure, but produced no surfaced/persisted/aggregated outcome statistic and did not alter the scientific contract. See Issue #125 integrity note and `RESULT.md`.

Exact restart: Stage 0 independent-candidate comparison. No US-RCRA-E01 rescue/reversal. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": "CHK-20260913-US-RCRA-E01-TERMINAL-PORTFOLIO-RETURN",
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 125,
    "last_completed_research": "US-RCRA-E01",
    "last_decision": "DEC-174",
    "updated": "2026-09-13"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
