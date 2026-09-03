---
id: US-GRID-F01-IDENTITY-ADJUDICATION
type: outcome-blind-identity-adjudication
created: 2026-09-04
relationship_outcome_computed: false
eia_operating_values_opened: false
incremental_monetary_cost_usd: 0
---

# US-GRID-F01 Identity Adjudication / 식별성 보정 판정

## Amendment applied / 보정 적용

- Primary LBNL identity: source-defined `entity` only.
- Project key: source-defined composite `entity + q_id`.
- EIA identity: explicit `BA Code` + `Balancing Authority Name`.
- No fuzzy matching, geography inference or relationship outcome was used.

## A. LBNL entity identity / LBNL entity 식별

- workbook SHA-256: `794582d3281c6a305e9615fcfec3fae9dc85be2165216d33760b677e976a08b6`
- project rows: **38201**
- unique nonblank `entity`: **57**
- blank entity rows: **0**
- blank q_id rows: **0**
- composite `entity+q_id` duplicates: **135**
- unique region vocabulary: `['CAISO', 'ERCOT', 'ISO-NE', 'MISO', 'NYISO', 'PJM', 'SPP', 'Southeast', 'West']`

### Codebook identity/date semantics

- q_id | queue position / ID number | Combine with "entity" to form a unique identifier across the full dataset
- q_date | interconnection request date (date project entered queue) | 
- on_date | date project became operational (if applicable) | 
- wd_date | date project withdrawn from queue (if applicable) | 
- ia_date | date of signed interconnection agreement (if applicable) | 
- region | standardized region where project is located | One of: the 7 ISOs; and West (non-ISO) or Southeast (non-ISO)
- entity | transmission provider entity name (ISO or utility) | One of the 57 regions listed on the 01. Balancing Areas sheet

### Source-defined `01. Balancing Areas` sheet / source-defined balancing-area sheet

- RETURN TO CONTENTS |  |  |  | Map of balancing areas included in data
- ISO/RTOs | Southeast (non-ISO) | 
- CAISO | Associated Electric Coop. | LG&E & KU Energy
- ERCOT | Dominion | Orlando Utilities Commission
- ISO-NE | Duke Carolinas | Santee Cooper
- MISO | Duke Florida | Seminole Electric Coop.
- NYISO | Duke Progress | Southern Company
- PJM | Florida Power & Light | Tampa Electric Co.
- SPP | Georgia Transmission Corp. | Tennessee Valley Authority
-  | Jacksonville Electric Authority | 
- West (non-ISO) |  | 
- Arizona Public Service | Idaho Power | Portland General Electric
- Avista | Imperial Irrigation District | Public Service Co. of CO / Public Service Co. of NM
- Black Hills / Black Hills Colorado | L.A. Dept. Water & Power | Puget Sound Energy
- Bonneville Power Admin. | Minnkota Power Cooperative | Sacramento Municipal Utility District
- Chelan PUD | Navajo-Crystal | Salt River Projects (5 entities)
- Cheyenne Light Fuel & Power | NorthWestern | Tacoma Public Utilities
- Colorado Springs Utilities | NV Energy | Tri-State G&T
- El Paso Electric | PacifiCorp | Tucson Electric Power
- Grant PUD | Platte River Power Authority | WAPA (5 entities)

### LBNL entity vocabulary / entity 목록

