# Global Public Data Source Registry v0.1

Purpose: maintain an authoritative shortlist of public-data sources to be harvested and evaluated by the innovation discovery pipeline.

This registry records sources, not yet individual dataset approvals. Counts and platform capabilities can change; dynamic facts should be re-verified during each harvesting wave.

## Wave 0 — Methodological Benchmark

| Jurisdiction | Source | URL | Role | Status |
|---|---|---|---|---|
| United States | NIST AM Bench / NIST data resources | https://www.nist.gov/ambench | Experimental/benchmark reference for advanced manufacturing | `ACTIVE_BENCHMARK` |
| United States | NIST Data Catalog | https://data.nist.gov/ | NIST research dataset discovery | `DISCOVERED` |

## Wave 1 — Priority Expansion

### United States

| Source | URL | Primary Use | Access/Metadata Notes | Status |
|---|---|---|---|---|
| Data.gov Catalog | https://catalog.data.gov/ | Federal/public dataset discovery | Catalog/API-based harvesting candidate | `PRIORITY_A` |
| Resources.data.gov | https://resources.data.gov/ | Data governance, metadata, quality, standards, tooling | Methodology/quality reference rather than a primary raw-data catalog | `PRIORITY_A` |
| NIST | https://www.nist.gov/ | Manufacturing, measurement, materials, standards | Agency-level deep search | `PRIORITY_A` |
| U.S. Department of Energy | https://www.energy.gov/data | Energy systems and infrastructure | Cross-agency join candidate | `PRIORITY_A` |
| NOAA | https://www.noaa.gov/ | Weather, climate, ocean/environment | Strong temporal/spatial join potential | `PRIORITY_A` |
| EPA | https://www.epa.gov/data | Environmental/emissions data | Industry-energy-emissions joins | `PRIORITY_A` |
| NASA Open Data | https://data.nasa.gov/ | Earth/space/remote-sensing data | Spatial and physical measurement datasets | `PRIORITY_B` |

### Korea

| Source | URL | Primary Use | Access/Metadata Notes | Status |
|---|---|---|---|---|
| 공공데이터포털 | https://www.data.go.kr/ | Central public-data discovery/API | Primary Korean catalog | `PRIORITY_A` |
| KOSIS 국가통계포털 | https://kosis.kr/ | Official statistics | Cross-domain baseline/context datasets | `PRIORITY_A` |
| 한국전력/전력데이터 개방 관련 공식 소스 | https://home.kepco.co.kr/ | Electricity demand/infrastructure candidates | Specific open-data endpoints to be verified | `DISCOVERED` |
| 기상청 기상자료개방포털 | https://data.kma.go.kr/ | Weather/climate | Strong temporal/spatial join potential | `PRIORITY_A` |
| 국토교통부/국가공간정보 관련 공개데이터 | https://www.vworld.kr/ | Land, building, geospatial data | Spatial joins; endpoint-specific review required | `PRIORITY_B` |

### European Union

| Source | URL | Primary Use | Access/Metadata Notes | Status |
|---|---|---|---|---|
| data.europa.eu | https://data.europa.eu/ | Pan-European open-data discovery | DCAT-AP / cross-country metadata integration candidate | `PRIORITY_A` |
| Eurostat | https://ec.europa.eu/eurostat/ | Harmonized EU statistics | Cross-national comparison backbone | `PRIORITY_A` |
| European Environment Agency | https://www.eea.europa.eu/ | Environment/climate | Energy/industry/environment joins | `PRIORITY_A` |
| ENTSO-E Transparency Platform | https://transparency.entsoe.eu/ | Electricity generation/load/grid data | High-value energy-system candidate; access terms/API review needed | `PRIORITY_A` |

## Wave 2 — Secondary Expansion

| Jurisdiction | Source | URL | Research Strength | Status |
|---|---|---|---|---|
| Japan | e-Stat | https://www.e-stat.go.jp/ | Official statistics, regional/mesh analysis | `WAVE_2` |
| Japan | DATA GO JP / government open-data resources | https://www.digital.go.jp/ | Government data ecosystem; exact catalog endpoints to verify | `WAVE_2` |
| United Kingdom | data.gov.uk | https://www.data.gov.uk/ | Business, economy, environment, land, transport | `WAVE_2` |
| Singapore | data.gov.sg | https://data.gov.sg/ | API-oriented urban, transport, environment, housing | `WAVE_2` |

## Wave 3 — Broader Expansion

| Jurisdiction | Source | URL | Research Strength | Status |
|---|---|---|---|---|
| Canada | Open Government | https://open.canada.ca/ | Resources, environment, industry, geospatial | `WAVE_3` |
| Australia | data.gov.au | https://data.gov.au/ | Resources, environment, geospatial | `WAVE_3` |
| Global | OECD Data | https://data.oecd.org/ | Cross-national normalization/comparison | `WAVE_3` |
| Global | World Bank Data | https://data.worldbank.org/ | Cross-national development/economic baseline | `WAVE_3` |

## Source Qualification Fields

Every source added in later revisions should progressively capture:

- `source_id`
- jurisdiction
- operator/publisher
- canonical URL
- API/catalog endpoint
- metadata standard (`DCAT`, `DCAT-AP`, `CKAN`, custom, etc.)
- authentication requirement
- rate/access constraints
- license/reuse policy
- update cadence
- machine-readable formats
- domain coverage
- provenance quality
- harvesting feasibility
- last verified date

## Next Registry Action

Wave 1 should be converted from source-level discovery into dataset-level candidates in this order:

1. United States — Data.gov/NIST/DOE/NOAA/EPA
2. Korea — data.go.kr/KOSIS/KMA plus energy and spatial sources
3. EU — data.europa.eu/Eurostat/EEA/ENTSO-E

The first dataset-level pass should prioritize advanced manufacturing, energy/grid, data-center-enabling infrastructure, supply chain/logistics, and climate/spatial datasets because these domains have strong cross-dataset relationship potential.
