---
id: US-GRID-F01-SOURCE-PREFLIGHT
type: source-semantic-preflight
created: 2026-09-04
relationship_outcome_computed: false
eia_operating_values_opened: false
incremental_monetary_cost_usd: 0
---

# US-GRID-F01 Source Preflight / 소스 사전검증

## Exposure boundary / 노출 경계

- No queue-duration-by-operator result was computed.
- No EIA demand/generation/interchange operating values were opened for relationship analysis.
- Only source files, workbook/codebook semantics, operator/status vocabularies, BA identity reference data, hashes and mapping cardinality diagnostics were inspected.

## A. LBNL Queued Up 2026 workbook / LBNL workbook

- exact URL: `https://eta-publications.lbl.gov/sites/default/files/2026-05/lbnl_ix_queue_data_file_thru2025.xlsx`
- HTTP: `200`
- final URL: `https://eta-publications.lbl.gov/sites/default/files/2026-05/lbnl_ix_queue_data_file_thru2025.xlsx`
- bytes: **15571236**
- SHA-256: `794582d3281c6a305e9615fcfec3fae9dc85be2165216d33760b677e976a08b6`
- sheets (43): `['Introduction', 'Contents', '00. Background + Methods', '01. Balancing Areas', '02. Data Sample by Region', '03. Complete Queue Data', '04. Data Codebook', '05. Annual Requests', '06. Capacity Change YoY', '07. Active Capacity by Year', '08. Active Capacity by Type', '09. Active Cap. Region+Type', '10. Queues vs. Installed', '11. Active Cap. Maps', '12. Ix. Request Size Trends', '13. Other Gen. + Storage', '14. Hybrid Capacity', '15. ERIS + NRIS Capacity', '16. Cap. by Prop. Online Year', '17. Cap. by Ix. Phase', '18. IA Executed Capacity', '19. IA Throughput by Region', '20. ERAS and RRI Requests', '21. Operational Volume Trend', '22. Withdrawn Volume Trend', '23. Completion Rate Trend', '24. Comp. Rate Gen Type', '25. Comp. Rate Region', '26. Withdrawn Ix. Phase', '27. Post-IA Completion', '28. IR to WD', '29. IR to IA - all', '30. IR to IA - region', '31. IR to IA - type', '32. IR to IA - size', '33. IR to IA - service', '34. IA to COD - all', '35. IA to COD - region', '36. IA to COD - type', '37. IR to COD - all', '38. IR to COD - region', '39. IR to COD - type', '40. IR to COD - size']`

### Sheet row cardinality / sheet row 수

- `Introduction`: **39** rows
- `Contents`: **42** rows
- `00. Background + Methods`: **24** rows
- `01. Balancing Areas`: **20** rows
- `02. Data Sample by Region`: **27** rows
- `03. Complete Queue Data`: **38203** rows
- `04. Data Codebook`: **32** rows
- `05. Annual Requests`: **32** rows
- `06. Capacity Change YoY`: **15** rows
- `07. Active Capacity by Year`: **30** rows
- `08. Active Capacity by Type`: **200** rows
- `09. Active Cap. Region+Type`: **848** rows
- `10. Queues vs. Installed`: **33** rows
- `11. Active Cap. Maps`: **235** rows
- `12. Ix. Request Size Trends`: **67** rows
- `13. Other Gen. + Storage`: **28** rows
- `14. Hybrid Capacity`: **32** rows
- `15. ERIS + NRIS Capacity`: **61** rows
- `16. Cap. by Prop. Online Year`: **18** rows
- `17. Cap. by Ix. Phase`: **15** rows
- `18. IA Executed Capacity`: **21** rows
- `19. IA Throughput by Region`: **63** rows
- `20. ERAS and RRI Requests`: **28** rows
- `21. Operational Volume Trend`: **35** rows
- `22. Withdrawn Volume Trend`: **33** rows
- `23. Completion Rate Trend`: **36** rows
- `24. Comp. Rate Gen Type`: **16** rows
- `25. Comp. Rate Region`: **17** rows
- `26. Withdrawn Ix. Phase`: **108** rows
- `27. Post-IA Completion`: **105** rows
- `28. IR to WD`: **10697** rows
- `29. IR to IA - all`: **46** rows
- `30. IR to IA - region`: **2733** rows
- `31. IR to IA - type`: **2493** rows
- `32. IR to IA - size`: **4216** rows
- `33. IR to IA - service`: **3415** rows
- `34. IA to COD - all`: **27** rows
- `35. IA to COD - region`: **950** rows
- `36. IA to COD - type`: **839** rows
- `37. IR to COD - all`: **40** rows
- `38. IR to COD - region`: **1862** rows
- `39. IR to COD - type`: **1630** rows
- `40. IR to COD - size`: **2958** rows

- selected project sheet candidate: `03. Complete Queue Data`
- selected codebook sheet candidate: `04. Data Codebook`
- project data rows after header: **38201**
- duplicate-ID diagnostic: NOT_EVALUATED_NO_CLEAR_ID_COLUMN

