---
id: AMBENCH-F31
stage: FEASIBILITY
status: PREREGISTERED
created: 2026-08-23
source_of_truth: github
incremental_monetary_cost_usd: 0
---

# AMBENCH-F31 — Alternate Pad-Geometry Turnaround Replication Source/Identity Qualification / 대체 pad-geometry turnaround 반복 source·identity 적격성

## Purpose / 목적

**KO:** F26에서 AMB2025-07에 `5 mm × 5 mm`와 `1 mm × 5 mm` 두 pad geometry가 존재한다고 확인했으나, E29/E30에서 사용한 plate-specific 45-track P1/P2/P3 route가 어느 geometry에 해당하며 `1 mm × 5 mm` geometry에 대해 별도의 plate-resolved physical-outcome route가 존재하는지는 아직 검증되지 않았다. F31은 numerical turnaround effect를 계산하지 않고 이 source/design identity만 판정한다.

**EN:** F26 established that AMB2025-07 contains both `5 mm × 5 mm` and `1 mm × 5 mm` pad geometries, but it remains unverified which geometry is represented by the plate-specific 45-track P1/P2/P3 route used in E29/E30 and whether the `1 mm × 5 mm` geometry has a distinct plate-resolved physical-outcome route. F31 evaluates only this source/design identity and computes no numerical turnaround effect.

## Allowed evidence / 허용 evidence

F31 may inspect only:
- current NIST `mds2-4103` NERDm metadata/component paths/sizes/checksums;
- exact root `4103_ReadMe.txt` documentation;
- authoritative design/parameter files such as `SampleIParameters.csv` if present, limited to sample identity and experimental-design fields;
- bounded schema/header information from candidate design-only files;
- documentation describing which directories/files correspond to each pad geometry and measurand.

F31 must **not** inspect or emit measurement outcome values from geometry-result CSVs, pixel-point coordinate rows, summary outcome tables, images, or masks.

## Questions / 질문

F31 must answer:
1. Does authoritative documentation explicitly distinguish the `1 mm × 5 mm` pad geometry from the already-used route?
2. Can the same six physical plates T72/T82/T92/T102/T112/T122 be deterministically associated with the alternate geometry without outcome-based selection?
3. Is there a distinct plate-resolved outcome representation for the alternate geometry?
4. Are authoritative measurands, units, spatial positions and nesting relationships documented?
5. Are the required candidate components immutable in current NERDm with checksum metadata?
6. Can a future low-DOF plate-level replication/falsification experiment be specified without inventing a mapping?

## Frozen interpretation / 고정 해석

A different **pad geometry** is a design robustness axis, not a new independent set of plates if it is measured on the same six physical plates. Any future inference must continue to use physical plate as the independent unit and treat multiple geometries/sections/tracks within plate as nested outcomes.

The F31 purpose is to establish whether an alternate-geometry route exists at all, not to strengthen the E29/E30 claim by default.

## Frozen gates / 고정 gate

### `PASS_F31_ALTERNATE_PAD_GEOMETRY_ROUTE_READY`
All required source/design conditions are met:
- `1 mm × 5 mm` geometry is explicitly documented;
- its outcome representation is distinct and identifiable;
- same six target physical plates can be deterministically bound to that representation;
- measurand/unit/spatial/nesting semantics are sufficient for a plate-level experiment;
- required components have immutable current NERDm identities/checksums;
- no outcome-value inspection is required to select the route.

### `PARTIAL_F31_ALTERNATE_GEOMETRY_DESIGN_READY`
Alternate geometry is clearly documented, but at least one of plate-resolved outcome identity, deterministic mapping, measurand semantics, or immutable component route remains unresolved. No experiment may start.

### `HOLD_F31_SOURCE_OR_IDENTITY`
Required authoritative documentation/design source cannot be safely retrieved/verified or conflicts prevent a source identity decision.

### `REJECT_F31_ALTERNATE_GEOMETRY_ROUTE`
Authoritative source structure establishes that no distinct deterministic plate-resolved alternate-geometry physical-outcome route is available for the intended replication.

## Exposure / 노출
Permanent inherited disclosure remains:
`NEW_F31_ALTERNATE_GEOMETRY_OUTCOME_BLIND = NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

F31 itself must not expose new alternate-geometry outcome values.

## Capability / Portfolio / 비용
Use existing project-local NERDm/source-verification pattern. Classification remains `SHARED-INTERNAL-CANDIDATE`; do not create a new Skill/MCP/Plugin. Shared paid quota/budget is not assumed.

Incremental monetary cost must remain `0 USD`; potentially billable work requires prior explicit approval.
