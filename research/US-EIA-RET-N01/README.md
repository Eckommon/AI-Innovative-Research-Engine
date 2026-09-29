---
id: US-EIA-RET-N01
type: outcome-blind-prospective-design
created: 2026-09-30
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-EIA-RET-F01
parent_decision: DEC-280
parent_evidence_commit: d96ccc4346484cb39f719f98eeaca75b142d1301
future_retirement_membership_opened: false
post_august_2026_860m_body_opened: false
planned_retirement_used_as_exposure: false
eia923_row_bodies_opened: 0
incremental_monetary_cost_usd: 0
---

# US-EIA-RET-N01 — same-configuration redundancy prospective cohort lock

## Mission / 목적

Before opening any post-August-2026 retirement membership, determine whether the August-2026 EIA-860M Operating population can support a balanced prospective comparison of generator-level **same-configuration redundancy**.

The hypothesis is deliberately two-sided:

> For otherwise comparable generators, future retirement incidence may differ between generators embedded in a plant with at least three simultaneously operable generators of the same technology/fuel/prime-mover configuration and generators at pure-singleton plants.

N01 does not assume which direction the difference should take and computes no retirement outcome.

## Parent authority / 상위 권한

`US-EIA-RET-F01` passed 18/18 under `DEC-280`.

Canonical F01 evidence:
- Attempt 02 commit: `d96ccc4346484cb39f719f98eeaca75b142d1301`
- August-2026 Operating exact pairs: 28,377
- 12-month continuity: 97.8151%
- future retirement membership opened: false

The older R36 `US-EIA-GEN-F01` remains unrelated and terminal.

## Frozen baseline source / 고정 baseline

N01 must use the **same exact twelve EIA-860M workbook bodies fingerprinted in F01 Attempt 02**, September 2025 through August 2026.

Every re-downloaded workbook SHA-256 must exactly equal the F01 Attempt 02 fingerprint. Any changed body is source-version drift and fails the baseline-integrity gate; N01 may not silently accept a revised workbook.

Only the exact main `Operating` sheet row bodies may be used in N01.

Prohibited row bodies:
- Planned / Planned_PR
- Retired / Retired_PR
- Canceled or Postponed
- EIA-923 data
- September-2026-or-later EIA-860M

## Frozen generator identity / 고정 식별자

Exact identity remains the F01 pair:

> **(Plant ID, Generator ID)**

No name, owner, address, location, geography, Entity ID or fuzzy/manual identity repair.

## Frozen baseline eligibility / baseline 적격성

A generator enters the N01 candidate pool only if all conditions are satisfied:

1. present in the exact August-2026 main `Operating` sheet;
2. exact Plant ID + Generator ID is valid under F01 normalization;
3. appears in the main `Operating` sheet in at least **6 of the 12** frozen baseline months;
4. nonblank source-native:
   - Plant State
   - Sector
   - Technology
   - Energy Source Code
   - Prime Mover Code
   - Status
5. positive finite Nameplate Capacity (MW);
6. parseable Operating Month and Operating Year yielding a nonnegative operating age as of August 2026.

No planned-retirement value is used in eligibility, exposure, matching or covariates.

## Frozen exposure / 고정 노출

For every eligible August-2026 generator, define its configuration group:

> `(Plant ID, Technology, Energy Source Code, Prime Mover Code)`

using only eligible August-2026 Operating rows.

### Exposed — `REDUNDANT_3PLUS`

The generator's configuration group contains **at least 3** eligible August-2026 generators.

### Control — `PURE_SINGLETON`

The generator's configuration group size is exactly **1**, and **every** eligible configuration group at that Plant ID has size exactly 1.

This plant-purity rule prevents one plant from simultaneously contributing generators to both study arms.

### Excluded

- configuration-group size exactly 2;
- singleton group at a plant that also contains any group of size ≥2;
- invalid/missing matching covariates.

The exposure uses no future, retired, planned-retirement, generation-performance or compliance information.

## Frozen matching covariates / 고정 matching 변수

For each eligible generator calculate:

- operating age in complete years as of August 2026;
- age band:
  - 0–9
  - 10–19
  - 20–29
  - 30–39
  - 40–59
  - 60+
- natural log of Nameplate Capacity MW.

### Exact matching stratum

Match only within exact:

> `Technology × Energy Source Code × Prime Mover Code × Plant State × Sector × Status × age band`

### Continuous calipers

For an exposed-control candidate pair:

- absolute age difference ≤ **8 years**;
- capacity ratio must be between **2/3 and 1.5** inclusive.

### Deterministic 1:1 no-replacement algorithm

1. sort exposed units by exact stratum, operating age, log capacity, Plant ID, Generator ID;
2. among unused controls in the same exact stratum satisfying both calipers, choose the minimum:
   `age_difference / 8 + |log(capacity_exposed / capacity_control)| / log(1.5)`;
3. ties resolve by control Plant ID then Generator ID;
4. each control may be used once.

No rematching, caliper expansion, propensity tuning or post-hoc stratum merging is permitted after results are observed.

