---
id: AMBENCH-F18-RESULT
type: feasibility-result
state: COMPLETED_PARTIAL_MANAGEABLE_X16_ROUTE_READY
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F18/README.md
  - Issue #36
---

# AMBENCH-F18 Result — X16 Manageable Representation Feasibility
# AMBENCH-F18 결과 — X16 관리가능 표현 feasibility

**Frozen final gate / 고정 최종 판정:** **`PARTIAL_MANAGEABLE_X16_ROUTE_READY`**

## 1. Executive result / 핵심 결과

**KO:** F18은 Overhang X16의 향후 process↔XCT 검증을 위해 raw MPM 전체 대신 작은 XCT histogram workbook과 중앙 25-layer DAQ+XYPT만 사용하는 bounded representation을 사전고정했다. 공식 NIST/Data.gov 자료는 이 선택이 규모와 의미 면에서 합리적임을 지지한다. XCT workbook은 약 193.26 KB이고, 선택된 DAQ `L101-125`는 약 482.12 MB, XYPT `L101-125`는 약 157.62 MB로 각각 공개되어 선택된 compressed in-situ source는 합쳐서 1 GiB 미만이다. Authoritative User Notes와 X4 data-description semantics에 따르면 DAQ는 100 kHz에서 actual Galvo X/Y, LTZ, laser-power reference를 기록하고 XYPT는 10 us 간격 command path/power를 제공한다.

그러나 현재 zero-cost execution context에서는 XCT workbook 및 its checksum sidecar, 그리고 선택된 DAQ/XYPT checksum sidecar의 실제 bytes를 회수하지 못했다. 따라서 local checksum verification, workbook sheet/header schema, selected archive inventory를 재현하지 못했다. 또한 X16의 16-part layout은 authoritative 문서에서 식별되지만, future part-level DAQ segmentation을 위한 exact numeric spatial-boundary rule은 아직 frozen/verified되지 않았다. 따라서 full representation-ready PASS가 아니라 **PARTIAL**이다.

**EN:** F18 preregistered a bounded representation for future Overhang X16 process↔XCT validation: one small XCT histogram workbook plus only the central 25-layer DAQ and XYPT groups, explicitly excluding full-build MPM and other high-volume sources. Official NIST/Data.gov evidence supports the practical scale and semantics of this route. The XCT workbook is about 193.26 KB; the selected DAQ `L101-125` archive is about 482.12 MB and the selected XYPT `L101-125` archive about 157.62 MB, keeping the selected compressed in-situ source below 1 GiB. Authoritative User Notes and the inherited X4 data-description semantics establish DAQ as actual Galvo X/Y, LTZ, and laser-power-reference sampling at 100 kHz and XYPT as commanded path/power at 10 us resolution.

However, the current zero-cost execution context could not retrieve actual bytes for the XCT workbook or its checksum sidecar, nor for the selected DAQ/XYPT checksum sidecars. Therefore local checksum reproduction, workbook sheet/header semantics, and selected archive inventory could not be completed. In addition, although the authoritative documentation identifies the 16-part layout, an exact numeric spatial-boundary rule for future part-level DAQ segmentation remains unfrozen/unverified. Therefore the full PASS gate does not qualify; the result is **`PARTIAL_MANAGEABLE_X16_ROUTE_READY`**.

No X16 numerical outcome was analyzed in F18.

## 2. Frozen representation / 고정 표현

### XCT
Only:
- NIST `mds2-2514`;
- `OverhangX16_ImageHistograms.xlsx`;
- its `.sha256` sidecar.

Current NIST metrics report workbook size about `193.26 KB`. Raw TIFF and STL outcomes remain excluded.

### In-situ
Only NIST `mds2-2309` central layer group:
- `DAQ_L101-L125.zip` + `.sha256`;
- `XYPT_L101-L125.zip` + `.sha256`.

Current NIST metrics report:
- `DAQ_L101-L125.zip`: about `482.12 MB`;
- `XYPT_L101-L125.zip`: about `157.62 MB`.

This is materially smaller than MPM layer-group sources, which are multi-GB per 25 layers.

## 3. Authoritative semantic qualification / 권위 semantics

The X16 User Notes were available through the authoritative NIST route and establish:
- the July 3, 2019 X16 build;
- 16 nominally identical parts in one build;
- part labels/layout `1-1` through `4-4`;
- 250 layers;
- XYPT source archives grouped into 25-layer blocks;
- XYPT rows represent 10 us command intervals;
- DAQ source archives grouped into layer blocks;
- DAQ text rows represent 10 us time steps;
- X16 file formats otherwise inherit the technical structure documented for the prior X4 dataset.

