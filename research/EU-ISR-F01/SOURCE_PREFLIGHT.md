---
id: EU-ISR-F01-SOURCE-PREFLIGHT
type: source-join-preflight
created: 2026-09-03
gate: PASS_EU_ISR_FACILITY_CLIMATE_JOIN_READY
incremental_monetary_cost_usd: 0
---

# EU-ISR-F01 Source Preflight / Source 사전검증

**Gate / 게이트:** `PASS_EU_ISR_FACILITY_CLIMATE_JOIN_READY`

## Frozen route / 고정 경로

- EEA official `IED_SiteMap` layer 0; deterministic first `OBJECTID ASC` feature.
- EEA service-side `outSR=4326` from documented layer CRS EPSG:3857.
- NASA POWER Daily Point API, `2024-01-01..2024-01-03`, `time-standard=UTC`.
- Fixed fields: `T2M_MAX,T2M_MIN,PRECTOTCORR,WS10M`.
- No raw facility coordinate or meteorological numerical value is written to the repository.

## Checks / 검증

| Check / 검증 | Result |
|---|---|
| EEA query returns exactly one deterministic feature | PASS |
| EEA OBJECTID non-null | PASS |
| EEA Site_reporting_year non-null | PASS |
| EEA InspireSiteId non-null | PASS |
| EEA countryCode non-null | PASS |
| EEA geometry returned in valid WGS84 bounds via outSR=4326 | PASS |
| NASA POWER parameter T2M_MAX present | PASS |
| NASA POWER T2M_MAX covers frozen 3 dates | PASS |
| NASA POWER parameter T2M_MIN present | PASS |
| NASA POWER T2M_MIN covers frozen 3 dates | PASS |
| NASA POWER parameter PRECTOTCORR present | PASS |
| NASA POWER PRECTOTCORR covers frozen 3 dates | PASS |
| NASA POWER parameter WS10M present | PASS |
| NASA POWER WS10M covers frozen 3 dates | PASS |
| NASA POWER response reports UTC time standard | PASS |

## Reproducibility diagnostics / 재현 진단

- `eea_country_code_present`: `True`
- `eea_http_status`: `200`
- `eea_inspire_site_id_present`: `True`
- `eea_reporting_year_present`: `True`
- `eea_response_sha256`: `0a5c0b45166aded3bf1fec6c742251446025d5d59d7a779158d57ffc4c370d3d`
- `eea_selected_feature_sha256`: `9f1d41a6ec314219d08e9ed7dcc34f210913a14c47705fea2c0e2e1f3c9512da`
- `eea_wgs84_coordinate_valid`: `True`
- `meteorological_values_emitted`: `False`
- `power_http_status`: `200`
- `power_parameters_present`: `PRECTOTCORR, T2M_MAX, T2M_MIN, WS10M`
- `power_response_sha256`: `4ac281be5d9c5f09c83b970d52a27355e69f40b4274bc112830cd324ca4f4118`
- `power_time_standard_reported`: `UTC`
- `raw_coordinates_emitted`: `False`

## Claim boundary / 주장 경계

A PASS proves only that one official EEA point feature can be deterministically transformed/requested as WGS84 and used to construct a bounded NASA POWER meteorological point request with fixed time semantics. It does not establish facility-scale local-weather accuracy, climate causality, emissions sensitivity, or a risk ranking.

Facilities mapped to the same POWER source grid cell must be treated as sharing climate exposure in any later experiment; they are not independent meteorological measurements.

Incremental monetary cost remained **0 USD**.