### Project headers / project header

- column 1: `q_id`
- column 2: `q_status`
- column 3: `q_date`
- column 4: `prop_date`
- column 5: `on_date`
- column 6: `wd_date`
- column 7: `ia_date`
- column 8: `IA_phase_raw`
- column 9: `IA_phase_clean`
- column 10: `county`
- column 11: `state`
- column 12: `fips_code`
- column 13: `poi_name`
- column 14: `region`
- column 15: `project_name`
- column 16: `utility`
- column 17: `entity`
- column 18: `developer`
- column 19: `cluster`
- column 20: `service`
- column 21: `project_type`
- column 22: `type_1`
- column 23: `type_2`
- column 24: `type_3`
- column 25: `type_clean`
- column 26: `mw_1`
- column 27: `mw_2`
- column 28: `mw_3`
- column 29: `q_year`
- column 30: `prop_year`

### Codebook semantic hits / codebook 관련 semantics

- q_id | queue position / ID number | Combine with "entity" to form a unique identifier across the full dataset
- q_status | current queue status | One of: active, withdrawn, suspended, or operational
- q_date | interconnection request date (date project entered queue) | 
- prop_date | proposed online date from interconnection application | Proposed date can be revised during the interconnection process
- on_date | date project became operational (if applicable) | 
- wd_date | date project withdrawn from queue (if applicable) | 
- ia_date | date of signed interconnection agreement (if applicable) | 
- IA_phase_raw | non-standardized interconnection study phase / status from queue | 
- IA_phase_clean | standardized interconnection study phase / status | We impute "IA Executed" if q_status is "operational". One of: IA Executed, Withdrawn, System Impact Study, Feasibility Study, Facility Study, In Progress (unknown study), Cluster Study, IA Pending, Not Started, Construction, Suspended
- region | standardized region where project is located | One of: the 7 ISOs; and West (non-ISO) or Southeast (non-ISO)
- utility | utility name | Same as "entity" in non-ISO/RTO balancing areas
- entity | transmission provider entity name (ISO or utility) | One of the 57 regions listed on the 01. Balancing Areas sheet
- cluster | queue cluster (if applicable) | 
- project_type | type of project or interconnection request | One of: Generation, Surplus, Upgrade, or Replacement. Not all upgrades / uprates are identified
- q_year | year project entered queue | Derived from q_date
- prop_year | proposed online year from interconnection application | Derived from prop_date

### Identity/status vocabulary / identity·status vocabulary

