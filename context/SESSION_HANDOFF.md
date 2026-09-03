---
id: SESSION-HANDOFF
type: memory
state: ACTIVE
checkpoint_id: CHK-20260903-KR-PORT-F01-ACTIVE
active_issue: 65
active_research: KR-PORT-F01
last_completed_issue: 64
last_completed_research: PORTFOLIO-R01
last_decision: DEC-094
created: 2026-08-22
updated: 2026-09-03
source_of_truth: github
---

# Session Handoff / 세션 인수인계

## Mandatory first read / 의무 선읽기

Before material work, read and reconcile:
1. `README.md`;
2. `STATUS.md`;
3. `context/PROJECT_MEMORY.md`;
4. **`context/MEM-054-MISSION-ANCHOR.md`**;
5. this `SESSION_HANDOFF.md`;
6. live GitHub Issue state;
7. `registry/DEC-093.md`, `registry/DEC-094.md`, and relevant research/claim records.

`MEM-054` is the fixed purpose anchor. If a proposed next step conflicts with it, the Mission Anchor wins unless the user explicitly changes the project mission.

## Fixed Mission / 고정 목적

**KO:** 프로젝트의 최상위 목적은 특정 데이터셋·실험·도구를 끝까지 완주하는 것이 아니다. 공공·연구 데이터를 발견·정규화·결합하고, **데이터 간 관계에서 새롭고 반증 가능하며 재현 가능하고 실용적인 산업·기술·사회 혁신 기회 또는 구조적 병목 통찰을 발견·검증·축적하는 것**이다.

**EN:** The highest-level purpose is not to finish a particular dataset, experiment or toolchain. It is to discover, normalize and combine public/research data and **discover, test and accumulate new, falsifiable, reproducible and practically useful innovation opportunities or structural-bottleneck insights from relationships among data**.

Mission priority:
`mission innovation/bottleneck value → cross-dataset/cross-agency/cross-national value → falsifiability/reproducibility → practical utility/scalability → efficient route → branch completion`.

## Branch-Stop / Mission-ROI / Branch 중단

Mandatory `MEM-054 / DEC-093` default:

**>=2 consecutive infrastructure/runtime/source-transfer descendants without new scientific evidence + credible alternative + route not uniquely mission-critical → HOLD/ARCHIVE route and RETURN_TO_PORTFOLIO.**

A technically possible workaround alone does not justify another research ID.

## Portfolio reset result / 포트폴리오 재선정 결과

Issue #64 `PORTFOLIO-R01` completed under `DEC-094`.

Selected primary:
**`C-KR-003 Port Weakest-Link Intelligence / 항만 최약고리 지능화`**.

Secondary ranking:
2. `C-EU-001` Cross-National Grid Stress — HOLD_READY_SECONDARY;
3. `C-EU-004` Industrial Site Climate Risk — HOLD_READY_SECONDARY;
4. `C-US-003` Critical Mineral Resilience — HOLD_READY_SECONDARY;
5. Wave 2 Japan/UK/Singapore discovery — CONTINUE_AFTER_PRIMARY_GATE;
6. independent non-P01 F37 thermal-history continuation — HOLD_BRANCH_LEVEL.

Durable portfolio result: `research/PORTFOLIO-R01/RESULT.md`.

## AMBENCH disposition / AMBENCH 상태

Preserve valid scientific/methodological assets. P01/E43-F46 transport/runtime route is not active.

`RHF_Command.zip` 18,079,576 bytes is a **route dependency, not a project dependency**.

F46 = **`DORMANT__NOT_ACTIVE__REQUIRES_REAUTHORIZATION`**.

## Active Issue #65 — KR-PORT-F01

Purpose: qualify a deterministic official Korean port-call identity and a defensible arrival→departure operational turnaround/stay target before long-history extraction or modeling.

Frozen candidate identity:
`(port/port-authority identifier, arrival year, arrival count, call sign)`.

Frozen target candidate if same-call semantics pass:
`port_stay_hours = departure_timestamp - arrival_timestamp`.

Current official metadata supports the candidate route:
- vessel/entry-exit data describe port, call sign, arrival count and arrival/departure time;
- port-facility-use API explicitly uses `prtAgCd + etryptYear + etryptCo + clsgn` and returns berth/mooring context;
- KMA ASOS provides hourly physical-weather context.

Important boundary: `port_stay_hours` is not automatically berth waiting, congestion delay or cargo-handling time.

Preregistration: `research/KR-PORT-F01/README.md`.

## Exact Next Action / 정확한 다음 행동

Execute only KR-PORT-F01 feasibility checks:
- exact source/schema field correspondence;
- duplicate/correction semantics;
- same-call arrival/departure validity;
- nested facility-use relation;
- weather join route;
- bounded free sample access if available.

No long-history download or predictive model yet.

If HOLD/REJECT: immediate Stage 0 portfolio return. If PASS: at most one separately preregistered controlled experiment before another mandatory Mission-ROI review.

`COST-001` remains mandatory; incremental monetary cost stays `0 USD`.
