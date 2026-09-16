---
id: C-EU-F01
issue: 139
state: AUTHORIZED_OUTCOME_BLIND_FEASIBILITY
portfolio_decision: DEC-190
contract_decision: DEC-191
hazard_family: ERA5_LAND_2M_TEMPERATURE
industrial_outcomes_opened: false
temperature_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# C-EU-F01 — EEA industrial-site × ERA5-Land 2m-temperature source/access/identity feasibility

## Objective / 목적

Test whether a reproducible zero-cost exact-site → official ERA5-Land grid identity can be established **before any industrial outcome or site temperature magnitude is opened**. / 산업 outcome이나 site 온도값을 열기 전에 exact industrial-site → ERA5-Land grid identity가 재현 가능하게 성립하는지 검증한다.

## Frozen industrial source / 고정 산업 source

Primary route: EEA Discomap `Air/IED_SiteMap/MapServer/0`, feature layer `ied_SiteMap`.

Allowed fields only:
- `OBJECTID` for transport/pagination;
- `InspireSiteId` exact site identity;
- `siteName` diagnostic label only;
- `countryCode`;
- `x_4258`, `y_4258` coordinate diagnostics;
- `Site_reporting_year` support metadata;
- geometry only if needed to verify point geometry/coordinate route.

No pollutant, release, waste, fuel, operating-hour, energy, production or other thematic/outcome field may be used to select, filter, rank or compare sites.

## Frozen hazard family / 고정 hazard family

Exactly one family: **ERA5-Land `2m temperature`**.

F01 may verify only semantic/access/grid metadata: variable identity, units K, hourly resolution, 1950-present, 0.1° regular latitude-longitude point time-series/grid semantics, nearest-grid behavior and official access/authentication requirements. No site temperature magnitude may be persisted or summarized.

## Frozen identity / grid rules

- site key = exact nonblank `InspireSiteId` only; no fuzzy site-name repair;
- valid coordinates = finite `x_4258` in [-180,180] and `y_4258` in [-90,90];
- duplicate site ID is non-conflicting only when all valid coordinate pairs are identical after decimal parsing;
- invalid coordinates are excluded, never imputed;
- country coverage uses exact `countryCode` only;
- authoritative ERA5 coordinate arrays/grid endpoint convention must come from an official route before point→grid fingerprinting;
- nearest official ERA5 latitude/longitude coordinate is used; exact half-distance ties resolve to the lower array index after coordinate ordering is known;
- do not infer the grid origin from 0.1° alone.

## Frozen PASS requirements / 고정 PASS 요건

1. EEA layer metadata/query route accessible at 0 USD and metadata hash persisted.
2. Required identity/coordinate fields present and layer point geometry confirmed.
3. >=10,000 distinct exact nonblank `InspireSiteId` identities.
4. >=95% of distinct site identities have at least one valid non-conflicting coordinate pair.
5. >=25 country codes among coordinate-qualified sites.
6. conflicting duplicate exact site identities = 0.
7. official ERA5-Land metadata confirms 2m temperature, K, hourly, 1950-present and 0.1° point/grid semantics.
8. actual zero-cost programmatic official climate route is executable from the runner and yields authoritative coordinate-array/grid metadata without auth bypass.
9. deterministic grid identities can be frozen for >=95% of coordinate-qualified sites and fingerprinted before industrial outcome access.
10. no industrial outcome/thematic magnitude or site temperature magnitude opened/persisted, no relationship computed, cost=0.

## Frozen dispositions / 고정 판정

- `PASS_C_EU_F01_SITE_HEAT_JOIN_READY`
- `PARTIAL_C_EU_F01_SITE_IDENTITY_READY__CDS_CREDENTIAL_REQUIRED`
- `HOLD_C_EU_F01_SOURCE_OR_IDENTITY`

PARTIAL is allowed only when requirements 1–7 and 10 pass and the sole blocker for 8–9 is the official free CDS credential requirement unavailable to the runner. No mirror, unofficial source or authentication bypass may be substituted.

## Claim boundary / 주장 경계

PASS/PARTIAL establishes only public-data source/access/identity readiness. It establishes no heat vulnerability, industrial-performance effect, emissions effect, predictive utility or causality.

Incremental monetary cost remains **0 USD**.


## Final disposition / 최종 처분

Corrected Run `35039383396` terminates C-EU-F01 at **`HOLD_C_EU_F01_SOURCE_OR_IDENTITY`**. The complete EEA population was retrieved, but **38,752** exact `InspireSiteId` values have multiple distinct valid coordinate pairs and only **60.4123%** of exact site IDs satisfy the frozen invariant-coordinate rule versus **95% required**. ERA5 semantics passed and the unauthenticated ARCO probe returned 401, but credential access is not the sole blocker, so the frozen PARTIAL disposition does not apply. No industrial outcome or temperature magnitude was opened and no relationship was computed.
