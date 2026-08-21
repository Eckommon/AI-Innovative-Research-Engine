---
id: MOC-EXPERIMENTS
type: moc
state: ACTIVE
tags:
  - type/moc
  - domain/experiment
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# Experiments MOC / 실험 MOC

## Calibration Experiments / 보정 실험
- [AMBENCH-001](../research/AMBENCH-001/README.md) — aggregate multimodal feasibility; negative/conditional result retained / 집계 멀티모달 feasibility, 부정적·조건부 결과 보존.

## Feasibility Gates / 실행가능성 게이트
- [KR-GRID-F01](../research/KR-GRID-F01/README.md) — `HOLD`, completed / 지역 모선 mapping 미확립.
- [EU-IEE-F02](../research/EU-IEE-F02/README.md) — `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`, completed.

## Controlled Experiments / 통제실험
- [EU-IEE-E01](../research/EU-IEE-E01/README.md) — empirical `VALIDATED`, novelty `LOW / NOT NOVEL`.

## Reproduction Experiments / 독립 재현 실험
- **[EU-STEEL-R01](../research/EU-STEEL-R01/README.md) — Issue #8 `ACTIVE`: reproduce EEA E-PRTR × PRODCOM steel-mercury intensity relationship. / EEA 철강 수은집약도 raw 독립 재현.**

## Experiment Rule / 실험 규칙
Every controlled/reproduction experiment must predefine target, source crosswalk, baseline/reference, evaluation design, primary metric, material tolerance, rejection/hold criterion, and reproducibility reference before interpreting the final result. / 모든 통제·재현 실험은 최종 결과 해석 전 target·source crosswalk·기준값·평가설계·주요지표·허용오차·기각/HOLD 기준·재현참조를 사전 정의한다.

No post-hoc filtering is allowed solely to force agreement with a published reference. / 발표 기준값에 맞추기 위한 사후 필터 조정 금지.

Official artifacts comply with `LANG-001`, `READ-001`, and `FACT-001`. / 공식 산출물은 관련 규약을 따른다.
