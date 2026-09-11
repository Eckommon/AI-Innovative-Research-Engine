---
id: US-UTIL-F02-RESULT
type: outcome-blind-longitudinal-comparability-result
created: 2026-09-11
issue: 96
gate: PASS_US_UTIL_F02_PANEL_DESIGN_READY
reliability_magnitudes_parsed: false
ami_magnitudes_parsed: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F02 Result — 2019–2024 Longitudinal Comparability
# US-UTIL-F02 결과 — 2019–2024 다년 비교가능성

## Outcome-blind boundary / 결과 비사용 경계

- Reliability SAIDI/SAIFI/CAIDI numeric magnitudes were never converted, summarized, ranked or persisted.
- IEEE-with-MED support used only blank/nonblank presence under the frozen BASIS_ADJUDICATION contract.
- AMI/AMR/standard-meter numeric magnitudes were never parsed; only header routes were inspected.
- Storm severity/damage magnitudes and all relationship coefficients were excluded.

## Frozen repeated-support gate / 고정 반복지원 gate

- utilities with Reliability+AMI+Service Territory in >=4/6 years: **883** (threshold 500)
- utilities with >=4 comparable IEEE-with-MED + complete-geography years: **819** (threshold 300)
- qualified repeated-support utility-year observations: **4,857** (threshold 2,000)
- qualified utility-year×county mappings: **37,156** (threshold 8,000)
- Reliability basis route identifiable all six years: **True**
- AMI numerator/denominator header route identifiable all six years: **True**
- NOAA county-key route reproducible all six years: **True**

## Per-year structural support / 연도별 구조 지원

| Year | Triple utilities | IEEE-with-MED complete | Geography complete | Comparable | Qualified utility×county | AMI route |
|---:|---:|---:|---:|---:|---:|---|
| 2019 | 1120 | 1121 | 1054 | 1054 | 7014 | True |
| 2020 | 881 | 881 | 824 | 824 | 6238 | True |
| 2021 | 893 | 893 | 835 | 835 | 6281 | True |
| 2022 | 894 | 895 | 832 | 832 | 6301 | True |
| 2023 | 901 | 902 | 838 | 838 | 6334 | True |
| 2024 | 907 | 906 | 842 | 840 | 6333 | True |

## Gate / 판정

**`PASS_US_UTIL_F02_PANEL_DESIGN_READY`**

A PASS is PANEL_DESIGN_READY only. It does not authorize or establish an AMI effect, storm effect, resilience benefit, causality, novelty or utility. / PASS여도 효과검증은 별도 사전등록이 필요하다.

## Durable derived artifacts / 영속 파생 산출물

- `SOURCE_MANIFEST.csv`
- `YEAR_SCHEMA_SUPPORT.csv`
- `UTILITY_YEAR_SUPPORT.csv`
- `QUALIFIED_UTILITY_YEAR_COUNTY.csv`

Raw EIA/Census/NOAA bytes were transient under RAW-001.

Incremental monetary cost remained **0 USD**.
