---
id: US-HUD-MF-F01-IMPLEMENTATION-CORRECTION-03
type: implementation-only-correction
created: 2026-09-21
issue: 168
attempt_02_run: 35614642101
attempt_02_commit: 0dcd10db85848957ae950b592a13ed83348c1964
attempt_02_runner_disposition: HOLD_US_HUD_MF_F01_EXACT_PROJECT_ADVERSE_TERMINATION_DESIGN_NOT_READY
canonical_attempt_02_adjudication: IMPLEMENTATION_NONCONFORMITY_NOT_TERMINAL_SCIENTIFIC_HOLD
scientific_threshold_changed: false
snapshot_changed: false
identity_rule_changed: false
future_outcome_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# US-HUD-MF-F01 — Attempt 03 parser-only correction

Attempt 02 is immutable and preserved at commit `0dcd10db85848957ae950b592a13ed83348c1964` / Run `35614642101`.

The Attempt-02 runner emitted a nominal 13/18 HOLD, but the evidence itself demonstrates that the focal active-mortgage gate was **not empirically evaluated as specified** because the parser rejected a source field that satisfies the frozen concept.

## Demonstrated implementation defect / 확인된 구현 결함

The frozen Gate 5 requires the active workbook to expose FHA Project Number plus units, original mortgage amount, maturity date and an unpaid-principal-balance concept.

Attempt 02 directly observed the active source header:

`AMORITIZED PRINCIPAL BALANCE`

HUD's workbook spells this header **AMORITIZED**. The parser accepted `amortized...`, `unpaidprincipalbalance`, or `upb` aliases but not the exact observed source spelling `amoritizedprincipalbalance`.

Consequences in Attempt 02:

- header row and `HUD PROJECT NUMBER` were correctly found;
- `active_ok` nevertheless became false solely because the balance-column alias was not recognized;
- therefore the runner deliberately skipped active row iteration;
- `rows=0`, `nonblank_fha=0`, `valid_fha=0`, `distinct_valid_fha=0` were parser artifacts, not observed source cardinalities;
- Gates 7, 8, 13 and 15 then failed mechanically from the same artificial empty active cohort.

This is not a scientific support failure and does not justify changing any frozen criterion.

## Allowed Attempt-03 correction / 허용 보정

Attempt 03 may add exactly the observed normalized source alias:

`amoritizedprincipalbalance`

to the existing balance-column resolver. It may also retain the correctly spelled `amortizedprincipalbalance` alias for equivalent source spelling, without changing the required concept.

No other scientific or semantic change is authorized.

## Frozen boundaries retained / 유지되는 경계

Attempt 03 must retain exactly:

- pre-Issue contract `73eec2f714f3e1c89d0441ffb9f746721bda3443`;
- Issue #168;
- 2026-08-31 active/terminated mortgage snapshot;
- 2026-09-02 property/inspection snapshot;
- exact FHA normalization: trim + uppercase + remove literal hyphen/ASCII spaces only, then exact 8 digits; **no zero-padding**;
- all 18 gates and every numeric threshold;
- source-native termination-reason requirement;
- exact mortgage→property→inspection identity rules;
- future post-2026-09-21 terminated membership sealed;
- future entity-body bytes = 0;
- no relationship/prediction/ranking/causal computation;
- incremental monetary cost = 0 USD.

Attempt 03 is the next valid adjudication opportunity. If it computes the actual active cohort and one or more frozen scientific gates fail, that result is terminal for this exact F01. Further parser corrections may not be used to rescue an observed scientific failure.
