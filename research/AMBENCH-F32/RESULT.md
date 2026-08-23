---
id: AMBENCH-F32-RESULT
type: feasibility-result
state: COMPLETED_PASS_OUTCOME_UNSEEN_INDEPENDENT_FALSIFICATION_CANDIDATE
created: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F32/README.md
  - registry/DEC-066.md
  - research/AMBENCH-F26/RESULT.md
  - research/AMBENCH-F26/CANDIDATE_A_SOURCE_QUALIFICATION.md
  - research/AMBENCH-F13/RESULT.md
  - research/AMBENCH-F08/RESULT.md
  - research/AMBENCH-E30/SEMANTIC_CORRECTION.md
  - Issue #50
---

# AMBENCH-F32 Result — Independent Outcome-Unseen Candidate Qualification
# AMBENCH-F32 결과 — 독립 Outcome-Unseen 후보 적격성

**Frozen final gate / 고정 최종 판정:** **`PASS_F32_OUTCOME_UNSEEN_INDEPENDENT_FALSIFICATION_CANDIDATE`**

**Primary candidate / 1차 후보:** **A — NIST `mds2-3662` rapid-turnaround converging/diverging IN625 experiment**.

## 1. Executive result / 핵심 결과

**KO:** F32는 새 후보를 추가하지 않고 사전고정된 A–D 네 source만 기존 canonical evidence와 current NIST metadata로 재평가했다. A=`mds2-3662`만 독립 physical units, project-history numerical-outcome non-exposure, deterministic condition→physical-outcome route, immutable source identity, low-DOF experimentability, claim-transfer integrity의 6개 차원을 모두 충족한다. 다만 A의 조건축은 AMB2025-07의 `0.75 ms vs 5.0 ms` turnaround-time 축과 동일하지 않다. 따라서 A는 **same-construct replication이 아니라 independent rapid-turnaround scan-strategy falsification axis**로만 승격된다.

**EN:** Without adding any candidate, F32 re-evaluated only the four prospectively frozen A–D sources using canonical project evidence and current NIST metadata. Only A=`mds2-3662` satisfies all six dimensions: independent physical units, project-history numerical-outcome non-exposure, deterministic condition→physical-outcome route, immutable source identity, low-DOF experimentability, and claim-transfer integrity. However, A's condition axis is not the same construct as the AMB2025-07 `0.75 ms vs 5.0 ms` turnaround-time contrast. A is therefore promoted only as an **independent rapid-turnaround scan-strategy falsification axis**, not as a same-construct replication.

## 2. Frozen qualification matrix / 고정 적격성 matrix

| Candidate | Independent physical units | Outcome-unseen status | Deterministic condition→outcome | Immutable source | Low-DOF experimentability | Claim-transfer integrity | Disposition |
|---|---|---|---|---|---|---|---|
| **A `mds2-3662`** | **PASS** | **PASS_WITH_DISCLOSED_DESIGN/PUBLICATION_CONTEXT** | **PASS** | **PASS** | **PASS** | **PASS — falsification only, not same-construct replication** | **PRIMARY_F32** |
| B `mds2-2525` | PASS | **FAIL — publication-level aggregates preobserved** | PARTIAL / repeat-resolved identity NOT_VERIFIED | PASS | PARTIAL | PARTIAL | NOT_SELECTED |
| C `mds2-3842` | PASS as distinct BP4 source | PASS for coupling waveform values | **FAIL for same-specimen physical-outcome route** | PASS | PARTIAL | PARTIAL — only unpaired nominal case-family relation | NOT_SELECTED |
| D `mds2-4103` P3 | **FAIL as new independent source — same six E29/E30 plates** | **FAIL — P3 numerical outcomes already observed in E30** | PASS | PASS | technically possible but not new | PASS only as already-exposed same-family geometry route | NEGATIVE_CONTROL / INELIGIBLE |

No weighted score or outcome-value ranking was used.

## 3. Candidate A — `mds2-3662` / selected

### 3.1 Independent experiment structure / 독립 실험 구조
Existing F26 source/design evidence establishes:
- IN625 beam-on-plate rapid-turnaround experiment;
- explicit **converging vs diverging scan strategy** condition axis;
- Set 2 includes **three physical samples per converging/diverging condition** across track-count snapshots;
- ex-situ top-surface melt-pool width and area physical outcomes;
- multiple operators are measurement replication and are not substitutes for physical replication.

These physical samples are independent of the AMB2025-07 IN718 six-plate chain used in E29/E30.

### 3.2 Outcome-exposure boundary / outcome 노출 경계
F26's candidate-A qualification:
- emitted no numerical outcome values;
- inspected the workbook only at schema level;
- verified README and archive semantics;
- did not download the ~495 MB image archive;
- did not compute an effect, ranking, test, or model.

The associated publication/design context was used earlier to establish condition/repeat/outlier provenance. F32 therefore does **not** claim pristine literature-level hypothesis blindness. The narrower verified boundary is:

