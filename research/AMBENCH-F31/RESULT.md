---
id: AMBENCH-F31-RESULT
type: feasibility-result
state: COMPLETED_PASS_ALTERNATE_PAD_GEOMETRY_ROUTE_READY
created: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F31/README.md
  - research/AMBENCH-F31/AMENDMENT-01.md
  - research/AMBENCH-F31/SOURCE_DESIGN_RESULT.md
  - research/AMBENCH-E30/SEMANTIC_CORRECTION.md
  - Issue #49
---

# AMBENCH-F31 Result — Alternate Pad-Geometry Source/Identity Qualification
# AMBENCH-F31 결과 — 대체 Pad-Geometry Source/Identity 적격성

**Frozen source/design gate / 고정 source·design 판정:** **`PASS_F31_ALTERNATE_PAD_GEOMETRY_ROUTE_READY`**

## 1. Result / 결과

**KO:** 현재 NIST `mds2-4103` v1.0.0의 exact root README, checksum-verified `SampleIParameters.csv`, NERDm component metadata 및 NIST AMB2025-06/07 공식 design documentation을 source/design-only 범위에서 검증했다. `1 mm × 5 mm` pad geometry는 별도 plate 집단이 아니라 동일 physical plate의 `P3` section으로 결정론적으로 식별된다. Bare turnaround 비교에 사용된 T72/T82/T92 및 T102/T112/T122 모두에서 P1/P2는 5 mm pad, P3는 1 mm pad이다. 따라서 alternate geometry는 동일 six physical plates에 대해 distinct, plate-resolved, immutable component route를 가진다.

**EN:** Source/design-only verification of the current NIST `mds2-4103` v1.0.0 exact root README, checksum-verified `SampleIParameters.csv`, NERDm component metadata, and official NIST AMB2025-06/07 design documentation establishes that the `1 mm × 5 mm` pad geometry is deterministically represented by section `P3` on the same physical plates rather than by a separate plate group. For all six bare turnaround plates T72/T82/T92 and T102/T112/T122, P1/P2 are 5 mm pad sections and P3 is the 1 mm pad section. The alternate geometry therefore has a distinct, plate-resolved, immutable component route on the same six physical plates.

## 2. Authoritative design mapping / 권위 설계 매핑

Current `SampleIParameters.csv` design-only schema contains:
`Sample ID`, laser power, laser spot diameter, laser scan speed, hatch spacing, powder thickness, turnaround time, `Pad_Width`, and `Location`.

For the six bare plates:
- 0.75 ms: `T72`, `T82`, `T92`;
- 5.00 ms: `T102`, `T112`, `T122`;
- every plate: `P1 = 5 mm @ 0.460 mm`, `P2 = 5 mm @ 2.546 mm`, `P3 = 1 mm @ 0.556 mm` in current design table.

The official NIST challenge Table 8 independently confirms the geometry assignment; its P2 position is printed as 2.545 mm, a 0.001 mm documentation/table difference that does not alter source identity or geometry mapping.

## 3. Immutable route / 불변 route

Current NERDm metadata uniquely identifies all target `P1/P2/P3` `Cross_Sections/Tracks_Results/*_pixel_points.csv` components for the six bare physical plates, with component size and SHA-256 metadata. The F31 workflow opened none of these measurement-result files.

Exact design-source integrity:
- `4103_ReadMe.txt`: size `23849`, SHA-256 `857ed848396ebce7e88ccfe95c1b6ac9dd75ba8337fd570e78a797bad5a45d94`, local/current NERDm match `YES`;
- `SampleIParameters.csv`: size `2086`, SHA-256 `ad3efdd8757d19f435bb234483ed6ebdaea3e3ee5149aee77113d0d7bdff9e8c`, local/current NERDm match `YES`.

## 4. Nesting and inference boundary / nesting·추론 경계

- independent experimental unit remains physical plate;
- P1/P2/P3 are section-specific outcomes nested within each plate;
- P1 and P2 are two locations in the 5 mm pad;
- P3 is the 1 mm pad geometry;
- track rows remain nested below plate-section and must not be counted as independent physical replicates.

## 5. Integrity discovery affecting E30 / E30에 영향을 주는 무결성 발견

F31 source qualification falsified the prior E30 semantic assumption that P2 and P3 were merely two spatial repeats of the same pad geometry. See `research/AMBENCH-E30/SEMANTIC_CORRECTION.md` and `DEC-065`.

Consequences:
- E30 P2 remains a same-5-mm-geometry spatial sensitivity;
- E30 P3 was already an alternate-1-mm-geometry numerical outcome;
- the E30 P2/P3 combined endpoint is a mixed geometry+position composite, not a pure spatial-robustness endpoint.

No historical E30 numerical values are deleted or recomputed by F31.

## 6. Exposure / 노출

F31 itself opened no new alternate-geometry outcome rows, images, masks, result summaries, effects, or models. However P3 numerical outcomes were already observed in E30 under the incorrect spatial-repeat interpretation.

Permanent corrected disclosure:
`NEW_F31_ALTERNATE_GEOMETRY_OUTCOME_BLIND = NO__P3_ALTERNATE_GEOMETRY_NUMERICAL_OUTCOMES_ALREADY_OBSERVED_IN_E30__PLUS_INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

Therefore a subsequent P3 analysis may be confirmatory/reinterpretive but **must not be represented as a fresh outcome-blind alternate-geometry experiment**.

## 7. Gate application / gate 적용

### `PASS_F31_ALTERNATE_PAD_GEOMETRY_ROUTE_READY`
- explicit 1 mm geometry documentation: PASS;
- deterministic geometry/turnaround/plate mapping: PASS;
- distinct plate-resolved representation: PASS (`P3`);
- documented spatial/nesting semantics sufficient for plate-level analysis: PASS;
- immutable current NERDm source identities/checksums: PASS;
- route selection did not require new outcome inspection: PASS.

**Final source/design gate: PASS.**

## 8. Next-action constraint / 다음 행동 제약

Do **not** launch the originally contemplated “fresh alternate-geometry P3 replication experiment”; its outcomes are already exposed through E30. The next new numerical experiment must use a genuinely outcome-unseen independent source/condition/representation and must be separately preregistered.

A source-only next stage may evaluate already-qualified independent candidates, including the F26 secondary `mds2-3662` route, for whether they provide a scientifically transferable falsification/replication axis without claiming they reproduce the same AMB2025-07 turnaround contrast.

## 9. Capability / Portfolio / 비용
Repeated source-integrity/preregistration workflow remains `SHARED-INTERNAL-CANDIDATE`. No new Skill/MCP/Plugin is justified. No shared paid quota or resource is assumed.

Incremental monetary cost: `0 USD`.
