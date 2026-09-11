---
id: US-UTIL-F02-BASIS-ADJUDICATION
type: prospective-semantic-contract
created: 2026-09-11
issue: 96
state: FROZEN_BEFORE_SOURCE_VALUES
reliability_magnitudes_parsed: false
ami_magnitudes_parsed: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F02 Reliability Basis and Grain Adjudication
# US-UTIL-F02 Reliability Basis 및 Grain 사전판정

## Why this clarification is required / 명시 이유

EIA-861 schedules can contain a utility in more than one state. Therefore F02 must preserve `Utility Number × State` support rather than silently treating every Utility Number as one homogeneous row. / 다주 utility의 state-level 구조를 보존한다.

## Frozen reporting-basis support rule / 보고기준 지원도 규칙

F02 may inspect **blank/nonblank presence only**, never the numerical magnitude, in the Reliability cells prospectively identified from workbook header groups as:

- `IEEE Standard`;
- `With Major Event Days` / equivalent with-MED header group;
- `SAIDI` and `SAIFI`.

A utility-state-year is `IEEE_WITH_MED_SUPPORTED` only when both prospectively resolved IEEE-with-MED SAIDI and SAIFI cells are nonblank. The cell contents are never converted to numbers, summarized, ranked or persisted. / 값 자체는 읽지 않고 존재 여부만 사용한다.

If the headers cannot unambiguously distinguish IEEE vs Other Standard and with-MED vs without-MED, that year fails reporting-basis identifiability.

## Multi-state utility rule / 다주 utility 규칙

A utility-year counts toward the frozen `comparable Reliability basis` threshold only when:

1. it has the required Reliability + AMI + Service Territory identity support for that year;
2. every Reliability state row for that utility-year is `IEEE_WITH_MED_SUPPORTED`;
3. none of its required state/county geography is unresolved under the deterministic county rule.

A multi-state utility is not split or selectively retained based on outcomes. If one required reporting state fails the basis rule, that utility-year is not counted as comparable. / 일부 state만 선택해 favorable subset을 만들지 않는다.

## AMI schema route / AMI schema 경로

F02 may inspect header labels only to establish whether every selected year contains identifiable routes for:

- AMI meter count numerator;
- AMR meter count component;
- standard/non-AMI/non-AMR meter component required for a future total-meter denominator.

F02 does not read those meter-count cell values.

## Future experiment boundary / 향후 실험 경계

F02 does not choose the final E01 unit or outcome. A later E01 must explicitly decide whether the scientific unit is utility-state-year or another defensible aggregation and must preregister the exact AMI penetration denominator and Reliability outcome before magnitudes are opened.

Incremental monetary cost remains **0 USD**.
