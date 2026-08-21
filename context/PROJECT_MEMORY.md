---
id: PROJECT-MEMORY
type: memory
state: ACTIVE
tags:
  - type/memory
  - state/validated
  - domain/governance
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# Project Memory / 지속 프로젝트 메모리

> 이 파일은 브레인스토밍 저장소가 아니라 **다음 세션이 반드시 알아야 하는 지속 사실·규약·판단의 압축 인덱스**다. / This is not a brainstorming store; it is a compact index of durable facts, policies, and decisions that the next session must know.

## Durable Memory Items / 지속 메모리 항목

### `MEM-001` — Repository Authority / 저장소 권위
- **KO:** `Eckommon/AI-Innovative-Research-Engine` GitHub 저장소가 프로젝트의 공식 지속 Source of Truth다.
- **EN:** The `Eckommon/AI-Innovative-Research-Engine` GitHub repository is the project's official persistent Source of Truth.
- **State:** `VALIDATED`
- **Source:** `README.md`, `docs/GOVERNANCE.md`, `docs/GPT_GITHUB_SYNC_PROTOCOL.md`
- **verified_at:** 2026-08-22

### `MEM-002` — Bilingual Policy / 병기 규약
- **KO:** `LANG-001`은 주요 사람이 읽는 산출물의 한글/영문 병기를 의무화한다.
- **EN:** `LANG-001` mandates Korean-English bilingual major human-readable artifacts.
- **State:** `VALIDATED`
- **Source:** `docs/LANGUAGE_POLICY.md`
- **verified_at:** 2026-08-22

### `MEM-003` — Wave 1 Completed / Wave 1 완료
- **KO:** 공식 초기 Work Queue #1–#4(AMBENCH, 미국, 한국, EU)는 완료됐다.
- **EN:** Initial official Work Queue Issues #1–#4 (AMBENCH, U.S., Korea, EU) are complete.
- **State:** `VALIDATED`
- **Source:** closed Issues #1–#4; `research/WAVE1-SYNTHESIS.md`
- **verified_at:** 2026-08-22

### `MEM-004` — KR-GRID-F01 HOLD / 한국 계통 mapping HOLD
- **KO:** KPX `bus_number`를 현행 공개 근거만으로 지역·설비에 안정적으로 귀속하는 경로는 확립되지 않았다. Issue #5 feasibility는 `HOLD` 결과로 완료됐다. 지리 귀속 없는 system-level 연구만 허용된다.
- **EN:** A defensible current public mapping from KPX `bus_number` to stable geography/assets has not been established. Issue #5 feasibility is complete with a `HOLD` outcome. System-level research without geographic attribution remains eligible.
- **State:** `VALIDATED`
- **Source:** closed Issue #5; `research/KR-GRID-F01/README.md`
- **verified_at:** 2026-08-22

### `MEM-005` — First Cross-Dataset Experiment / 첫 cross-dataset 실험
- **KO:** `EU-IEE-E01`은 EEA 산업배출 + Eurostat 산업 GVA 관계에서 사전 decoupling gate를 통과했다. 실증상태는 `VALIDATED`이나 신규성은 `LOW / NOT NOVEL`이다.
- **EN:** `EU-IEE-E01` passed its predefined decoupling gate using the EEA industrial-emissions + Eurostat industrial-GVA relationship. Empirical state is `VALIDATED`; novelty is `LOW / NOT NOVEL`.
- **State:** `VALIDATED`
- **Source:** closed Issue #6; `research/EU-IEE-E01/README.md`
- **verified_at:** 2026-08-22

### `MEM-006` — Active Work Queue / 활성 Work Queue
- **KO:** 현재 활성 연구 큐는 Issue #8 `EU-STEEL-R01`이며 EEA가 발표한 E-PRTR × PRODCOM 철강 수은집약도 2008→2017 `-36%` 관계를 raw 공식 입력에서 독립 재현한다.
- **EN:** The active research queue is Issue #8 `EU-STEEL-R01`, independently reproducing EEA's published E-PRTR × PRODCOM steel-mercury intensity 2008→2017 `-36%` relationship from official raw inputs.
- **State:** `ACTIVE`
- **Source:** Issue #8; `research/EU-STEEL-R01/README.md`
- **verified_at:** 2026-08-22
- **supersedes:** previous `MEM-006` active Issue #7 state.

