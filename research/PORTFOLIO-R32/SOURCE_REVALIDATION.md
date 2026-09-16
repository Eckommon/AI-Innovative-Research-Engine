---
id: PORTFOLIO-R32-SOURCE-REVALIDATION
type: prospective-source-revalidation
created: 2026-09-16
issue: 144
after_contract_commit: 75c5e9d9074e1083d9a00fd021b50f184b09a2a2
candidate_outcomes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R32 Source Revalidation / 공식 원천 재검증

This revalidation is written **after** Issue #144 binding and **before** `SCORECARD.md`, preserving the R32 prospective ordering. It validates source/access/identity/time semantics only. No candidate-specific outcome magnitude or relationship is opened.

## 1. `US-FMCSA-HAZ-001`

### Official FMCSA inspection side

Current FMCSA Open Data Program:

- https://www.fmcsa.dot.gov/registration/fmcsa-data-dissemination-program

The current official page states:

- FMCSA shares regulated-entity census and safety-performance information **at no charge** through the DOT Public Data Portal;
- USDOT Number is the native unique FMCSA safety-registration number for an entity;
- public Inspection Files are updated daily from a ~24-hour-old database;
- three years of historical inspection data are published because of file size;
- the Vehicle Inspection File includes USDOT Number and inspection details;
- `INSPECTION_ID` links the Vehicle Inspection File to the other inspection files;
- Vehicle Inspections and Violations contains violation code/category and OOS information;
- SMS Input – Inspection contains U.S. DOT#, Report Number and Inspection Date, one inspection per row;
- SMS Input – Violation links violation rows to inspections.

Important current limitation preserved prospectively: the general public Inspection Files exclude inactive USDOT numbers, shipper-only business types, and entities with an active HMSP on file. Therefore any descendant must make an explicit **publicly represented inspection-cohort** claim rather than a population-wide hazardous-material-carrier claim.

### Official PHMSA incident side

Current PHMSA incident source:

- https://www.phmsa.dot.gov/hazmat-program-management-data-and-statistics/data-operations/incident-statistics
- https://portal.phmsa.dot.gov/HIP_Help/DataDictionary.pdf

PHMSA states that Form DOT F 5800.1 incident data are updated nightly and can be searched/downloaded. The current data dictionary exposes, among other fields:

- report/incident identity;
- incident date;
- mode/route information;
- `Carrier/Reporter Name`;
- `Carrier/Reporter FED DOT ID`, defined as the modal carrier identifier number or code;
- `Carrier/Reporter HAZMAT Reg ID`.

### Prospective join assessment

The intended F01 identity is **exact native carrier identifier only**:

`FMCSA USDOT Number ↔ PHMSA Carrier/Reporter FED DOT ID`

restricted prospectively to PHMSA Highway mode and only after F01 verifies that the Highway-mode FED DOT ID values behave as USDOT carrier identifiers. No carrier-name matching, address matching, fuzzy linkage or manual repair is authorized.

The time axis is structurally promising: inspection dates on FMCSA and incident dates on PHMSA. Independent carrier units are expected to be large, but cardinality/overlap remains an empirical F01 question and is not assumed here.

### Overlap / novelty boundary

FMCSA safety systems already use inspection, OOS, crash and hazardous-material safety information for regulatory monitoring, and general roadside-inspection/crash-risk research exists. Current searches did **not** establish a clearly identical public design that prospectively links a frozen FMCSA roadside violation/OOS profile by exact USDOT to **subsequent PHMSA Form 5800.1 highway hazmat incidents**. This is not a novelty proof; the overlap risk remains non-zero.

**Revalidation disposition:** `SOURCE_ID_TIME_PROSPECT_STRONG__BOUNDED_PUBLIC_COHORT`

---

## 2. `US-FTA-TRANSIT-001`

### Official reliability / breakdown side

Current FTA NTD source:

- https://www.transit.dot.gov/ntd/ntd-data
- https://www.transit.dot.gov/ntd/data-product/2024-breakdowns
- https://catalog.data.gov/dataset/2022-2024-ntd-annual-data-breakdowns

FTA/DOT currently publish the 2022–2024 Breakdowns dataset as zero-cost CSV/JSON/XML and retain earlier annual Vehicle Maintenance/Breakdowns files for prior years. The dataset is organized by reporting transit agency, mode and type of service and reports major/other mechanical failures. Only Full Reporters report breakdowns.

### Official safety-event side

Current FTA safety source:

