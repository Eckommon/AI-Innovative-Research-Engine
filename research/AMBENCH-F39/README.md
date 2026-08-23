---
id: AMBENCH-F39
type: added-value-falsification-design-gate
state: PREREGISTERED_ACTIVE
created: 2026-08-23
source_of_truth: github
incremental_monetary_cost_usd: 0
---

# AMBENCH-F39 — Multi-Actuator Added-Value Falsification Design Gate
# AMBENCH-F39 — Multi-Actuator Added-Value 반증 설계 Gate

## Purpose / 목적

Determine whether `HYP-F37-01` can be tested as a **non-trivial engineering addition** over strong known history-aware controls before any prototype expenditure.

The target is not “beat constant parameters.” The target is:

> Does one shared recent-scan-history state coordinating power + timing + local path/order provide material incremental benefit over the strongest known single/two-actuator history-aware comparator under matched productivity/energy constraints?

## Frozen comparator ladder / 고정 비교군

C0 — constant/fixed process parameters.  
C1 — history-state power-only (`RHF/GCF-like`).  
C2 — thermal/history-state power + timing/dwell.  
C3 — thermal-history-state path/order-only.  
C4 — joint shared-state `{power + timing + local path/order}`.

C4 is the candidate; C2 is the primary strong comparator because F38 established thermal-model-driven power+dwell as prior art.

## Shared state requirement / 공통 state 조건

A valid F39 design must use one common, frozen state representation across C1–C4. Candidate families may include RHF-like recent-event state or a path-level thermal-state estimator, but the state definition must not change by controller after outcomes.

## Matched constraints / 동일 제약

Any executable design must constrain or report:
- identical geometry/material/source case;
- identical nominal laser/scan process envelope;
- total build or scan time / productivity budget;
- integrated or average energy input;
- allowed actuator bounds;
- no controller-specific access to extra outcome information.

A slower controller may not claim superiority solely by adding unconstrained cooling time.

## Primary outcome family / 1차 outcome군

Prefer directly physical, low-DOF stability endpoints available from authoritative source/simulation:
1. melt-pool area/width variability or deviation from target;
2. peak/local temperature or thermal-uniformity error;
3. secondary productivity penalty.

No high-capacity surrogate/ML search is allowed until a low-DOF controller comparison is executable.

## Frozen design gates / 고정 설계 판정

### `PASS_F39_EXECUTABLE_ADDED_VALUE_TEST_READY`
All must hold:
1. one zero-cost or already-owned executable thermal/process environment is identified;
2. the same case can run C0–C4 without unsupported source substitution;
3. one common history-state representation can feed C1–C4;
4. power, timing and path/order are all controllable in the environment;
5. matched productivity/energy constraints can be enforced;
6. physical/thermal endpoints can be computed without pseudo-replication;
7. C4 can be evaluated against C2 as the primary incremental comparator.

### `PARTIAL_F39_TWO_ACTUATOR_OR_PATH_ONLY_ENVIRONMENT`
A rigorous C0–C3 comparison is executable but the same environment cannot jointly manipulate all three actuator classes.

### `HOLD_F39_NO_COMPARABLE_EXECUTION_ENVIRONMENT`
No zero-cost source/model/runtime can support comparable controlled execution without inventing a simulator or materially changing source semantics.

### `REJECT_F39_INCREMENTAL_TEST_NOT_IDENTIFIABLE`
The candidate C4 cannot be separated from the known comparator under any defensible frozen design.

## Allowed source search / 허용 source 탐색

Source/design qualification may inspect open papers, open-source simulators, NIST/public models and existing repository capabilities. Do not adopt paid cloud, paid solver licenses, paid patent tools or new hardware.

## Capability boundary / capability 경계

If a reusable controller-evaluation harness becomes justified through actual use, classify first as `SHARED-INTERNAL-CANDIDATE`. Do not create/promote a Skill/MCP/Plugin during F39.
