---
id: SESSION-HANDOFF
type: memory
state: ACTIVE
checkpoint_id: CHK-20260823-F26-PASS-INDEPENDENT-CONDITION-CANDIDATE-READY
active_issue: none
active_research: none
last_completed_issue: 44
last_completed_research: AMBENCH-F26
last_decision: DEC-054
created: 2026-08-22
updated: 2026-08-23
source_of_truth: github
---

# Session Handoff / 세션 인수인계

## Current State / 현재 상태
- Checkpoint: `CHK-20260823-F26-PASS-INDEPENDENT-CONDITION-CANDIDATE-READY`
- Active Issue: none
- Active research: none
- Last completed: #44 `AMBENCH-F26 — PASS_F26_INDEPENDENT_CONDITION_CANDIDATE_READY`
- Last decision: `DEC-054`

## Cost Authority / 비용 권위
`COST-001` + `DEC-028`: any potentially billable action requires explicit user approval before execution. Unknown billing = `HOLD_COST_APPROVAL`.

## Preserved branches / 보존 branch
- E14 remains `HOLD_SOURCE_INTEGRITY`; no redesign.
- X16 F19 segmentation remains frozen.
- F20 X16 workbook immutable identity/schema remains PASS.
- F21 rejects only the X16 histogram-workbook-only structural-quality endpoint route.
- F22 registered-X4 immutable source bytes remain valid.
- F23 registered-X4 headerless positional 40-column parser contract remains PASS.
- E24 remains `NO_MATERIAL_E24_ASSOCIATION`.
- D25 remains `D25_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE`; same-representation escalation on `mds2-3761` remains prohibited by `DEC-052`.

## F26 Result / F26 결과
Frozen final gate: **`PASS_F26_INDEPENDENT_CONDITION_CANDIDATE_READY`**.

### Primary candidate / 1차 후보
**AMB2025-07 optical route — NIST `mds2-4103`.**

Frozen independent physical repeat groups:
- `0.75 ms` turnaround: T72, T82, T92;
- `5.0 ms` turnaround: T102, T112, T122.

Plate identity is the independent replicate. `P1..P3` are sectioned pieces nested within each physical plate and must not be treated as independent repeats.

Current NIST NERDm `mds2-4103`:
- version `1.0.0`;
- 552 components;
- each of the six repeat plates has plate-specific P1/P2/P3 `Cross_Sections/Tracks_Results` CSV identities.

Selected future relation:
`turnaround/skywriting condition → ex-situ optical melt-pool geometry`.

The exact public AMB2025-07 raw/analysis-ready thermography PDR remains `NOT_VERIFIED`. This does not block the selected optical-only route and no thermal↔geometry pairing readiness may be inferred.

### Secondary candidate / 2차 후보
NIST `mds2-3662` rapid-turnaround IN625 passes all six F26 dimensions and remains `SECONDARY_F26`.

Current source facts:
- NERDm version `1.0.1`;
- all five components carry checksum metadata;
- `README.txt`, `Measurements.xlsx`, and `Scan Strategy Data.zip` were transiently downloaded and local SHA-256 exactly matched NIST NERDm;
- large `Image Data.zip` was not downloaded;
- no numerical workbook outcome values were emitted or analyzed.

It remains secondary because its track-count × direction design and source-author repeat outlier/attrition history are less clean than the AMB2025-07 two-condition repeat-plate design under the frozen tie-break rule.

### Not selected / 미선정
- `mds2-2525`: simultaneous absorptance/X-ray source integrity is strong, but repeat-resolved public event identity sufficient for deterministic repeat-level physical pairing remains `NOT_VERIFIED`.
- `mds2-3842`: 7 conditions × 3 repeats and source integrity remain strong, but BP4 coupling specimens are not BP1 geometry/thermal specimens; cross-BP same-track pairing remains prohibited.

### Protocol deviation / 프로토콜 deviation
During F26 review of the current NIST AMB2025-06/07 design PDF, numerical values in a **single-track calibration table** were unintentionally exposed. No AMB2025-07 pad turnaround-condition outcome values from `mds2-4103` were read or compared, and no candidate association/ranking/model was computed.

Descendant disclosure:
**`NEW_F26_B_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED_CALIBRATION_TABLE_PREOBSERVED`**.

Do not claim pristine outcome blindness in E27 or descendants, and do not use the preobserved calibration numbers to choose endpoint, transform, threshold or gate.

Durable artifacts:
- `research/AMBENCH-F26/README.md`
- `research/AMBENCH-F26/AMENDMENT-01.md`
- `research/AMBENCH-F26/NERDM_INVENTORY.md`
- `research/AMBENCH-F26/CANDIDATE_A_SOURCE_QUALIFICATION.md`
- `research/AMBENCH-F26/CANDIDATE_B_METADATA_QUALIFICATION.md`
- `research/AMBENCH-F26/RESULT.md`
- `registry/CLM-089.md`
- `registry/CLM-090.md`
- `registry/CLM-091.md`
- `registry/DEC-053.md`
- `registry/DEC-054.md`
- `context/MEM-048-AMBENCH-F26.md`

## Exact Next Eligible Work / 정확한 다음 eligible 작업
No numerical experiment is active. Do **not** open `mds2-4103` outcome values yet.

Next: separately preregister **AMBENCH-E27 — AMB2025-07 Six-Plate Turnaround-Time → Optical Geometry Controlled Experiment**.
Before any outcome-value access, freeze:
1. one pad geometry;
2. one fixed cross-section position;
3. one primary melt-pool geometry measurand and at most one sensitivity measurand;
4. plate as the independent replicate; P sections nested only;
5. exact six-plate small-sample permutation/randomization statistic and effect-size/materiality gate;
6. missingness and measurement-uncertainty rules;
7. `VIOLATED_LIMITED_CALIBRATION_TABLE_PREOBSERVED` disclosure;
8. no endpoint fishing, post-hoc switching, or high-capacity ML.

Any paid/potentially paid route requires prior explicit user approval.
