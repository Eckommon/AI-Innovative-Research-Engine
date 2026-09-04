---
id: CA-RAIL-F01-SOURCE-PREFLIGHT
type: outcome-blind-source-preflight
created: 2026-09-04
relationship_outcome_computed: false
weather_values_opened: false
rail_dwell_magnitudes_persisted: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-F01 Source Preflight

No weather observations or rail-weather relationship were computed. Target dwell magnitudes were not persisted.

## A. Transport Canada frozen source

- page: https://tdih-cdit.tc.canada.ca/en/rail-2023
- page SHA-256: `a38c15636c7c6746c514669c37a2eccb188d4b994f2013d063c018c5bf5de5a3`
- ZIP: https://tdih-cdit.tc.canada.ca/sites/default/files/ferroviaire-rail.zip
- ZIP bytes: **36317934**
- ZIP SHA-256: `e29cd33ea9e65601b4945b7d196cef0fbd539831377a7666ce0ea65886dfd088`

### Annual English members

| Member | Bytes | SHA-256 |
|---|---:|---|
| weekly_rail_system_performance_indicators_eng_2023.csv | 76654234 | c9042cd4fbd0f81bb34a58c8649930a0159da2e2faf9007e00076b86d4c9f4d6 |
| weekly_rail_system_performance_indicators_eng_2024.csv | 107019893 | e901de6d3b4398b0414907cb3f7164a5cb1ee761fcc5ad9bfc77585d56d10b9f |
| weekly_rail_system_performance_indicators_eng_2025.csv | 105251502 | 75d62bc5f9c76c81742bb23a9a3a7f306e67ca264d1fab442d0a958c809acda4 |
| weekly_rail_system_performance_indicators_eng_2026.csv | 68819740 | ddddfdad0e40961a1a1188996bb1f67bc46a5f0102ec433e2d7684fc5032cec4 |

- schema identical across 2023–2026: **YES**
- exact 25-column schema: ['Reference_Date', 'Carrier_SortId', 'Carrier', 'Measure_SortId', 'Measure', 'Unit_of_Measure', 'Geography_SortId', 'Geography', 'Segment_Distance_km', 'Commodity_SortId', 'Commodity', 'Car_Type_SortId', 'Car_Type', 'Dwell_Time_Range_SortId', 'Dwell_Time_Range', 'Fleet_Status_SortId', 'Fleet_Status', 'Employee_Type_SortId', 'Employee_Type', 'Measure_Value', 'Status_of_Value', 'Rowid', 'Coordinate_Dimension', 'Coordinate_Sort', 'Last_Updated']

## B. Frozen target outcome structure