- identity `region`: **9** unique → `['CAISO', 'ERCOT', 'ISO-NE', 'MISO', 'NYISO', 'PJM', 'SPP', 'Southeast', 'West']`
- identity `utility`: **387** unique → `['ABB Equity Ventures Inc', 'AEC', 'AECC', 'AEP', 'AEP/OGE', 'AES Indiana', 'AES Pacific Inc', 'AMEREN ILLINOIS', 'AMEREN MISSOURI', 'AMEREN TRANSMISSION COMPANY OF ILLINOIS', 'AMERICAN TRANSMISSION COMPANY', 'AMPT', 'APS', 'ARKANSAS ELECTRIC COOPERATIVE CORPORATION', 'ATSI', 'Alliant Energy East', 'Alliant Energy West', 'Ameren Missouri', 'American Transmission Co.', 'Arizona Public Service', 'Associated Electric Cooperative, Incorporated', 'Avangrid Power, LLC', 'Avista Corporation', 'Avista Power, LLC', 'Avista Utilities', 'BEPC', 'BGE', 'BHE', 'BIG RIVERS ELECTRIC CORPORATION', 'BP Energy Company', 'BPA Corporate', 'BPA Power Services', 'Basin Electric Power Cooperative', 'Blachly-Lane County Cooperative Electric Association', 'Black Hills Cheyenne Light Fuel and Power Transmission', 'Black Hills Colorado Electric', 'Black Hills Energy Capital Inc', 'Black Hills Power', 'CBPC', 'CHG&E', 'CHGE', 'CITY OF COLUMBIA, MISSOURI (WATER AND LIGHT DEPT.)', 'CITY WATER LIGHT & POWER', 'CLECO POWER', 'CMP', 'CONED', 'CONSUMERS ENERGY COMPANY', 'COOPERATIVE ENERGY', 'CPEC', 'Cal Geo Company', 'Calpine Energy Services, L.P.', 'Cannon Power Corporation', 'Cedar Hills Energy LLC', 'CenHud', 'Chelan County Public Utility District', 'Cielo Wind Power', 'City Water Light & Power (CWLP)', 'City of Columbia, MO', 'City of Independence MO', 'City of Springfield, IL - CWLP', 'City of Tacoma, Department of Public Utilities, Light Division', 'City of Whitefish, Montana', 'Clark Public Utilities', "Clatskanie People's Utility District", 'Cleco Power LLC', 'Clipper Windpower Development, Inc.', 'Coastal Energy Project, LLC', 'Coberg Power LLC', 'Cogentrix Energy, Inc.', 'Colorado Springs Utilities', 'Columbia Rural Electric Association', 'ComEd', 'ConED', 'ConEd', 'ConEd/O&R', 'Coned', 'Confederated Tribes Umatilla Indian Reservation', 'Consumers Energy', 'Continental Energy Services, Inc.', 'DAIRYLAND POWER COOPERATIVE', 'DCRT', 'DEMCO', 'DEOK', 'DL', 'DPL', 'DSLK', 'DTE Electric', 'DUKE ENERGY INDIANA', 'Dayton', 'Dominion', 'Dominion Energy South Carolina', 'Duke', 'Duke Energy Carolinas', 'Duke Energy Corporation', 'Duke Energy Florida', 'Duke Energy North America, LLC', 'Duke Energy Progress', 'EAST TEXAS ELECTRIC COOPERATIVE, INC.', 'EDE', 'EDP Renewables North America LLC', 'EKPC', 'EMDE', 'ENTERGY ARKANSAS', 'ENTERGY ARKANSAS INC.', 'ENTERGY LOUISIANA', 'ENTERGY MISSISSIPPI', 'ENTERGY MISSISSIPPI, LLC.', 'ENTERGY NEW ORLEANS', 'ENTERGY TEXAS, INC.', 'EREC', 'ETEC', 'Effective Energy Corporation', 'El Paso Electric Company', 'Energy Northwest (CGS)', 'Energy Northwest Inc', 'Enron Power Marketing, Inc.', 'Entergy', 'Entergy Louisiana, LLC', 'Entergy Mississippi, LLC', 'Entergy Texas, Inc.', 'Essential Power', 'Eugene Water & Electric Board', 'Eurus Combine Hills II LLC', 'Evergy', 'F.H. Stoltze Land and Lumber Co.', 'FPL Energy Power Marketing Inc', 'FPL Energy Vansycle L.L.C.', 'Farm Power Misty Meadow, LLC', 'Farm Power Tillamook LLC', 'Flathead Electric Cooperative, Inc.', 'Florida Power & Light', 'Fort Rock Interconnection II LLC', 'Frederickson Power, LP', 'Frontier Technology, Inc', 'GHP', 'GLW', 'GMO', 'GNA Energy, LLC', 'GRDA', 'GREAT RIVER ENERGY', 'Georgia Transmission', 'Goldendale Energy Center, LLC', 'Goose Prairie Solar LLC', 'Grant County Public Utility District', 'Grant Generation, LLC', 'Grays Harbor Energy LLC', 'Great River Energy (GRE)', 'Green Energy Today, LLC', 'GridLiance', 'GridUnity', 'HENDERSON UTILITY COMM DBA HENDERSON MUNICIPAL POWER AND LIGHT', 'HOOSIER ENERGY', 'HOOSIER ENERGY REC, INC', 'Hallador Power', 'Harvest Wind Project', 'Hoosier Energy', 'Horse Butte Wind I LLC', 'IID', 'INDIANAPOLIS POWER & LIGHT COMPANY', 'INDN', 'ITC', 'ITC MIDWEST', 'ITCGP', 'ITCI', 'Idaho Power Company', 'Imperial Irrigation District', 'Indiana Municipal Power Agency (IMPA)', 'Interstate Power and Light Company (IPL)', 'Invenergy Wind Development LLC', 'J P Saylor & Associates', 'JCPL', 'Jacksonville Electric Authority', 'KACP', 'KACY', 'KCPL', 'KPP', 'Klondike Wind Power II, LLC', 'Klondike Wind Power III, LLC', 'Klondike Wind Power, LLC', 'Kootenai Electric Cooperative, Inc.', 'LAFAYETTE UTILITIES SYSTEM', 'LCEC', 'LEA', 'LES', 'LIPA', 'LS Power', 'LS Power/NYPA', 'LSPC', 'LSPower', 'LYREC', 'Lane Electric Cooperative, Inc.', 'Lifeline Renewable Energy, Inc.', 'Lilliwaup Falls Generating Company', 'Los Angeles Department of Water and Power', 'Louisville Gas & Electric and Kentucky Utilities Energy', 'MC Boonville', 'ME', 'METC', 'MICHIGAN PUBLIC POWER AGENCY', 'MIDAMERICAN ENERGY CO.', 'MIDAMERICAN ENERGY COMPANY', 'MIDW', 'MINNESOTA MUNICIPAL POWER AGENCY', 'MINNESOTA POWER', 'MINNESOTA POWER INC.', 'MIPU', 'MISSOURI RIVER ENERGY SERVICES', 'MISSOURI RIVER ENERGY SERVICES - TRANSMISSION', 'MKEC', 'MMPA (Minnesota Municipal Power Agency)', 'MONTANA-DAKOTA UTILITIES CO.', 'MPS', 'MUSCATINE POWER AND WATER', 'MWEC', 'MidAmerican Energy Company', 'Minnesota Power', 'Minnkota Power Cooperative', 'N/A', 'NEET', 'NEETSW', 'NGRID', 'NGrid', 'NIPCO', 'NIPSCO', 'NM-NG', 'NM-NG/NYSEG', 'NM/CONED', 'NORTHERN INDIANA PUBLIC SERVICE COMPANY', 'NORTHERN STATES POWER COMPANY', 'NPPD', 'NSTAR', 'NU', 'NV Energy', 'NWPS', 'NYPA', 'NYPA ConEd', 'NYPA/NM-NG', 'NYSEG', 'NYSEG, NM-NG', 'NYSEG/NM-NG', 'NYSEG;', 'NYTransco', 'NYTransco/NM-NG', 'National Energy & Gas Transmission, Inc.', 'Navajo-Crystal', 'NewSun Energy Transmission Company LLC', 'Newport Northwest, LLC', 'NextEra', 'NextEra Energy Resources, LLC', 'Nippon Paper Industries USA Co., Ltd.', 'Nordic Energy Barge #1, LLC', 'Nordic Energy Barge #2, LLC', 'NorthWestern Energy', "Northern Wasco County People's Utility District", 'Northwestern Wind Power, LLC', 'O & R', 'O&R', 'ODEC', 'OG&E', 'OGE', 'OGE/AEP', 'OPPD', 'OTTER TAIL POWER COMPANY', 'OVEC', "Olympic Converter, LP - Don'T Use", 'Or-Cal Power, Inc.', 'Orcas Power & Light Cooperative', 'Oregon Energy Company LLC', 'Oregon Wind, LLC', 'Orion Energy, LLC', 'Orlando Utilities Commission', 'Otter Tail Power Company', 'Outback Solar, LLC', 'PEC', 'PECO', 'PENELEC', 'PEPCO', 'PG&E', 'PG&E Energy Services', 'PGAE', 'PJM', 'PPL', 'PRAIRIE POWER, INC.', 'PSEG', 'PSEG; PSEG', 'PacifiCorp', 'Pacific Wind Development, LLC', 'Pacific Winds, Inc.', 'Peoples Energy Resources Corporation', 'Platte River Power Authority', 'Plymouth Energy, LLC', 'Port of Tillamook Bay', 'Portland General Electric', 'Portland General Electric Company', 'Public Service Company Of Colorado', 'Public Service Company of New Mexico', 'Public Utility District No. 1 of Benton County', 'Public Utility District No. 1 of Snohomish County', 'Puget Sound Energy', 'Puget Sound Energy, Inc.', 'RE', 'RECO', 'RES North America', 'RG&E', 'RGE', 'ROCHESTER PUBLIC UTILITIES', 'Riley Interconnection LLC', 'Rochester Public Utilities', 'Rock Creek Hydro LLC', 'SCE', 'SDGE', 'SEPC', 'SMECO', 'SMMPA', 'SOUTH MISSISSIPPI ELECTRIC POWER ASSOCIATION', 'SOUTHERN INDIANA GAS & ELECTRIC COMPANY D/B/A CENTERPOINT ENERGY INDIANA SOUTH', 'SOUTHERN MINNESOTA MUNICIPAL POWER AGENCY', 'SPRM', 'SPS', 'SUNC', 'SWPA', 'Sacramento Municipal Utility District', 'Sagebrush Power Partners, LLC', 'Salt River Project', 'Santee Cooper', 'Seawest Windpower, Inc.', 'Seminole Electric Cooperative', 'Sempra Generation, LLC', 'Shepherds Flat Wind, LLC', 'Southern Company', 'Southern Illinois Power Cooperative', 'Southern Indiana Gas & Electric Company d/b/a Centerpoint Energy Indiana South', 'Southern Indiana Gas & Electric Company d/b/a Vectren Energy Delivery of Indiana, Inc.', 'Summit Power Northwest Project, LLC', 'TMO', 'TSGT', 'Tacoma Public Utilities', 'Tampa Electric Company', 'Tenaska, Inc.', 'Tennessee Valley Authority', 'The City of Seattle, City Light Department', 'Three Sisters Irrigation District', 'TransAlta Utilities Cooperative', 'Transco', 'Tri-State', 'Tri-State Generation and Transmission Association', 'Tucson Electric Power Company', 'UGI', 'UI', 'US Electric Power Corporation', 'US Geothermal, Inc.', 'Umatilla Electric Cooperative', 'University of Oregon', 'Unknown', 'VEA', 'Village of Arcade', 'WABASH VALLEY POWER ASSOCIATION, INC.', 'WAPA', 'WAPA Desert Southwest Region', 'WAPA Rocky Mountain Region', 'WAPA Sierra Nevada', 'WAPA/BEPC/HCPD Integrated System', 'WEPL', 'WERE', 'WFEC', 'WFEC & SWPA', 'WM Renewable Energy, LLC', 'WOLVERINE POWER SUPPLY COOPERATIVE', 'WPEK', 'Washington Winds, Inc.', 'Wheat Field Power Partners, LLC', 'Wheatridge Solar Energy Center, LLC', 'Wheatridge Wind Energy, LLC', 'Whistling Ridge Energy, LLC', 'White Creek Wind I, LLC', 'Wind Ridge Power Partners, LLC', 'Windland, Inc.', 'Winds Over Washington Energy Group', 'Windtricity Ventures', 'Windy Point Partners, LLC', 'Wisconsin Electric', 'Wisconsin Electric Power Company', 'Wisconsin Power and Light Company (WPL)', 'Xcel', 'Xcel Energy', 'Xcel/SPS', 'enXco Northwest']`
- status `q_status`: **5** unique → `['active', 'operational', 'suspended', 'unknown', 'withdrawn']`