## Frozen balance metrics / 균형 지표

Continuous standardized mean differences use the pooled standard deviation of matched exposed/control values.

Required:
- `|SMD(log capacity)| ≤ 0.10`
- `|SMD(operating age)| ≤ 0.10`

Exact categorical covariates must match pairwise by construction.

Cluster concentration:
- calculate matched-generator share for every Plant ID within each arm;
- maximum single-plant share in each arm must be ≤ **2.00%**.

## Frozen future retirement event / 미래 은퇴 사건

N01 opens **no** future file.

If N01 passes, a separately preregistered E01 may define the primary event window as:

> retirement year-month from **September 2026 through August 2027 inclusive**

A future generator retirement may count only if:
1. baseline generator is in the locked matched cohort;
2. exact Plant ID + Generator ID first appears in an official post-August-2026 main Retired inventory;
3. source-native retirement year-month is within the event window;
4. the same exact retired pair and retirement year-month persists in the immediately following monthly inventory.

A September-2027 file may be used only to confirm an August-2027 event.

Disappearance from Operating without a qualifying Retired record is **not** retirement. No name-based continuity repair is allowed.

## EIA-923 boundary / EIA-923 경계

The primary N01 design uses **no EIA-923 row data**. EIA-923 performance-based hypotheses are deferred to a separately preregistered descendant and may not be added after observing this N01 cohort.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical checkpoint is `CHK-20260930-US-EIA-RET-F01-TERMINAL`; last decision `DEC-280`; F01 terminal gate is PASS |
| 2 | Issue binding | runner executes only after a new Issue is bound to this exact pre-Issue contract commit |
| 3 | Baseline fingerprint integrity | all 12 re-downloaded workbook SHA-256 values equal F01 Attempt 02 exactly |
| 4 | August matching schema | exact main Operating sheet contains all frozen identity/exposure/matching concepts |
| 5 | Stable baseline support | ≥ **90.00%** of August exact Operating pairs satisfy the ≥6/12-month continuity condition |
| 6 | Eligible cohort | ≥ **15,000** generators satisfy all frozen eligibility rules |
| 7 | Arm support | `REDUNDANT_3PLUS ≥ 3,000` and `PURE_SINGLETON ≥ 3,000` |
| 8 | Common exact strata | ≥ **50** exact strata contain at least one exposed and one control candidate |
| 9 | Deterministic matching integrity | 1:1 without replacement, all matched pairs satisfy exact strata + both calipers, duplicate control use = 0 |
| 10 | Matched cohort size | ≥ **2,000** matched pairs |
| 11 | Exposed match coverage | matched exposed / eligible exposed ≥ **40.00%** |
| 12 | Exposed plant support | matched exposed arm contains ≥ **300** distinct Plant IDs |
| 13 | Control plant support | matched control arm contains ≥ **300** distinct Plant IDs |
| 14 | Cross-arm plant separation | Plant IDs appearing in both matched arms = **0** |
| 15 | Capacity balance | `|SMD(log capacity)| ≤ 0.10` |
| 16 | Age balance | `|SMD(operating age)| ≤ 0.10` |
| 17 | Exact-category / concentration / outcome firewall | pairwise exact categorical mismatch = 0; max single-plant share in each arm ≤ 2.00%; planned-retirement exposure used = false; EIA-923 rows = 0; post-August files = 0; future retirement membership = false; relationship/prediction/ranking/causal metric = false; identity repair = false |
| 18 | Reproducibility/cost | immutable evidence records contract/F01 evidence SHA, all source fingerprints, eligibility/exposure/matching counts, strata, balance, deterministic matched-manifest SHA, runner SHA and cost = 0 USD |

## Frozen terminal rule / 종결 규칙

PASS:

`PASS_US_EIA_RET_N01_REDUNDANCY_MATCHED_COHORT_LOCKED`

Any valid failure:

`HOLD_US_EIA_RET_N01_REDUNDANCY_MATCHED_COHORT_NOT_READY`

A valid HOLD is terminal for this N01. Do not change:
- group-size cutoffs;
- pure-singleton rule;
- matching variables;
- age bands;
- calipers;
- thresholds;
- baseline months;
- source version;
- exposure definition

after observing N01 results.

Implementation/parser defects may be corrected only if all scientific criteria remain unchanged and prior attempts remain immutable.

## PASS consequence / PASS 이후

PASS authorizes only a **separately preregistered, still outcome-sealed E01 protocol**. Before E01 opens the first post-August file, it must freeze:
- primary estimand and statistical test;
- plant-cluster treatment;
- minimum confirmed retirement events;
- handling of unresolved disappearance and source revisions;
- materiality/significance gates.

N01 PASS alone does not authorize opening future retirement rows.

## Non-claims / 비주장

N01 makes no claim that redundancy increases or decreases retirement. It does not rank generators, plants, owners or technologies and does not recommend retirement, investment, dispatch, reliability or policy decisions.

Incremental monetary cost must remain **0 USD**.
