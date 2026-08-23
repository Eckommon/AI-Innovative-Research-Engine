---
id: AMBENCH-F26-RESULT
type: feasibility-result
state: COMPLETED_PASS_INDEPENDENT_CONDITION_CANDIDATE_READY
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F26/README.md
  - research/AMBENCH-F26/AMENDMENT-01.md
  - research/AMBENCH-F26/NERDM_INVENTORY.md
  - research/AMBENCH-F26/CANDIDATE_A_SOURCE_QUALIFICATION.md
  - research/AMBENCH-F26/CANDIDATE_B_METADATA_QUALIFICATION.md
  - Issue #44
---

# AMBENCH-F26 Result — Independent-Condition Candidate Qualification
# AMBENCH-F26 결과 — 독립 조건 후보 적격성

**Frozen final gate / 고정 최종 판정:** **`PASS_F26_INDEPENDENT_CONDITION_CANDIDATE_READY`**

**Primary candidate / 1차 후보:** **B — AMB2025-07 optical condition→geometry route (`mds2-4103`)**.

## 1. Executive result / 핵심 결과

**KO:** D25 이후 동일 `mds2-3761` representation을 확장하지 않고, 사전 고정한 네 후보를 독립 condition, physical repeat, deterministic outcome pairing, outcome interpretability, official source integrity, low-DOF experimentability의 6개 비가중 차원으로 평가했다. AMB2025-07 optical route와 `mds2-3662` rapid-turnaround route가 모두 다음 controlled experiment 후보가 될 수 있는 수준으로 적격하다. Tie-break rule에 따라, 명확한 단일 turnaround-time axis (`0.75 ms` vs `5.0 ms`), 각 조건의 3 physical repeat plates, 그리고 repeat-plate→sectioned optical component mapping이 직접 고정되는 AMB2025-07을 `PRIMARY_F26`로 선택한다. `mds2-3662`는 secondary candidate로 보존한다.

**EN:** After D25, the same `mds2-3761` representation was not expanded. The four prospectively frozen candidates were evaluated on six unweighted dimensions: independent condition, physical replication, deterministic outcome pairing, outcome interpretability, official source integrity, and low-DOF experimentability. Both the AMB2025-07 optical route and the `mds2-3662` rapid-turnaround route qualify as credible next-experiment sources. Under the frozen tie-break rule, AMB2025-07 is selected as `PRIMARY_F26` because it provides a simple explicit turnaround-time axis (`0.75 ms` vs `5.0 ms`), three physical repeat plates per condition, and a directly documented repeat-plate→sectioned-optical-component mapping. `mds2-3662` is retained as the secondary candidate.

## 2. Candidate qualification matrix / 후보 적격성 matrix

| Candidate | Independent condition | >=3 physical repeats | Deterministic condition→outcome pairing | Outcome interpretable | Official source integrity | Low-DOF experimentable | Disposition |
|---|---|---|---|---|---|---|---|
| **B AMB2025-07 / `mds2-4103` optical** | PASS | PASS | PASS | PASS | PASS | PASS | **PRIMARY_F26** |
| **A `mds2-3662` rapid-turnaround IN625** | PASS | PASS | PASS | PASS | PASS | PASS | SECONDARY_F26 |
| C `mds2-2525` A-AMB | PASS | PASS at experiment-design level | **FAIL / repeat-resolved public pairing NOT_VERIFIED** | PASS | PASS | PARTIAL | NOT_SELECTED |
| D `mds2-3842` BP4 coupling | PASS | PASS | **FAIL — same-specimen physical outcome absent; cross-BP pairing prohibited** | PARTIAL | PASS | PARTIAL | NOT_SELECTED |

No weighted score or outcome-value ranking was used.

## 3. Primary candidate B — AMB2025-07 optical route

### 3.1 Independent condition structure / 독립 condition 구조
Current official NIST measurement description establishes:
- AMB2025-07 is bare IN718 with two laser turnaround/skywriting times: `0.75 ms` and `5.0 ms`;
- primary power, speed, spot diameter and hatch spacing are fixed while turnaround time is deliberately varied;
- both `5 mm × 5 mm` and `1 mm × 5 mm` pad geometries are present;
- the same experiment family includes in-situ thermography and ex-situ cross-sectional measurements.

For F26 primary qualification, **thermography is not required**. The selected route is deliberately narrower:
`turnaround condition → ex-situ optical melt-pool geometry`.

### 3.2 Physical repeat identity / physical repeat identity
Official specimen naming states `T#2`, with the variable digit representing 12 plates = 4 conditions × 3 repeats. For the AMB2025-07 bare subset:
- `0.75 ms`: **T72, T82, T92**;
- `5.0 ms`: **T102, T112, T122**.

`P1..P3` are sectioned pieces, **not independent repeat plates**. Future inference must use plate identity as the physical replicate and treat multiple sections within a plate as nested outcomes.

### 3.3 Current PDR source identity / 현재 PDR source identity
Current NIST NERDm:
- `mds2-4103`;
- version `1.0.0`;
- 552 components;
- official component-level metadata/checksum route available.

