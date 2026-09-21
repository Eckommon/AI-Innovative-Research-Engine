---
id: US-HUD-MF-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-09-21
issue: 168
attempt_01_run: 35612698293
attempt_01_commit: 73ce4cfe7f475bb177186ab7d38ce7374f5e8fee
attempt_01_disposition: IMPLEMENTATION_BLOCKED_US_HUD_MF_F01_ATTEMPT_01
scientific_threshold_changed: false
snapshot_changed: false
identity_rule_changed: false
future_outcome_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# US-HUD-MF-F01 — Attempt 02 implementation-only correction

Attempt 01 is immutable and preserved. It successfully reached all three frozen HUD landing pages, resolved all four official HUD file selectors, downloaded the frozen active/terminated/property/inspection files, and preserved the future-outcome firewall, but it did **not** complete a valid 18-gate empirical execution.

## Demonstrated implementation defects / 확인된 구현 결함

1. **Active mortgage header alias**
   - Source header observed: `HUD PROJECT NUMBER`.
   - Runner recognized only FHA-oriented aliases such as `FHA Project Number`.
   - This caused the source-native identifier column to be treated as missing and produced artificial zero row/cardinality statistics.
   - Correction: add exact normalized alias `hudprojectnumber`. No identifier transformation changes.

2. **Terminated worksheet header detection**
   - Runner accepted the worksheet title/count row (`FHA_BF90_RM_T`, `58780`) as a header because the detector required only an FHA-like token.
   - Correction: require simultaneous project/FHA plus termination/date/reason header concepts before a terminated header row is accepted.
   - No termination category, threshold or semantic rule changes.

3. **Inspection file format**
   - Frozen official selector resolved to `MF-Inspection-Report.xls`, a legacy Excel binary file.
   - Attempt 01 tried to parse it as XLSX and stopped with `BadZipFile`.
   - Correction: add deterministic legacy-XLS parsing with pinned `xlrd==2.0.1`; XLSX remains pinned `openpyxl==3.1.5`.
   - The exact official inspection selector, snapshot and gate thresholds remain unchanged.

## Frozen boundaries retained / 유지되는 경계

Attempt 02 must retain exactly:
- contract `73eec2f714f3e1c89d0441ffb9f746721bda3443`;
- Issue #168;
- 2026-08-31 mortgage historical snapshot;
- 2026-09-02 property/inspection structural snapshot;
- exact FHA normalization: trim + uppercase + remove literal hyphen/ASCII spaces only, then exact 8 digits; no zero-padding;
- all 18 gates and thresholds;
- source-native adverse/routine semantic separation rule;
- future post-2026-09-21 terminated rows opened = 0;
- no relationship/prediction/ranking/causal computation;
- incremental monetary cost = 0 USD.

If Attempt 02 reaches the empirical gates and any frozen gate fails, the result is terminal scientific HOLD. A second implementation correction is not authorized merely to improve observed scientific support.
