---
id: AMBENCH-D06
type: diagnostic
state: COMPLETED
evidence_class: OBSERVED_DERIVED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-E05/RESULT.md
  - research/AMBENCH-F04/RESULT.md
  - research/AMBENCH-D06/RESULT.md
---

# AMBENCH-D06 — Outcome-Blind Thermal Representation Geometry Diagnostic / outcome 비사용 열표현 구조 진단

**State / 상태:** `COMPLETED — PROCESS_CASE_PROXY_DOMINANT`  
**Evidence Run / 증거 Run:** `32541722347`  
**Parent / 상위 결과:** `AMBENCH-E05 — MIXED`

## 1. Research Question / 연구 질문

**KO:** E05의 8개 calibrated thermal occupancy feature는 21개 physical repeat 수준에서 독립적인 열변동을 충분히 보존하는가, 아니면 대부분 7개 process-case 차이를 저차원으로 재표현하는가?  
**EN:** Do the eight E05 calibrated thermal occupancy features preserve substantial independent repeat-level thermal variation across 21 physical tracks, or do they mostly re-express the seven process-case differences in a low-dimensional form?

This diagnostic uses **no optical depth/width outcomes**. / optical depth·width outcome 완전 미사용.

## 2. Frozen Source & Representation / 고정 source·표현

- NIST thermography `mds2-2716` v1.3.1
- frozen HDF5 SHA-256 `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`
- exact calibration `A=0.9655`, `B=197.2`, `C=43,920,000`, `ε=0.5`, `30,000 fps`
- exact integer thresholds `366 / 836 / 1081 / 1380 DL`
- exactly the same eight E05 thermal occupancy features; no new feature is introduced.

Process descriptors retained only as explanatory covariates: / 공정 설명변수
- laser power
- scan speed
- spot size

## 3. Frozen Diagnostics / 고정 진단

### A. Repeat-vs-case variance decomposition / 반복·case 분산분해
For each thermal feature `j`: / feature별

`within_fraction_j = SS_within_process_case / SS_total`

where `SS_within` sums squared deviations of the three repeats from their process-case mean. / 각 case 내부 반복편차 제곱합.

Primary case-dominance rule: / case 지배 규칙
- feature is `CASE_DOMINATED` if `within_fraction <= 0.10`.

### B. Thermal effective dimension / thermal 유효차원
Standardize the 8 thermal columns over all 21 tracks and perform deterministic PCA/SVD. / 8개 열 feature 표준화 후 PCA/SVD.

Record:
- singular values / 특이값
- cumulative explained variance
- `PCA95_DIM` = minimum components explaining ≥95% variance.

Low-dimensional rule: / 저차원 규칙
- `LOW_DIMENSIONAL` if `PCA95_DIM <= 3`.

### C. Process association / process 연관성
For each thermal feature, compute the maximum absolute Pearson correlation with the three process descriptors. / feature별 process 변수와 최대 절대 Pearson 상관.

Strong-association rule: / 강연관 규칙
- feature = `STRONG_PROCESS_ASSOCIATION` if `max_abs_r >= 0.90`.

This is descriptive association, not causation. / 인과 주장 금지.

### D. LOCO feature-space extrapolation / LOCO feature-space 외삽
For each held-out process case, fit standardization on the other 18 tracks only and compute: / holdout별 train-only scaling
- mean nearest-neighbor Euclidean distance from each held-out track to any training track in process-only 3D standardized space;
- same distance in 8D thermal space;
- same distance in 11D combined space.

No universal pass/fail threshold is imposed on distance; rank the seven held-out cases and retain it as diagnostic evidence. / 임의 거리 threshold 없이 순위·수치만 기록.

### E. Fold design conditioning / fold 설계 conditioning
For each LOCO training set, standardized design matrices are evaluated by SVD. / training fold별 SVD.

Record condition numbers for:
- process-only 3D
- thermal-only 8D
- combined 11D

If numerical rank is deficient, record `INF / RANK_DEFICIENT` rather than silently regularizing the diagnostic. / rank deficiency를 숨기지 않는다.

## 4. Frozen Diagnostic Gate / 고정 진단 게이트

Define:
- `case_dominated_count` = number of 8 thermal features with `within_fraction <= 0.10`
- `strong_process_count` = number of 8 features with `max_abs_r >= 0.90`
- `low_dimensional = PCA95_DIM <= 3`

Classification: / 분류

1. **`PROCESS_CASE_PROXY_DOMINANT`** if `case_dominated_count >= 6` **and** `low_dimensional`.
2. **`PARTIAL_REPEAT_INFORMATION`** if only one of those two primary conditions holds.
3. **`REPEAT_INFORMATION_PRESENT`** if neither primary condition holds.

`strong_process_count`, LOCO distances, and condition numbers are secondary diagnostics and **do not alter the primary gate after inspection**. / process 상관·거리·condition number는 보조이며 사후 gate 변경 금지.

## 5. Decision Consequence / 후속 의사결정

If `PROCESS_CASE_PROXY_DOMINANT`: / case proxy 지배
- do **not** increase model capacity on the same 21 tracks;
- prioritize independent process-condition/sample expansion or a genuinely different sensing relationship.

If `PARTIAL_REPEAT_INFORMATION`: / 일부 반복정보
- same-data follow-up requires a new physically justified representation hypothesis and must explicitly address low sample/effective-case count.

If `REPEAT_INFORMATION_PRESENT`: / 반복정보 존재
- repeat-level physical diagnostics may remain eligible, but predictive follow-up still requires separate preregistration.

No classification validates the E05 width effect as causal or generalizable by itself. / 어떤 판정도 E05 width 효과의 인과·일반화를 자동 승인하지 않는다.

## 6. COST-001 / 비용 규약

Use only a public repository standard GitHub-hosted runner and public/free NIST/PyPI inputs. / public standard runner·무료입력만 사용.

- no larger/GPU runner;
- no optical data download required;
- no artifact upload;
- raw HDF5 remains ephemeral;
- any billing uncertainty => `HOLD_COST_APPROVAL` before execution.

## 7. Frozen Execution Order / 고정 실행순서

1. checksum-verify exact thermography HDF5;
2. reproduce exact E05 eight features only;
3. verify 21 tracks / 7×3 identity;
4. compute A–E diagnostics without optical outcomes;
5. apply frozen diagnostic gate;
6. persist result and next-direction decision;
7. do not tune E05 or open a predictive experiment automatically.

## 8. Final Result / 최종 결과

Run `32541722347` completed successfully under the frozen design. / 고정 설계로 실행 성공.

- `case_dominated_count = 8/8`
- `PCA95_DIM = 2`
- first two PCs explain `98.2647%` of standardized thermal variance
- `strong_process_count = 4/8`; all four `any_hot_duration_*` features have `|r|≈0.981–0.985` with scan speed
- frozen gate = **`PROCESS_CASE_PROXY_DOMINANT`**

**KO:** 현재 8개 E05 feature는 repeat-level 독립정보보다 process-case 구조를 주로 표현하므로, 동일 21 tracks에서 단순 모델 고용량화는 후속 방향으로 허용하지 않는다. 다음 후보는 독립 process-condition 확장 또는 실제로 다른 sensing/data 관계를 우선한다.  
**EN:** The current eight E05 features primarily encode process-case structure rather than substantial independent repeat-level information. Model-capacity escalation on the same 21 tracks is therefore not an eligible next direction; priority moves to independent process-condition expansion or a genuinely different sensing/data relationship.

Detailed result / 상세 결과: [`RESULT.md`](RESULT.md).

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `FACT-001`, and `UNKNOWN-001`. / 관련 규약 준수.