The NIST X4 data-description article defines the DAQ channels inherited by X16 as:
1. Galvo X-mirror encoder;
2. Galvo Y-mirror encoder;
3. LTZ lens encoder;
4. laser power reference signal;
with 100 kHz sampling and per-file calibration polynomials. It explicitly distinguishes XYPT commanded path/power from DAQ actual path/power.

Therefore DAQ+XYPT is a physically meaningful, lower-volume in-situ representation candidate rather than a metadata-only command proxy.

## 4. Retrieval tests / retrieval 시험

### XCT workbook
Authoritative current Data.gov metadata explicitly exposes:
- `OverhangX16_ImageHistograms.xlsx`;
- `OverhangX16_ImageHistograms.xlsx.sha256`.

Observed size from NIST metrics: about 193.26 KB.

Actual workbook and sidecar byte retrieval through available zero-cost NIST/cache and provided transient-download routes failed in F18. Therefore:
- workbook numerical cells inspected: **NO**;
- sheet names inspected: **NO**;
- header/column semantics inspected: **NO**;
- local workbook checksum: **NOT_COMPUTED**.

### Selected in-situ sidecars
Current Data.gov metadata explicitly exposes:
- `DAQ_L101-L125.zip.sha256`;
- `XYPT_L101-L125.zip.sha256`.

Both sidecar byte fetches returned cache/access failure in the current zero-cost context. Under the frozen sidecar-first rule, F18 did not initiate the larger selected archive downloads after sidecar failure.

Therefore:
- selected DAQ local checksum: **NOT_COMPUTED**;
- selected XYPT local checksum: **NOT_COMPUTED**;
- selected archive inventory: **NOT_VERIFIED**.

No paid or unverified mirror route was substituted.

## 5. Part-level segmentation feasibility / part-level segmentation 가능성

Supported:
- the build contains a deterministic 16-part label family `1-1`…`4-4`;
- XCT resource naming preserves `Part1_1`…`Part4_4`;
- DAQ provides actual X/Y coordinates plus laser power;
- XYPT provides commanded path/power.

Not yet qualified:
- exact numeric X/Y spatial boundaries for assigning each DAQ sample to a specific part;
- a frozen deterministic segmentation algorithm validated against authoritative build coordinates.

Therefore F18 does **not** authorize part-level process-summary calculation yet.

## 6. Frozen gate application / 고정 gate 적용

### `PASS_MANAGEABLE_X16_REPRESENTATION_READY`
- XCT workbook + checksum locally verified: **FAIL**;
- workbook 16-part schema qualified: **FAIL / NOT VERIFIED**;
- selected DAQ+XYPT checksums and bytes verified: **FAIL**;
- archive inventory 101–125 verified: **FAIL**;
- deterministic part segmentation fully qualified: **FAIL / PARTIAL SEMANTICS ONLY**;
- selected scale below budget: **PASS**.

Result: **FAIL**.

### `PARTIAL_MANAGEABLE_X16_ROUTE_READY`
- authoritative candidate assets exist: PASS;
- practical bounded scale exists: PASS;
- in-situ physical semantics support the route: PASS;
- selected source bytes/checksum/schema/inventory remain incomplete without contradiction: PASS condition.

Result: **PASS**.

### `HOLD_XCT_SUMMARY_SEMANTICS`
Not selected as final label because the workbook itself could not be retrieved; no evidence shows the schema is unsuitable.

### `HOLD_INSITU_ACCESS_OR_SEGMENTATION`
Not selected as final label because the overall route is already qualified as practical PARTIAL, while in-situ access/segmentation remains one of the unresolved sub-gaps.

### `REJECT_MANAGEABLE_REPRESENTATION`
Not applicable.

## 7. Outcome-blindness / outcome 비열람

`NEW_X16_NUMERICAL_OUTCOME_BLIND = YES` remains intact.

F18 did not inspect:
- XCT workbook numerical cells;
- DAQ process values;
- XYPT command values;
- any process↔XCT relationship.

No model/statistic was computed.

## 8. Consequence / 후속

Do **not** start E19 process↔XCT modeling yet.

The next eligible step should be narrowly targeted to the two remaining blockers rather than expanding data volume:
1. recover the exact XCT workbook + checksum through an authoritative zero-cost route and qualify only its non-numerical schema/16-part mapping first;
2. recover/freeze a deterministic X16 part-coordinate segmentation rule for DAQ/XYPT, preferably from authoritative build command/layout metadata, before computing any process summaries.

If both pass, the already-frozen `L101-125` DAQ+XYPT representation can be used in a later separately preregistered low-degree-of-freedom 16-part technical-replicate process↔XCT experiment.

Do not switch layer groups, add MPM, or expand model capacity to rescue F18.

## 9. Cost / 비용

No paid or potentially paid route was used. `COST-001` + `DEC-028` remain mandatory; explicit user approval is required before any potentially billable action.
