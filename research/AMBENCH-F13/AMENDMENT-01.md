---
id: AMBENCH-F13-AMENDMENT-01
type: preregistration-amendment
state: FROZEN_BEFORE_GATE_APPLICATION
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F13/README.md
  - Issue #31
---

# AMBENCH-F13 Amendment 01 — Outcome-Blindness Correction
# AMBENCH-F13 수정 01 — outcome-blindness 정정

## Correction / 정정

**KO:** F13 README 작성 전 post-D12 source triage 과정에서 2024 A-AMB benchmark publication의 검색/본문 결과에 **scanned aluminum aggregate geometry 값(average maximum width/depth 및 표준편차)**이 노출되었다. 따라서 README의 `NEW_EXTERNAL_OUTCOME_BLIND = YES`는 엄밀히 사실이 아니다.

**EN:** Before the F13 README was written, the post-D12 source-triage search exposed **publication-level aggregate scanned-aluminum geometry values (average maximum width/depth and standard deviations)** from the 2024 A-AMB benchmark article. Therefore the README statement `NEW_EXTERNAL_OUTCOME_BLIND = YES` is not strictly correct.

Correct status / 교정 상태:

`NEW_EXTERNAL_OUTCOME_BLIND = NO — PUBLICATION_LEVEL_AGGREGATES_PREOBSERVED`

## What remains protected / 보호되는 범위

- No `mds2-2525` numerical CSV outcome file was downloaded or numerically inspected under F13.
- No time-dependent absorptance values, time-dependent width series, correlation, descriptor, alignment statistic, or predictive metric was calculated.
- F13's frozen gate depends only on source identity, component provenance, external independence, same-experiment/same-condition semantics, timing semantics, and repeat-resolution identity.
- The preobserved publication-level aggregate values are **not inputs to the F13 gate** and must not be used to tune a future experiment.

## Governance consequence / 거버넌스 결과

The original README is preserved as historical preregistration; this amendment supersedes only its outcome-blindness status. Frozen F13 gate definitions remain unchanged. / 원 README는 이력으로 보존하며 이 수정은 outcome-blindness 상태만 정정한다. F13 gate 정의는 변경하지 않는다.
