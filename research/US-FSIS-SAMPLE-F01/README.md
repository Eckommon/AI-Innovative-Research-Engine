---
id: US-FSIS-SAMPLE-F01
type: preregistered-outcome-blind-feasibility
created: 2026-09-17
parent: PORTFOLIO-R37
parent_decision: DEC-227
status: CONTRACT_FROZEN_PRE_ISSUE
candidate_future_recall_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-FSIS-SAMPLE-F01 — outcome-blind exact establishment identity and longitudinal sampling feasibility

## Mission / 목적

Determine whether official FSIS establishment-specific **Raw Poultry Sampling** data and the official Meat, Poultry and Egg Product Inspection Directory support a deterministic, longitudinal establishment-level exposure universe that could later be linked to a separately preregistered recall/public-health-alert outcome using official establishment-number semantics only.

F01 is structural only. It must not open candidate future recall membership, calculate sampling→recall relationships, rank establishments, estimate recall probability, or claim causality/novelty.

## Frozen exposure window / 고정 노출기간

Use only official Raw Poultry Sampling fiscal-year data for **FY2021, FY2022 and FY2023**.

These years are fixed before row-level access in this branch. They may not be broadened or shifted after support counts are observed.

## Frozen identity rule / 고정 식별 규칙

Canonical establishment identity is the **official FSIS establishment-number field present in the sampling data and official MPI Directory**.

Allowed normalization is deliberately minimal:

1. convert to string;
2. trim leading/trailing whitespace;
3. uppercase ASCII letters;
4. remove internal ASCII spaces only when the source documentation or both official source headers explicitly establish the same establishment-number representation.

Not allowed:

- establishment-name matching;
- address/city/state matching;
- geospatial proximity;
- fuzzy/edit-distance matching;
- manual lookup or hand repair;
- dropping regulatory prefixes or extracting only a numeric core unless official FSIS documentation explicitly defines that equivalence before empirical support counts are inspected;
- using a corporate/parent identity as a substitute for establishment identity.

If exact source-native identity cannot be established under these rules, F01 must HOLD.

## Candidate future outcome firewall / 미래 결과 방화벽

The candidate later outcome family is FSIS recall/public-health-alert activity in **2024-01-01 through 2025-12-31**.

During F01:

- recall/public-health-alert individual notice rows must not be downloaded, enumerated, parsed or opened;
- establishment membership in any 2024–2025 recall/public-health-alert must remain unknown;
- recall reason, class, pounds, pathogen, dates, product or establishment values must remain unopened;
- annual recall-summary pages may be accessed only to establish page/source availability and documentation/schema labels, not row values;
- FSIS recall guidance may be read to establish official establishment-number semantics.

A PASS authorizes only a separate outcome-blind N01 design. It does not authorize E01.

## Frozen official source families

1. FSIS Laboratory Sampling Data — Raw Poultry Sampling
   - `https://www.fsis.usda.gov/science-data/data-sets-visualizations/laboratory-sampling-data`
   - `https://catalog.data.gov/dataset/fsis-laboratory-sampling-data-raw-poultry-sampling`
2. FSIS Meat, Poultry and Egg Product Inspection Directory / Establishment Demographic Data
   - `https://www.fsis.usda.gov/inspection/establishments/meat-poultry-and-egg-product-inspection-directory`
3. FSIS recall guidance / source-family availability only
   - `https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/understanding-fsis-food-recalls`
   - `https://www.fsis.usda.gov/food-safety/recalls-public-health-alerts/annual-recall-summaries`

No paid API, commercial data, private PHIS access, FOIA-only source, or third-party mirror is authorized.

## Frozen PASS/HOLD gate

All **18** requirements must pass for:

`PASS_US_FSIS_SAMPLE_F01_EXACT_ESTABLISHMENT_LONGITUDINAL_JOIN_READY`

Otherwise any valid scientific execution terminates as:

`HOLD_US_FSIS_SAMPLE_F01_EXACT_ESTABLISHMENT_LONGITUDINAL_JOIN_NOT_READY`

Implementation/network/parser defects are not scientific HOLD and may be transparently corrected without changing this contract.

### Requirements

1. Official FSIS Raw Poultry Sampling source is publicly machine-readable at zero incremental cost.
2. Dataset documentation/metadata establishes fiscal-year partitioning and field semantics before support counts are evaluated.
3. FY2021, FY2022 and FY2023 source partitions are all reproducibly accessible and fingerprintable.
4. A source-native establishment-number field is present in all three exposure partitions.
5. Sampling-date or fiscal-year semantics are present and sufficient to assign rows to the frozen exposure years without inference from filenames alone.
6. Official MPI Directory machine-readable data are reproducibly accessible and fingerprintable.
7. MPI Directory exposes an official establishment-number field suitable for exact source-native linkage.
8. FSIS recall guidance/source documentation establishes that establishment numbers are part of recall identification when available, without opening candidate 2024–2025 recall rows.
9. No candidate 2024–2025 recall/public-health-alert membership or row value is opened.
10. No fuzzy/name/address/geospatial/manual identity repair is used.
11. After exact duplicate collapse and identity-conflict exclusion, **>=150 distinct sampled establishments** remain across FY2021–FY2023.
12. **>=100 distinct establishments** have sampling records in at least **2** of the 3 frozen fiscal years.
13. **>=50 distinct establishments** have sampling records in all **3** frozen fiscal years.
14. **>=95%** of otherwise structurally usable sampling rows carry a nonblank valid official establishment number under the frozen normalization rule.
15. **>=90%** of distinct sampled establishment identities link exactly to the official MPI Directory under the frozen normalization rule.
16. Among linked establishments, **>=99%** map to exactly one canonical MPI establishment record after exact duplicate collapse; ambiguous mappings are excluded, not repaired.
17. Deterministic source fingerprints, schema/header manifest, exclusion counts and an exposure-only establishment-year manifest are persisted; no pathogen→recall relationship/prediction/ranking/causal/novelty statistic is computed.
18. Incremental monetary cost is exactly **0 USD**.

## Exposure-only manifest boundary

If F01 executes, the durable exposure manifest may contain only structural fields needed to prove feasibility, such as:

- canonical establishment number;
- fiscal year;
- sampling-row count per establishment-year;
- documented product/sampling-program family if structurally required;
- MPI exact-link status;
- deterministic source fingerprint lineage.

It must not contain candidate future recall membership or derived recall labels.

## Interpretation boundary

A PASS would establish only that an exact, longitudinal FSIS establishment sampling universe is structurally ready for a separately preregistered next-stage design.

A HOLD is terminal for this frozen F01. Thresholds, years and normalization rules may not be loosened after observing support.

Incremental monetary cost: **0 USD**.
