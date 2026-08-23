---
id: AMBENCH-F35-RESULT
type: source-design-result
state: COMPLETED_PASS
created: 2026-08-23
source_of_truth: github
raw_candidate_numerical_outcomes_inspected: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F35 Result — NIST RHF External Confirmatory Source Gate
# AMBENCH-F35 결과 — NIST RHF 외부 Confirmatory Source Gate

**Final gate / 최종 gate:** **`PASS_F35_RHF_EXTERNAL_CONFIRMATORY_SOURCE_READY`**

## 1. Executive result / 핵심 결과

NIST `mds2-2507` RHF experiment is fully source/design-ready for a separately preregistered external residual-history confirmatory analysis.

The source provides:
- 55 independent physical rectangular scan parts `P01–P55` on IN625 bare plate;
- exactly 5 constant-positive-power baseline parts and 50 RHF variable-power parts recovered directly from checksum-frozen command inputs;
- deterministic shared `PXX` identity across command, MPM, encoder, analysis-result and microscope routes;
- precomputed per-part analysis CSV semantics including melt-pool area/length/width;
- visible-light microscopy `PXX.jpg` post-process route;
- a small (~1.64 MB) checksum-addressable analysis-results archive suitable for a later schema-first low-DOF confirmatory experiment without opening 55 raw MPM AVIs.

No raw candidate numerical monitoring, analysis-result or microscopy outcome was inspected in F35.

## 2. Immutable source identity / 불변 source identity — PASS

Current official NERDm:
- dataset: `mds2-2507`;
- title: `Process Monitoring Dataset from the Additive Manufacturing Metrology Testbed (AMMT): RHF Experiment`;
- version: `1.0.1`;
- components: `119`;
- checksum-bearing components: `117`.

Exact data-description byte verification:
- `HY-RHF-DataDescription.pdf` size `960223`;
- SHA-256 NERDm/local: `2b1531d64bd03507ba1fabb271f96d9d5ed7af05666ff2641741a37c169c4177` — PASS.

Important source routes:
- `RHF_Command.zip` size `18079576`, SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
- `RHF_Encoder.zip` size `28987689`, SHA-256 `2f953f9d45f665e02d9a473c22475be5a68e3c551212b0e7d1ebe9a2ddcc94f6`;
- `RHF_Analysis_Results.zip` size `1637430`, SHA-256 `306a3d26e6e77d6fef44b1bf7b1dd2c817560a84f21f27fc4cec8cdb10cabe59`;
- `RHF_MP_Area.zip` size `14828989`, SHA-256 `e68dbac4ec15e0accd41c6222f4d1a4947aab01b9dcaec36e09a567ac11c55c5`;
- `RHF Microscopic Images.zip` size `32694863`, SHA-256 `91a378f313bb934868606276486af40095be5f7fd7e94d2d5a2963cf96b1206b`.

## 3. Independent experiment/unit semantics / 독립 실험·단위 의미 — PASS

Official data-description:
- 55 physical `3 mm × 2 mm` rectangular scan parts on a bare IN625 plate;
- same geometric scan pattern, unique laser-power profile by part;
- physical part `PXX` is the independent experimental unit for part-level comparison;
- command timesteps, MPM frames, pixels and processed rows are nested measurements, not independent physical replicates.

Checksum-frozen `RHF_Command.zip` independently recovered exactly `P01–P55`.

## 4. Direct residual-history intervention / 직접 잔류이력 개입 — PASS

Official RHF design defines Residual Heat Factor from spatial/temporal scan history and adjusts laser power according to RHF. The publication design states 55 rectangles, with 5 baseline and 50 RHF-controlled conditions.

Corrected command-input preflight reproduced this structure without outcomes:
- baseline constant-positive-power parts: `P01, P12, P23, P34, P45`;
- RHF variable-positive-power parts: the other 50;
- source gate: `PASS_F35_COMMAND_INTERVENTION_STRUCTURE`.