- target: **Average Terminal Dwell Time - Loaded Cars and Intermodal Containers**
- target rows, all geographies/dimensions: **43365**
- target rows on carrier-specific terminal areas: **39294**
- annual target counts: {'2023': 9310, '2024': 12985, '2025': 12740, '2026': 8330}
- unique terminal-area labels: **22**
- unique place tokens: **15**
- reference-date range among terminal-area target rows: **2023-04-10 .. 2026-08-24**
- carriers: {'CN': 19470, 'CPKC': 19470, 'BNSF': 354}
- units: {'Hours': 39294}
- statuses: {'0 - Available': 39263, '1 - Not Available': 20, '2 - Not Available Long-term': 11}
- car types: {'Not Applicable': 38940, 'Loaded cars and intermodal containers combined (BNSF)': 354}
- commodities: {'All Western grain': 3540, 'Agricultural products and food': 3540, 'All Forest products': 3540, 'Chemicals and plastics': 3540, 'Fertilizers': 3540, 'All Petroleum products, including liquefied petroleum gases': 3540, 'Coal and petroleum coke': 3540, 'All Metals and minerals': 3540, 'Motor vehicles and equipment': 3540, 'Other products': 3540, 'Intermodal containers': 3540, 'Not Applicable': 354}
- dwell ranges: {'Not Applicable': 39294}
- employee types: {'Not Applicable': 39294}
- fleet status: {'Not Applicable': 39294}
- segment distance: {'0.0': 39294}
- Last_Updated distinct values by source year: {'2023': ['2023-04-25', '2023-04-27', '2023-05-09', '2023-05-11', '2023-05-18', '2023-05-25', '2023-06-01', '2023-06-08', '2023-06-15', '2023-06-22', '2023-06-29', '2023-07-06', '2023-07-12', '2023-07-20', '2023-07-27', '2023-08-02', '2023-08-09', '2023-08-16', '2023-08-29', '2023-08-30', '2023-09-07', '2023-09-14', '2023-09-20', '2023-09-27', '2023-10-04', '2023-10-11', '2023-10-18', '2023-10-27', '2023-11-02', '2023-11-08', '2023-11-16', '2023-11-22', '2023-11-30', '2023-12-07', '2023-12-14', '2023-12-20', '2023-12-28', '2024-01-04'], '2024': ['2024-01-11', '2024-01-18', '2024-01-25', '2024-02-01', '2024-02-08', '2024-02-14', '2024-02-21', '2024-02-28', '2024-03-06', '2024-03-13', '2024-03-21', '2024-03-28', '2024-04-03', '2024-04-10', '2024-04-17', '2024-04-25', '2024-05-01', '2024-05-09', '2024-05-15', '2024-05-22', '2024-05-30', '2024-06-06', '2024-06-12', '2024-06-20', '2024-06-26', '2024-07-03', '2024-07-11', '2024-07-18', '2024-07-24', '2024-08-01', '2024-08-07', '2024-08-14', '2024-08-21', '2024-08-29', '2024-09-05', '2024-09-11', '2024-09-18', '2024-09-25', '2024-10-02', '2024-10-10', '2024-10-16', '2024-10-23', '2024-10-30', '2024-11-06', '2024-11-13', '2024-11-21', '2024-11-27', '2024-12-04', '2024-12-11', '2024-12-18', '2024-12-29', '2025-01-06', '2025-01-09'], '2025': ['2025-01-15', '2025-01-23', '2025-01-30', '2025-02-05', '2025-02-13', '2025-02-19', '2025-02-26', '2025-03-05', '2025-03-12', '2025-03-21', '2025-03-26', '2025-04-02', '2025-04-09', '2025-04-16', '2025-04-23', '2025-04-30', '2025-05-09', '2025-05-14', '2025-05-21', '2025-05-28', '2025-06-05', '2025-06-11', '2025-06-18', '2025-06-26', '2025-07-03', '2025-07-09', '2025-07-18', '2025-07-24', '2025-07-30', '2025-08-07', '2025-08-13', '2025-08-20', '2025-08-27', '2025-09-11', '2025-09-12', '2025-09-18', '2025-09-25', '2025-10-01', '2025-10-08', '2025-10-17', '2025-10-22', '2025-10-29', '2025-11-05', '2025-11-13', '2025-11-19', '2025-11-26', '2025-12-04', '2025-12-10', '2025-12-18', '2026-01-05', '2026-01-08'], '2026': ['2026-01-14', '2026-01-22', '2026-01-28', '2026-02-04', '2026-02-11', '2026-02-19', '2026-02-25', '2026-03-05', '2026-03-11', '2026-03-18', '2026-03-26', '2026-04-01', '2026-04-09', '2026-04-16', '2026-04-23', '2026-04-29', '2026-05-07', '2026-05-13', '2026-05-20', '2026-05-27', '2026-06-03', '2026-06-11', '2026-06-18', '2026-06-25', '2026-07-02', '2026-07-08', '2026-07-15', '2026-07-23', '2026-07-30', '2026-08-06', '2026-08-13', '2026-08-20', '2026-08-26', '2026-09-02']}
- numeric target cells: **39294**
- blank/non-numeric target cells: **0**
- duplicate full structural identities: **0**; max multiplicity **1**

### Terminal-area geography labels

