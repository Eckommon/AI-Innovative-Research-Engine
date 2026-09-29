---
id: PORTFOLIO-R48-IDENTIFIER-CORRECTION-01
type: governance-identifier-correction
created: 2026-09-30
issue: 183
original_scorecard_commit: 6fc8132426cf10bd54baf195c6d915884ccdf7ea
original_result_commit: 384a4a12ed483ee4aec6cb50e5399f48a1adcf63
scientific_selection_changed: false
score_changed: false
candidate_concept_changed: false
outcome_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R48 — Identifier Correction 01 / 식별자 충돌 교정

## Defect / 결함

The immutable R48 scorecard labeled the selected retirement candidate as `US-EIA-GEN-001` and described the next gate as `US-EIA-GEN-F01`.

Repository re-read after selection established that those identifiers were already occupied by a distinct terminal branch created under `PORTFOLIO-R36` on 2026-09-17:

- `US-EIA-GEN-001` = proposed/co-located solar+storage generator schedule → commissioning slippage;
- `US-EIA-GEN-F01` = Issue #156 structural feasibility;
- terminal result = `HOLD_US_EIA_GEN_F01_COLOCATED_SOLAR_STORAGE_LONGITUDINAL_DESIGN_NOT_READY`;
- 17/18 gates passed, with frozen cohort gate 8 failing at 664 < 1,000;
- that branch remains immutable and is not reopened.

This is a canonical identifier collision, not a scientific score or outcome defect.

## Correction / 교정

The R48-selected concept remains exactly:

> generator structure/performance → subsequent source-native generator retirement

Only its canonical identifiers are corrected prospectively to:

- candidate: **`US-EIA-RET-001`**
- F01: **`US-EIA-RET-F01`**

## Frozen items unchanged / 변경 없는 항목

The following remain unchanged:

- R48 candidate concepts;
- all nine score dimensions;
- all four numerical candidate scores;
- ordering: EIA retirement 43 > SEC adviser 40 = EPA RCRA 40 > FMCSA 38;
- all official-source evidence and longitudinal revalidation;
- anti-tautology boundary excluding planned/announced retirement signals;
- candidate future-event membership = unopened;
- zero-cost requirement.

The immutable scorecard itself is not rewritten. Wherever it uses `US-EIA-GEN-001` for the R48 retirement candidate, this correction supplies the canonical non-colliding identifier `US-EIA-RET-001`.

## Consequence / 후속

- Existing R36 `US-EIA-GEN-001 / US-EIA-GEN-F01` stays terminal and untouched.
- R48's selected retirement concept proceeds only as `US-EIA-RET-001`.
- The next gate, if opened, must be a new pre-Issue contract at `research/US-EIA-RET-F01/README.md`.
- No issue for the retirement F01 may be created until that new contract is committed.

Incremental monetary cost: **0 USD**.