`NEW_A_NUMERICAL_OUTCOME_VALUES_OR_PROJECT_EFFECTS_PREOBSERVED = NO`

under the durable project record reviewed by F32.

To reduce sensitivity to qualitative publication context, any descendant numerical experiment must use a preregistered **two-sided / nondirectional primary falsification test** unless an independent pre-outcome physical theory justifies direction and is frozen separately.

### 3.3 Current source identity / 현재 source identity
Current same-day official NIST NERDm inventory:
- dataset: `mds2-3662`;
- version: `1.0.1`;
- component count: `5`;
- components with checksum: `5/5`.

F26 transient local byte verification matched current NERDm for all small required components:
- `README.txt`: SHA-256 `e9c33b0b31f7d1548b68041f469e84c6342c974c00e54c387952a24569835918`;
- `Measurements.xlsx`: SHA-256 `9e21a77f0c526aa0a913a3f14e2bba7b36640b0fd319febcf8ebfdc9dd5d0edf`;
- `Scan Strategy Data.zip`: SHA-256 `f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee`.

`Image Data.zip` is not required for the next low-DOF experiment and remains excluded unless separately justified.

### 3.4 Claim-transfer boundary / claim 이전 경계
The future A experiment may test:

> Whether changing rapid-turnaround **scan-path geometry** (converging vs diverging) changes physical melt-pool geometry under a preregistered low-DOF physical-sample analysis.

It must **not** claim:
- replication of the AMB2025-07 `0.75 ms vs 5.0 ms` turnaround-time contrast;
- independent replication of E29/E30's exact physical mechanism;
- broad LPBF causal generalization across materials or machines.

A future result may instead be interpreted as **cross-experiment mechanistic consistency, inconsistency, or falsification of a broader residual-heat/rapid-turnaround hypothesis**, subject to the frozen endpoint and analysis contract.

## 4. Candidate B — `mds2-2525` / not selected
F13 establishes strong external independence and same-experiment absorptance+X-ray provenance, but:
- publication-level aggregate outcome values were already exposed;
- repeat-resolved public event identity sufficient for direct repeated-unit pairing remains `NOT_VERIFIED`.

Therefore B fails F32's outcome-unseen requirement and does not pass deterministic repeat-resolved pairing.

## 5. Candidate C — `mds2-3842` / not selected
F08 establishes a reproducible distinct dynamic-coupling modality and no coupling time-series numerical exposure in that gate. However:
- BP4 coupling specimens and BP1 thermography/optical specimens are different physical plates;
- repeat-to-repeat cross-BP pairing is prohibited;
- actual process parameter vectors differ, especially beam diameter;
- supported relation is only `UNPAIRED_NOMINAL_CASE_FAMILY / AGGREGATE_ONLY`;
- a case 3.2 repeat filename inconsistency remains.

Thus C does not provide the deterministic same-unit physical-outcome route required by F32.

## 6. Candidate D — `mds2-4103` P3 / negative control
F31 proves that P3 is the deterministic `1 mm` alternate pad geometry on the same six AMB2025-07 plates. E30 already numerically observed and reported P3. Therefore D fails both independence-as-new-source and outcome-unseen status.

## 7. Frozen gate application / 고정 gate 적용

`PASS_F32_OUTCOME_UNSEEN_INDEPENDENT_FALSIFICATION_CANDIDATE` requires at least one candidate to pass all six dimensions. Candidate A satisfies the gate under the explicitly bounded exposure and claim-transfer rules.

**Final: PASS — select A `mds2-3662`.**

## 8. Exact next mission action / 정확한 다음 mission action

Open a separately preregistered low-DOF numerical experiment:

**`AMBENCH-E33 — IN625 converging-vs-diverging rapid-turnaround melt-pool geometry falsification`**.

Before opening any `Measurements.xlsx` numerical outcome cell, E33 must freeze from documentation/schema only:
1. exact Set-2 physical-sample identities and condition labels;
2. all available track-count snapshot identities;
3. operator nesting/aggregation rule;
4. one primary geometry endpoint and at most one sensitivity endpoint;
5. whether the primary statistic uses a terminal snapshot or a simple across-track-count sample-level descriptor;
6. a two-sided exact six-sample permutation test or another equally low-DOF preregistered test;
7. missing/outlier handling that preserves source-authored exclusions without inventing replacements;
8. current immutable source hashes;
9. no high-capacity ML and no image archive unless separately justified.

E33 must describe itself as independent falsification/mechanistic transfer, **not** same-construct replication of AMB2025-07 turnaround time.

## 9. Capability / Portfolio / 비용
Existing source-integrity/preregistration/exact-small-n pattern remains `SHARED-INTERNAL-CANDIDATE`. No new Skill/MCP/Plugin is justified. No shared paid resource is assumed.

Incremental monetary cost: `0 USD`.
