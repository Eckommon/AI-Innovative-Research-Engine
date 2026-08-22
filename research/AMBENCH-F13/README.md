---
id: AMBENCH-F13
type: feasibility-preregistration
state: PREREGISTERED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-POST-D12-TRIAGE.md
  - research/AMBENCH-D12/RESULT.md
  - registry/DEC-031.md
---

# AMBENCH-F13 — A-AMB2022-01 External Physical-Validation Source/Identity Feasibility
# AMBENCH-F13 — A-AMB2022-01 외부 물리검증 source/identity feasibility

## 1. Scientific question / 과학 질문

**KO:** NIST `mds2-2525`가 BP4와 독립적인 재료·실험조건에서 time-resolved absorptance와 melt-pool physical outcome을 동일 실험 계보 안에서 재현 가능하게 연결하여, 향후 D12 temporal-morphology 외부검증 실험을 사전등록할 수 있을 정도의 source/identity/time-alignment 준비도를 제공하는가?

**EN:** Does NIST `mds2-2525` provide sufficiently reproducible source, identity, and time-alignment provenance to preregister a future external validation of D12 temporal morphology using time-resolved absorptance and melt-pool physical outcomes from an experiment independent of BP4?

## 2. Outcome blindness / outcome 비열람

`NEW_EXTERNAL_OUTCOME_BLIND = YES` for F13.

F13 may inspect only publication/PDR metadata, release history, component names, sizes, checksums, descriptions, experimental-condition semantics, repeat-structure statements, timing/synchronization semantics, and file headers/schema if needed.

F13 must not inspect or calculate numerical absorptance, width, depth, solidification-rate, oscillation amplitude, correlation, predictive score, or any target-aware statistic.

## 3. Candidate source / 후보 source

- DOI: `10.18434/mds2-2525`
- Title: `Asynchronous AM Bench 2022 Challenge Data: Real-time, simultaneous absorptance and high-speed Xray imaging`
- PDR release history: `v1.3.2` reported 2026-01-07 as `added to additiveman collection`; checksum-rich `v1.3.1` is the exact data-bearing snapshot used for component-level provenance unless current component identity is independently verified unchanged.

Relevant public components include:
- `Al_Spot_TDA_Results.csv` — time-dependent absorption, aluminum stationary spot;
- `Al_Spot_TDW_Results.csv` — time-dependent melt-pool width, aluminum stationary spot;
- `Al_Scan_TDA_v2_Results.csv` — time-dependent absorption, aluminum scan;
- `Al_Scan_AA_MWD_ASR_Results.csv` — average absorption / maximum width-depth / solidification-rate scan results;
- `Spot on Bare Metal_Calibrated Absorption Data.csv` and `Scan on Bare Metal_Calibrated Absorption Data.csv` — Ti-6Al-4V training absorptance with camera/frame timing;
- simultaneous X-ray image components for stationary and scanned training experiments.

## 4. Frozen feasibility checks / 고정 feasibility 검사

F13 will determine only:
1. **source identity** — DOI/release lineage and exact checksum-bearing component identities are authoritative and reproducible;
2. **independence** — material/measurement context is genuinely distinct from BP4 IN718 `mds2-3842`;
3. **same-experiment physical pairing** — official documentation establishes simultaneous absorptance + X-ray melt-pool acquisition and/or paired challenge outcomes within the same experimental condition;
4. **time semantics** — time-dependent absorption and geometry have explicit, deterministic time definitions adequate for a future preregistration;
5. **repeat resolution** — whether individual repeated experiments are separately identifiable in public authoritative components, versus only chosen/averaged challenge results;
6. **measurand boundary** — absorptance/coupling similarity is documented without treating the two measurement systems as identical.

## 5. Frozen gates / 고정 판정

Apply exactly one:

### `PASS_REPEAT_RESOLVED_EXTERNAL_VALIDATION_READY`
All must hold:
- authoritative reproducible source/components;
- external material/condition independence;
- same-experiment absorptance + physical outcome pairing;
- deterministic time alignment;
- at least 3 separately identifiable repeated measurements under one or more comparable conditions with absorptance and physical outcome both available at repeat level.

### `PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY`
All must hold:
- authoritative reproducible source/components;
- external material/condition independence;
- same-experiment or same-condition absorptance + physical outcome provenance is established;
- time-resolved pairing or a qualified physical outcome can be deterministically defined;
- but repeat-resolved public identity is insufficient for direct replication of D12's repeat-level claim.

### `HOLD_TIME_ALIGNMENT_OR_EVENT_IDENTITY`
Use if relevant public components exist but same-event/same-condition identity or timing relation cannot be established without inference.

### `HOLD_VERSION_OR_COMPONENT_PROVENANCE`
Use if release/component/checksum lineage cannot be frozen reproducibly.

### `REJECT_NOT_EXTERNAL_OR_NOT_PHYSICAL_PAIR`
Use if the candidate is not materially independent of BP4 or does not contain a qualified absorptance/coupling + physical-outcome relationship.

## 6. Interpretation boundary / 해석 경계

A F13 PASS/PARTIAL is a **source-readiness** result only. It does not establish that D12 descriptors generalize, that absorptance predicts geometry, or that BP4 and A-AMB measurands are numerically interchangeable.

A later experiment must separately preregister descriptor transformation, time windows, alignment, endpoints, statistics, and gates before numerical outcome access.

## 7. Cost and raw-data boundary / 비용·raw 경계

- `COST-001` + `DEC-028`: any potentially billable action requires explicit user approval before execution; unknown billing = `HOLD_COST_APPROVAL`.
- F13 uses only verified zero-incremental-cost public-source inspection.
- `RAW-001` applies if any source file is transiently retrieved; no raw-data commit or artifact upload.
