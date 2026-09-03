---
checkpoint_id: CHK-20260903-EU-ISR-F01-ACTIVE
active_issue: 66
active_research: EU-ISR-F01
last_completed_issue: 65
last_completed_research: KR-PORT-F01
last_decision: DEC-096
updated: 2026-09-03
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**State / 상태:** `MISSION_ANCHOR_FIXED__PORTFOLIO_RETURN_COMPLETE__EU_ISR_F01_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #66 `EU-ISR-F01 — Facility-coordinate × climate-exposure join feasibility`.

## Fixed Mission / 고정 목적

The project exists to discover and validate **new, falsifiable, reproducible and practically useful innovation opportunities or structural bottlenecks from relationships among public/research data**. `context/MEM-054-MISSION-ANCHOR.md` is mandatory durable memory.

특정 데이터셋·실험·도구·접근경로 완주는 목적이 아니다. Route dependency를 mission dependency로 승격하지 않는다.

## Governance / 거버넌스

Mandatory:
- `MEM-054` Mission Anchor;
- `DEC-093` Mission-ROI / Branch-Stop;
- Stage 0 Portfolio Selection + Stage 9 Portfolio Return in `docs/METHODOLOGY.md`;
- `COST-001` zero-incremental-cost default.

Default stop: >=2 infrastructure/runtime/source-transfer descendants without new scientific evidence + credible alternative + route not uniquely mission-critical → `HOLD/ARCHIVE → RETURN_TO_PORTFOLIO`.

## KR-PORT-F01 completed / KR-PORT-F01 완료

Issue #65 closed as:
**`PARTIAL_KR_PORT_METADATA_SCHEMA_READY__SAMPLE_ACCESS_PENDING`**.

Durable records:
- `research/KR-PORT-F01/RESULT.md`;
- `research/KR-PORT-F01/AMENDMENT-01.md`;
- `registry/CLM-118.md`;
- `registry/DEC-095.md`.

`C-KR-003` remains `HOLD_READY__HIGH_VALUE__SAMPLE_ACCESS_PENDING`. No KR-PORT-F02 is authorized automatically.

## Portfolio return / Portfolio 복귀

`DEC-096` selected **`C-EU-004 Industrial Site Climate Risk`** as the next primary branch.

Why:
- EEA Industrial Reporting ver.16.0 (20 Feb 2026) has direct-download spatial/tabular official data covering 2007–2024;
- official Industrial Emissions Portal exposes site/facility identity and spatial geometry semantics;
- NASA POWER provides a free public point API for meteorological data with explicit UTC/LST standards;
- the next uncertainty is scientific/spatial-temporal joinability rather than credential acquisition.

Original ERA5 route is not used for F01 because current official CDS/ARCO programmatic access requires a CDS API key. This route choice was made prospectively before any facility-climate association or model result.

## Active EU-ISR-F01 / 활성 EU-ISR-F01

Preregistration: `research/EU-ISR-F01/README.md`.
Outcome-blind deterministic sample route: `research/EU-ISR-F01/AMENDMENT-01.md`.

Frozen test route:
1. official EEA `IED_SiteMap` ArcGIS REST layer 0;
2. deterministic first feature: `where=1=1`, `OBJECTID ASC`, one record;
3. server-side `outSR=4326` from documented EPSG:3857 layer;
4. require `InspireSiteId`, reporting year, country and valid point geometry;
5. request NASA POWER Daily Point for the returned coordinate, 2024-01-01..2024-01-03, UTC, fixed low-DOF climate fields;
6. validate access/schema/date coverage only — do not emit or interpret meteorological values or facility associations.

Official EEA ArcGIS service already documents:
- Feature Layer / point geometry;
- spatial reference 102100 (3857);
- query support (JSON/GeoJSON/PBF);
- `x_4258`, `y_4258`, `Site_reporting_year`, `siteName`, `InspireSiteId`, `countryCode`, sector/activity fields.

## Exact next action / 정확한 다음 행동

Run the frozen bounded EU-ISR-F01 public-source preflight and write back one gate:
- `PASS_EU_ISR_FACILITY_CLIMATE_JOIN_READY`;
- `PARTIAL_EU_ISR_METADATA_SCHEMA_READY__FEATURE_SAMPLE_PENDING`;
- `HOLD_EU_ISR_SPATIAL_OR_TEMPORAL_SEMANTICS_GAP`;
- `REJECT_EU_ISR_JOIN_ROUTE`.

No large bulk download, risk score, ranking or predictive model is authorized. PASS allows at most one separately preregistered low-DOF experiment before mandatory portfolio return.

Incremental monetary cost remains `0 USD`.
