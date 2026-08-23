---
id: AMBENCH-F34-RESULT
type: source-design-result
state: COMPLETED_PARTIAL
created: 2026-08-23
source_of_truth: github
candidate_outcomes_inspected: false
large_archives_downloaded: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F34 Result — Independent External Scan-History Source Gate
# AMBENCH-F34 결과 — 독립 외부 Scan-History Source Gate

**Final gate / 최종 gate:** **`PARTIAL_F34_METADATA_READY_OUTCOME_ROUTE_GAP`**

## 1. Executive result / 핵심 결과

NIST `10.18434/M32044` / `mds1103vzr` is a reproducible, independent IN625 AMMT 3D-build source with deliberately varied scan strategies, command-level monitoring triggers, co-axial melt-pool monitoring, and layer imaging. Current PDR identity and checksum-frozen `Metadata.zip` were verified at zero incremental monetary cost.

However, F34 cannot assign full PASS without opening the multi-GB command/measurement archives because:
- exact part→scan-strategy descriptions reside in `Build Command Data.zip`, not `Metadata.zip`;
- the monitoring route is deterministic at layer/trigger/file-naming level, but exact strategy→monitoring pairing cannot be enumerated from the small metadata surface alone;
- each documented part uses a unique strategy, so same-strategy physical replication is not established;
- current NIST AMMT summary says ten rectangular parts, while the linked detailed data-description labels Part 1–12 and a 12-layer MPM cycle;
- no small, checksum-addressable tabular physical-quality endpoint is exposed by the metadata-only route.

Therefore the source is promising but not fully experiment-ready under the frozen F34 rules.

## 2. Immutable source identity / 불변 source identity — PASS

Current official NERDm endpoint:
- identifier: `ark:/88434/mds1103vzr`;
- title: `Process Monitoring Dataset from the Additive Manufacturing Metrology Testbed (AMMT): 3D Scan Strategies`;
- version: `1.0.4`;
- `Metadata.zip`: `2,489,233` bytes;
- `Metadata.zip` SHA-256 NERDm/preregistered/local: `cf788593b45675dfbf380782b9141ebafd85bf6653f8ca57f0cf69d578c60ee6` — exact match.

Large source identities were recorded from NERDm but not downloaded:
- `Build Command Data.zip`: `7,419,446,651` bytes, SHA-256 `de8a05ebd27f80bd79b6545c9f8a79c0e60230290e1799d9151f14f7429594b1`;
- `In-situ Meas Data.zip`: `9,170,420,366` bytes, SHA-256 `4db83f84cce2f4a28e75830a5df496c9a04db5e5554513924434463081ab645f`;
- `Movies.zip`: `698,954,503` bytes, SHA-256 `df63cbc6f07c0cad11cff2f01355ac583da0079d04370f21e9a93f746319c545`.

## 3. Independent physical units / 독립 물리 단위 — PARTIAL

The detailed NIST data-description establishes physically separate build parts with common nominal `10 mm × 10 mm × 5 mm` geometry and unique scan strategies, plus 250 build layers. It explicitly identifies Part 1 through Part 12 and states the MPM selection cycle repeats every 12 layers.

Boundary:
- part = physical build unit;
- layer = nested process stage within a part/build, not an independent replicated part;
- frame = measurement unit, never an independent physical replicate;
- same-strategy replicated parts are not established because each documented part uses a unique strategy.

Source-integrity caveat: the current NIST AMMT Datasets summary says `ten rectangular IN625 parts`, conflicting with the detailed article's Part 1–12 structure. See `SOURCE_CONFLICT.md`.

## 4. Explicit scan-strategy intervention / 명시 scan-strategy 개입 — PASS

The official data-description states:
- experiment purpose was to study effects of varying laser scan strategies on final 3D part quality;
- each part uses a unique scan strategy;
- variation includes scan path/geometry, laser power, and scan velocity;
- all parts share the same nominal part geometry;
- nominal scan speed is `800 mm/s`, nominal laser power `195 W`, layer height `20 µm`, spot diameter `85 µm`, while parameters may vary within and across parts.

Thus scan-strategy variation is deliberate, not merely sensor assignment.

## 5. Deterministic strategy→monitoring route / 결정론적 strategy→monitoring route — PARTIAL

Strong documented semantics:
- AM G-code folders are labeled with part number plus a scan-strategy description;
- XYPT command files contain X, Y, laser power and trigger at 10 µs / 100 kHz;
- trigger channel 1 (`T=2`) corresponds to MPM image capture;
- MPM data directories are layer-indexed `MIA_LXXXX`, with `frameYYYYY.bmp` frames;
- MPM was collected for one part per layer, cycling by part number every 12 layers;
- documented timing offset is `1.21 ms` between XYPT indication and actual camera triggering.

But exact part→strategy labels are inside the ~7.42 GB command archive and are not present in `Metadata.zip`. F34 therefore cannot enumerate a complete immutable strategy→part→layer→frame map without crossing its frozen large-archive boundary.

## 6. Outcome semantics / outcome 의미 — PASS at documentation level, route incomplete

Documented monitoring/geometry semantics include:
- co-axial MPM images at 2 kHz for this dataset;
- MPM spatial scale `8 µm/pixel`;
- documented melt-pool width/length/orientation and melt-pool area processing in synchronized example movies;
- layer images before/after processing each layer.

These provide defensible future low-DOF physical-monitoring endpoint concepts. F34 did not inspect or compute candidate numerical outcomes.

## 7. Claim-transfer integrity / claim 이전 무결성 — PASS

M32044 is independent of E33's `mds2-3662` partial-artifact workbook and can test scan-history/process-strategy transfer in a different 3D-build monitoring context.

A future analysis must not claim:
- same construct or same treatment as E33;
- direct row/track identity with E33;
- frame-level pseudo-replication;
- strategy causality without controlling part/build-location confounding;
- physical replication of a strategy unless separately established.

## 8. Zero-cost feasibility / 무비용 가능성 — PASS for F34 source gate; downstream unresolved

F34 itself used only official public metadata and `Metadata.zip`; incremental monetary cost = `0 USD`.

The large archives were deliberately not opened. Any downstream need for ~7.42 GB command data or ~9.17 GB monitoring data requires a separate preregistration and explicit confirmation that execution remains zero incremental cost before access.

## 9. Frozen gate application / 고정 gate 적용

| Dimension | Result |
|---|---|
| Immutable source identity | PASS |
| Independent physical units | PARTIAL |
| Explicit scan-strategy intervention | PASS |
| Deterministic strategy→monitoring route | PARTIAL |
| Outcome semantics | PASS / route incomplete |
| Claim-transfer integrity | PASS |
| Zero-cost F34 qualification | PASS |

Full PASS requires all seven dimensions PASS, so it is not selected.

**Final:** **`PARTIAL_F34_METADATA_READY_OUTCOME_ROUTE_GAP`**.

## 10. Exposure / 노출

`NEW_F34_CANDIDATE_NUMERICAL_OUTCOME_BLIND = YES`

No M32044 candidate numerical monitoring or quality outcome was inspected; no large measurement/command/movie archive was opened.

## 11. Consequence / 후속

Do not open the multi-GB M32044 archives merely to rescue F34. Preserve M32044 as a qualified `PARTIAL` external source.

The next source-only mission candidate should more directly manipulate/encode residual thermal history while offering a simpler bounded source route. NIST `mds2-2507` / RHF is the priority because its experiment explicitly develops a **Residual Heat Factor from temporal/spatial scan history** and tests residual-heat compensation on IN625 bare plate with in-situ melt-pool monitoring and post-process quality measurements.
