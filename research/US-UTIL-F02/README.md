---
id: US-UTIL-F02
issue: 96
state: ACTIVE_SOURCE_COMPARABILITY_PREFLIGHT
mission_anchor: MEM-054
portfolio_decision: DEC-131
contract_decision: DEC-132
period: 2019-2024
outcome_values_opened: false
ami_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F02 — 2019–2024 Longitudinal Comparability and Panel Feasibility
# US-UTIL-F02 — 2019–2024 다년 비교가능성 및 Panel Feasibility

## Objective / 목적

Test whether the 2024 JOIN_READY utility structure can be extended to a defensible multi-year panel **before any Reliability or AMI magnitude is opened**. / 효과값을 보기 전에 다년 비교가능성을 검증한다.

## Frozen sources / 고정 source

- EIA Form EIA-861 final annual ZIPs for **2019, 2020, 2021, 2022, 2023, 2024**.
- Schedule families: Reliability, Advanced Metering, Service Territory, and only the identity/frame support needed for cross-year continuity.
- NOAA/NCEI Storm Events annual bulk source for the same six years.
- Year-appropriate deterministic county-key support; no fuzzy utility names and no invented county weights.
- EIA 2025 early release excluded.

## Outcome-blind allowed reads / 결과 비사용 허용범위

F02 may read:
- source URL/bytes/SHA-256;
- archive member/workbook/sheet names;
- complete header strings needed to establish semantic continuity;
- EIA Utility Number identity;
- Reliability categorical/reporting-basis metadata needed to distinguish IEEE/other and major-event handling;
- Advanced Metering **field names only** required to identify future AMI numerator/denominator routes;
- Service Territory state/county identity;
- NOAA county FIPS/name identity and row/cardinality support;
- repeated-support counts across years.

F02 must not read into analysis, summarize or rank:
- SAIDI, SAIFI or CAIDI magnitudes;
- AMI, AMR or standard-meter count magnitudes;
- storm severity, damage, deaths/injuries or other intensity magnitudes;
- any AMI/storm/reliability coefficient.

## Frozen identity/comparability rules / 고정 identity·비교가능성 규칙

1. Utility identity = exact EIA `Utility Number` only.
2. Utility↔county remains many-to-many in each year.
3. No customer allocation across counties unless an official future weight is separately established.
4. Reliability reporting basis is not assumed homogeneous. Record the categorical method/major-event metadata that can be prospectively used to keep one comparable basis.
5. Header/schema changes are explicit drift, never silently repaired.
6. County identity changes are recorded and adjudicated deterministically; unresolved geography is excluded rather than fuzzily repaired.
7. Missing year support is missing; never impute a utility-year.

## Frozen structural PASS gate / 고정 구조 PASS gate

Require all:
- **>=500** unique utilities with Reliability + AMI + Service Territory support in at least **4 of 6 years**;
- **>=300** utilities with at least **4 years** on one prospectively identifiable comparable Reliability reporting basis;
- **>=2,000** qualified repeated-support utility-year observations;
- **>=8,000** qualified utility-year×county mappings after deterministic geography qualification;
- reproducible NOAA county-key route for **all 6 years**;
- future AMI numerator/denominator field route identifiable for **all 6 years** without reading magnitudes;
- zero incremental monetary cost.

If any condition fails:

**`HOLD_US_UTIL_F02_LONGITUDINAL_COMPARABILITY → Stage 0`**

Do not lower thresholds or substitute another outcome, period or exposure definition inside F02.

## PASS meaning / PASS 의미

A PASS means only:

**`PASS_US_UTIL_F02_PANEL_DESIGN_READY`**

It does not establish an AMI effect, storm effect, resilience benefit, causality, novelty or utility.

## Exact next action / 정확한 다음 행동

Execute the six-year source/schema/identity/reporting-basis/cardinality preflight only. Persist derived manifests and counts; keep raw ZIP/XLSX/GZ/CSV bytes transient under RAW-001.

Incremental monetary cost remains **0 USD**.