- `AEC` — rows `94`
- `APS` — rows `619`
- `Avista` — rows `173`
- `BHCT` — rows `51`
- `BHP` — rows `26`
- `BPA` — rows `998`
- `CAISO` — rows `2868`
- `CLPT` — rows `40`
- `CPUD` — rows `3`
- `CSU` — rows `8`
- `Dominion` — rows `118`
- `Duke` — rows `1069`
- `EPE` — rows `66`
- `ERCOT` — rows `3757`
- `FPL` — rows `385`
- `GTC` — rows `107`
- `GrantPUD` — rows `9`
- `IID` — rows `33`
- `IP` — rows `824`
- `ISO-NE` — rows `1282`
- `JEA` — rows `12`
- `LADWP` — rows `113`
- `LGE-KU` — rows `136`
- `MISO` — rows `5378`
- `MPC` — rows `46`
- `N-C` — rows `7`
- `NVE` — rows `505`
- `NWMT` — rows `448`
- `NYISO` — rows `1936`
- `OUC` — rows `13`
- `PGE` — rows `114`
- `PJM` — rows `7666`
- `PNM` — rows `356`
- `PRPA` — rows `62`
- `PSCo` — rows `408`
- `PSE` — rows `142`
- `PacifiCorp` — rows `2160`
- `S-C` — rows `317`
- `SEC` — rows `25`
- `SMUD` — rows `33`
- `SOCO` — rows `1245`
- `SPP` — rows `2837`
- `SRP` — rows `155`
- `SRP_ANPP` — rows `45`
- `SRP_Gila` — rows `3`
- `SRP_PV-PC` — rows `33`
- `SRP_SWV` — rows `5`
- `TEC` — rows `108`
- `TEP` — rows `120`
- `TPU` — rows `1`
- `TSGT` — rows `104`
- `TVA` — rows `705`
- `WAPA-DSW` — rows `34`
- `WAPA-IS` — rows `273`
- `WAPA-MPP` — rows `4`
- `WAPA-RM` — rows `110`
- `WAPA-SN` — rows `12`

## B. EIA 2025 early-release BA identity / EIA BA identity

- source ZIP SHA-256: `bcbba24da0071114dfa6080b4f63989717e23f159a0ace63ffd5cb82098b9a50`
- BA workbook: `Balancing_Authority_2025_Data_Early_Release.xlsx`
- parsed rows: **187**
- unique BA codes: **64**
- unique BA names: **64**

### EIA BA code/name pairs

- `AECI` → `Associated Electric Cooperative, Inc.`
- `AMPL` → `Anchorage Municipal Light & Power`
- `AVA` → `Avista Corporation`
- `AVRN` → `Avangrid Renewables LLC`
- `AZPS` → `Arizona Public Service Company`
- `BANC` → `Balancing Authority of Northern California`
- `BPAT` → `Bonneville Power Administration`
- `CEA` → `Chugach Electric Assn Inc`
- `CHPD` → `Public Utility District No. 1 of Chelan County`
- `CISO` → `California Independent System Operator`
- `CPLE` → `Duke Energy Progress East`
- `CPLW` → `Duke Energy Progress West`
- `DEAA` → `Arlington Valley, LLC - AVBA`
- `DOPD` → `PUD No. 1 of Douglas County`
- `DUK` → `Duke Energy Carolinas`
- `EPE` → `El Paso Electric Company`
- `ERCO` → `Electric Reliability Council of Texas, Inc.`
- `FMPP` → `Florida Municipal Power Pool`
- `FPC` → `Duke Energy Florida Inc`
- `FPL` → `Florida Power & Light Company`
- `GCPD` → `Public Utility District No. 2 of Grant County, Washington`
- `GRID` → `Gridforce Energy Management, LLC`
- `GRIS` → `Gridforce South`
- `GVL` → `Gainesville Regional Utilities`
- `GWA` → `NaturEner Power Watch, LLC (GWA)`
- `HECO` → `Hawaiian Electric Co Inc`
- `HST` → `City of Homestead`
- `IID` → `Imperial Irrigation District`
- `IPCO` → `Idaho Power Company`
- `ISNE` → `ISO New England Inc.`
- `JEA` → `JEA`
- `LDWP` → `Los Angeles Department of Water and Power`
- `LGEE` → `Louisville Gas and Electric Company and Kentucky Utilities Company`
- `MISO` → `Midcontinent Independent Transmission System Operator, Inc..`
- `NBSO` → `New Brunswick System Operator`
- `NEVP` → `Nevada Power Company`
- `NWMT` → `NorthWestern Energy (NWMT)`
- `NYIS` → `New York Independent System Operator`
- `PACE` → `PacifiCorp - East`
- `PACW` → `PacifiCorp - West`
- `PGE` → `Portland General Electric Company`
- `PJM` → `PJM Interconnection, LLC`
- `PNM` → `Public Service Company of New Mexico`
- `PSCO` → `Public Service Company of Colorado`
- `PSEI` → `Puget Sound Energy`
- `SC` → `South Carolina Public Service Authority`
- `SCEG` → `Dominion Energy South Carolina`
- `SCL` → `Seattle City Light`
- `SEC` → `Seminole Electric Cooperative`
- `SEPA` → `Southeastern Power Administration`
- `SOCO` → `Southern Company Services, Inc. - Trans`
- `SPA` → `Southwestern Power Administration`
- `SRP` → `Salt River Project`
- `SWPP` → `Southwest Power Pool`
- `TAL` → `City of Tallahassee`
- `TEC` → `Tampa Electric Company`
- `TEPC` → `Tucson Electric Power Company`
- `TIDC` → `Turlock Irrigation District`
- `TPWR` → `City of Tacoma, Department of Public Utilities, Light Division`
- `TVA` → `Tennessee Valley Authority`
- `WACM` → `Western Area Power Administration - Rocky Mountain Region`
- `WALC` → `Western Area Power Administration - Desert Southwest Region`
- `WAUW` → `Western Area Power Administration UGP West`
- `YAD` → `Alcoa Power Generating, Inc. - Yadkin Division`

