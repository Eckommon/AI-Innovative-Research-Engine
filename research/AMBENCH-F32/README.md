---
id: AMBENCH-F32
stage: FEASIBILITY
status: PREREGISTERED
created: 2026-08-23
source_of_truth: github
incremental_monetary_cost_usd: 0
---

# AMBENCH-F32 — Independent Outcome-Unseen Replication/Falsification Candidate Gate
# AMBENCH-F32 — 독립 Outcome-Unseen 반복/반증 후보 Gate

## Purpose / 목적

**KO:** E30/F31 integrity correction 이후 이미 노출된 AMB2025-07 P3를 새 실험으로 재포장하지 않고, 기존에 source-qualified된 후보들 중 **새 numerical outcome을 아직 보지 않았고**, 독립 physical experimental unit을 가지며, 과학적으로 과장 없는 falsification/replication 가설을 동결할 수 있는 후보가 있는지 source/design-only로 판정한다.

**EN:** After the E30/F31 integrity correction, avoid repackaging the already-exposed AMB2025-07 P3 route as a new experiment. Determine, using source/design-only evidence, whether any already source-qualified candidate still has unseen numerical outcomes, independent physical experimental units, and a scientifically non-overclaiming falsification/replication hypothesis that can be frozen before numerical work.

## Frozen candidate set / 고정 후보 집합

Only the following already-qualified sources may be evaluated in F32:

- **A — `mds2-3662`**: F26 secondary rapid-turnaround converging/diverging candidate;
- **B — `mds2-2525`**: absorptance / high-speed X-ray candidate retained with repeat-resolved pairing gap;
- **C — `mds2-3842`**: BP4 dynamic laser-coupling candidate retained with same-specimen physical-outcome gap;
- **D — `mds2-4103` P3**: current alternate 1 mm AMB2025-07 geometry, included only as a negative-control/exposure reference and **ineligible for outcome-unseen status** because E30 already observed P3 numerical outcomes.

No new candidate may be added after F32 source/design inspection. A separate discovery stage is required if none qualifies.

## Allowed / 허용

- existing canonical GitHub records from F26/F08/F13/E30/F31;
- current official NIST NERDm metadata, version, component path/size/checksum;
- exact source README/design documentation already within the qualified source routes;
- exposure-history records showing what numerical outcomes were or were not opened/emitted;
- bounded schema/inventory checks that do not inspect candidate numerical outcome rows.

## Forbidden / 금지

F32 must not:
- open new candidate measurement-result values;
- compute any condition effect, p-value, model, ranking by outcome, or feature importance;
- add a candidate after seeing source details;
- call an adjacent physical axis a replication of AMB2025-07 turnaround time unless the source truly manipulates the same construct;
- ignore prior numerical/literature outcome exposure;
- use high-capacity modeling;
- incur incremental monetary cost.

## Frozen qualification dimensions / 고정 적격성 차원

Each candidate is judged `PASS / PARTIAL / FAIL / UNKNOWN` on:

1. **Independent physical units** — distinct physical samples/builds from E29/E30 and adequate physical replication;
2. **Outcome-unseen status** — no candidate numerical outcome values/effects have been inspected in project history; uncertainty is `UNKNOWN`, not PASS;
3. **Deterministic condition→outcome route** — repeat-resolved or otherwise scientifically valid pairing;
4. **Immutable current source identity** — official source/version/component identity recoverable;
5. **Low-DOF experimentability** — a small preregistered test is possible without pseudo-replication or high-capacity ML;
6. **Claim-transfer integrity** — the hypothesis can be worded without falsely claiming same-construct replication.

No weighted score is used.

## Frozen gates / 고정 gate

### `PASS_F32_OUTCOME_UNSEEN_INDEPENDENT_FALSIFICATION_CANDIDATE`
At least one candidate passes all six dimensions. Select exactly one primary candidate using this tie-break order:
1. outcome-unseen certainty;
2. deterministic physical-repeat pairing;
3. claim-transfer clarity;
4. simpler low-DOF design.

### `PARTIAL_F32_INDEPENDENT_CANDIDATE_NEEDS_BOUNDARY_RESOLUTION`
At least one candidate has independent physical units and credible source identity but one non-outcome dimension remains resolvable without new numerical inspection.

### `HOLD_F32_NO_ELIGIBLE_OUTCOME_UNSEEN_CANDIDATE`
No frozen candidate is eligible for a new outcome-unseen numerical experiment because of prior exposure, pairing failure, physical-outcome absence, or incompatible claim transfer.

A HOLD is a valid completed feasibility result and triggers a new source-discovery stage rather than weakening gates.

## Reporting / 보고

Durable output may record only:
- candidate identities/versions;
- exposure classification and evidence reference;
- physical-unit/repeat structure;
- source/pairing/claim-transfer status;
- qualification matrix;
- selected candidate or HOLD reason;
- next source-only action.

No new numerical outcome value may be emitted by F32.

## Capability / Portfolio / 비용

Reuse existing source-integrity and preregistration patterns. Classification remains `SHARED-INTERNAL-CANDIDATE`; do not create a new Skill/MCP/Plugin. No shared paid quota is assumed.

Incremental monetary cost: `0 USD`. Potentially billable work => `HOLD_COST_APPROVAL` pending explicit user approval.