### `MEM-007` — Facility Denominator Constraint / 시설 분모 제약
- **KO:** 국가·sector 생산량을 임의로 개별 시설에 배분하여 시설단위 배출효율을 만들지 않는다. plant-level production denominator 또는 권위 있는 allocation method가 필요하다.
- **EN:** Do not arbitrarily allocate country/sector production to individual facilities to create facility-level efficiency metrics. Plant-level production denominators or an authoritative allocation method are required.
- **State:** `VALIDATED` governance decision
- **Source:** closed Issue #7; `research/EU-IEE-F02/README.md`; `registry/DECISION_LOG.md`
- **verified_at:** 2026-08-22

### `MEM-008` — Obsidian Knowledge Layer / Obsidian 지식 레이어
- **KO:** 저장소 루트를 Obsidian Vault로 사용하며 GitHub Markdown이 기준 기록이다. Obsidian은 MOC·백링크·태그·Graph 탐색 레이어다.
- **EN:** The repository root is used as the Obsidian Vault while committed GitHub Markdown remains authoritative. Obsidian provides MOC, backlinks, tags, and graph navigation.
- **State:** `VALIDATED` policy
- **Source:** `docs/OBSIDIAN_KNOWLEDGE_MANAGEMENT.md`
- **verified_at:** 2026-08-22

### `MEM-009` — Hallucination Control / 환각 방지
- **KO:** 실질 작업 전 `READ-001` 선읽기가 의무이며, 미확인은 `UNKNOWN/HOLD`로 유지하고 ChatGPT 모델 기억을 프로젝트 사실의 단독 근거로 사용하지 않는다.
- **EN:** `READ-001` is mandatory before material work; unknowns remain `UNKNOWN/HOLD`, and ChatGPT model memory is never used as the sole authority for project facts.
- **State:** `VALIDATED` policy
- **Source:** `docs/HALLUCINATION_CONTROL_PROTOCOL.md`
- **verified_at:** 2026-08-22

### `MEM-010` — Critical Infrastructure Safety / 중요 인프라 안전
- **KO:** 간접 공개 식별자에서 중요 인프라의 정확한 위치나 운영 topology를 재구성·공개하지 않는다.
- **EN:** Do not reconstruct or publish precise critical-infrastructure locations or operational topology from indirect public identifiers.
- **State:** `VALIDATED` policy
- **Source:** `docs/GOVERNANCE.md`, Issue #5
- **verified_at:** 2026-08-22

### `MEM-011` — EU Normalization Granularity / EU 정규화 해상도
- **KO:** Issue #7은 `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`로 완료됐다. 명시적 E-PRTR activity ↔ PRODCOM product mapping이 있는 sector 집계는 가능하지만 일반 시설단위 분모는 보류한다.
- **EN:** Issue #7 completed as `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`. Explicitly mapped E-PRTR activity ↔ PRODCOM product sector aggregation is feasible; a generic facility denominator remains held.
- **State:** `VALIDATED`
- **Source:** closed Issue #7; `research/EU-IEE-F02/README.md`
- **verified_at:** 2026-08-22

## Maintenance Rule / 유지 규칙

- Add only durable, decision-relevant facts. / 지속적 의사결정 관련 사실만 추가.
- Supersede old items explicitly; do not silently rewrite historical decisions. / 과거 결정을 조용히 덮지 말고 supersede 관계 명시.
- Dynamic facts require freshness verification. / 동적 사실은 최신성 재검증.
- `context/SESSION_HANDOFF.md` carries operational detail; this file stays compact. / 운영 세부는 Session Handoff에 두고 본 파일은 압축 유지.

Official artifacts comply with `LANG-001`, `READ-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
