---
checkpoint_id: CHK-20260904-CA-RAIL-E01-PREREGISTERED
active_issue: 84
active_research: CA-RAIL-E01
last_completed_issue: 83
last_completed_research: CA-RAIL-F01
last_decision: DEC-116
updated: 2026-09-04
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**State / 상태:** `MISSION_ANCHOR_FIXED__CA_RAIL_F01_PASS__CA_RAIL_E01_PREREGISTERED_OUTCOME_BLIND`  
**Active Work Queue / 활성 작업 큐:** Issue #84 `CA-RAIL-E01 — weekly extreme-cold × intermodal terminal-dwell panel experiment`.

## Fixed Mission / 고정 목적

Discover and validate **new, falsifiable, reproducible and practically useful innovation opportunities or structural bottlenecks from relationships among public/research data**. `MEM-054` remains mandatory.

## Parent feasibility / 상위 실행가능성

`CA-RAIL-F01` completed as:

**`PASS_CA_RAIL_TERMINAL_WEATHER_JOIN_READY`**

Frozen parent universe:
- 19 CN/CPKC carrier-terminal series;
- 105 Monday reporting weeks;
- maximum 1,995 carrier-terminal-week keys;
- support-key SHA-256 `454bce3a77510cedbe4ff0f81cdc561500ec40462396e63f6f36ef8ebaf361e7`.

## Active preregistered experiment / 활성 사전등록 실험

Primary question:

**Are colder weekly extreme minimum temperatures associated with longer weekly intermodal terminal dwell?**

Frozen weather exposure:
- ECCC daily **Minimum Temperature (°C)** only;
- weekly exposure = minimum daily Min Temp over Monday–Sunday;
- 7/7 valid daily values required.

Frozen outcome:
- Transport Canada intermodal terminal dwell hours;
- primary transform = `log1p(dwell hours)`.

Frozen model:
- carrier-terminal fixed effects;
- reporting-week fixed effects;
- one-way CR1 clustered by ECCC Climate ID;
- `t_(G-1)` inference.

Frozen hypothesis:
**beta < 0**.

Frozen PASS:
**`PASS_CA_RAIL_E01_EXTREME_COLD_DWELL_ASSOCIATION`**
only if beta is negative and the upper bound of the two-sided 95% station-clustered CI is below zero.

## Exposure boundary / 노출 경계

No selected ECCC weather observation has been opened yet.

Do not:
- inspect multiple weather variables;
- search temperature thresholds;
- test lags/leads;
- alter terminal/station universe;
- substitute another commodity or rail outcome.

## Exact next action / 정확한 다음 행동

Execute **Stage A only**:

1. resolve all 14 frozen ECCC Climate IDs to official daily-download station identities;
2. retrieve only 2024–2025 official daily data needed for the frozen stations;
3. pin request/response bytes and SHA-256;
4. validate station/date/schema identity;
5. parse only Min Temp + flag for 7/7 weekly completeness;
6. persist the station-week eligibility manifest;
7. apply the frozen Stage-A integrity gate.

Only if Stage A passes may Stage B open the frozen Transport Canada dwell magnitudes for the relationship calculation.

Incremental monetary cost remains **0 USD**. Any potentially billable action requires explicit prior approval.
