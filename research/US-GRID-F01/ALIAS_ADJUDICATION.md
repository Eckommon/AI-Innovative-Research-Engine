---
id: US-GRID-F01-ALIAS-ADJUDICATION
type: outcome-blind-source-backed-identity-adjudication
created: 2026-09-04
relationship_outcome_computed: false
eia_operating_values_opened: false
qualified_entities: 41
excluded_entities: 16
incremental_monetary_cost_usd: 0
---

# US-GRID-F01 Source-Backed Alias Adjudication
# US-GRID-F01 공식근거 기반 BA alias 판정

## Final prospective rule / 최종 사전 규칙

An LBNL `entity` is admitted only when its EIA-930 balancing-authority identity is fixed before relationship outcomes by one of four evidence classes:

- **E0 — exact identity:** LBNL entity directly equals an EIA BA code/name after punctuation/case normalization only.
- **E1 — official ISO/RTO alias:** LBNL's official ISO/RTO acronym maps one-to-one to the EIA BA code/name, supported by EIA's own ISO/RTO naming.
- **E2 — source-defined legal/name alias:** LBNL's source-defined balancing-area/entity or single utility label resolves to one and only one EIA BA legal name/code. Legal suffix/punctuation expansion is allowed; geography inference is not.
- **E3 — explicit operating-footprint / grouped-entity rule:** an official source explicitly states the BA responsibility, or LBNL itself defines several entity codes as one named BA family and all rows preserve that same parent BA.

Anything else is **X — excluded prospectively**.

No fuzzy matching, county/state inference, nearest-area assignment, observed queue duration, or EIA operating value is used.

## Qualified 41 / 적격 41

| LBNL entity | EIA BA | Class | Prospective source-semantic basis |
|---|---|---|---|
| `EPE` | `EPE` | E0 | exact EIA BA code |
| `FPL` | `FPL` | E0 | exact EIA BA code |
| `IID` | `IID` | E0 | exact EIA BA code |
| `JEA` | `JEA` | E0 | exact EIA BA code/name; duplicate code+name hit is same BA concept |
| `MISO` | `MISO` | E0 | exact EIA BA code |
| `NWMT` | `NWMT` | E0 | exact EIA BA code |
| `PGE` | `PGE` | E0 | exact EIA BA code |
| `PJM` | `PJM` | E0 | exact EIA BA code |
| `PNM` | `PNM` | E0 | exact EIA BA code |
| `PSCo` | `PSCO` | E0 | case-only EIA BA code normalization |
| `S-C` | `SC` | E0 | LBNL source label Santee Cooper; EIA `SC` = South Carolina Public Service Authority |
| `SEC` | `SEC` | E0 | exact EIA BA code |
| `SOCO` | `SOCO` | E0 | exact EIA BA code |
| `SRP` | `SRP` | E0 | exact EIA BA code |
| `TEC` | `TEC` | E0 | exact EIA BA code |
| `TVA` | `TVA` | E0 | exact EIA BA code |
| `CAISO` | `CISO` | E1 | EIA identifies California Independent System Operator as `CISO`; LBNL uses official acronym CAISO |
| `ERCOT` | `ERCO` | E1 | EIA identifies Electric Reliability Council of Texas as `ERCO`; LBNL uses ERCOT |
| `ISO-NE` | `ISNE` | E1 | EIA identifies New England ISO as `ISNE`; LBNL uses ISO-NE |
| `NYISO` | `NYIS` | E1 | EIA identifies New York ISO as `NYIS`; LBNL uses NYISO |
| `SPP` | `SWPP` | E1 | EIA identifies Southwest Power Pool as `SWPP`; LBNL uses SPP |
| `AEC` | `AECI` | E2 | LBNL single utility = Associated Electric Cooperative, Incorporated; EIA `AECI` = Associated Electric Cooperative, Inc. |
| `APS` | `AZPS` | E2 | LBNL single utility = Arizona Public Service; EIA `AZPS` = Arizona Public Service Company |
| `Avista` | `AVA` | E2 | LBNL balancing-area label Avista / single utility Avista Utilities; EIA `AVA` = Avista Corporation |
| `BPA` | `BPAT` | E2 | LBNL balancing-area sheet identifies Bonneville Power Admin.; EIA `BPAT` = Bonneville Power Administration |
| `CPUD` | `CHPD` | E2 | LBNL single utility = Chelan County Public Utility District; EIA `CHPD` = PUD No. 1 of Chelan County |
| `Dominion` | `SCEG` | E2 | LBNL single utility = Dominion Energy South Carolina; EIA current BA name for `SCEG` = Dominion Energy South Carolina |
| `GrantPUD` | `GCPD` | E2 | LBNL single utility = Grant County Public Utility District; EIA `GCPD` = PUD No. 2 of Grant County, Washington |
| `IP` | `IPCO` | E2 | LBNL single utility = Idaho Power Company; EIA `IPCO` = Idaho Power Company |
| `LADWP` | `LDWP` | E2 | LBNL single utility = Los Angeles Department of Water and Power; EIA `LDWP` same legal name |
| `LGE-KU` | `LGEE` | E2 | LBNL single utility = Louisville Gas & Electric and Kentucky Utilities Energy; EIA `LGEE` = Louisville Gas & Electric Company & Kentucky Utilities Company |
| `PSE` | `PSEI` | E2 | LBNL single utility = Puget Sound Energy; EIA `PSEI` = Puget Sound Energy, Inc. |
| `TEP` | `TEPC` | E2 | LBNL single utility = Tucson Electric Power Company; EIA `TEPC` same legal name |
| `TPU` | `TPWR` | E2 | LBNL balancing-area label Tacoma Public Utilities; EIA `TPWR` = City of Tacoma, Department of Public Utilities, Light Division |
| `SMUD` | `BANC` | E3 | BANC states it assumed BA responsibilities from SMUD on 2011-05-01; frozen cohort begins 2019 |
| `SRP_ANPP` | `SRP` | E3 | LBNL BA sheet explicitly groups Salt River Projects as five entities; utility rows = Salt River Project |
| `SRP_Gila` | `SRP` | E3 | same LBNL grouped-entity rule |
| `SRP_PV-PC` | `SRP` | E3 | same LBNL grouped-entity rule |
| `SRP_SWV` | `SRP` | E3 | same LBNL grouped-entity rule |
| `WAPA-DSW` | `WALC` | E3 | WAPA states Desert Southwest operates the WALC balancing authority |
| `WAPA-RM` | `WACM` | E3 | WAPA states Rocky Mountain Region operates WACM |

