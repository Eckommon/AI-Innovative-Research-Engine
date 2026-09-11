---
id: PORTFOLIO-R12-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-11
issue: 95
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-005
selected_gate: US-UTIL-F02
next_issue: 96
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R12 Result — Post-US-UTIL JOIN_READY Reselection
# PORTFOLIO-R12 결과 — US-UTIL JOIN_READY 이후 재선정

## Final selection / 최종 선정

**`SELECT_C_US_005_LONGITUDINAL_COMPARABILITY_PREFLIGHT`**

Selected next gate:

**Issue #96 `US-UTIL-F02` — 2019–2024 longitudinal comparability and panel-feasibility preflight.**

This selection opens no SAIDI/SAIFI magnitude, AMI meter-count magnitude, storm severity/damage value or relationship coefficient. / 본 선정은 효과값을 열지 않는다.

## Why F02, not an immediate E01 / 즉시 E01이 아닌 이유

US-UTIL-F01 established a strong one-year 2024 deterministic join asset: 842 fully county-qualified reliability utilities with AMI support and 6,341 qualified utility×county mappings. That removes source/join uncertainty but not longitudinal comparability. / 2024 결합 가능성은 확인됐지만 다년 비교가능성은 아직 미검증이다.

EIA documents Advanced Metering from 2007-present, Reliability from 2013-present, Service Territory from 2001-present, and the respondent Frame from 2016-present. Reliability respondents may use IEEE standards or another method, and official reliability tables distinguish all-events/major-event-inclusive from without-major-event measures. Therefore a direct effect experiment before prospectively controlling reporting basis would mix measurement regimes. / 보고방식·MED 의미를 먼저 고정해야 한다.

External prior evidence also means generic `AMI helps outage management/resilience` is not itself a defensible novelty claim: NIST has quantified smart-grid operational resilience using AMI penetration as a proxy, and DOE has long described AMI as a storm-response/outage-management technology. F02 therefore asks a narrower question: can a reproducible national multi-year panel exist under stable semantics before any outcome is opened? / 일반 메커니즘 신규성은 가정하지 않는다.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; total /45. Scores are selection aids, not empirical findings. / 점수는 선정 보조이며 실증결과가 아니다.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-UTIL-F02 longitudinal comparability** | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | **43** | **SELECT** |
| C-US-006 Inland Waterway Hydrology × Lock Delay | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | **41** | HOLD_SECOND |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_OPERABILITY |
| C-CA-002 Grain Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 1 | **35** | NO_AUTO_CONTINUATION |
| US-AIR descendant | 3 | 4 | 4 | 5 | 3 | 5 | 5 | 2 | 0 | **31** | NO_AUTO_CONTINUATION |

## C-US-006 operability refresh / C-US-006 운용성 갱신

USGS now exposes historical daily hydrology through modern machine-readable APIs, and Corps Locks exposes public LPMS-derived reports. However, the readily public Corps Locks views separate short-window queue/status from annual usage/unavailability summaries; a clean long historical vessel-delay panel still requires a separate source-feasibility gate. / hydrology는 강하지만 장기 delay outcome route는 아직 US-UTIL보다 불확실하다.

## Exact next gate / 정확한 다음 gate

Execute only **US-UTIL-F02 outcome-blind longitudinal comparability preflight** over 2019–2024 final EIA-861 and matched NOAA Storm Events sources.

Do not read reliability magnitudes or AMI meter-count magnitudes. First establish source hashes, schema continuity, utility identity continuity, Reliability reporting-basis metadata, AMI numerator/denominator field routes, Service Territory county continuity, NOAA county routes and frozen repeated-support counts. / 먼저 다년 비교가능성만 검증한다.

## Official/current source basis / 공식·현행 source 근거

- EIA-861 annual detailed data: https://www.eia.gov/electricity/data/eia861/
- USGS Water Data API: https://api.waterdata.usgs.gov/
- Corps Locks / LPMS public reports: https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home
- NIST, Quantifying Operational Resilience Benefits of the Smart Grid: https://www.nist.gov/publications/quantifying-operational-resilience-benefits-smart-grid

Incremental monetary cost remained **0 USD**.
