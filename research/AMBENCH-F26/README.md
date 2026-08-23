---
id: AMBENCH-F26
type: preregistration
state: PREREGISTERED
created: 2026-08-23
source_of_truth: github
inherits:
  - AMBENCH-D25
  - DEC-052
---

# AMBENCH-F26 — Independent-Condition Candidate Qualification Gate
# AMBENCH-F26 — 독립 조건 후보 적격성 게이트

## Purpose / 목적

**KO:** D25에서 `mds2-3761` aggregate representation이 block/build-progression 지배 구조임을 확인했으므로, 동일 representation을 확장하지 않고 다음 mechanistic controlled experiment에 적합한 **독립적으로 변한 공정조건 + 반복 + 해석 가능한 물리 outcome** source를 선별한다. F26은 모델링을 수행하지 않고 source/design qualification만 수행한다.

**EN:** After D25 established block/build-progression dominance in the `mds2-3761` aggregate representation, do not escalate that representation. Qualify a source for the next mechanistic controlled experiment that contains **independently varied process conditions, physical replication, and interpretable physical outcomes**. F26 performs source/design qualification only, not modeling.

## Frozen candidate set / 고정 후보군
No candidate may be added after numerical/source qualification results are inspected.

### A — NIST `mds2-3662`
`Dataset for Model Validation of Transient Melt Pool Dynamics in Laser Powder Bed Fusion of Nickel Super Alloy 625: Top Surface Melt Pool Width and Area Measurements from Beam on Plate Experiments`.

Prospectively known from official NIST publication + associated 2025 paper:
- rapid-turnaround IN625 artifact;
- converging vs diverging scan strategy is an explicit independent scan-condition axis;
- Set 2 contains three repeats of converging and diverging geometries across track-count snapshots;
- ex-situ top-surface melt-pool width/area measurements;
- separate operators provide measurement replication, but operator repeats are not substitutes for physical repeats.

### B — AMB2025-07
- independent turnaround/skywriting conditions `0.75 ms` and `5.0 ms`;
- 3 repeat plates per condition;
- two pad geometries;
- optical PDR `mds2-4103` known;
- thermography modality experimentally documented;
- current public exact thermography PDR/source identity must be rechecked.

### C — A-AMB2022-01 `mds2-2525`
- simultaneous absorptance + high-speed X-ray provenance;
- materially independent material/facility/measurement chain;
- experimental repeats known from publication;
- repeat-resolved public event identity/pairing previously not verified.

### D — BP4 dynamic laser coupling `mds2-3842`
- 7 nominal process conditions × 3 repeats;
- dynamic coupling waveform source available;
- BP1 geometry/thermal outcomes are separate specimens; cross-BP specimen pairing prohibited;
- candidate only if a same-specimen or independently valid physical outcome is newly established without inference.

## Frozen qualification dimensions / 고정 적격성 차원
Each candidate is scored PASS/FAIL/UNKNOWN on six dimensions; no weighted score is used.

1. **Independent condition axis** — condition is deliberately/naturally varied independently of part/block identity.
2. **Physical replication** — at least 3 physical repeats per primary condition or an equivalent repeated-unit design.
3. **Deterministic condition→outcome pairing** — physical outcome belongs to the same specimen/event/qualified unit; no nominal-case cross-specimen inference.
4. **Outcome interpretability** — outcome is a physical geometry/structure/thermal measurand and is not known to be dominated by deterministic build progression under the proposed analysis unit.
5. **Authoritative source integrity path** — official NIST/PDR identity plus checksum/immutable component route can be established at zero incremental cost.
6. **Low-DOF experimentability** — a future experiment can be preregistered at condition/repeat level without high-capacity ML or pseudo-replication.

## Selection rule / 선정 규칙
A candidate may be selected `PRIMARY_F26` only if dimensions 1–6 are all PASS.

If multiple candidates pass, choose in this order:
1. strongest physical repeat independence;
2. strongest deterministic same-unit pairing;
3. simplest low-DOF endpoint;
4. smallest official-source burden.

If no candidate passes all six dimensions, final gate is HOLD/PARTIAL and no experiment is opened.

## Frozen gates / 고정 판정
- `PASS_F26_INDEPENDENT_CONDITION_CANDIDATE_READY`
- `PARTIAL_F26_PROMISING_CANDIDATE_SOURCE_GAP`
- `HOLD_F26_NO_FULLY_QUALIFIED_CANDIDATE`
- `REJECT_F26_CURRENT_CANDIDATES`

## Source-extraction boundary / source 추출 경계
Allowed:
- current official NIST/Data.gov metadata and publications;
- NIST NERDm component names, sizes, download URLs and checksums;
- experimental design, condition count, repeat identity, specimen pairing and measurement semantics;
- small documentation components if needed.

Forbidden in F26:
- candidate outcome numerical values/distributions;
- association tests, ranking, feature selection, model fitting;
- using challenge/result values to choose a candidate;
- raw measurement archive commits/artifacts/cache.

## Existing exposure / 기존 사전노출
The `mds2-3761` branch retains `NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`; it is not reused for F26 candidate selection.
F13's publication-level aggregate pre-exposure remains disclosed for candidate C.

## Cost / 비용
Only zero-incremental-cost official public routes and standard public GitHub-hosted runners are authorized. Any potentially billable route requires explicit prior user approval.
