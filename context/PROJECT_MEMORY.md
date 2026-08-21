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

### `MEM-006` — Former Active Issue #8 / 이전 활성 Issue #8
- **KO:** Issue #8 `EU-STEEL-R01`은 EEA 철강 수은집약도 historical `-36%` 관계의 독립 재현으로 시작됐다.
- **EN:** Issue #8 `EU-STEEL-R01` began as an independent reproduction of EEA's historical steel-mercury `-36%` relationship.
- **State:** `SUPERSEDED_BY_MEM-012`
- **Source:** Issue #8; `research/EU-STEEL-R01/README.md`
- **verified_at:** 2026-08-22

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

### `MEM-012` — EU-STEEL-R01 Final HOLD / 철강 수은집약도 재현 최종 HOLD
- **KO:** Issue #8은 `COMPLETED — HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`다. EEA `F1_3`·`F1_4`에서 2008 수은 4,312.9 kg, 2017 3,327.1 kg가 V3 재현됐지만, EEA가 사용한 historical `DS-066342`의 exact 2017 분모는 시험한 현행 Eurostat 공식 API/dataflow에서 더 이상 배포되지 않는다. 현행 EEA figure CSV의 35.0→20.5 g/kt는 -41.4286%로 2019 briefing 본문의 -36%와 충돌한다. 원인은 UNKNOWN으로 유지한다.
- **EN:** Issue #8 completed as `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`. EEA `F1_3` and `F1_4` V3-reproduce Hg totals of 4,312.9 kg (2008) and 3,327.1 kg (2017), but the exact 2017 denominator from historical `DS-066342` is no longer disseminated through tested current Eurostat official APIs/dataflow. The current EEA figure CSV's 35.0→20.5 g/kt implies -41.4286%, conflicting with the 2019 briefing narrative -36%; cause remains UNKNOWN.
- **State:** `VALIDATED` project outcome
- **Source:** closed Issue #8; `research/EU-STEEL-R01/REPRODUCTION_RESULT.md`; `CLM-010..013`; `DEC-009`
- **verified_at:** 2026-08-22

### `MEM-013` — Snapshot/Version Lineage Gate / Snapshot·버전 계보 게이트
- **KO:** historical 연구는 현재 URL/API 접근성만으로 재현 가능하다고 판단하지 않는다. exact/official archived snapshot 또는 요구 범위를 덮는 권위 있는 replacement correspondence가 필요하다. `reproduction_risk`는 우선 IPS 가중치가 아닌 별도 gate/modifier다.
- **EN:** Historical research is not considered reproducible from current URL/API accessibility alone. It requires an exact/official archived snapshot or authoritative replacement correspondence covering the required scope. `reproduction_risk` is initially a separate gate/modifier rather than an IPS weight.
- **State:** `VALIDATED` methodology policy
- **Source:** Issue #10 `METHOD-001`; `docs/METADATA_SCHEMA.md` v0.3; `registry/GLOBAL_PUBLIC_DATA_SOURCE_REGISTRY.md` v0.2; `DEC-010`
- **verified_at:** 2026-08-22

### `MEM-014` — Former Queue State / 이전 큐 상태
- **KO:** Issue #8·#10 이후의 `READY_FOR_NEXT_CANDIDATE` 상태는 Issue #11 `AMBENCH-F02` 착수로 종료됐다.
- **EN:** The post-Issue-#8/#10 `READY_FOR_NEXT_CANDIDATE` state ended when Issue #11 `AMBENCH-F02` began.
- **State:** `SUPERSEDED_BY_MEM-015`
- **Source:** historical `STATUS.md`; Issue #11
- **verified_at:** 2026-08-22

### `MEM-015` — AMBENCH-F02 Track-Level Alignment PASS / AM Bench track-level 정렬 PASS
- **KO:** Issue #11 `AMBENCH-F02`는 `COMPLETED — PASS`다. NIST thermography README의 `/ThermalData/Line_X_Y_Z/`에서 `Z`가 각 line의 3개 반복 중 하나로 명시되고, optical README·checksum 검증 XLSX가 동일 case+track 번호를 보존한다. 따라서 21개 single-track에 대해 exact track/repeat ID 조인이 가능하다. 단, optical은 line당 두 단면 측정이므로 이를 별도 thermography 반복으로 취급하지 않고 nested/집계 outcome으로 사용한다.
- **EN:** Issue #11 `AMBENCH-F02` completed as `PASS`. NIST thermography defines `Z` in `/ThermalData/Line_X_Y_Z/` as one of three repeats per line, while the optical README and checksum-verified workbook preserve matching case+track numbers. Exact track/repeat joins are therefore available for all 21 single tracks. Because optical data contain two cross-sections per line, they must be modeled as nested/aggregated outcomes rather than extra thermography repeats.
- **State:** `VALIDATED`
- **Source:** closed Issue #11; Run `32535986814`; `research/AMBENCH-F02/README.md`; `CLM-014..015`; `DEC-011`
- **verified_at:** 2026-08-22

### `MEM-016` — AM Bench Snapshot Risk Low / AM Bench snapshot 위험 낮음
- **KO:** `mds2-2716`·`mds2-2718`의 시험한 version-specific PDR manifest는 공식 NIST에서 직접 복구되며 optical 결과 XLSX는 actual bytes·sidecar·PDR metadata checksum이 3중 일치한다. 두 소스의 `reproduction_risk`는 `LOW`로 판정한다.
- **EN:** Tested version-specific PDR manifests for `mds2-2716` and `mds2-2718` are directly recoverable from NIST, and the optical result workbook has an exact three-way checksum match across downloaded bytes, sidecar, and PDR metadata. `reproduction_risk` is `LOW` for both sources.
- **State:** `VALIDATED`
- **Source:** Run `32535986814`; `research/AMBENCH-F02/README.md`
- **verified_at:** 2026-08-22

### `MEM-017` — AMBENCH-E03 Negative Calibration / AM Bench 음성 보정
- **KO:** Issue #13 `AMBENCH-E03`은 `COMPLETED — NO_MATERIAL_GAIN`이다. 21개 physical track, process-case LOCO, 동일 Ridge, outcome-blind 10개 raw-DL thermography feature를 사전고정한 뒤 실행했으며 Combined 대비 Process-only pooled RMSE 개선율은 depth `-19.2914%`, width `-21.1668%`로 둘 다 악화했다. 이 결과를 E03 내부 tuning으로 제거하지 않는다.
- **EN:** Issue #13 `AMBENCH-E03` completed as `NO_MATERIAL_GAIN`. With 21 physical tracks, process-case LOCO, identical Ridge models, and ten outcome-blind raw-DL thermography features frozen before outcomes, Combined-vs-Process pooled RMSE improvement was `-19.2914%` for depth and `-21.1668%` for width. The result must not be tuned away inside E03.
- **State:** `VALIDATED`
- **Source:** closed Issue #13; Run `32537495534`; artifact `9465900222`; `research/AMBENCH-E03/RESULT.md`; `CLM-016..017`; `DEC-012`
- **verified_at:** 2026-08-22

## Maintenance Rule / 유지 규칙

- Add only durable, decision-relevant facts. / 지속적 의사결정 관련 사실만 추가.
- Supersede old items explicitly; do not silently rewrite historical decisions. / 과거 결정을 조용히 덮지 말고 supersede 관계 명시.
- Dynamic facts require freshness verification. / 동적 사실은 최신성 재검증.
- `context/SESSION_HANDOFF.md` carries operational detail; this file stays compact. / 운영 세부는 Session Handoff에 두고 본 파일은 압축 유지.

Official artifacts comply with `LANG-001`, `READ-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