### Direct outcome semantic diagnostic / 직접 outcome semantics

- IR/request semantic present: **True**
- COD/commercial-operation semantic present: **True**
- prospective priority outcome status: **`IR_TO_COD_DURATION`**

## B. EIA public identity routes / EIA 공개 identity 경로

- EIA bulk manifest URL: `https://www.eia.gov/opendata/bulk/manifest.txt`
- HTTP: `200`
- final URL: `https://www.eia.gov/opendata/bulk/manifest.txt`
- manifest SHA-256: `cb3a0ea50cf473367c9c92bcc8561ed2a5ca10bd6c06cb989e65835a179a8722`
- current operating-data target entries detected: **1**

- title=`U.S. Electric System Operating Data (Older Than 7 Days)` identifier=`EBA` last_updated=`2026-09-03T05:04:09-04:00` accessURL=`https://www.eia.gov/opendata/bulk/EBA.zip`
- target asset HEAD: `200`; final URL `https://www.eia.gov/opendata/bulk/EBA.zip`; content-type `application/x-zip-compressed`; content-length `686467513`

### Supporting EIA-861 2025 early-release BA identity snapshot / 보조 BA identity

- ZIP URL: `https://www.eia.gov/electricity/data/eia861/zip/f8612025er.zip`
- HTTP: `200`
- ZIP SHA-256: `bcbba24da0071114dfa6080b4f63989717e23f159a0ace63ffd5cb82098b9a50`
- ZIP members: `['Energy_Efficiency_2025_Data_Early_Release.xlsx', 'Frame_2025_Data_Early_Release.xlsx', 'Mergers_2025_Data_Early_Release.xlsx', 'Net_Metering_2025_Data_Early_Release.xlsx', 'Non_Net_Metering_Distributed_2025_Data_Early_Release.xlsx', 'Operational_Data_2025_Data_Early_Release.xlsx', 'Reliability_2025_Data_Early_Release.xlsx', 'Sales_Ult_Cust_2025_Data_Early_Release.xlsx', 'Sales_Ult_Cust_CS_2025_Data_Early_Release.xlsx', 'Service_Territory_2025_Data_Early_Release.xlsx', 'Short_Form_2025_Data_Early_Release.xlsx', 'Utility_Data_2025_Data_Early_Release.xlsx', 'Advanced_Meters_2025_Data_Early_Release.xlsx', 'Balancing_Authority_2025_Data_Early_Release.xlsx', 'Delivery_Companies_2025_Data_Early_Release.xlsx', 'Demand_Response_2025_Data_Early_Release.xlsx', 'Distribution_Systems_2025_Data_Early_Release.xlsx', 'Dynamic_Pricing_2025_Data_Early_Release.xlsx']`
- balancing-authority file candidate(s): `['Balancing_Authority_2025_Data_Early_Release.xlsx']`
- parsed BA records: **187**
- unique BA names: **64**
- unique BA codes: **0**
- BA headers: `[(2, 'Data Year'), (3, 'BA ID'), (4, 'BA Code'), (5, 'State'), (6, 'Balancing Authority Name')]`