The first parser's false HOLD was superseded before any outcome access because headerless XYPT plus laser-off `0 W` rows had been misclassified. The corrected parser uses the documented positional `X,Y,Power,Trigger` schema and positive commanded power only.

## 5. Deterministic condition→monitoring route / 조건→monitoring route — PASS

The official naming/timing contract is deterministic:
- command: `RHF_PXX_layer0001.csv`;
- MPM: `RHF_MPM_PXX.avi`;
- encoder/power feedback: `DAQ_PXX_layer0001.csv`;
- XYPT command and camera trigger share the documented `PXX` identity;
- 10 µs command/DAQ timing and 20 kHz MPM acquisition are documented;
- `T=2` identifies MPM trigger events.

No outcome value is needed to establish the route.

## 6. Deterministic condition→post-process route / 조건→후처리 route — PASS

Official data-description supplies:
- analysis result: `DAQ_RHF_PXX_layer0001_T80_XYPVALWI.csv`;
- microscopy: `PXX.jpg`;
- both inherit the same physical part number `PXX`.

This is an explicit condition→processed-monitoring and condition→microscopy identity route.

## 7. Low-DOF confirmatory experimentability / 저자유도 확인 실험성 — PASS

`RHF_Analysis_Results.zip` is ~1.64 MB and officially documents per-part CSV columns for measured position/power/speed and processed MPM area/length/width/intensity/spatter fields.

A future E36 can therefore:
- inspect schema first without numerical cells;
- freeze one or a very small number of part-level aggregate endpoints;
- use the 5 known baseline physical units and 50 RHF intervention units without frame-level pseudo-replication;
- avoid high-capacity ML and raw AVI processing.

No E36 numerical statistic is authorized by F35 itself.

## 8. Claim-transfer integrity / cost — PASS

RHF is an independent AMMT experiment directly tied to residual thermal history, but any descendant result must be described as **external RHF/residual-history confirmation or reproduction**, not same-construct replication of E33's rapid-turnaround trapezoid design.

F35 incremental monetary cost: `0 USD`.

## 9. Exposure / 노출

Permanent:
`NEW_F35_PUBLICATION_LEVEL_OUTCOME_BLIND = NO__DIRECTIONAL_RHF_RESULT_PREOBSERVED`.

Still true at F35 completion:
`NEW_F35_RAW_DATA_NUMERICAL_OUTCOME_BLIND = YES`.

The official publication-level direction and some publication summary numbers were preobserved during source qualification. No `RHF_Analysis_Results.zip` numerical cell, encoder measurement, raw MPM frame or microscopy outcome was opened. Descendant execution is confirmatory/reproduction only.

## 10. Frozen gate application / 고정 gate 적용

| Dimension | Result |
|---|---|
| Immutable source identity | PASS |
| Independent experiment/unit semantics | PASS |
| Direct residual-history intervention | PASS |
| Deterministic condition→monitoring route | PASS |
| Deterministic condition→post-process route | PASS |
| Low-DOF confirmatory experimentability | PASS |
| Claim-transfer integrity / cost | PASS |

**Final:** **`PASS_F35_RHF_EXTERNAL_CONFIRMATORY_SOURCE_READY`**.

## 11. Next / 다음
Exact next action: **AMBENCH-E36 — RHF external confirmatory reproduction, schema-first**.

Before opening any `RHF_Analysis_Results.zip` numerical value, E36 must freeze:
- exact member inventory and PXX coverage;
- CSV headers/types only;
- independent unit = physical part;
- primary endpoint and aggregation;
- baseline handling for the 5 command-verified constant-power parts;
- treatment handling for the 50 RHF parts without post-hoc outcome selection;
- exact statistic/permutation/bootstrap if any;
- publication-target reproduction vs broader mechanism-transfer claims;
- permanent publication-level pre-exposure disclosure.