## Prospectively excluded 16 / 사전 제외 16

| LBNL entity | Reason |
|---|---|
| `BHCT` | no one-to-one EIA BA identity established without geography/parent inference |
| `BHP` | no one-to-one EIA BA identity established without geography/parent inference |
| `CLPT` | no one-to-one EIA BA identity established without geography/parent inference |
| `CSU` | utility/transmission identity is not itself an EIA-930 BA in the frozen reference; assignment would require external geography attribution |
| `Duke` | LBNL single entity contains Duke Carolinas, Duke Florida, and Duke Progress; EIA has multiple BA codes (`DUK/FPC/CPLE/CPLW`) |
| `GTC` | Georgia Transmission cannot be assigned to one EIA BA from frozen source identity alone |
| `MPC` | Minnkota identity does not itself resolve to one frozen EIA BA without service-territory attribution |
| `N-C` | Navajo-Crystal does not resolve to one frozen EIA BA from source identity alone |
| `NVE` | LBNL uses parent/brand-level NV Energy while frozen EIA BA is Nevada Power Company; parent-to-BA allocation is not assumed |
| `OUC` | Orlando Utilities Commission is not itself one unambiguous frozen EIA-930 BA identity under the available source semantics |
| `PRPA` | Platte River Power Authority is not itself a frozen EIA BA; WACM attribution would require service-territory inference |
| `PacifiCorp` | EIA explicitly separates PacifiCorp East `PACE` and West `PACW`; LBNL entity does not preserve that split |
| `TSGT` | Tri-State is not itself one frozen EIA BA; WACM attribution would require service-territory inference |
| `WAPA-IS` | historical Integrated-System identity does not uniquely preserve a 2019–2025 EIA BA without time/footprint reinterpretation |
| `WAPA-MPP` | source label is insufficient to assign one EIA BA without interpretation |
| `WAPA-SN` | WAPA states Sierra Nevada facilities/load span SMUD/BANC and CAISO footprints; one-BA attribution is not valid for the whole entity |

## Official evidence anchors / 공식 근거

### EIA
- EIA-930 BA code/name table:
  `https://www.eia.gov/conference/2015/pdf/presentations/kaplan.pdf`
- EIA Hourly Electric Grid Monitor article confirming ISO/RTO code/name identities:
  `https://www.eia.gov/todayinenergy/detail.php?id=40993`
- Frozen EIA-861 2025 early-release BA identity snapshot is hashed in `IDENTITY_ADJUDICATION.md`.

### LBNL
- Frozen Queued Up 2026 workbook and internal `01. Balancing Areas` / `04. Data Codebook` sheets.
- Workbook SHA-256:
  `794582d3281c6a305e9615fcfec3fae9dc85be2165216d33760b677e976a08b6`.

### BANC / WAPA
- BANC home: `https://thebanc.org/` — BANC assumed BA responsibilities from SMUD on 2011-05-01.
- WAPA OASIS: `https://www.wapa.gov/transmission/oasis/` — Desert Southwest / WALC and Rocky Mountain / WACM source identities.
- WAPA transmission: `https://www.wapa.gov/transmission/`.
- WAPA Sierra Nevada: `https://www.wapa.gov/about-wapa/regions/sn/about-sn/` — current SN footprint is not a single-BA identity, supporting exclusion.

## Duplicate interaction / 중복과의 결합

The complete workbook has 135 repeated `entity+q_id` groups, but `COHORT_DIAGNOSTIC.md` shows that the frozen 2019–2025 completed-project cohort has:

- duplicate key groups: **0**;
- semantic-conflict groups: **0**;
- invalid `on_date < q_date`: **0**.

Therefore no arbitrary row preference or deduplication is needed for the primary completed-project cohort.

## Gate implication / 게이트 의미

The intended unit does **not** require all 57 LBNL entities. F01 can use a prospectively support-qualified subset because all exclusions are fixed before any queue-duration or EIA operating relationship is calculated.

The final F01 decision must use only the 41 qualified entities above. Excluded entities may not be reintroduced after outcomes merely because they improve coverage or results.

Incremental monetary cost remained **0 USD**.
