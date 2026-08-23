---
id: AMBENCH-F26-AMENDMENT-01
type: preregistration-amendment
state: ACTIVE
created: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F26/README.md
  - Issue #44
---

# AMBENCH-F26 Amendment 01 — Limited calibration-table pre-exposure
# AMBENCH-F26 수정 01 — 제한적 calibration table 사전노출

## Event / 사건

**KO:** F26의 AMB2025-07 design/source qualification 중 현재 NIST `AMB2025-06 and AMB2025-07 Benchmark Measurements and Challenge Problems` PDF를 확인하는 과정에서, PDF의 single-track calibration section에 포함된 Table 5의 numerical melt-pool measurements가 도구 출력 및 render에 노출됐다. 이는 F26 preregistration의 numerical-outcome non-exposure boundary보다 넓은 노출이므로 숨기지 않고 기록한다.

**EN:** During F26 AMB2025-07 design/source qualification, inspection of the current NIST `AMB2025-06 and AMB2025-07 Benchmark Measurements and Challenge Problems` PDF exposed numerical single-track calibration melt-pool measurements in Table 5 through tool output/render. This exceeded F26's intended numerical-outcome non-exposure boundary and is recorded explicitly.

## Scope / 범위
- exposed values were **single-track calibration measurements**, not the AMB2025-07 pad turnaround-condition outcome table intended for a future experiment;
- no AMB2025-07 pad outcome values from `mds2-4103` files were read;
- no candidate outcome association, ranking, condition comparison, effect size, feature selection, or model was computed;
- F26 selection criteria remain design/source-only and do not use the exposed calibration values.

## Consequence / 결과
For candidate B and any descendant numerical experiment:

`NEW_F26_B_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED_CALIBRATION_TABLE_PREOBSERVED`.

Do not claim pristine outcome blindness. Future preregistration must disclose this event and must not use the preobserved calibration table to select the turnaround-condition endpoint, transform, threshold, or gate.

This amendment does not silently relax the F26 six-dimensional qualification rule.