- BNSF terminal area, Vancouver: 177
- BNSF terminal area, Winnipeg: 177
- CN terminal area, Edmonton: 1947
- CN terminal area, Kamloops: 1947
- CN terminal area, Montreal: 1947
- CN terminal area, Prince George: 1947
- CN terminal area, Prince Rupert: 1947
- CN terminal area, Sarnia: 1947
- CN terminal area, Saskatoon: 1947
- CN terminal area, Toronto: 1947
- CN terminal area, Vancouver: 1947
- CN terminal area, Winnipeg: 1947
- CPKC terminal area, Calgary: 1947
- CPKC terminal area, Edmonton: 1947
- CPKC terminal area, Lethbridge: 1947
- CPKC terminal area, Montreal: 1947
- CPKC terminal area, Moose Jaw: 1947
- CPKC terminal area, Red Deer: 1947
- CPKC terminal area, Thunder Bay: 1947
- CPKC terminal area, Toronto: 1947
- CPKC terminal area, Vancouver: 1947
- CPKC terminal area, Winnipeg: 1947

### Target dimension combinations

| Car type | Commodity | Dwell range | Employee | Fleet | Unit | Status | Rows |
|---|---|---|---|---|---|---|---:|
| Not Applicable | Agricultural products and food | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3540 |
| Not Applicable | Chemicals and plastics | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3540 |
| Not Applicable | All Petroleum products, including liquefied petroleum gases | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3540 |
| Not Applicable | All Metals and minerals | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3540 |
| Not Applicable | Other products | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3540 |
| Not Applicable | All Western grain | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3539 |
| Not Applicable | All Forest products | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3539 |
| Not Applicable | Fertilizers | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3538 |
| Not Applicable | Motor vehicles and equipment | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3534 |
| Not Applicable | Intermodal containers | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3530 |
| Not Applicable | Coal and petroleum coke | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 3529 |
| Loaded cars and intermodal containers combined (BNSF) | Not Applicable | Not Applicable | Not Applicable | Not Applicable | Hours | 0 - Available | 354 |
| Not Applicable | Coal and petroleum coke | Not Applicable | Not Applicable | Not Applicable | Hours | 1 - Not Available | 8 |
| Not Applicable | Intermodal containers | Not Applicable | Not Applicable | Not Applicable | Hours | 1 - Not Available | 6 |
| Not Applicable | Motor vehicles and equipment | Not Applicable | Not Applicable | Not Applicable | Hours | 1 - Not Available | 4 |
| Not Applicable | Intermodal containers | Not Applicable | Not Applicable | Not Applicable | Hours | 2 - Not Available Long-term | 4 |
| Not Applicable | Coal and petroleum coke | Not Applicable | Not Applicable | Not Applicable | Hours | 2 - Not Available Long-term | 3 |
| Not Applicable | Motor vehicles and equipment | Not Applicable | Not Applicable | Not Applicable | Hours | 2 - Not Available Long-term | 2 |
| Not Applicable | Fertilizers | Not Applicable | Not Applicable | Not Applicable | Hours | 1 - Not Available | 1 |
| Not Applicable | All Forest products | Not Applicable | Not Applicable | Not Applicable | Hours | 1 - Not Available | 1 |
| Not Applicable | All Western grain | Not Applicable | Not Applicable | Not Applicable | Hours | 2 - Not Available Long-term | 1 |
| Not Applicable | Fertilizers | Not Applicable | Not Applicable | Not Applicable | Hours | 2 - Not Available Long-term | 1 |

### Prospective aggregate-row diagnostic

- candidate dimensions: ('Total (All equipment types)', 'Not Applicable', 'Not Applicable', 'Not Applicable', 'Not Applicable', 'Hours', '0 - Available')
- matching rows: **0**
- unique carrier-terminal-week keys: **0**
- duplicate candidate carrier-terminal-week keys: **0**
- max candidate key multiplicity: **0**

This diagnostic does not yet adopt the aggregate row; it only checks whether the source itself exposes a deterministic total-equipment row.

## C. NRCan CGNDB exact-name structural probe

