---
id: US-MINE-F01
issue: 134
state: AUTHORIZED_OUTCOME_BLIND_FEASIBILITY
created: 2026-09-16
support_window: 2019-2025
injury_outcome_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-MINE-F01 — Outcome-blind mine-quarter operational-stress × injury feasibility

## Objective
Prove a deterministic, zero-cost MSHA mine-quarter structural route between operator employment/production reporting and accident/injury record identity **without opening injury outcome magnitudes or computing any relationship**.

## Frozen official sources
1. MSHA Open Government `Mines.zip` and `Mines_Definition_File.txt`.
2. MSHA Open Government `MinesProdQuarterly.zip` and `MineSProdQuarterly_Definition_File.txt`.
3. MSHA Open Government `Accidents.zip` and `Accidents_Definition_File.txt`.
4. MSHA Part 50 documentation only for source/update semantics.

Official source family:
- https://arlweb.msha.gov/OpenGovernmentData/OGIMSHA.asp
- https://arlweb.msha.gov/STATS/PART50/p50y2k/p50y2k.HTM

Raw source bytes are transient under RAW-001. Durable evidence may retain only hashes, member names/hashes, schemas and structural support diagnostics.

## Frozen support window
Calendar years **2019–2025 inclusive**. 2026 is excluded as a partial publication year. The window may not change after accident structural data are read.

## Frozen identities
- mine: exact `MINE_ID`; no fuzzy mine-name repair;
- employment key: `(MINE_ID, CAL_YR, CAL_QTR, SUBUNIT_CD)`;
- accident join key: `(MINE_ID, CAL_YR, CAL_QTR, SUBUNIT_CD)`;
- accident record identity: `DOCUMENT_NO`;
- sector: `COAL_METAL_IND`;
- operator/contractor split: `CONTRACTOR_ID` blank/nonblank only.

## Prohibited fields / values
F01 must not access or use injury degree, days lost/restricted, number of injuries, injury classification/type/source/nature/body-part, severity, incidence rate or any linked injury magnitude. It must not compute production-per-hour or any exposure→injury association.

Structural accident record counts and exact key-overlap counts are allowed only for source/cardinality/identifiability gating.

## Frozen reporting-semantic boundary
MSHA states that Metal/Nonmetal operators are not required to report production. Therefore F01 may **not** promote a national Coal+MNM production-pressure exposure. A PASS can establish structural join readiness while preserving `PRODUCTION_SCOPE_RESTRICTED`. Any later exposure family requires separate outcome-blind N01 authorization.

## Frozen PASS requirements
1. All three ZIPs and definition files accessible at 0 USD; source and member SHA-256 recorded.
2. Mines exposes `MINE_ID`, `COAL_METAL_IND`, `STATE`; `MINE_ID` unique.
3. Quarterly operator employment exposes `MINE_ID`, `SUBUNIT_CD`, `CAL_YR`, `CAL_QTR`, `HOURS_WORKED`, `COAL_PRODUCTION`, `COAL_METAL_IND`.
4. Accidents exposes `MINE_ID`, `DOCUMENT_NO`, `SUBUNIT_CD`, `CAL_YR`, `CAL_QTR`, `CONTRACTOR_ID`, `COAL_METAL_IND`; prohibited outcome fields remain unaccessed.
5. No conflicting duplicate employment key in 2019–2025.
6. >=3,000 distinct operator mine IDs have employment records and >=2 distinct calendar quarters in the window.
7. Both `C` and `M` sectors present; `HOURS_WORKED` nonblank support >=95% of retained quarterly rows in each sector, without parsing hour magnitude.
8. Among valid operator-attributed accident structural keys, >=80% have exact employment-key overlap in the same window.
9. Overlapping mine IDs span >=30 states via Mines `STATE`.
10. No fuzzy repair, outcome-driven eligibility choice, paid source or prohibited outcome access.

## Frozen dispositions
- `PASS_US_MINE_F01_STRUCTURAL_JOIN_READY__PRODUCTION_SCOPE_RESTRICTED`
- `PARTIAL_US_MINE_F01_IDENTITY_READY__JOIN_OR_HOURS_SUPPORT_PENDING`
- `HOLD_US_MINE_F01_SOURCE_OR_IDENTITY_SUPPORT`

No threshold/source/window rescue after execution.

## If PASS
A later N01 must choose exactly one exposure family from source semantics/support before any injury values are opened. It must separately freeze sector scope, contractor handling, subunit aggregation, denominator, timing/lag, repeated-quarter eligibility, comparator/estimand, minimum support, materiality and non-causal claim boundaries.

Incremental monetary cost: **0 USD**.
