---
id: MEM-024
type: memory
state: VALIDATED_DIRECTION_GATE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-E09/README.md
  - Issue #24
  - registry/DEC-021.md
---

# MEM-024 — AMBENCH-E09 Preregistered / AMBENCH-E09 사전등록

**KO:** Issue #24 `AMBENCH-E09`가 F08의 `PARTIAL_CASE_LEVEL_READY` 경계를 이어받아 활성화됐다. 실험은 BP1/BP4를 paired track으로 결합하지 않고 **nominal case-family aggregate ordering**만 비교한다. 1차 predictor는 BP4 공식 `VEDσ/VED0`에 case-level coupling ratio를 곱한 `X_coupled`; 1차 BP1 endpoint는 기존 E05의 `hot_pixel_time_integral_1298C_px_s` case median이다. process-only comparator와의 Spearman 차이 `delta_rho_thermal` 및 세 factor-axis sign concordance를 고정 gate로 사용한다. BP4 coupling 값은 사전등록 시점까지 미열람이다. 단 BP1 결과는 과거 E03/E05/D06에서 이미 관측되어 `FULL_OUTCOME_BLIND = NO — BP1_PREOBSERVED`를 명시한다.

**EN:** Issue #24 `AMBENCH-E09` is active under the F08 `PARTIAL_CASE_LEVEL_READY` boundary. The experiment never joins BP1/BP4 as paired tracks; it compares only **nominal case-family aggregate ordering**. The primary predictor is BP4 official `VEDσ/VED0` multiplied by the case-level coupling ratio (`X_coupled`); the primary BP1 endpoint is the case median of the pre-existing E05 `hot_pixel_time_integral_1298C_px_s`. The frozen gate uses the Spearman improvement over the process-only comparator (`delta_rho_thermal`) plus three factor-axis sign-concordance checks. BP4 coupling values were not accessed before preregistration. BP1 outcomes were previously observed in E03/E05/D06, so `FULL_OUTCOME_BLIND = NO — BP1_PREOBSERVED` is explicit.

**State:** `PREREGISTERED / ACTIVE`

**Source:** `research/AMBENCH-E09/README.md`; Issue #24; `registry/DEC-021.md`