Metadata-only qualification directly confirmed all six repeat plates are represented. For every T72/T82/T92/T102/T112/T122 plate, NERDm exposes three `Cross_Sections/Tracks_Results/...P1s/P2s/P3s_pixel_points.csv` components. No file content or numerical outcome values were read by this metadata check.

This establishes deterministic plate→section component identity sufficient for a future low-DOF plate-level experiment.

### 3.4 Thermography publication status / thermography publication 상태
Current official AM Bench direct-data guidance still does not identify a separate exact AMB2025-07 raw/analysis-ready thermography PDR publication. Therefore:
`AMB2025_07_THERMOGRAPHY_PDR = NOT_VERIFIED`.

This does **not** block the selected optical-only F26 route. Do not silently claim thermal↔geometry pairing readiness.

## 4. Secondary candidate A — `mds2-3662`

Current NIST NERDm:
- version `1.0.1`;
- five components, all carrying checksum metadata;
- `Measurements.xlsx` SHA-256 `9e21a77f0c526aa0a913a3f14e2bba7b36640b0fd319febcf8ebfdc9dd5d0edf`;
- `README.txt` SHA-256 `e9c33b0b31f7d1548b68041f469e84c6342c974c00e54c387952a24569835918`;
- `Scan Strategy Data.zip` SHA-256 `f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee`.

All three small components were transiently downloaded and local hashes exactly matched NERDm. `Image Data.zip` (~495 MB) was not needed or downloaded.

The associated NIST-authored 2025 paper establishes:
- explicit converging vs diverging rapid-turnaround scan conditions;
- Set 2 used three physical repeats for each converging/diverging geometry over track-count snapshots;
- melt-pool width/area are ex-situ physical outcomes;
- two operators measured outcomes, which is measurement replication rather than physical replication;
- in some cases one of three physical samples was removed by the source authors as an outlier attributed to likely local lens contamination.

Therefore A qualifies, but the repeat-attrition/outlier history and more complex track-count×direction design make it less clean than B under the frozen tie-break rule.

## 5. Candidate C — `mds2-2525`

Current NERDm version is `1.3.2`, with 28/28 components carrying checksum metadata. Same-experiment absorptance and high-speed X-ray provenance remains strong.

However F13's unresolved boundary persists:
- experimental repeats existed;
- repeat-resolved public event identity adequate for deterministic repeat-level absorptance↔physical-outcome pairing remains `NOT_VERIFIED`.

Therefore candidate C cannot satisfy all six F26 dimensions and is not selected.

## 6. Candidate D — `mds2-3842`

Current NERDm version `1.0.3` remains source-ready with authoritative checksum-bearing coupling data. Seven nominal process cases × three repeats provide independent condition/repeat structure.

But the prior F08 boundary remains decisive:
- BP4 coupling specimens and BP1 geometry/thermal specimens are separate;
- cross-BP physical-track pairing is prohibited;
- no same-specimen physical outcome is newly established in F26.

Therefore candidate D fails deterministic condition→outcome pairing for the intended mechanistic experiment.

## 7. Protocol deviation / protocol deviation
See `AMENDMENT-01.md`.

While reviewing the current NIST AMB2025-06/07 design PDF, a single-track **calibration** table containing numerical melt-pool values was unintentionally exposed. No AMB2025-07 pad turnaround-condition outcome values from `mds2-4103` were read and no candidate effect/ranking/model was computed.

Inherited state for candidate B descendants:
**`NEW_F26_B_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED_CALIBRATION_TABLE_PREOBSERVED`**.

F26 candidate selection uses only design/source criteria and does not use the exposed calibration numbers.

## 8. Frozen gate application / 고정 gate 적용

### `PASS_F26_INDEPENDENT_CONDITION_CANDIDATE_READY`
- at least one candidate passes all six qualification dimensions: PASS;
- primary selected using frozen tie-break rule: PASS;
- no candidate added after source/design inspection: PASS;
- no association/model/feature selection performed: PASS;
- protocol deviation explicitly recorded: PASS as disclosure; pristine outcome blindness is not claimed.

**Final:** **PASS**.

## 9. Consequence / 후속
The next numerical work must **not** start until a new preregistration freezes the AMB2025-07 plate-level experiment.

Recommended next experiment design boundary:
1. independent replicate = plate T72/T82/T92 vs T102/T112/T122;
2. choose one pad geometry and one fixed cross-section position **before opening result values**;
3. multiple P sections are nested outcomes, never extra independent repeats;
4. freeze one primary geometry measurand and at most one sensitivity measurand;
5. use an exact small-sample randomization/permutation test at the six-plate level or another preregistered low-DOF statistic;
6. no high-capacity ML;
7. disclose `VIOLATED_LIMITED_CALIBRATION_TABLE_PREOBSERVED`;
8. thermography remains outside the primary experiment unless an exact public PDR is separately qualified later.

## 10. Cost / 비용
Incremental monetary cost: `0 USD`. Official NIST sources and public standard GitHub-hosted runners only; no paid API/source, larger runner, artifact storage or cache.
