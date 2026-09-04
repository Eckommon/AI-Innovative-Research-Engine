---
id: CA-RAIL-F01-OUTCOME-ADJUDICATION
type: outcome-blind-source-dimension-adjudication
created: 2026-09-04
issue: 83
relationship_outcome_computed: false
weather_values_opened: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-F01 Outcome-Dimension Adjudication
# CA-RAIL-F01 결과 차원 사전 판정

## Problem / 문제

Transport Canada's source-defined measure:

**Average Terminal Dwell Time - Loaded Cars and Intermodal Containers**

does not expose one all-commodity terminal-total row for CN/CPKC.

For CN/CPKC, the measure is published separately by commodity. BNSF uses a different combined-car-type / commodity-not-applicable contract.

Therefore F01 must not average or sum commodity rows to manufacture a terminal-level outcome.

## Prospective primary stratum / 사전 고정 primary stratum

Freeze for the first simple descendant:

- Carrier: **CN or CPKC**
- Measure: **Average Terminal Dwell Time - Loaded Cars and Intermodal Containers**
- Commodity: **Intermodal containers**
- Car_Type: **Not Applicable**
- Dwell_Time_Range: **Not Applicable**
- Fleet_Status: **Not Applicable**
- Employee_Type: **Not Applicable**
- Segment_Distance_km: **0.0**
- Unit_of_Measure: **Hours**
- Status_of_Value: **0 - Available**

BNSF is excluded from the primary simple route because its source dimension contract is not the same as CN/CPKC.

## Why Intermodal containers / 왜 Intermodal containers인가

This choice is frozen before any weather value or rail-weather relationship is opened.

Reasons:
1. it is an explicit source-defined commodity stratum, not a synthetic aggregation;
2. it is directly relevant to general freight/logistics reliability rather than one seasonal bulk commodity;
3. it is broadly represented across CN and CPKC terminal-area records;
4. it avoids arbitrary weighting across heterogeneous commodity strata;
5. it preserves a simple independent candidate unit: carrier × terminal area × reference week.

The choice is not based on observed weather sensitivity.

## Frozen candidate period / 고정 후보 기간

Primary support qualification will test complete calendar years:

**2024-01-01 through 2025-12-31**

Reasons:
- 2023 begins after the April 2023 reporting change and is not a full year;
- 2026 is incomplete at the current snapshot;
- 2024–2025 are the two complete calendar years in the frozen Transport Canada ZIP.

The rail source remains labelled preliminary/currently revisable. The descendant must describe this as a frozen preliminary snapshot, not final historical truth.

## Structural gate / 구조 gate

Before any weather value:
- require one unique source row per `Reference_Date × Carrier × Geography` under the frozen stratum;
- require no duplicate structural key;
- report missing source weeks rather than imputing;
- require a nontrivial multi-terminal universe;
- do not restore BNSF or alternate commodity strata after outcomes.

## Spatial bridge / 공간 bridge

Terminal-place identity must be established prospectively:
1. parse place token from `<carrier> terminal area, <place>`;
2. normalize Unicode accents only for exact linguistic equivalence (e.g. Montreal ↔ Montréal);
3. require exactly one CGNDB result with Generic Term = `City` and Status = `Official`;
4. use only that official place detail/coordinates;
5. map to an eligible ECCC station using a distance/availability rule frozen before weather outcomes.

No fuzzy geocoder or manual city substitution is allowed.

Incremental monetary cost remains **0 USD**.
