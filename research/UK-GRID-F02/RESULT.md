---
id: UK-GRID-F02-RESULT
type: boundary-identity-alignment-feasibility-result
state: COMPLETED_PASS
created: 2026-09-03
parent: UK-GRID-F02
issue: 69
gate: PASS_UK_GRID_BOUNDARY_IDENTITY_READY
incremental_monetary_cost_usd: 0
---

# UK-GRID-F02 Result — Boundary Headroom × Thermal-Cost Identity/Alignment
# UK-GRID-F02 결과 — Boundary Headroom × Thermal-Cost 식별자·정렬

## Final gate / 최종 게이트

**`PASS_UK_GRID_BOUNDARY_IDENTITY_READY`**

## What was demonstrated / 검증된 내용

Two current official NESO resources share exact source-defined `Constraint Group` identity and compatible 2026 time coverage sufficient for a future same-boundary group-day experiment, without opening observation-level flow, limit or cost values.

두 현행 공식 NESO resource가 observation-level flow·limit·cost 수치를 열지 않은 상태에서 향후 동일 boundary group-day 실험에 필요한 정확한 source-defined `Constraint Group` identity와 2026 시간범위를 공유함을 검증했다.

### Frozen resources / 고정 resource
- Day Ahead Constraint Flows and Limits: `38a18ec1-9e40-465d-93fb-301e80fd1352`
- Thermal Constraint Costs Data 26-27: `c730b788-4328-43dc-9f84-27fd3adeda59`

## Identity result / 식별자 결과

Day-ahead source groups: `31`.

Thermal-cost source groups: `6`.

Exact trim-whitespace-only common groups:
- `ESTEX`
- `SCOTEX`
- `SEIMP`
- `SSE-SP`
- `SSHARN`
- `SWALEX`

Exact common groups with overlapping source coverage on/after `2026-04-01`:
- `ESTEX: 2026-04-01..2026-08-18`
- `SCOTEX: 2026-04-01..2026-08-18`

No fuzzy matching, alias inference, B-number translation or manual mapping was used.

## Outcome-blind integrity / 결과 비사용 무결성

F02 retrieved only:
- schema metadata;
- exact `Constraint Group` strings;
- group-level min/max datetime/date and structural cardinality metadata;
- response hashes.

It did **not** request or emit observation-level:
- `Limit (MW)`;
- `Flow (MW)`;
- `Daily Cost (GBP)`.

`NEW_UK_GRID_BOUNDARY_NUMERICAL_OBSERVATION_BLIND = YES_AT_F02_COMPLETION`.

## Methodology boundary / 방법론 경계

NESO states that from `2024-04-22` the Day Ahead Constraint Flow methodology no longer incorporates expected constraint mitigation or optimisation actions. Both exact overlap-ready 2026 routes lie wholly after that change.

## Scientific implication / 과학적 함의

F02 removes a material source-semantic uncertainty: a same-code boundary relationship can be tested without speculative spatial or naming reconciliation.

This supports a stronger construct than the generic GB-wide F01 proxy route:

`named boundary day-ahead flow relative to named boundary limit → same named boundary realized daily thermal-constraint cost`.

## Claim boundary / 주장 경계

PASS establishes **exact identity + temporal join feasibility only**.

It does not establish that day-ahead headroom predicts, explains or causes realized thermal-constraint cost. It also does not establish that a published day-ahead limit is a purely thermal physical limit under every operating condition.

## Next / 다음

Select at most one boundary using official structural semantics only, then fully preregister the single numerical experiment allowed under `DEC-098 / DEC-099` before retrieving any selected flow/limit/cost observations.

Official NESO material gives `SCOTEX` the strongest outcome-blind structural rationale because it is the Anglo-Scottish B6 boundary, where rising Scottish renewable generation drives predominantly north-to-south transfer requirements and the published B6 base capability is explicitly described as thermally limited by the Harker–Moffat 400 kV circuit.

## Cost / 비용

Incremental monetary cost remained **0 USD**.
