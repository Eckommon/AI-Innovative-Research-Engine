---
id: AMBENCH-F19
type: preregistration
state: PREREGISTERED
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F18/RESULT.md
  - research/AMBENCH-F17/RESULT.md
---

# AMBENCH-F19 — X16 Blocker Resolution: XCT Workbook Qualification + Deterministic Part Segmentation
# AMBENCH-F19 — X16 차단요인 해소: XCT workbook qualification + 결정론적 part segmentation

## 1. Purpose / 목적

**KO:** F18에서 남은 두 blocker만 해결한다. (1) `mds2-2514`의 `OverhangX16_ImageHistograms.xlsx`를 authoritative zero-cost route에서 byte/checksum/schema 수준으로 qualification하고, (2) 이미 고정된 `mds2-2309` DAQ/XYPT `L101-L125` representation에서 16개 part를 outcome-blind하게 결정론적으로 분할하는 규칙을 authoritative source semantics로 고정한다. 이 단계는 수치 process↔XCT association 실험이 아니다.

**EN:** Resolve only the two blockers left by F18: (1) qualify `OverhangX16_ImageHistograms.xlsx` from `mds2-2514` at authoritative byte/checksum/non-numerical-schema level through a zero-cost route, and (2) freeze an outcome-blind deterministic rule for assigning the already-frozen `mds2-2309` DAQ/XYPT `L101-L125` representation to the sixteen parts using authoritative source semantics. This is not a numerical process↔XCT association experiment.

## 2. Pre-registration evidence boundary / 사전등록 전 증거 경계

Before this F19 freeze, the following metadata/structural evidence had already been reviewed:
- current Data.gov metadata for `mds2-2514` and `mds2-2309`;
- NIST X16 User Notes, including Figure 1 part topology/layout and file semantics;
- NIST X4 data-description semantics for XYPT and DAQ;
- repeated zero-cost attempts to fetch the X16 histogram workbook/checksum, all returning no usable bytes.

No `OverhangX16_ImageHistograms.xlsx` numerical cells, no selected DAQ/XYPT numerical values, and no process↔XCT statistic/model had been accessed/computed before this freeze.

`NEW_X16_NUMERICAL_OUTCOME_BLIND = YES`

## 3. Frozen sources / 고정 source

### XCT
- authoritative current dataset identity: `ark:/88434/mds2-2514`;
- `OverhangX16_ImageHistograms.xlsx`;
- `OverhangX16_ImageHistograms.xlsx.sha256`;
- no TIFF/STL numerical processing.

### In-situ
- authoritative dataset identity: `ark:/88434/mds2-2309`;
- only `DAQ_L101-L125.zip` and `XYPT_L101-L125.zip` selected by F18;
- no MPM, layer camera, other layer groups, or full-build expansion.

## 4. Frozen workbook qualification / workbook qualification 고정

Workbook branch passes only if:
1. exact authoritative workbook bytes are retrieved through a verified zero-incremental-cost route;
2. exact authoritative checksum sidecar or equivalent immutable hash is retrieved;
3. local workbook SHA-256 matches the authoritative value;
4. only workbook container/schema metadata are inspected at F19: sheet names, used ranges, header text, formula presence, and explicit part identifiers;
5. numerical cell values used as XCT outcomes remain unread/uncomputed.

If bytes cannot be retrieved, do not substitute mirrors, screenshots, digitized values, or inferred schema.

## 5. Frozen deterministic part-segmentation rule / 결정론적 part segmentation 규칙

F19 does **not** digitize numeric boundaries from Figure 1.

The future DAQ segmentation rule is frozen as follows:

1. Use authoritative XYPT commanded data for layer `125`, the same layer explicitly used by the NIST X16 User Notes Figure 1.
2. Restrict to commanded laser-on scan coordinates according to the authoritative XYPT power/laser-on field semantics inherited from the NIST X4 data description.
3. Derive exactly `16` spatial groups from the commanded laser-on XY coordinate cloud using a deterministic clustering procedure fixed before process/XCT outcome analysis:
   - standardize neither X nor Y;
   - deterministic `k=16` clustering in physical millimeter coordinates;
   - initialize centers from the Cartesian product of four ordered X quantile centers and four ordered Y quantile centers computed from the commanded laser-on point cloud;
   - Lloyd updates to convergence with deterministic tie-breaking by lexicographic center order.
4. Label the final 16 command-space clusters using the authoritative Figure 1 topology:
   - four X columns ordered left→right map to group prefixes `1`, `2`, `3`, `4`;
   - within each column, Y ordered top→bottom maps to suffixes `1`, `2`, `3`, `4`;
   - expected labels are `1-1`…`4-4`.
5. Define the part assignment surface for actual DAQ XY samples as the Voronoi partition of the 16 frozen XYPT cluster centroids in machine-coordinate millimeters.
6. DAQ samples are eligible for future part-level aggregation only when temporally aligned to commanded laser-on intervals in the matching XYPT layer file; laser-off/reposition intervals are excluded.
7. No part boundary, centroid, clustering count, layer, label topology, or assignment rule may be altered after XCT outcomes are viewed.

This is a deterministic rule derived from authoritative command-space data and authoritative label topology. It is **not** a claim that Figure 1 itself supplies exact numeric boundaries.

## 6. Frozen validation checks for segmentation / segmentation 검증조건

The segmentation branch is qualified only if, after authoritative XYPT byte access in a future execution:
- exactly 16 non-empty clusters are produced at layer 125;
- centroid ordering matches the 4×4 topology shown in NIST Figure 1 without label inversion;
- each selected L101–125 layer can assign commanded laser-on coordinates to the same 16 centroid/Voronoi labels with no empty part for more than 20% of selected layers;
- no manual reassignment is permitted.

Failure of these checks = segmentation HOLD.

## 7. Frozen gates / 고정 gate

### `PASS_F19_BOTH_BLOCKERS_RESOLVED`
Requires both:
- workbook byte/checksum/non-numerical schema qualification PASS; and
- deterministic segmentation rule plus authoritative-input feasibility PASS.

### `PARTIAL_F19_SEGMENTATION_RULE_READY`
Use when:
- segmentation semantics/rule can be frozen from authoritative sources;
- workbook authoritative bytes/checksum/schema remain inaccessible;
- no numerical outcomes have been accessed.

### `PARTIAL_F19_WORKBOOK_READY`
Use when:
- workbook byte/checksum/schema qualification passes;
- segmentation semantics remain unresolved.

### `HOLD_F19_XCT_ACCESS`
Use when workbook access/provenance is materially contradicted or source identity is lost.

### `HOLD_F19_SEGMENTATION_SEMANTICS`
Use when deterministic 16-part command-space mapping cannot be justified from authoritative source semantics.

### `REJECT_F19_ROUTE`
Use only if the F18 bounded route is shown to be semantically invalid for part-level process↔XCT linkage.

## 8. Anti-tuning / 사후튜닝 금지

- no alternative layer group;
- no MPM rescue;
- no TIFF/STL rescue;
- no figure digitization for numeric boundaries;
- no k other than 16;
- no manual cluster relabeling;
- no outcome-aware feature/segmentation changes;
- no high-capacity model.

## 9. Cost / 비용

`COST-001` + `DEC-028` remain mandatory. Only verified zero-incremental-cost public/source-inspection routes are authorized. Any potentially billable action requires explicit user approval **before execution**; uncertain billing = `HOLD_COST_APPROVAL`.
