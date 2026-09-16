---
id: US-FTA-TRANSIT-F01-RESULT
type: outcome-blind-source-schema-agency-mode-time-feasibility
created: 2026-09-16
issue: 147
state: COMPLETED_PASS
gate: PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY
source_run: 35063556654
staging_commit: de03e3e01b8b516e17ebb4baa1ef047a707d1a9c
breakdown_conditioned_major_safety_event_occurrence_opened: false
row_level_breakdown_event_join_persisted: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FTA-TRANSIT-F01 Result — agency-mode/time join-ready PASS

**`PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY`**

Run `35063556654` validly executed the frozen official-source FTA/NTD feasibility contract. All **19/19** preregistered requirements passed. This establishes source/schema/identity/time feasibility only; it does not establish that mechanical breakdowns predict or are associated with Major Safety Events.

## Empirical structural support / 구조적 실증 지원

### Breakdowns (`amkt-4ehs`)

- rows read: **3,731**
- supported report years: **2022, 2023, 2024**
- valid exact `NTD ID × mode × TOS × year` keys: **3,731**
- duplicate source-grain rows: **0**
- conflicting duplicate keys: **0**
- nonnumeric mechanical rows: **0**
- distinct `NTD ID × mode` pairs: **1,199**
- pairs represented in >=2 Breakdown years: **1,131**

### Monthly Modal (`5ti2-5uiv`)

- rows read: **192,312**
- supported years: **2014–2026**
- distinct calendar periods: **151**
- distinct `NTD ID × mode` pairs: **1,387**
- Breakdowns pairs represented in Monthly: **1,167 / 1,199 = 97.3311%**

Monthly duplicate structural rows are expected to be non-unique at the reduced `NTD ID × mode × year × month` projection because the source can contain additional scope dimensions. N01 must prospectively freeze the exact service-denominator aggregation semantics before using any service measure; F01 does not infer those semantics post hoc.

### Major Safety Events (`9ivb-8ae9`)

- structural-only rows read: **115,454**
- supported years: **2014–2026** across **13** distinct years
- distinct calendar periods: **149**
- distinct `NTD ID × mode` pairs: **1,038**
- exact aggregate Breakdowns∩Major pair overlap: **968**

Only `NTD ID`, mode and incident-time structural fields were requested from the Major Safety Events source. Event type, severity, casualty, agency-mode event count/rate and Breakdown-conditioned occurrence were not used for F01.

## Deterministic identity fingerprints / identity 지문

- Breakdowns pairs: `e14c25ba7c0d45ffbc4d42bc02ca8d378de5d42376ef378b54e95b5f3ec04e83`
- Monthly pairs: `06c6a5a224e3672df3cc237cd0f0dc45eacfdc39ec8f8f27a4a2781fbfbc9ae8`
- Major-event pairs: `d5b75b1cbdd001444e61477b356d84d8e16e4b9f0607f435f9923d09e9030559`
- Breakdowns∩Monthly: `284470d6ef552e448353925d1ec47cfb54d375fa56df836f1364a87632c79bba`
- Breakdowns∩Major: `e3ce8025e88a3ce264ac8cfcf9f81257d1d32d378e164c1f7c04b491f5092dcd`

## Outcome-blind boundary / 결과 비개봉 경계

- agency-name/address/manual/fuzzy identity repair: **not used**;
- Breakdown-conditioned Major Safety Event occurrence/rate/count: **not opened**;
- row-level Breakdown→event membership: **not persisted**;
- relationship/predictive statistic: **not computed**;
- causal or transit-agency safety-rating claim: **not made**;
- unofficial mirror/authentication bypass: **not used**;
- incremental monetary cost: **0 USD**.

## Interpretation / 해석

This PASS establishes that the selected official FTA/NTD source family is sufficiently large, repeated, source-native and structurally overlapping to support a **separate outcome-blind design-identifiability gate**. It does not authorize opening Major Safety Event outcome values directly from F01.

## Exact next action / 정확한 다음 행동

Open and preregister a separate `US-FTA-TRANSIT-N01` before any Breakdown-conditioned Major Safety Event outcome is opened. N01 must prospectively freeze the exposure measure, service-denominator aggregation, time ordering, eligible agency-mode-year units, missingness/exclusion rules and the exact future E01 statistical contract while keeping safety-event outcome values closed.

Incremental monetary cost remains **0 USD**.
