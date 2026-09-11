---
id: US-UTIL-F02-BASIS-HEADER-RESOLUTION
type: outcome-blind-schema-resolution
created: 2026-09-11
issue: 96
state: FROZEN_BEFORE_MAGNITUDES
reliability_magnitudes_parsed: false
ami_magnitudes_parsed: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F02 Basis Header Resolution
# US-UTIL-F02 보고기준 Header 해석 고정

## Trigger / 발생 사유

Run `34553361343` persisted a diagnostic showing 2024 Reliability/AMI identity counts of only `3/8`, while the already validated US-UTIL-F01 2024 source has `908/2,379`. This proves the F02 workbook selector chose a documentation/auxiliary worksheet rather than the data worksheet. / 동일 source에 대한 기존 검증값과 불일치하므로 research HOLD가 아니라 parser 오류다.

The same diagnostic exposed two distinct IEEE with-MED header families without opening values:
- full/all-events `SAIDI/SAIFI With MED`;
- `With MED Minus LOS` or `Loss of Supply Removed (With Major Event Days)` variants.

## Frozen execution resolution / 고정 실행 해석

1. For Reliability and Advanced Metering workbooks, select among worksheets containing an exact `Utility Number`/`Utility ID` header the worksheet with the **largest unique utility-ID cardinality**. This uses identity only and cannot select on outcomes.
2. The comparable Reliability basis remains **IEEE Standard, all events, with Major Event Days**.
3. Exclude header groups explicitly labeled `Minus LOS`, `Loss of Supply Removed`, `Without MED`, `Excluding`, or equivalent variants from the primary basis-support route.
4. Require exactly one resulting SAIDI and one SAIFI column for the primary basis in each year.
5. Continue using only blank/nonblank support of those two cells; never convert or persist their numerical contents.
6. AMI schema continues to use header labels only; no meter-count magnitudes are read.

## Boundary / 경계

This resolves source schema ambiguity only. Frozen years, cardinality thresholds, utility/county rules, PASS/HOLD gates and scientific promotion boundaries from DEC-132 are unchanged.

Run `34553361343` is therefore classified **EXECUTION/PARSER_INVALID_FOR_GATE**, not a scientific HOLD result, and must not be used as evidence for longitudinal infeasibility.

Incremental monetary cost remains **0 USD**.
