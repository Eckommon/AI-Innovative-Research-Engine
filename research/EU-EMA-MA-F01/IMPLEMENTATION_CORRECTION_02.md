---
id: EU-EMA-MA-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-09-29
issue: 175
attempt_01_run: 36529679263
attempt_01_commit: 56c557a334ee82401217e99d4700825889f248a9
attempt_01_disposition: IMPLEMENTATION_BLOCKED_EU_EMA_MA_F01_ATTEMPT_01
scientific_threshold_changed: false
population_changed: false
identity_rule_changed: false
historical_event_rule_changed: false
future_outcome_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# EU-EMA-MA-F01 — Attempt 02 implementation-only correction

Attempt 01 is immutable and preserved. It passed Gates 1–4, resolved the official EMA download selector to:

`https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx`

and then stopped before baseline row parsing because the runner stored the downloaded XLSX bytes in an intermediate file named `medicines.bin`. `openpyxl` rejects unsupported filename extensions even when the body is a valid XLSX ZIP container.

## Authorized correction / 허가된 보정

Attempt 02 may only:
1. derive the temporary baseline filename extension from the already-resolved official URL;
2. preserve `.xlsx` for the current EMA table;
3. write evidence to separate immutable `attempt-02.json/.md` files.

No parser field alias, scientific threshold, population definition, EMA product-number rule, historical event threshold, event hierarchy, source selector, cutoff date or future-event firewall may change in this correction.

## Frozen boundaries retained / 유지 경계

- contract: `215cd9dd74a358e412a86de5d41a039c2f8186cb`
- Issue #175
- human centrally authorised medicine focal population
- exact ID pattern `^EMEA/H/C/[0-9]{6}$`
- all 18 gates and thresholds
- historical source cutoff: 2026-09-29
- future event membership from 2026-09-30 onward remains unopened
- no medicine-name/holder/substance/fuzzy/manual identity repair
- no relationship/prediction/ranking/causal computation
- cost = 0 USD

If Attempt 02 reaches empirical gates and any frozen gate fails, that result is scientific evidence and must not be improved by changing thresholds or event definitions after observation.