- https://www.transit.dot.gov/ntd/accessing-national-transit-database-ntd-safety-and-security-event-data
- https://www.transit.dot.gov/ntd/data-product/safety-security-major-only-time-series-data

FTA states that Safety & Security datasets are updated monthly. Relevant products include:

- agency × mode annual/calendar time series from 2002-present;
- Major-Only Safety & Security time series;
- individual Major Safety Events from 2014-present, with unique date/time, transit agency, mode, location and description;
- monthly modal time series from 2014-present.

The monthly S&S products primarily cover urban agencies operating more than 30 vehicles in maximum service; annual reduced-reporter safety information covers smaller/rural reporters separately. Reporter-scope compatibility therefore must be frozen and checked in F01 rather than silently mixed.

### Prospective join assessment

A descendant may use source-native **NTD agency identity × mode** and a preregistered annual-to-subsequent-period mapping. Type of service may be aggregated only if F01 proves that the selected safety product lacks an equivalent TOS dimension and freezes the aggregation before any event magnitude is opened.

No agency-name matching or manual entity repair is authorized.

### Overlap / novelty boundary

FTA policy treats system reliability and safety events as related national transit performance areas, and agency planning documents commonly report both. Current searches did not identify a clearly identical national prospective design using prior NTD mechanical-breakdown burden to predict later NTD Major Safety Events. This is not proof of novelty and the fact that both measures sit inside NTD lowers cross-source independence.

**Revalidation disposition:** `SOURCE_ID_TIME_PROSPECT_STRONG__SAME_PROGRAM_AND_REPORTER_SCOPE_LIMIT`

---

## 3. `KR-GG-CHEM-001`

Current official Gyeonggi sources remain available:

- hazardous-chemical handling businesses: https://data.gg.go.kr/portal/data/service/selectServicePage.do?infId=M37YD49AM5UFN6VJM2CZ29567068&infSeq=1
- public-data portal listing for hazardous-chemical accidents: https://www.data.go.kr/dataset/15011194/openapi.do?lang=en
- Gyeonggi annual chemical-accident publications: https://www.gg.go.kr/opendata/openDataBoard.do?boardIdx=AVB

The facility dataset offers downloadable tabular formats and an Open API. The accident listing describes accident region/date/content/cause/address/latitude/longitude. Gyeonggi also publishes annual accident occurrence reports through 2025.

However, current public descriptions still do **not** establish a stable business identifier shared natively between the facility source and accident source. Address/name/geospatial matching would therefore require fuzzy or tolerance-based entity resolution, which R32 does not authorize. Prior Korean work and policy analysis already use business risk factors and accident history, further reducing marginal novelty.

**Revalidation disposition:** `SOURCE_TIME_AVAILABLE__COMMON_NATIVE_BUSINESS_ID_UNPROVEN`

---

## 4. `US-PIPE-001`

Current official PHMSA pipeline incident files remain publicly downloadable, including 2010-present hazardous-liquid and gas transmission/gathering incident ZIPs:

- https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data

This preserves the outcome side and long time axis. The prior portfolio restriction remains unchanged: unrestricted national NPMS line geometry cannot be assumed, substituted or bypassed for the intended hydrologic-stress exposure construction. Public incident/mileage support therefore does not eliminate the geometry bottleneck. The domain also has substantial direct prior overlap on weather/hydrologic exposure and pipeline incidents.

**Revalidation disposition:** `PUBLIC_OUTCOME_READY__EXPOSURE_GEOMETRY_RESTRICTED_HIGH_OVERLAP`

---

## Comparative source conclusion / 원천 비교 결론

Before scoring, source revalidation establishes only the following structural ordering facts:

- `US-FMCSA-HAZ-001`: strongest new cross-agency exact-ID/time prospect, but F01 must prove Highway FED DOT ID semantics, actual overlap and bounded public-cohort support.
- `US-FTA-TRANSIT-001`: strong machine-readable agency/mode/time support with manageable reporter-scope questions, but both exposure and outcome live within NTD and direct conceptual overlap is not zero.
- `KR-GG-CHEM-001`: public data remain available but a shared native business ID is unproven.
- `US-PIPE-001`: outcome source remains public but the previously frozen national geometry restriction and high overlap remain unresolved.

No candidate outcome magnitude, exposure-conditioned outcome count, effect estimate, predictive metric or relationship direction was inspected in this revalidation.

Incremental monetary cost remains **0 USD**.
