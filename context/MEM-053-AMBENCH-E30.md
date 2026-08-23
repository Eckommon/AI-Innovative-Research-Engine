---
id: MEM-053-AMBENCH-E30
type: memory
state: ACTIVE
created: 2026-08-23
source_of_truth: github
research: AMBENCH-E30
---

# MEM-053 — AMBENCH-E30 / E30

## Final / 최종
`PASS_E30_SPATIALLY_ROBUST_DIRECTIONAL_EFFECT`

## Source/integrity / source·무결성
- current NIST `mds2-4103` v1.0.0;
- exact root `4103_ReadMe.txt`: 23849 bytes, SHA-256 `857ed848396ebce7e88ccfe95c1b6ac9dd75ba8337fd570e78a797bad5a45d94`, local match PASS;
- authoritative scale `0.174 µm/px`;
- exact Micrographs surface-reference component: 1653 bytes, SHA-256 `98c898fd78be88c5f0a318575ad6468dc03a3cdeaa31dc19d03605a2df9f7c22`, local match PASS;
- exactly one P2 and one P3 surface-reference binding per target plate;
- all 12 P2/P3 plate-position components exact NERDm/local size/hash PASS;
- all 12 cells have 44/45 valid tracks.

## Result / 결과
Position means (µm):
- T72 P2 119.014018773; P3 133.372320818
- T82 P2 121.352475955; P3 132.278892955
- T92 P2 122.505894273; P3 135.392437091
- T102 P2 95.800180500; P3 98.630962773
- T112 P2 97.151974636; P3 97.034663045
- T122 P2 97.057065545; P3 97.655514818

Equal-weight P2/P3 plate endpoints (µm):
- T72 126.193169795
- T82 126.815684455
- T92 128.949165682
- T102 97.215571636
- T112 97.093318841
- T122 97.356290182

Frozen statistics:
- `Delta_P2 = +24.287722773 µm`
- `Delta_P3 = +35.907503409 µm`
- `Delta_combined = +30.097613091 µm`
- exact one-sided combined permutation `p=0.05`
- combined plate rank-biserial `1.0` (9/0/0)
- global common-valid tracks 44
- `Delta_common_combined = +30.097613091 µm`

## Boundary / 경계
Physical plate remains the independent unit, n=3 vs n=3. P2/P3 are nested spatial repeats and tracks are further nested. P1 was not used to rescue/weight E30. No imputation, position dropping, endpoint search, sign/scale/source adaptation or model escalation.

Permanent disclosure:
`NEW_E30_NUMERICAL_OUTCOME_BLIND = NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

## Next / 다음
Per `DEC-063`, preregister `AMBENCH-F31` as a source/identity qualification gate for the alternate `1 mm × 5 mm` pad geometry before any alternate-geometry numerical outcome inspection. Determine whether a distinct plate-resolved low-DOF replication route actually exists; no effect calculation in F31.

## Capability / Portfolio
Workflow remains `SHARED-INTERNAL-CANDIDATE`; no new Skill/MCP/Plugin. Shared paid resources remain non-assumed without canonical ledger.

Incremental monetary cost: `0 USD`.
