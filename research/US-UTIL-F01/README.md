---
id: US-UTIL-F01
issue: 94
state: COMPLETED_JOIN_READY
mission_anchor: MEM-054
decision: DEC-130
outcome_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F01 — EIA-861 Utility AMI/Reliability/Service Territory × NOAA Storm Events
# US-UTIL-F01 — EIA-861 유틸리티 AMI/신뢰도/서비스영역 × NOAA Storm Events

## Objective / 목적

Qualify a nationwide, many-to-many utility-year join before any effect calculation. / 효과계산 전 전국 utility-year 결합의 source·identity·cardinality를 검증한다.

## Frozen source snapshot / 고정 source snapshot

- EIA Form EIA-861 **2024 final data** ZIP.
- EIA schedules required: Reliability, Advanced Metering, Service Territory and utility identity/frame support.
- NOAA/NCEI Storm Events **2024** annual bulk details/location source family.
- EIA 2025 early release is excluded from this first gate.

## Outcome-blind rules / 결과 비사용 규칙

- EIA identifiers only; no fuzzy utility-name matching.
- Preserve utility↔county many-to-many mapping.
- A county shared by multiple utilities is shared exposure, not independent replication.
- Do not invent county customer weights.
- Do not read, rank or summarize SAIDI/SAIFI magnitudes in F01.
- Do not estimate AMI effects or storm effects.
- Raw ZIP/GZ/XLSX/CSV bytes remain transient under RAW-001.

## Frozen initial structural gate / 고정 초기 구조 gate

Require all for source-side structural PASS:
- >=300 reliability-reporting utility identities with deterministic Service Territory joins;
- >=250 of those utilities with an Advanced Metering record/support route;
- >=1,000 unique qualified utility×county mappings;
- reproducible NOAA 2024 county-key route for Storm Events;
- no paid data/API/compute.

These thresholds qualify structure only; they do not imply a useful or novel AMI-resilience relationship.

## Final disposition / 최종 처분

**`PASS_US_UTIL_F01_JOIN_READY`**

Verified: **842** completely county-qualified reliability utilities with AMI support and **6,341** qualified utility×county mappings under the deterministic Census GEOID→NOAA FIPS route. No reliability/AMI magnitude or relationship was opened. / 결과값 비사용 JOIN_READY다.

## Exact next action / 정확한 다음 행동

Return to **Stage 0 portfolio control**. Do not automatically fit an AMI × storm × reliability model. Any relationship descendant requires separate portfolio selection and preregistration. / Stage 0로 복귀하며 효과실험 자동진입을 금지한다.
