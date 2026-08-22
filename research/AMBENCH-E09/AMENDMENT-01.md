---
id: AMBENCH-E09-AMENDMENT-01
type: preregistration-amendment
state: FROZEN_PRE_OUTCOME_ACCESS
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-E09/README.md
  - docs/RAW_DATA_TRANSIENT_POLICY.md
  - registry/DEC-022.md
  - Issue #24
---

# AMBENCH-E09 Amendment 01 — Execution & Gate Operationalization / 실행·판정 세부 사전고정

**Timing / 시점:** This amendment is frozen **before any BP4 coupling ZIP download or numeric coupling access in E09**. / E09의 BP4 coupling ZIP 다운로드·숫자값 열람 전에 고정한다.

It does not change the scientific question, primary endpoint, primary predictor, or full-positive thresholds. It only operationalizes previously named but incompletely numerical rules and applies `RAW-001`. / 과학적 질문·1차 endpoint·predictor·양성 threshold는 변경하지 않는다.

## 1. RAW-001 / raw-data 정책

All NIST raw inputs are `RAW_DATA_TRANSIENT_ONLY`. They may exist only in the execution workspace and are not committed or uploaded as raw-data Actions artifacts. Persist source/version/checksum, filename inventory, code and derived summaries/results only. / raw bytes 영구저장 금지.

## 2. Gate precedence / 판정 우선순위

Apply exactly one final gate in this order:
1. `HOLD_DATA_INTEGRITY` if an integrity condition is met;
2. compute primary thermal gate candidate from the original README thresholds;
3. apply the endpoint-conflict override below only if its exact numerical condition is met;
4. otherwise return the primary thermal gate candidate.

Primary thermal candidate rules remain:
- `CROSS_MODAL_ORDERING_SIGNAL`: original full gate, unchanged;
- `PARTIAL_CROSS_MODAL_SIGNAL`: original partial gate, unchanged;
- `PROCESS_ONLY_OR_REDUNDANT_AT_CASE_LEVEL`: `delta_rho_thermal <= 0` and `rho_process_thermal >= 0.60`;
- `NO_COHERENT_CROSS_MODAL_RELATIONSHIP`: `rho_coupled_thermal < 0.60` and fewer than `2/3` of available axes concordant;
- if none match exactly, classify `INCONCLUSIVE_CASE_LEVEL` rather than inventing a post-hoc threshold. / 어느 조건에도 정확히 안 맞으면 사후 threshold 생성 대신 INCONCLUSIVE.

## 3. MIXED_ENDPOINT_SPECIFIC exact override / endpoint 충돌 수치 정의

Return `MIXED_ENDPOINT_SPECIFIC` only when **both** are true:
- the primary thermal candidate is `CROSS_MODAL_ORDERING_SIGNAL` or `PARTIAL_CROSS_MODAL_SIGNAL`; and
- at least one secondary geometry endpoint has `rho_coupled <= -0.70`, **or** width and depth have opposite signs with `abs(rho_coupled) >= 0.70` for both.

Otherwise geometry is reported descriptively and does not override the primary gate. / 위 강한 충돌조건 외에는 geometry는 보조 보고만 한다.

## 4. Exact permutation reference / exact permutation 기준

For the primary thermal endpoint, permute the case labels of `Y_thermal` across the analyzable cases while holding both predictors fixed. Report the full exact permutation distribution and both:
- one-sided reference fraction: `Pr(delta_rho_perm >= delta_rho_observed)`;
- two-sided absolute reference fraction: `Pr(|delta_rho_perm| >= |delta_rho_observed|)`.

These are descriptive exact case-label-null references, not randomized-trial causal p-values. / 무작위실험 인과 p-value 아님.

## 5. Case 3.2 / 3.2

Filename-only archive inventory remains mandatory before any numeric coupling read. If archive evidence resolves three distinct repeat files, use all three and mark `3.2_ID_RESOLVED_BY_ARCHIVE`. If not, use only verified unique files, mark `3.2_PARTIAL_REPEAT_ID`, make power axis `NOT_TESTABLE`, and run the preregistered sensitivity excluding case `3.2`.

**Outcome access at freeze:** `NONE — BP4 COUPLING UNSEEN`.
