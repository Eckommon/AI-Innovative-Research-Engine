---
id: EU-ISR-F01-AMENDMENT-01
type: outcome-blind-sample-route-freeze
state: ACTIVE
created: 2026-09-03
parent: EU-ISR-F01
incremental_monetary_cost_usd: 0
---

# EU-ISR-F01 AMENDMENT-01 — Deterministic Public Feature Sample Route
# EU-ISR-F01 수정-01 — 결정론적 공개 Feature 표본 경로

## Trigger / 발동 사유

Before any facility-level climate values or associations were inspected, the official EEA ArcGIS REST `IED_SiteMap` service was confirmed to expose a public queryable point feature layer.

시설별 기후값이나 연관성을 확인하기 전에 EEA 공식 ArcGIS REST `IED_SiteMap`이 공개 query 가능한 point feature layer를 제공함을 확인하였다.

## Frozen EEA sample selection / 고정 EEA 표본 선택

Use only official EEA service:
`https://air.discomap.eea.europa.eu/arcgis/rest/services/Air/IED_SiteMap/MapServer/0/query`

Request prospectively:
- `where=1=1`;
- `orderByFields=OBJECTID ASC`;
- `resultRecordCount=1`;
- `returnGeometry=true`;
- `outSR=4326`;
- `f=json`;
- output fields only: `OBJECTID,x_4258,y_4258,Site_reporting_year,siteName,InspireSiteId,countryCode,eprtr_sectors,eea_activities`.

The first OBJECTID is chosen only for deterministic source-mechanics testing. It is not selected for emissions, sector, climate exposure, geography, or any outcome.

## Frozen NASA request / 고정 NASA 요청

From the returned WGS84 coordinate, request NASA POWER Daily Point API for exactly:
- dates `2024-01-01` through `2024-01-03`;
- `time-standard=UTC`;
- community `AG`;
- parameters `T2M_MAX,T2M_MIN,PRECTOTCORR,WS10M`;
- JSON format.

Do not emit or interpret the meteorological numerical values in F01. Validate only:
- HTTP/access success;
- coordinate/request construction;
- requested parameter presence;
- expected date-key coverage;
- response time-standard metadata when supplied;
- missing/sentinel structure needed for join feasibility.

## Frozen identity/geometry checks / 고정 식별자·geometry 검증

EEA sample must contain:
- non-null `InspireSiteId`;
- non-null `Site_reporting_year`;
- non-null `countryCode`;
- point geometry convertible/returned within valid WGS84 longitude/latitude bounds.

The service layer itself documents spatial reference `102100 (3857)`. Using `outSR=4326` is an explicit server-side coordinate transformation, not a guessed CRS conversion.

## Claim boundary / 주장 경계

A successful sample proves only a reproducible official facility-coordinate→meteorological-point request route. It does not prove local meteorological accuracy at facility scale, climate causality, emissions sensitivity, or risk ranking.

NASA POWER grid-cell sharing must be handled as shared exposure in any later experiment; facilities receiving the same source grid cell are not independent climate measurements.

## Cost / 비용

Incremental monetary cost remains `0 USD`.
