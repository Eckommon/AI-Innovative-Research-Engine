---
id: AMBENCH-F19-RESULT
type: blocker-resolution-feasibility-result
state: COMPLETED_PARTIAL_F19_SEGMENTATION_RULE_READY
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F19/README.md
  - Issue #37
---

# AMBENCH-F19 Result — X16 Workbook/Segmentation Blocker Resolution
# AMBENCH-F19 결과 — X16 workbook/segmentation 차단요인 해소

**Frozen final gate / 고정 최종 판정:** **`PARTIAL_F19_SEGMENTATION_RULE_READY`**

## 1. Executive result / 핵심 결과

**KO:** F19는 F18에서 남은 두 blocker 중 **결정론적 16-part segmentation 규칙**을 outcome-blind 상태에서 고정하는 데 성공했다. NIST X16 User Notes의 layer-125 Figure 1은 authoritative 4×4 part-label topology를 제공하며, NIST XYPT/DAQ semantics는 commanded XY/power와 actual Galvo XY/power-reference의 10 µs 정렬 가능성을 제공한다. 따라서 Figure 1에서 숫자 경계를 digitize하지 않고도 layer-125 XYPT laser-on command-space를 deterministic `k=16`으로 분할하고 공식 topology로 `1-1`…`4-4` label을 매핑한 뒤, frozen centroid Voronoi를 DAQ actual XY에 적용하는 규칙을 사전에 고정할 수 있다.

반면 `mds2-2514`의 `OverhangX16_ImageHistograms.xlsx`와 `.sha256`는 current authoritative metadata에서 계속 확인되지만, 현재 이용 가능한 검증된 zero-cost 실행경로에서는 실제 bytes를 회수하지 못했다. 따라서 local checksum, workbook sheet/header/part schema qualification은 수행되지 않았다. Full `PASS_F19_BOTH_BLOCKERS_RESOLVED`는 실패하며, **`PARTIAL_F19_SEGMENTATION_RULE_READY`**가 frozen gate와 일치한다.

**EN:** F19 successfully freezes the deterministic sixteen-part segmentation rule while preserving outcome blindness. NIST X16 User Notes provide the authoritative layer-125 4×4 part-label topology, while NIST XYPT/DAQ semantics support commanded XY/power and actual Galvo XY/power-reference alignment at 10 µs sampling intervals. Thus F19 can pre-freeze a deterministic `k=16` partition of layer-125 laser-on XYPT command space, label the clusters `1-1`…`4-4` using the official topology, and use the frozen centroid Voronoi partition for later DAQ actual-XY assignment, without digitizing numeric boundaries from Figure 1.

However, although current authoritative metadata continues to expose `OverhangX16_ImageHistograms.xlsx` and its `.sha256` sidecar from `mds2-2514`, the actual bytes remained inaccessible through the currently verified zero-cost execution routes. Local checksum and workbook sheet/header/part-schema qualification therefore remain unperformed. The full `PASS_F19_BOTH_BLOCKERS_RESOLVED` gate fails, and the frozen result is **`PARTIAL_F19_SEGMENTATION_RULE_READY`**.

## 2. Source state / source 상태

### XCT workbook / XCT workbook
Current authoritative metadata continues to identify:
- dataset `ark:/88434/mds2-2514`;
- `OverhangX16_ImageHistograms.xlsx`;
- `OverhangX16_ImageHistograms.xlsx.sha256`.

Post-preregistration zero-cost retrieval attempts returned no usable authoritative workbook or checksum bytes in the current execution context.

Therefore:
- source identity: `VERIFIED`;
- resource/sidecar existence: `VERIFIED_METADATA`;
- workbook bytes: `NOT_RETRIEVED`;
- checksum sidecar bytes: `NOT_RETRIEVED`;
- local SHA-256: `NOT_COMPUTED`;
- workbook sheet/header/part schema: `NOT_INSPECTED`;
- numerical XCT cells: `NOT_ACCESSED`.

No mirror, screenshot-derived values, or inferred workbook schema was substituted.

### In-situ selected route / 선택 in-situ 경로
F18's selection remains unchanged:
- `mds2-2309` `DAQ_L101-L125.zip` + `.sha256`;
- `mds2-2309` `XYPT_L101-L125.zip` + `.sha256`.

Current authoritative metadata continues to expose these exact resources and sidecars. Actual selected archive/sidecar bytes were not numerically inspected in F19.

## 3. Authoritative segmentation semantics / authoritative segmentation 의미론

The authoritative X16 User Notes establish:
- sixteen nominally identical parts in one build;
- labels arranged as `1-1` through `4-4`;
- Figure 1 depicts the build layout at layer 125;
- XYPT, DAQ, and MPM sources are organized in 25-layer groups;
- XYPT/DAQ records use 10 µs row intervals.

