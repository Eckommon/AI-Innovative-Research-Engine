---
id: PORTFOLIO-R13-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-11
issue: 97
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-006
selected_gate: US-WATERWAY-F01
next_issue: 98
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R13 Result — Post-US-UTIL PANEL_DESIGN_READY Reselection
# PORTFOLIO-R13 결과 — US-UTIL PANEL_DESIGN_READY 이후 재선정

## Final selection / 최종 선정

**`SELECT_C_US_006_INLAND_WATERWAY_HYDROLOGY_LOCK_DELAY_FEASIBILITY`**

Selected next gate:

**Issue #98 `US-WATERWAY-F01` — LPMS historical delay × USGS hydrology source/identity feasibility.**

This selection opens no vessel-delay magnitude, hydrology magnitude, SAIDI/SAIFI value, AMI meter count or relationship coefficient. / 본 선정은 결과값을 열지 않는다.

## Why C-US-006 now wins / C-US-006이 우선인 이유

US-UTIL-F02 established a strong 2019–2024 panel-design asset, but external novelty risk has materially increased: a 2025 peer-reviewed study already used 2014–2022 EIA-861 data to estimate associations between AMI adoption and SAIDI/SAIFI. A storm-moderation descendant could still be scientifically distinct, but its marginal mission value is lower until novelty and decision utility are separately justified. / US-UTIL은 실행가능성이 높지만 일반 AMI→reliability 관계의 한계수익이 낮아졌다.

USACE states that LPMS collects vessel movements, lockage times and delays. Public Lock Usage Report material has historically included lock-level Average Delay and Average Processing Time, while current Corps Locks also exposes official reports and Data Web Services. USGS modern Water Data APIs expose historical daily hydrology and monitoring-location metadata. The unresolved high-value uncertainty is whether a current, official, reproducible public route can support >=3 years of lock-level delay identity and deterministic hydrology matching. / 현재 공개경로의 재현가능성이 핵심 불확실성이다.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; total /45. Scores are selection aids, not empirical findings. / 점수는 선정 보조이며 실증결과가 아니다.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-US-006 Inland Waterway Hydrology × Lock Delay F01** | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | **43** | **SELECT** |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_OPERABILITY |
| US-UTIL preregistered AMI × Storm × Reliability descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_READY_HIGH_OVERLAP |
| C-CA-002 Grain Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 1 | **35** | NO_AUTO_CONTINUATION |
| US-AIR descendant | 3 | 4 | 4 | 5 | 3 | 5 | 5 | 2 | 0 | **31** | NO_AUTO_CONTINUATION |

## Official/current source basis / 공식·현행 source 근거

- USACE/NDC Locks and LPMS: https://www.iwr.usace.army.mil/About/Technical-Centers/NDC-Navigation-and-Civil-Works-Decision-Support/NDC-Locks/
- Corps Locks public system: https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home
- USACE Lock Characteristics FeatureServer: https://services7.arcgis.com/n1YM8pTrFmm7L4hs/arcgis/rest/services/Locks/FeatureServer
- USGS Water Data APIs: https://api.waterdata.usgs.gov/
- 2025 EIA-861 AMI/reliability precedent: https://doi.org/10.4018/JGIM.368257

## Exact next gate / 정확한 다음 gate

Execute only **US-WATERWAY-F01 source/schema/date-range/identity feasibility**.

Do not inspect delay values or hydrology values. First establish whether the official public USACE route provides >=3 contiguous years of lock-level historical delay or sufficient arrival/start timing fields, then test stable lock identity/location and USGS monitoring-location/date-support matching. / 먼저 공개 historical delay source와 identity만 검증한다.

Incremental monetary cost remained **0 USD**.
