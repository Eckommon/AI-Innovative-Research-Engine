---
id: MEM-054
type: memory
state: VALIDATED
created: 2026-09-03
source_of_truth: github
related:
  - docs/RESEARCH_PROCESS_AUDIT_2026-09-03.md
  - docs/GOVERNANCE.md
  - docs/METHODOLOGY.md
  - registry/DEC-093.md
---

# MEM-054 — Mission Anchor & Branch-Stop Memory / 목적 고정기억 및 Branch-Stop 규칙

## Fixed Mission / 고정 목적

**KO:** AI-Innovative-Research-Engine의 최상위 목적은 특정 데이터셋·실험·도구를 끝까지 완주하는 것이 아니다. 공공·연구 데이터를 발견·정규화·결합하고, **데이터 간 관계에서 새롭고 반증 가능하며 재현 가능하고 실용적인 산업·기술·사회 혁신 기회 또는 구조적 병목 통찰을 발견·검증·축적하는 것**이다.

**EN:** The highest-level purpose of AI-Innovative-Research-Engine is not to finish any particular dataset, experiment, or toolchain at all costs. It is to discover, normalize, and combine public/research data and to **discover, test, and accumulate new, falsifiable, reproducible, and practically useful innovation opportunities or structural-bottleneck insights from relationships among data**.

## Mission Priority / 목적 우선순위

When priorities conflict, use this order: / 우선순위 충돌 시 다음 순서를 적용한다.

1. **Mission-level innovation/bottleneck discovery value / 미션 수준 혁신·병목 발견 가치**
2. **Cross-dataset / cross-agency / cross-national relationship value / 데이터셋·기관·국가 간 관계 가치**
3. **Falsifiability and reproducible evidence / 반증 가능성·재현 증거**
4. **Practical utility and scalability / 실용성·확장성**
5. **Efficient source/compute route / 효율적 source·연산 경로**
6. **Completion of a particular branch / 특정 branch 완주**

A route dependency must never be silently promoted into a mission dependency. / 특정 경로의 의존성을 프로젝트 전체의 필수 의존성으로 승격하지 않는다.

## Branch-Stop / MISSION-ROI Rule / Branch 중단 규칙

Before opening any descendant gate after a `HOLD`, `REJECT`, runtime failure, or source-access failure, explicitly answer:

1. Does the proposed next gate reduce a **scientific/innovation uncertainty**, or mainly a tooling/transport/runtime uncertainty?
2. Is the blocked source or route uniquely necessary to the **project-level hypothesis**, or only to one implementation route?
3. Is a higher-value independent candidate available in the portfolio?
4. Have there been **two consecutive infrastructure/runtime/source-transfer gates** without new scientific evidence?
5. Would stopping the branch lose a unique validated claim, or only defer one test?

### Default stop condition / 기본 중단 조건

If items 1–4 indicate primarily infrastructure/tooling work and an alternative candidate exists, default to:

**`HOLD_BRANCH / ARCHIVE_ROUTE → RETURN_TO_PORTFOLIO`**

Do not open another numbered descendant merely because a technically possible workaround exists.

### Override / 예외

Continue a tooling-heavy branch only when at least one is true:
- the source/route is uniquely necessary for a high-value project claim;
- no credible alternative candidate exists;
- the expected next gate has clearly documented high mission-level information value;
- the user explicitly prioritizes finishing that branch.

## AMBENCH P01 / 18 MB Example / 현재 사례

`RHF_Command.zip` (18,079,576 bytes) is **not project-essential**. It is a route dependency of the exact P01/3DThesis descendant benchmark. E43/F44/F45 are preserved as valid HOLD records. F46 remains dormant unless a future portfolio review or explicit user instruction reauthorizes it.

## Mandatory Session Behavior / 세션 의무

Before material work, future sessions must recover this Mission Anchor together with README, STATUS, PROJECT_MEMORY, SESSION_HANDOFF, live Issues, and relevant decision records. When a proposed next action conflicts with this mission anchor, the mission anchor wins unless the user explicitly changes the project mission.

## Cost / 비용

`COST-001` remains mandatory. Mission alignment does not authorize paid work; any potentially billable action still requires explicit prior user approval.
