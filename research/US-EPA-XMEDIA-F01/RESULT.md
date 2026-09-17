---
id: US-EPA-XMEDIA-F01-RESULT
type: outcome-blind-cross-media-source-schema-frs-identity-feasibility
created: 2026-09-17
issue: 150
state: COMPLETED_PASS
gate: PASS_US_EPA_XMEDIA_F01_EXACT_FRS_CROSS_PROGRAM_JOIN_READY
source_run: 35166942067
staging_commit: 7a9599ae76af2e93d5806a0473ad17f6bbc1ac93
effluent_violation_rows_opened: false
dmr_outcome_rows_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-EPA-XMEDIA-F01 Result — exact FRS cross-program join-ready PASS

**`PASS_US_EPA_XMEDIA_F01_EXACT_FRS_CROSS_PROGRAM_JOIN_READY`**

Corrected immutable Run `35166942067` validly executed the pre-Issue contract frozen at `86a7a01ba3b64160ee21a7ea821536d3d1adbb14`. All **18/18** preregistered requirements passed. This is a structural source/schema/identity/time feasibility result only; it does not establish any RCRA→NPDES outcome relationship.

## Structural evidence / 구조적 근거

- RCRA evaluation rows: **200,759**; valid identity/date rows: **200,759**
- distinct RCRA `SOURCE_ID`: **90,302**; distinct RCRA `REGISTRY_ID`: **89,636**
- RCRA valid evaluation years: **1982–2026** (45 years)
- exact RCRA↔FRS corroboration: **90,196/90,196 = 100.000000%**
- FRS Program Link rows: **4,424,484**
- exact FRS RCRAInfo↔NPDES Registry-ID intersection: **60,677**
- NPDES facility rows / distinct IDs: **1,214,104 / 1,214,104**
- NPDES distinct Registry IDs: **1,029,367**
- exact NPDES↔FRS corroboration: **1,207,049/1,207,078 = 99.997598%**
- NPDES permit rows: **1,728,112**
- valid structural permit-date years after mechanical parser correction: **1900–2100**, **79** distinct years
- exact Registry IDs simultaneously supported by valid RCRA evaluation + both non-conflicting FRS program links + ICIS-NPDES Part 1 permit identity: **18,415**

## Deterministic fingerprints / 결정론적 지문

- RCRA exact identity pairs: `f40d51b00cb2ebef4e2b44b26e40d5bb77981c2f5bb8db2833c8e2eb775b3af1`
- FRS RCRAInfo exact pairs: `7ef51065e6366cd1b7eb3f1d0498e5650b6caede08fb7965833dbf8d32cd71db`
- FRS NPDES exact pairs: `856b1938a812f83c5f733806f237867090f7a510624290a11d201c1258900a69`
- NPDES Part 1 exact identity pairs: `ab55a67210f83c58d271924ed8afa99daaf32252c52c18fce573c70aa5ce79b1`
- FRS cross-program Registry intersection: `3355572a1b5e91c8f9227a0859f0a78b87d5633cd811d801798ab47c0b8d1a2c`
- fully cross-supported Registry IDs: `0b17a285f863e55340413416a05d37615af8bb6da02827c60fb3c57dde497c4e`

## Implementation correction / 구현 보정

The first immutable staging result is preserved. Review detected that its fallback date parser could admit malformed/out-of-range calendar years. The corrected rerun changed **only** that parser boundary to valid years `1900–2100`; the frozen contract, source set, thresholds, identity rules and outcome firewall were unchanged. The corrected run remained **18/18 PASS**, and all identity counts/fingerprints remained unchanged.

## Outcome-blind boundary / 결과 비개봉 경계

- ICIS-NPDES Part 2 / effluent-violation rows: **not opened**;
- DMR reported values, limits or exceedance rows: **not opened**;
- name/address/geospatial/fuzzy/manual/post-outcome identity repair: **not used**;
- RCRA-conditioned NPDES outcome occurrence/rate/magnitude: **not computed**;
- relationship/prediction/causality: **not computed or claimed**;
- incremental monetary cost: **0 USD**.

## Interpretation / 해석

The official EPA RCRA Pipeline, FRS and ICIS-NPDES Part 1 sources provide a large, exact, source-native cross-program identity surface suitable for a separately preregistered outcome-blind design gate. F01 alone does not authorize opening downstream effluent outcomes.

## Exact next action / 정확한 다음 행동

Freeze a separate `US-EPA-XMEDIA-N01` design-identifiability contract before Issue binding and before any Part 2/DMR outcome access. N01 must prospectively define the RCRA structural exposure, facility eligibility, time ordering, matching/stratification, missingness rules and the exact later E01 outcome/statistical contract.