## C. Conservative operator/BA exact-identity diagnostic / 보수적 exact identity 진단

- LBNL identity values across detected operator/region-like columns: **395**
- exact normalized EIA name/code matches: **17**
- unmatched: **378**
- ambiguous exact matches: **0**
- exact-match ratio: **0.043038**

### Exact matches

- `Avista Corporation` → `name` `Avista Corporation`
- `City of Tacoma, Department of Public Utilities, Light Division` → `name` `City of Tacoma, Department of Public Utilities, Light Division`
- `Dominion Energy South Carolina` → `name` `Dominion Energy South Carolina`
- `Duke Energy Carolinas` → `name` `Duke Energy Carolinas`
- `El Paso Electric Company` → `name` `El Paso Electric Company`
- `Idaho Power Company` → `name` `Idaho Power Company`
- `Imperial Irrigation District` → `name` `Imperial Irrigation District`
- `Los Angeles Department of Water and Power` → `name` `Los Angeles Department of Water and Power`
- `Portland General Electric Company` → `name` `Portland General Electric Company`
- `Public Service Company Of Colorado` → `name` `Public Service Company of Colorado`
- `Public Service Company of New Mexico` → `name` `Public Service Company of New Mexico`
- `Puget Sound Energy` → `name` `Puget Sound Energy`
- `Salt River Project` → `name` `Salt River Project`
- `Seminole Electric Cooperative` → `name` `Seminole Electric Cooperative`
- `Tampa Electric Company` → `name` `Tampa Electric Company`
- `Tennessee Valley Authority` → `name` `Tennessee Valley Authority`
- `Tucson Electric Power Company` → `name` `Tucson Electric Power Company`