| Place token | Exact-name result rows | Exact result metadata |
|---|---:|---|
| Calgary | 1 | [{'cells': ['Calgary', '24-1-W5', 'Alberta', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/IAKID'}] |
| Edmonton | 1 | [{'cells': ['Edmonton', '', 'Alberta', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/IACMP'}] |
| Kamloops | 2 | [{'cells': ['Kamloops', 'Kamloops Division Yale Land District', 'British Columbia', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/JAFNW'}, {'cells': ['Kamloops', 'Kamloops Division Yale Land District', 'British Columbia', 'Railway Point', 'Previously Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/JBUED'}] |
| Lethbridge | 2 | [{'cells': ['Lethbridge', '8,9-21-W4', 'Alberta', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/IADGP'}, {'cells': ['Lethbridge', '', 'Newfoundland and Labrador', 'Settlement', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/AAMCH'}] |
| Montreal | 0 | [] |
| Moose Jaw | 1 | [{'cells': ['Moose Jaw', '', 'Saskatchewan', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/HALTS'}] |
| Prince George | 1 | [{'cells': ['Prince George', 'Cariboo Land District', 'British Columbia', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/JBLVS'}] |
| Prince Rupert | 1 | [{'cells': ['Prince Rupert', 'Range 5 Coast Land District', 'British Columbia', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/JCNWW'}] |
| Red Deer | 1 | [{'cells': ['Red Deer', '16-38-27-W4', 'Alberta', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/IAEJS'}] |
| Sarnia | 2 | [{'cells': ['Sarnia', 'Lambton', 'Ontario', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FEARV'}, {'cells': ['Sarnia', 'Lambton', 'Ontario', 'Geographic Township', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FDYKY'}] |
| Saskatoon | 1 | [{'cells': ['Saskatoon', '', 'Saskatchewan', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/HAHJJ'}] |
| Thunder Bay | 8 | [{'cells': ['Thunder Bay', 'Thunder Bay', 'Ontario', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FCWFX'}, {'cells': ['Thunder Bay', 'Thunder Bay', 'Ontario', 'Bay', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FCWFZ'}, {'cells': ['Thunder Bay', 'New Westminster Land District', 'British Columbia', 'Bay', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/JBHVI'}, {'cells': ['Thunder Bay', 'Niagara', 'Ontario', 'Urban Community', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FCWFV'}, {'cells': ['Thunder Bay', 'Simcoe', 'Ontario', 'Bay', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FCWFW'}, {'cells': ['Thunder Bay', 'Kenora', 'Ontario', 'Bay', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FCWGA'}, {'cells': ['Thunder Bay', 'Niagara', 'Ontario', 'Bay', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FCWFY'}, {'cells': ['Thunder Bay', '', 'Ontario', 'Geographic District', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FCWFU'}] |
| Toronto | 5 | [{'cells': ['Toronto', 'York', 'Ontario', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FEUZB'}, {'cells': ['Toronto', 'Queens', 'Prince Edward Island', 'Locality', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/BADHP'}, {'cells': ['Toronto', 'York', 'Ontario', 'Community', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FCWYG'}, {'cells': ['Toronto', 'Peel', 'Ontario', 'Geographic Township', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FEJJC'}, {'cells': ['Toronto', '', 'Ontario', 'Township Municipality', 'Previously Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/FDZNA'}] |
| Vancouver | 1 | [{'cells': ['Vancouver', 'New Westminster Land District', 'British Columbia', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/JBRIK'}] |
| Winnipeg | 1 | [{'cells': ['Winnipeg', '', 'Manitoba', 'City', 'Official'], 'href': 'https://geonames.nrcan.gc.ca/search-place-names/unique/GBEIN'}] |

## D. ECCC station inventory

- URL: https://collaboration.cmc.ec.gc.ca/cmc/climate/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv
- bytes: **1309532**
- SHA-256: `72751e152ba3206f74bbff6eac689ea209d93cab7b26428519088f72bbf38a1c`
- encoding: utf-8-sig
- data rows: **8640**
- fields: ['Modified Date: 2026-08-31 23:30 UTC']

## E. Immediate gate status

- Transport Canada full ZIP/file snapshot and annual schema are reproducible.
- The target measure and carrier-specific terminal-area labels are source-defined.
- The source includes value-status and Last_Updated fields, allowing a prospective revision/maturity contract.
- Exact terminal-week record identity depends on adopting one source-defined aggregate dimension combination; the canonical total-equipment diagnostic above informs that decision without using weather outcomes.
- CGNDB exact-name metadata and ECCC inventory now determine whether a deterministic spatial bridge can be frozen.

No F01 final PASS/PARTIAL/HOLD is declared in this file alone.

Incremental monetary cost remained **0 USD**.
