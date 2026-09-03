---
id: EU-ISR-F01-RESULT
type: feasibility-result
state: COMPLETED_PASS
created: 2026-09-03
parent: EU-ISR-F01
issue: 66
mission_anchor: MEM-054
portfolio_decision: DEC-096
incremental_monetary_cost_usd: 0
---

# EU-ISR-F01 Result — Facility-Coordinate × Climate-Exposure Join Feasibility
# EU-ISR-F01 결과 — 산업시설 좌표 × 기후노출 조인 실행가능성

## Final Gate / 최종 게이트

**`PASS_EU_ISR_FACILITY_CLIMATE_JOIN_READY`**

A bounded zero-cost public-source preflight demonstrated a deterministic official EEA industrial-site point → WGS84 → NASA POWER meteorological-point route with fixed time semantics and no credential provisioning.

제한된 무비용 공개-source 사전검증에서 EEA 공식 산업시설 point → WGS84 → NASA POWER 기상 point 요청 경로가 결정론적으로 동작했으며 별도 인증정보가 필요하지 않았다.

## Verified route / 검증 경로

- EEA official `Air/IED_SiteMap/MapServer/0` is a public Feature Layer with point geometry.
- Layer spatial reference is documented as `102100 (3857)` and the query supports server-side output transformation.
- The layer exposes `Site_reporting_year`, `InspireSiteId`, `countryCode`, site/sector/activity fields and geometry.
- Deterministic sample selection was frozen before execution: `where=1=1`, `OBJECTID ASC`, one record, `outSR=4326`.
- The selected feature returned non-null identity/reporting fields and valid WGS84 geometry.
- The resulting coordinate successfully constructed an unauthenticated NASA POWER Daily Point API request.
- Frozen NASA fields `T2M_MAX`, `T2M_MIN`, `PRECTOTCORR`, `WS10M` were all present for the frozen three dates.
- NASA response reported `UTC` time standard.
- Raw facility coordinates and meteorological numerical values were not written to the repository.

Durable preflight: `research/EU-ISR-F01/SOURCE_PREFLIGHT.md`.

## Reproducibility identities / 재현 식별자

From the durable preflight:
- EEA response SHA-256: `0a5c0b45166aded3bf1fec6c742251446025d5d59d7a779158d57ffc4c370d3d`
- selected EEA feature canonical SHA-256: `9f1d41a6ec314219d08e9ed7dcc34f210913a14c47705fea2c0e2e1f3c9512da`
- NASA POWER response SHA-256: `4ac281be5d9c5f09c83b970d52a27355e69f40b4274bc112830cd324ca4f4118`

## Independent-unit / pseudoreplication rule / 독립단위 규칙

A future research unit must be a qualified industrial site/facility × period. NASA POWER has coarser source resolution than facility coordinates; facilities mapped to the same POWER source grid cell share one exposure signal and must not be treated as independent meteorological measurements.

## Claim boundary / 주장 경계

This PASS establishes **join feasibility only**. It does not establish:
- facility-scale local-weather accuracy;
- climate causality;
- climate sensitivity of pollutant releases or energy input;
- a facility climate-risk score;
- a ranking of countries/sectors/sites.

## Mission-ROI decision / 목적-ROI 판단

Do **not** automatically launch a climate→emissions or climate→energy regression merely because the join is feasible.

Current EEA documentation confirms annual facility reporting and, for LCPs, energy input and emissions. Those outcomes are also strongly structured by facility capacity, fuel, dispatch, regulation, technology and country/system conditions. A simple climate-association experiment would therefore have weak construct validity unless a better low-DOF outcome/control design is established prospectively.

Under `MEM-054`, preserving a validated join route is preferable to forcing an under-specified experiment. Return to Stage 0 portfolio review; C-EU-004 remains a reusable high-value cross-agency asset.

## Cost / 비용

Incremental monetary cost remained **0 USD**.