## C. Conservative exact identity / 보수적 exact identity

- LBNL entities: **57**
- exact normalized matches to EIA BA name/code: **15**
- unmatched: **41**
- ambiguous exact: **1**
- exact-match share: **0.263158**

### Exact matches

- `EPE` → ('code', 'EPE', ['El Paso Electric Company'])
- `FPL` → ('code', 'FPL', ['Florida Power & Light Company'])
- `IID` → ('code', 'IID', ['Imperial Irrigation District'])
- `MISO` → ('code', 'MISO', ['Midcontinent Independent Transmission System Operator, Inc..'])
- `NWMT` → ('code', 'NWMT', ['NorthWestern Energy (NWMT)'])
- `PGE` → ('code', 'PGE', ['Portland General Electric Company'])
- `PJM` → ('code', 'PJM', ['PJM Interconnection, LLC'])
- `PNM` → ('code', 'PNM', ['Public Service Company of New Mexico'])
- `PSCo` → ('code', 'PSCO', ['Public Service Company of Colorado'])
- `S-C` → ('code', 'SC', ['South Carolina Public Service Authority'])
- `SEC` → ('code', 'SEC', ['Seminole Electric Cooperative'])
- `SOCO` → ('code', 'SOCO', ['Southern Company Services, Inc. - Trans'])
- `SRP` → ('code', 'SRP', ['Salt River Project'])
- `TEC` → ('code', 'TEC', ['Tampa Electric Company'])
- `TVA` → ('code', 'TVA', ['Tennessee Valley Authority'])

### Unmatched entities requiring source-backed adjudication

- `AEC`
- `APS`
- `Avista`
- `BHCT`
- `BHP`
- `BPA`
- `CAISO`
- `CLPT`
- `CPUD`
- `CSU`
- `Dominion`
- `Duke`
- `ERCOT`
- `GTC`
- `GrantPUD`
- `IP`
- `ISO-NE`
- `LADWP`
- `LGE-KU`
- `MPC`
- `N-C`
- `NVE`
- `NYISO`
- `OUC`
- `PRPA`
- `PSE`
- `PacifiCorp`
- `SMUD`
- `SPP`
- `SRP_ANPP`
- `SRP_Gila`
- `SRP_PV-PC`
- `SRP_SWV`
- `TEP`
- `TPU`
- `TSGT`
- `WAPA-DSW`
- `WAPA-IS`
- `WAPA-MPP`
- `WAPA-RM`
- `WAPA-SN`

### Ambiguous exact matches

- `JEA` → `[('name', 'JEA', ['JEA']), ('code', 'JEA', ['JEA'])]`

## D. Current gate / 현재 gate

**`CONTINUE_US_GRID_F01_SOURCE_BACKED_ALIAS_ADJUDICATION`**

Exact identity matching is now performed on the correct source-defined unit. Remaining unmatched entities may be admitted only through explicit one-to-one source-backed aliases. If a substantial share remains many-to-many or requires geographic inference, F01 must HOLD/REJECT.

No queue-duration result and no EIA operating-value relationship has been computed. Incremental monetary cost remained **0 USD**.