### Unmatched LBNL identities

- `ABB Equity Ventures Inc`
- `AEC`
- `AECC`
- `AEP`
- `AEP/OGE`
- `AES Indiana`
- `AES Pacific Inc`
- `AMEREN ILLINOIS`
- `AMEREN MISSOURI`
- `AMEREN TRANSMISSION COMPANY OF ILLINOIS`
- `AMERICAN TRANSMISSION COMPANY`
- `AMPT`
- `APS`
- `ARKANSAS ELECTRIC COOPERATIVE CORPORATION`
- `ATSI`
- `Alliant Energy East`
- `Alliant Energy West`
- `Ameren Missouri`
- `American Transmission Co.`
- `Arizona Public Service`
- `Associated Electric Cooperative, Incorporated`
- `Avangrid Power, LLC`
- `Avista Power, LLC`
- `Avista Utilities`
- `BEPC`
- `BGE`
- `BHE`
- `BIG RIVERS ELECTRIC CORPORATION`
- `BP Energy Company`
- `BPA Corporate`
- `BPA Power Services`
- `Basin Electric Power Cooperative`
- `Blachly-Lane County Cooperative Electric Association`
- `Black Hills Cheyenne Light Fuel and Power Transmission`
- `Black Hills Colorado Electric`
- `Black Hills Energy Capital Inc`
- `Black Hills Power`
- `CAISO`
- `CBPC`
- `CHG&E`
- `CHGE`
- `CITY OF COLUMBIA, MISSOURI (WATER AND LIGHT DEPT.)`
- `CITY WATER LIGHT & POWER`
- `CLECO POWER`
- `CMP`
- `CONED`
- `CONSUMERS ENERGY COMPANY`
- `COOPERATIVE ENERGY`
- `CPEC`
- `Cal Geo Company`
- `Calpine Energy Services, L.P.`
- `Cannon Power Corporation`
- `Cedar Hills Energy LLC`
- `CenHud`
- `Chelan County Public Utility District`
- `Cielo Wind Power`
- `City Water Light & Power (CWLP)`
- `City of Columbia, MO`
- `City of Independence MO`
- `City of Springfield, IL - CWLP`
- `City of Whitefish, Montana`
- `Clark Public Utilities`
- `Clatskanie People's Utility District`
- `Cleco Power LLC`
- `Clipper Windpower Development, Inc.`
- `Coastal Energy Project, LLC`
- `Coberg Power LLC`
- `Cogentrix Energy, Inc.`
- `Colorado Springs Utilities`
- `Columbia Rural Electric Association`
- `ComEd`
- `ConED`
- `ConEd`
- `ConEd/O&R`
- `Coned`
- `Confederated Tribes Umatilla Indian Reservation`
- `Consumers Energy`
- `Continental Energy Services, Inc.`
- `DAIRYLAND POWER COOPERATIVE`
- `DCRT`
- `DEMCO`
- `DEOK`
- `DL`
- `DPL`
- `DSLK`
- `DTE Electric`
- `DUKE ENERGY INDIANA`
- `Dayton`
- `Dominion`
- `Duke`
- `Duke Energy Corporation`
- `Duke Energy Florida`
- `Duke Energy North America, LLC`
- `Duke Energy Progress`
- `EAST TEXAS ELECTRIC COOPERATIVE, INC.`
- `EDE`
- `EDP Renewables North America LLC`
- `EKPC`
- `EMDE`
- `ENTERGY ARKANSAS`
- `ENTERGY ARKANSAS INC.`
- `ENTERGY LOUISIANA`
- `ENTERGY MISSISSIPPI`
- `ENTERGY MISSISSIPPI, LLC.`
- `ENTERGY NEW ORLEANS`
- `ENTERGY TEXAS, INC.`
- `ERCOT`
- `EREC`
- `ETEC`
- `Effective Energy Corporation`
- `Energy Northwest (CGS)`
- `Energy Northwest Inc`
- `Enron Power Marketing, Inc.`
- `Entergy`
- `Entergy Louisiana, LLC`
- `Entergy Mississippi, LLC`
- `Entergy Texas, Inc.`
- `Essential Power`
- `Eugene Water & Electric Board`
- `Eurus Combine Hills II LLC`
- `Evergy`
- `F.H. Stoltze Land and Lumber Co.`
- `FPL Energy Power Marketing Inc`
- `FPL Energy Vansycle L.L.C.`
- `Farm Power Misty Meadow, LLC`
- `Farm Power Tillamook LLC`
- `Flathead Electric Cooperative, Inc.`
- `Florida Power & Light`
- `Fort Rock Interconnection II LLC`
- `Frederickson Power, LP`
- `Frontier Technology, Inc`
- `GHP`
- `GLW`
- `GMO`
- `GNA Energy, LLC`
- `GRDA`
- `GREAT RIVER ENERGY`
- `Georgia Transmission`
- `Goldendale Energy Center, LLC`
- `Goose Prairie Solar LLC`
- `Grant County Public Utility District`
- `Grant Generation, LLC`
- `Grays Harbor Energy LLC`
- `Great River Energy (GRE)`
- `Green Energy Today, LLC`
- `GridLiance`
- `GridUnity`
- `HENDERSON UTILITY COMM DBA HENDERSON MUNICIPAL POWER AND LIGHT`
- `HOOSIER ENERGY`
- `HOOSIER ENERGY REC, INC`
- `Hallador Power`
- `Harvest Wind Project`
- `Hoosier Energy`
- `Horse Butte Wind I LLC`
- `IID`
- `INDIANAPOLIS POWER & LIGHT COMPANY`
- `INDN`
- `ISO-NE`
- `ITC`
- `ITC MIDWEST`
- `ITCGP`
- `ITCI`
- `Indiana Municipal Power Agency (IMPA)`
- `Interstate Power and Light Company (IPL)`
- `Invenergy Wind Development LLC`
- `J P Saylor & Associates`
- `JCPL`
- `Jacksonville Electric Authority`
- `KACP`
- `KACY`
- `KCPL`
- `KPP`
- `Klondike Wind Power II, LLC`
- `Klondike Wind Power III, LLC`
- `Klondike Wind Power, LLC`
- `Kootenai Electric Cooperative, Inc.`
- `LAFAYETTE UTILITIES SYSTEM`
- `LCEC`
- `LEA`
- `LES`
- `LIPA`
- `LS Power`
- `LS Power/NYPA`
- `LSPC`
- `LSPower`
- `LYREC`
- `Lane Electric Cooperative, Inc.`
- `Lifeline Renewable Energy, Inc.`
- `Lilliwaup Falls Generating Company`
- `Louisville Gas & Electric and Kentucky Utilities Energy`
- `MC Boonville`
- `ME`
- `METC`
- `MICHIGAN PUBLIC POWER AGENCY`
- `MIDAMERICAN ENERGY CO.`
- `MIDAMERICAN ENERGY COMPANY`
- `MIDW`
- `MINNESOTA MUNICIPAL POWER AGENCY`
- `MINNESOTA POWER`
- `MINNESOTA POWER INC.`
- `MIPU`
- `MISO`
- `MISSOURI RIVER ENERGY SERVICES`
- `MISSOURI RIVER ENERGY SERVICES - TRANSMISSION`
- `MKEC`
- `MMPA (Minnesota Municipal Power Agency)`
- `MONTANA-DAKOTA UTILITIES CO.`
- `MPS`
- `MUSCATINE POWER AND WATER`
- `MWEC`
- `MidAmerican Energy Company`
- `Minnesota Power`
- `Minnkota Power Cooperative`
- `N/A`
- `NEET`
- `NEETSW`
- `NGRID`
- `NGrid`
- `NIPCO`
- `NIPSCO`
- `NM-NG`
- `NM-NG/NYSEG`
- `NM/CONED`
- `NORTHERN INDIANA PUBLIC SERVICE COMPANY`
- `NORTHERN STATES POWER COMPANY`
- `NPPD`
- `NSTAR`
- `NU`
- `NV Energy`
- `NWPS`
- `NYISO`
- `NYPA`
- `NYPA ConEd`
- `NYPA/NM-NG`
- `NYSEG`
- `NYSEG, NM-NG`
- `NYSEG/NM-NG`
- `NYSEG;`
- `NYTransco`
- `NYTransco/NM-NG`
- `National Energy & Gas Transmission, Inc.`
- `Navajo-Crystal`
- `NewSun Energy Transmission Company LLC`
- `Newport Northwest, LLC`
- `NextEra`
- `NextEra Energy Resources, LLC`
- `Nippon Paper Industries USA Co., Ltd.`
- `Nordic Energy Barge #1, LLC`
- `Nordic Energy Barge #2, LLC`
- `NorthWestern Energy`
- `Northern Wasco County People's Utility District`
- `Northwestern Wind Power, LLC`
- `O & R`
- `O&R`
- `ODEC`
- `OG&E`
- `OGE`
- `OGE/AEP`
- `OPPD`
- `OTTER TAIL POWER COMPANY`
- `OVEC`
- `Olympic Converter, LP - Don'T Use`
- `Or-Cal Power, Inc.`
- `Orcas Power & Light Cooperative`
- `Oregon Energy Company LLC`
- `Oregon Wind, LLC`
- `Orion Energy, LLC`
- `Orlando Utilities Commission`
- `Otter Tail Power Company`
- `Outback Solar, LLC`
- `PEC`
- `PECO`
- `PENELEC`
- `PEPCO`
- `PG&E`
- `PG&E Energy Services`
- `PGAE`
- `PJM`
- `PPL`
- `PRAIRIE POWER, INC.`
- `PSEG`
- `PSEG; PSEG`
- `PacifiCorp`
- `Pacific Wind Development, LLC`
- `Pacific Winds, Inc.`
- `Peoples Energy Resources Corporation`
- `Platte River Power Authority`
- `Plymouth Energy, LLC`
- `Port of Tillamook Bay`
- `Portland General Electric`
- `Public Utility District No. 1 of Benton County`
- `Public Utility District No. 1 of Snohomish County`
- `Puget Sound Energy, Inc.`
- `RE`
- `RECO`
- `RES North America`
- `RG&E`
- `RGE`
- `ROCHESTER PUBLIC UTILITIES`
- `Riley Interconnection LLC`
- `Rochester Public Utilities`
- `Rock Creek Hydro LLC`
- `SCE`
- `SDGE`
- `SEPC`
- `SMECO`
- `SMMPA`
- `SOUTH MISSISSIPPI ELECTRIC POWER ASSOCIATION`
- `SOUTHERN INDIANA GAS & ELECTRIC COMPANY D/B/A CENTERPOINT ENERGY INDIANA SOUTH`
- `SOUTHERN MINNESOTA MUNICIPAL POWER AGENCY`
- `SPP`
- `SPRM`
- `SPS`
- `SUNC`
- `SWPA`
- `Sacramento Municipal Utility District`
- `Sagebrush Power Partners, LLC`
- `Santee Cooper`
- `Seawest Windpower, Inc.`
- `Sempra Generation, LLC`
- `Shepherds Flat Wind, LLC`
- `Southeast`
- `Southern Company`
- `Southern Illinois Power Cooperative`
- `Southern Indiana Gas & Electric Company d/b/a Centerpoint Energy Indiana South`
- `Southern Indiana Gas & Electric Company d/b/a Vectren Energy Delivery of Indiana, Inc.`
- `Summit Power Northwest Project, LLC`
- `TMO`
- `TSGT`
- `Tacoma Public Utilities`
- `Tenaska, Inc.`
- `The City of Seattle, City Light Department`
- `Three Sisters Irrigation District`
- `TransAlta Utilities Cooperative`
- `Transco`
- `Tri-State`
- `Tri-State Generation and Transmission Association`
- `UGI`
- `UI`
- `US Electric Power Corporation`
- `US Geothermal, Inc.`
- `Umatilla Electric Cooperative`
- `University of Oregon`
- `Unknown`
- `VEA`
- `Village of Arcade`
- `WABASH VALLEY POWER ASSOCIATION, INC.`
- `WAPA`
- `WAPA Desert Southwest Region`
- `WAPA Rocky Mountain Region`
- `WAPA Sierra Nevada`
- `WAPA/BEPC/HCPD Integrated System`
- `WEPL`
- `WERE`
- `WFEC`
- `WFEC & SWPA`
- `WM Renewable Energy, LLC`
- `WOLVERINE POWER SUPPLY COOPERATIVE`
- `WPEK`
- `Washington Winds, Inc.`
- `West`
- `Wheat Field Power Partners, LLC`
- `Wheatridge Solar Energy Center, LLC`
- `Wheatridge Wind Energy, LLC`
- `Whistling Ridge Energy, LLC`
- `White Creek Wind I, LLC`
- `Wind Ridge Power Partners, LLC`
- `Windland, Inc.`
- `Winds Over Washington Energy Group`
- `Windtricity Ventures`
- `Windy Point Partners, LLC`
- `Wisconsin Electric`
- `Wisconsin Electric Power Company`
- `Wisconsin Power and Light Company (WPL)`
- `Xcel`
- `Xcel Energy`
- `Xcel/SPS`
- `enXco Northwest`

## D. Interpretation / 해석

- The official LBNL workbook/codebook exposes source semantics sufficient to prospectively prioritize IR→COD elapsed duration for completed projects, without calculating any duration distribution in F01.
- Exact-name/code matching is a conservative diagnostic only. Unmatched identities are **not** fuzzy-matched, state-mapped, or service-territory inferred in this preflight.

## E. Errors / bounded unresolved diagnostics

- none

## F. Next gate / 다음 gate

**`CONTINUE_US_GRID_F01_IDENTITY_ADJUDICATION`**

Before PASS/PARTIAL/HOLD/REJECT, adjudicate unmatched identity semantics using only explicit LBNL/EIA source definitions or a prospectively documented one-to-one alias rule. Do not open EIA operating values or queue-vs-grid relationship outcomes to make that decision.

Incremental monetary cost remained **0 USD**.
