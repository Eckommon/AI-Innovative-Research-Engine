---
id: PORTFOLIO-R57-RESULT
created: 2026-10-16
issue: 214
status: COMPLETED_SELECTED_STRUCTURAL_F01_ONLY
contract: 602c33b6f53c6ae180408fa43ac88a90a6ff7c50
source_revalidation_commit: 7bea90e35bb1a81218821f63e80da51726e66239
scorecard_commit: 334a2c127a899dea5093b0203b1edd2c1cbcd614
selection: SELECT_US_FAA_AIR_003_COMPOUND_AIRCRAFT_IDENTITY_TO_FUTURE_DEREGISTRATION_F01
candidate_future_event_rows_opened: false
incremental_monetary_cost_usd: 0
---

# R57 — Independent parallel Stage-0 result / 병렬 독립 선별 최종 결과

**SELECT_US_FAA_AIR_003_COMPOUND_AIRCRAFT_IDENTITY_TO_FUTURE_DEREGISTRATION_F01**

| Frozen candidate | /45 | Stage-0 decision / 판정 |
|---|---:|---|
| FAA aircraft registration ↔ deregistration | **37** | **SELECT ONE STRUCTURAL F01 PROSPECT** |
| NHTSA vehicle-product ↔ future recalls | 31 | HOLD_UNPROVEN_EXACT_PRODUCT_AT_RISK_DENOMINATOR |
| FDA device listings ↔ device recall/enforcement | 25 | HOLD_UNPROVEN_DEVICE_ESTABLISHMENT_TO_RECALL_KEY |

**Interpretation / 해석:** FAA is the strongest prospect for a new, strictly independently preregistered F01 structural test because official daily full exports contain Master, Deregistered and manufacturer/model references. This is not proof that aircraft can be uniquely joined over time. The historical F01 outcome remains unknown; N-number alone is insufficient, and exact serial+manufacturer/model cardinality, event date, registration reuse and revision lineage must pass a separate **pre-outcome** gate.

**Traceability / 계보:** Candidate universe/rubric frozen before Issue #214, then independent first-party source and historical terminal equivalence review, then one frozen /45 scorecard, **then** this result. The two held candidates are not eligible for automatic runner-up promotion if FAA fails. Prior FAA-AIP airport grant/delay F01 was a materially different data/unit/event route; it remains terminal with its original HOLD.

**Next authorized scope:** Open exactly one separate `US-FAA-AIR-F01` scientific **structural preflight** after freezing its F01 contract in Git before its Issue. The F01 test must be outcome-blind and can return HOLD without downstream N01/E01. It must not compute existing/current deregistration rates by exposure, future deregistration membership, prediction, ranking or causality. The public downloadable ZIP is approximately 60MB; no binary was fetched during this Stage 0.

**Canonical dual-track boundary / 정본 분리:** `US-CMS-NPI-E01` stays the one canonical active research checkpoint / Issue #203; FAA F01 is an expressly authorized **parallel secondary research track**, not a state replacement.

**Cost / 비용:** 0 USD. No paid host, API, ZIP probe or data execution was performed in R57.