The authoritative XYPT/DAQ data-description semantics inherited from NIST AMMT documentation establish:
- XYPT = commanded scan path / commanded power semantics;
- DAQ = actual Galvo X/Y and laser-power-reference semantics;
- both permit deterministic time-aligned command/actual path handling at the native 100 kHz/10 µs scale.

These structural facts are sufficient to define a pre-outcome part-assignment rule without using XCT outcomes.

## 4. Frozen segmentation algorithm / 고정 segmentation 알고리즘

The exact rule frozen in the F19 preregistration is retained unchanged:

1. use XYPT commanded data for **layer 125**;
2. restrict to commanded laser-on coordinates using authoritative XYPT power/laser-on semantics;
3. cluster commanded XY in physical millimeter coordinates into exactly `k=16` groups;
4. no X/Y standardization;
5. deterministic initialization from Cartesian product of four ordered X-quantile centers × four ordered Y-quantile centers;
6. Lloyd updates to convergence, deterministic lexicographic tie-breaking;
7. map X columns left→right to prefixes `1..4` and Y positions top→bottom within each column to suffixes `1..4` using the official Figure-1 topology;
8. resulting canonical labels: `1-1`…`4-4`;
9. freeze centroid Voronoi partition as the later DAQ actual-XY assignment surface;
10. DAQ samples are eligible only when aligned to matching commanded laser-on intervals; laser-off/reposition intervals are excluded.

No numeric boundary was digitized from Figure 1. No manual relabeling is allowed.

## 5. Future validation conditions for the frozen rule / 향후 고정규칙 검증조건

The rule is methodologically frozen but not yet numerically executed because authoritative selected XYPT bytes were not qualified in F19.

Future source execution must satisfy:
- exactly 16 non-empty layer-125 clusters;
- centroid ordering consistent with the official 4×4 topology;
- across L101–125, no part is empty in more than 20% of selected layers;
- no manual reassignment;
- any failure => segmentation HOLD, not retuning.

Therefore `SEGMENTATION_RULE_FROZEN = YES`, while `SEGMENTATION_NUMERIC_VALIDATION = NOT_COMPUTED`.

## 6. Outcome-blindness / outcome-blindness

`NEW_X16_NUMERICAL_OUTCOME_BLIND = YES` remains intact.

F19 did not access or compute:
- XCT workbook numerical cells;
- XCT histogram outcome values;
- DAQ numerical process values;
- XYPT numerical process summaries;
- part-level process signatures;
- process↔XCT association statistics;
- prediction or machine-learning models.

The segmentation method was frozen entirely from source structure, command/actual-path semantics, and authoritative part topology.

## 7. Frozen gate application / 고정 gate 적용

### `PASS_F19_BOTH_BLOCKERS_RESOLVED`
- workbook byte/checksum/schema qualification: **FAIL / NOT COMPLETED**;
- deterministic segmentation rule: PASS at frozen-method level.

Result: **FAIL**.

### `PARTIAL_F19_SEGMENTATION_RULE_READY`
- authoritative source semantics sufficient to freeze deterministic 16-part segmentation: PASS;
- workbook authoritative bytes/checksum/schema remain inaccessible: PASS condition;
- numerical outcomes remain unaccessed: PASS.

Result: **PASS**.

### `PARTIAL_F19_WORKBOOK_READY`
Workbook qualification did not pass. **FAIL**.

### `HOLD_F19_XCT_ACCESS`
Not selected as final gate. The workbook source identity and current authoritative resource metadata remain intact; the problem is execution-path byte retrieval rather than a source contradiction or lost identity.

### `HOLD_F19_SEGMENTATION_SEMANTICS`
Not selected. Authoritative topology and XYPT/DAQ semantics are sufficient to freeze the deterministic rule.

### `REJECT_F19_ROUTE`
Not applicable. No evidence shows the bounded route is semantically invalid.

## 8. Final / 최종

**`PARTIAL_F19_SEGMENTATION_RULE_READY`**

## 9. Consequence / 후속

Do **not** start E19 yet.

F19 removes the conceptual segmentation blocker but leaves one dominant execution blocker:

> authoritative zero-cost retrieval + checksum + non-numerical schema qualification of `OverhangX16_ImageHistograms.xlsx`.

A future step should target only that remaining small-source retrieval problem and, once authoritative XYPT bytes become available, execute the already-frozen segmentation validation without changing its rule. Do not reopen MPM, change layer groups, digitize Figure 1 boundaries, or tune segmentation based on XCT outcomes.

If workbook qualification and actual frozen segmentation validation both pass, then a separate low-degree-of-freedom 16-part technical-replicate process-signature ↔ XCT-summary experiment may be preregistered.

## 10. Cost / 비용

No paid or potentially billable route was used. `COST-001` + `DEC-028` remain mandatory.
