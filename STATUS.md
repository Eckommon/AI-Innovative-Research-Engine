---
checkpoint_id: CHK-20260903-KR-PORT-F01-ACTIVE
active_issue: 65
active_research: KR-PORT-F01
last_completed_issue: 64
last_completed_research: PORTFOLIO-R01
last_decision: DEC-094
updated: 2026-09-03
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**State / 상태:** `MISSION_ANCHOR_FIXED__PORTFOLIO_RESET_COMPLETE__KR_PORT_F01_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #65 `KR-PORT-F01 — Port-call identity & turnaround-target feasibility`.

## Fixed Mission / 고정 목적

The highest-level purpose is to discover and validate **new, falsifiable, reproducible, and practically useful innovation opportunities or structural bottlenecks from relationships among public/research data**.

특정 데이터셋·실험·도구·시뮬레이터·재현경로의 완주는 목적이 아니다. `context/MEM-054-MISSION-ANCHOR.md` is mandatory durable memory.

## Governance correction / 거버넌스 보정

Mandatory controls:
- `MEM-054` Mission Anchor;
- `DEC-093` Mission-ROI / Branch-Stop;
- updated `docs/GOVERNANCE.md`;
- updated `docs/METHODOLOGY.md` with Stage 0 Portfolio Selection and Stage 9 Portfolio Return;
- `COST-001` zero-incremental-cost default.

Default branch stop:
**>=2 consecutive infrastructure/runtime/source-transfer descendants without new scientific evidence + credible alternative + route not uniquely mission-critical → HOLD/ARCHIVE route and RETURN_TO_PORTFOLIO.**

## PORTFOLIO-R01 completed / PORTFOLIO-R01 완료

Issue #64 completed under `DEC-094`.

Selected primary:
**`C-KR-003 Port Weakest-Link Intelligence / 항만 최약고리 지능화`**.

Ranked secondary portfolio:
2. `C-EU-001` Cross-National Grid Stress — HOLD_READY_SECONDARY;
3. `C-EU-004` Industrial Site Climate Risk — HOLD_READY_SECONDARY;
4. `C-US-003` Critical Mineral Resilience — HOLD_READY_SECONDARY;
5. Wave 2 Japan/UK/Singapore discovery — CONTINUE_AFTER_PRIMARY_GATE;
6. independent non-P01 F37 thermal-history continuation — HOLD_BRANCH_LEVEL.

Durable result: `research/PORTFOLIO-R01/RESULT.md`.

## AMBENCH disposition / AMBENCH 상태

Preserve valid historical scientific/methodological assets, but the P01/E43-F46 route is not active.

`RHF_Command.zip` 18,079,576 bytes = **route dependency, not project dependency**.

F46 = **`DORMANT__NOT_ACTIVE__REQUIRES_REAUTHORIZATION`**.

## Active KR-PORT-F01 / 활성 KR-PORT-F01

Purpose: before long-history extraction or modeling, qualify one deterministic port-call identity and one defensible arrival→departure operational turnaround/stay target across official Korean port data.

Frozen candidate identity:
`(port/port-authority identifier, arrival year, arrival count, call sign)`.

Frozen target candidate if same-call semantics pass:
`port_stay_hours = departure_timestamp - arrival_timestamp`.

Current official metadata already confirms:
- vessel/entry-exit data expose port, call sign, arrival count and arrival/departure-time semantics;
- Ministry of Oceans and Fisheries port-facility-use API queries by `prtAgCd + etryptYear + etryptCo + clsgn` and returns the same identifiers plus berth/mooring-place context;
- KMA ASOS provides hourly weather context through a free official API.

Do not call the target berth delay/congestion delay without additional timestamps establishing those constructs.

## Exact next action / 정확한 다음 행동

Execute only the frozen `KR-PORT-F01` feasibility checks in `research/KR-PORT-F01/README.md`:
- exact field/identity semantics;
- duplicate/correction rules;
- same-call arrival/departure validity;
- nested facility-use semantics;
- weather-join route;
- bounded free sample-access feasibility.

No long-history download or predictive model is authorized yet.

If HOLD/REJECT: return immediately to Stage 0 portfolio selection. If PASS: at most one preregistered controlled experiment before another mandatory Mission-ROI review.

Incremental monetary cost remains `0 USD`.
