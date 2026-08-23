---
id: AMBENCH-F28
type: feasibility-preregistration
state: PREREGISTERED
created: 2026-08-23
source_of_truth: github
parent: AMBENCH-E27
---

# AMBENCH-F28 — AMB2025-07 Plate-Specific P1 Optical Source/Schema Qualification Gate
# AMBENCH-F28 — AMB2025-07 plate-specific P1 optical source/schema qualification gate

## Purpose / 목적

Determine whether the six already identified plate-specific P1 optical result components in NIST `mds2-4103` provide an authoritative, deterministic route to one per-plate geometry endpoint suitable for a future separately preregistered six-plate experiment.

F28 is **source/schema/provenance only**. It does not compare conditions or calculate geometry outcomes.

## Frozen plates / 고정 plate
- 0.75 ms group identity: T72, T82, T92
- 5.0 ms group identity: T102, T112, T122
- inspect P1 only.

Condition labels are retained only as experiment provenance; F28 must not compare numerical values between groups.

## Frozen source scope / 고정 source 범위
1. current NIST NERDm `mds2-4103`;
2. exact plate-specific P1 component matching each frozen plate under `Cross_Sections/Tracks_Results/*_P1s_pixel_points.csv`;
3. small authoritative README/documentation component if needed for schema semantics.

No P2/P3 outcomes, summary outcome values, thermography, or alternate dataset may be used to select a route.

## Allowed inspection / 허용 검사
- NERDm filepath, size, SHA-256, media type;
- local size/SHA match;
- encoding;
- header field names only;
- row/column counts only;
- finite/nonempty structural counts without values;
- documentation term/semantic checks that do not emit outcome values;
- whether direct geometry metrics are present as documented fields;
- whether the component instead stores pixel/annotation coordinates requiring further reconstruction.

Forbidden:
- outputting raw coordinate values;
- computing depth/overlap depth/width/area;
- aggregating by turnaround condition;
- condition ranking/effect testing;
- choosing a different endpoint based on numerical content.

## Frozen gates / 고정 gate

### `PASS_F28_PLATE_SPECIFIC_GEOMETRY_SOURCE_READY`
All six P1 components:
- exact immutable source identity PASS;
- deterministic plate identity PASS;
- schema/documentation directly exposes the frozen geometry measurand or an authoritative deterministic reconstruction contract sufficient to calculate it without tuning.

### `PARTIAL_F28_PLATE_SPECIFIC_ANNOTATION_READY`
All six P1 components are immutable and plate-specific, but schema is raw pixel/annotation data and an authoritative deterministic per-plate geometry reconstruction contract is not yet established.

### `HOLD_F28_PLATE_COMPONENT_INTEGRITY`
One or more frozen plate P1 components cannot be immutably identified/retrieved/parsed.

### `REJECT_F28_PLATE_SPECIFIC_ROUTE`
Plate-specific P1 components are established not to contain or support geometry-relevant annotation/provenance for the intended route.

## Exposure / 사전노출
Permanent inherited state:
`NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

F28 may not use the pre-exposed malformed values to select schema, endpoint, transform, reconstruction, or gate.

## v2.1 overlay / v2.1 overlay
Mission continuity under `DEC-055`. No Skill/MCP/Plugin is required. The source-qualification workflow remains `SHARED-INTERNAL-CANDIDATE` pending later portfolio reconciliation.

## Cost / 비용
Zero incremental monetary cost only. No artifact/cache/larger runner. Paid/potentially paid route => `HOLD_COST_APPROVAL`.