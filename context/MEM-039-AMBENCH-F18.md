---
id: MEM-039-AMBENCH-F18
type: memory
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# MEM-039 — AMBENCH-F18
# MEM-039 — AMBENCH-F18 기억

## Result / 결과

`AMBENCH-F18` final frozen gate: **`PARTIAL_MANAGEABLE_X16_ROUTE_READY`**.

## Frozen representation / 고정 표현

XCT:
- `mds2-2514` `OverhangX16_ImageHistograms.xlsx` + `.sha256` only.

In-situ:
- `mds2-2309` `DAQ_L101-L125.zip` + `.sha256`;
- `mds2-2309` `XYPT_L101-L125.zip` + `.sha256`.

No MPM, layer-camera, extra layer groups, or full-build download is part of the frozen route.

## What is established / 확립

- XCT workbook is a very small public summary asset (~193 KB).
- selected DAQ and XYPT archives are bounded below the frozen 1 GiB compressed in-situ budget.
- authoritative X16 User Notes establish 16 nominally identical parts, part labels `1-1`…`4-4`, 250 layers, and 10 us XYPT/DAQ file semantics.
- inherited NIST X4 data description establishes DAQ actual Galvo X/Y, LTZ, and laser-power-reference channels at 100 kHz, whereas XYPT is commanded path/power.

## Remaining blockers / 잔여 차단

1. workbook + workbook `.sha256` actual bytes not retrieved;
2. DAQ/XYPT selected `.sha256` bytes not retrieved;
3. local checksums/archive inventories not reproduced;
4. workbook sheet/header/16-part schema not inspected;
5. exact authoritative numeric X/Y boundaries for 16-part DAQ segmentation not frozen/verified.

No X16 numerical outcome has been inspected or computed.

## Decision / 결정

`DEC-041`: preserve the bounded representation.  
`DEC-042`: do not start E19 until workbook byte/schema qualification and exact part-coordinate segmentation are both resolved.

## Cost / 비용

Zero incremental monetary cost only. Any potentially billable action requires explicit prior user approval under `COST-001` + `DEC-028`.
