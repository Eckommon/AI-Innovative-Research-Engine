---
id: PORTFOLIO-R11-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-11
issue: 93
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-005
selected_gate: US-UTIL-F01
next_issue: 94
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R11 Result — Post-Low-Novelty Fresh Opportunity Reselection
# PORTFOLIO-R11 결과 — 낮은 신규성 판정 이후 신규 기회 재선정

## Final selection / 최종 선정

**`SELECT_C_US_005_UTILITY_AMI_STORM_RELIABILITY_JOIN_FEASIBILITY`**

Selected next gate:

**Issue #94 `US-UTIL-F01` — EIA-861 utility AMI/reliability/service-territory × NOAA Storm Events join feasibility.**

This selection opens no SAIDI/SAIFI magnitude, AMI effect or storm-reliability relationship. / 본 선정은 SAIDI/SAIFI 값·AMI 효과·폭풍-신뢰도 관계를 열지 않는다.

## Why a fresh branch wins / 신규 분기가 우선인 이유

US-AIR has a valid 2025 relationship result, but `US-AIR-N01` found the core precipitation-delay mechanism to have **LOW novelty**. The mission therefore favors an independent bottleneck with a direct operational outcome and a prospective technology/intervention dimension rather than another automatic aviation descendant. / US-AIR 핵심관계 신규성이 낮으므로 자동 연장보다 독립 병목을 우선한다.

C-US-005 combines four official, structurally complementary data families:
- EIA-861 utility identity and annual reporting frame;
- EIA-861 Advanced Metering support;
- EIA-861 Reliability support (SAIDI/SAIFI family, values not opened in F01);
- EIA-861 Service Territory county mappings;
- NOAA/NCEI Storm Events county exposure.

EIA explicitly documents Advanced Metering from 2007-present, Reliability from 2013-present, and Service Territory from 2001-present. The 2024 EIA-861 final-data ZIP is directly published; 2025 is only an early release and is not selected for the first gate. NOAA Storm Events publishes annual bulk CSV files. / 2024 final source를 첫 gate로 사용하고 2025 early release는 제외한다.

## Fresh candidate comparison / 신규 후보 비교

0–5 each; total /45. Scores are portfolio aids, not empirical innovation findings. / 점수는 선정 보조이며 실증 혁신결과가 아니다.

| Candidate | Mission bottleneck | Cross-source contribution | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-US-005 Utility AMI × Storm × Reliability** | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | **44** | **SELECT** |
| C-US-006 Inland Waterway Hydrology × Lock Delay | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | **41** | HOLD_SECOND |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_OPERABILITY |
| C-CA-002 Grain Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 1 | **35** | PRESERVE_JOIN__NO_AUTO_CONTINUATION |
| US-AIR descendant without a new decision/propagation/utility question | 3 | 4 | 4 | 5 | 3 | 5 | 5 | 2 | 0 | **31** | NO_AUTO_CONTINUATION |

## Why C-US-005 beats C-US-006 / C-US-006 대비 우위

USACE/USGS inland-waterway hydrology × lock delay is promising, but the readily verified public LPMS route is strongest for current/short-window queue/status and aggregate usage reports. A long historical lock-delay panel therefore has higher source-access risk. EIA-861 already exposes a long annual utility frame with the required identity, AMI, reliability and service-territory schedules. / C-US-005가 장기 panel source operability에서 우위다.

## Official source routes / 공식 source 경로

- EIA Form EIA-861: https://www.eia.gov/electricity/data/eia861/
- 2024 final ZIP: https://www.eia.gov/electricity/data/eia861/zip/f8612024.zip
- NOAA Storm Events bulk CSV: https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/

## Exact next gate / 정확한 다음 gate

Execute **US-UTIL-F01 source-byte/schema/cardinality preflight only**.

Do not read/rank reliability magnitudes and do not estimate an AMI or storm effect. First establish stable utility IDs, schedule support, service-territory many-to-many county mapping, NOAA county keys and frozen structural counts. / 먼저 identity·schema·cardinality만 검증한다.

Incremental monetary cost remained **0 USD**.
