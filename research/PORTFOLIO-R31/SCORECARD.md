---
id: PORTFOLIO-R31-SCORECARD
type: immutable-mission-roi-scorecard
created: 2026-09-16
issue: 142
contract_decision: DEC-196
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R31 Immutable Scorecard / 고정 점수표

The candidate pool, rubric and tie-break were frozen in `research/PORTFOLIO-R31/README.md` and bound to Issue #142 before this scorecard was persisted.

No candidate outcome magnitude, relationship direction, coefficient or predictive result was opened while scoring.

## Final frozen scores / 최종 고정점수

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Score disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-NHTSA-MC-001** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 2 | **39/45** | **PROVISIONAL_SELECT** |
| KR-GG-CHEM-001 | 5 | 5 | 5 | 4 | 4 | 5 | 2 | 5 | 1 | **36/45** | HOLD_IDENTITY_AND_OVERLAP |
| US-PIPE-001 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | **36/45** | HOLD_RESTRICTED_GEOMETRY_AND_OVERLAP |

No tie-break is required because `US-NHTSA-MC-001` leads by total score.

## Scoring basis / 점수 근거

### US-NHTSA-MC-001 — 39/45

- **Mission 5 / Direct outcome 5 / Practical 5:** vehicle defect precursors and subsequent safety recalls are a direct operational safety bottleneck with a concrete regulatory outcome.
- **Cross-source 5:** NHTSA publishes separate manufacturer-communication and recall datasets.
- **Independent-unit 4:** the natural product identity is Model Year × Make × Model, but communications repeat across document/product/component rows and models can share platforms/components; a later gate must prevent pseudoreplication rather than assume independence.
- **Zero-cost 5:** current NHTSA flat files/data dictionaries are public and downloadable without a paid service.
- **Join defensibility 4:** both source families expose Model Year, Make and Model semantics, plus source-native communication/campaign identifiers. Exact normalization and collision/cardinality support still require F01 verification before a full join claim.
- **Next-gate information gain 4:** one F01 can cheaply resolve current product-normalization, temporal, multiplicity and overlap uncertainty without opening recall incidence by communication profile.
- **Low-overlap/novelty 2:** NHTSA itself uses manufacturer communications/service bulletins as Early Warning Reporting and defect-analysis information. The branch therefore does not claim novelty for the general signal; only a tightly bounded prospective public-data design may remain distinct.

### KR-GG-CHEM-001 — 36/45

- **Mission 5 / Direct outcome 5:** hazardous-chemical facility risk and chemical accidents are direct industrial-safety outcomes.
- **Cross-source 5:** Gyeonggi exposes separate facility and accident public datasets.
- **Independent-unit 4:** facility is a natural unit but facility continuity/change and repeated accidents require prospective handling.
- **Practical 4:** high local safety value, but the current source scope is Gyeonggi only and may not be generalized nationally.
- **Zero-cost 5:** public-data portal access is free.
- **Join defensibility 2:** the accident source currently exposes date/address/coordinates but has not established a stable common source-native business identifier shared with the facility table. Fuzzy entity resolution is not authorized.
- **Next-gate information gain 5:** an outcome-blind F01 can decisively test whether exact deterministic linkage exists or terminate the branch early.
- **Low-overlap/novelty 1:** Korean literature already links chemical-enterprise plant factors/handling characteristics with accident history and includes Seoul/Gyeonggi businesses; the general facility-profile → accident-risk proposition is materially overlapping.

### US-PIPE-001 — 36/45

Carry the R29/R30 source/access-informed score unchanged because no new official evidence was introduced before this scorecard:

`5 + 5 + 5 + 5 + 5 + 5 + 3 + 3 + 0 = 36/45`.

Public incident/mileage data remain useful, but unrestricted national NPMS line geometry may not be assumed by the zero-cost general-public runner and direct literature/domain overlap remains high.

## Immutable selection consequence / 고정 선정결과

The sole score-based provisional selection is:

**`SELECT_US_NHTSA_MC_001_COMMUNICATION_TO_RECALL_F01`**

R31 authorizes only a separate outcome-blind source/schema/product-identity/time F01 after atomic terminalization and State Integrity. It does not authorize opening recall incidence or testing a relationship.

This scorecard must not be revised based on downstream source support or eventual recall outcomes.

Incremental monetary cost: **0 USD**.
