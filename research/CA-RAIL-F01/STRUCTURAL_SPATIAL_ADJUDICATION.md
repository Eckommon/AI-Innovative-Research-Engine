---
id: CA-RAIL-F01-STRUCTURAL-SPATIAL-ADJUDICATION
type: outcome-blind-structural-spatial-adjudication
created: 2026-09-04
relationship_outcome_computed: false
weather_values_opened: false
rail_dwell_magnitudes_persisted: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-F01 Structural / Spatial Adjudication

No dwell magnitude, weather observation or rail-weather association is persisted.

## A. Frozen intermodal-dwell structural panel

- period: **2024-01-01 through 2025-12-31**
- carriers: **CN, CPKC only**
- commodity: **Intermodal containers**
- status: **0 - Available**
- source rows under frozen stratum: **2100**
- unique carrier-terminal-week keys: **2100**
- duplicate keys: **0**
- unique carrier-terminal series: **20**
- unique source reference dates: **105**
- date range: **2024-01-01 .. 2025-12-29**

### Per-terminal coverage

| Carrier | Terminal geography | Place token | Rows | Missing vs global dates | First missing examples |
|---|---|---|---:|---:|---|
| CN | CN terminal area, Edmonton | Edmonton | 105 | 0 |  |
| CN | CN terminal area, Kamloops | Kamloops | 105 | 0 |  |
| CN | CN terminal area, Montreal | Montreal | 105 | 0 |  |
| CN | CN terminal area, Prince George | Prince George | 105 | 0 |  |
| CN | CN terminal area, Prince Rupert | Prince Rupert | 105 | 0 |  |
| CN | CN terminal area, Sarnia | Sarnia | 105 | 0 |  |
| CN | CN terminal area, Saskatoon | Saskatoon | 105 | 0 |  |
| CN | CN terminal area, Toronto | Toronto | 105 | 0 |  |
| CN | CN terminal area, Vancouver | Vancouver | 105 | 0 |  |
| CN | CN terminal area, Winnipeg | Winnipeg | 105 | 0 |  |
| CPKC | CPKC terminal area, Calgary | Calgary | 105 | 0 |  |
| CPKC | CPKC terminal area, Edmonton | Edmonton | 105 | 0 |  |
| CPKC | CPKC terminal area, Lethbridge | Lethbridge | 105 | 0 |  |
| CPKC | CPKC terminal area, Montreal | Montreal | 105 | 0 |  |
| CPKC | CPKC terminal area, Moose Jaw | Moose Jaw | 105 | 0 |  |
| CPKC | CPKC terminal area, Red Deer | Red Deer | 105 | 0 |  |
| CPKC | CPKC terminal area, Thunder Bay | Thunder Bay | 105 | 0 |  |
| CPKC | CPKC terminal area, Toronto | Toronto | 105 | 0 |  |
| CPKC | CPKC terminal area, Vancouver | Vancouver | 105 | 0 |  |
| CPKC | CPKC terminal area, Winnipeg | Winnipeg | 105 | 0 |  |

## B. CGNDB Official / CITY-City identity

- unique place tokens: **15**
- unique Official + CITY-City matches with coordinates: **15**
- unresolved place tokens: **0**

| Source token | Official name | Province | CGNDB key | Latitude | Longitude |
|---|---|---|---|---:|---:|
| Calgary | Calgary | Alberta | IAKID | 51.0458333 | -114.0574999 |
| Edmonton | Edmonton | Alberta | IACMP | 53.5344445 | -113.4902778 |
| Kamloops | Kamloops | British Columbia | JAFNW | 50.6758330 | -120.3394440 |
| Lethbridge | Lethbridge | Alberta | IADGP | 49.6936111 | -112.8419444 |
| Montreal | Montréal | Quebec | EHHUN | 45.5088220 | -73.5540770 |
| Moose Jaw | Moose Jaw | Saskatchewan | HALTS | 50.3934194 | -105.5519522 |
| Prince George | Prince George | British Columbia | JBLVS | 53.9130560 | -122.7452780 |
| Prince Rupert | Prince Rupert | British Columbia | JCNWW | 54.3127780 | -130.3252780 |
| Red Deer | Red Deer | Alberta | IAEJS | 52.2686111 | -113.8102778 |
| Sarnia | Sarnia | Ontario | FEARV | 42.9813889 | -82.3177777 |
| Saskatoon | Saskatoon | Saskatchewan | HAHJJ | 52.1396500 | -106.6861833 |
| Thunder Bay | Thunder Bay | Ontario | FCWFX | 48.4013889 | -89.2677778 |
| Toronto | Toronto | Ontario | FEUZB | 43.7417000 | -79.3733000 |
| Vancouver | Vancouver | British Columbia | JBRIK | 49.2611110 | -123.1138890 |
| Winnipeg | Winnipeg | Manitoba | GBEIN | 49.8844440 | -97.1463890 |

## C. ECCC station-inventory contract

- inventory URL: https://collaboration.cmc.ec.gc.ca/cmc/climate/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv
- bytes: **1309532**
- SHA-256: 72751e152ba3206f74bbff6eac689ea209d93cab7b26428519088f72bbf38a1c
- metadata/header row index (1-based): **4**
- fields: ['Name', 'Province', 'Climate ID', 'Station ID', 'WMO ID', 'TC ID', 'Latitude (Decimal Degrees)', 'Longitude (Decimal Degrees)', 'Latitude', 'Longitude', 'Elevation (m)', 'First Year', 'Last Year', 'HLY First Year', 'HLY Last Year', 'DLY First Year', 'DLY Last Year', 'MLY First Year', 'MLY Last Year']
- parsed station rows: **8637**
- daily-coverage candidate rows spanning 2024–2025: **1169**
- unique Climate IDs with one coordinate row: **1169**
- ambiguous duplicated Climate IDs: **0**

## D. Official-city → ECCC daily-coverage station structural support

| Max distance | Supported city tokens | Share of resolved cities |
|---:|---:|---:|
| 10 km | 13 | 86.666667% |
| 20 km | 14 | 93.333333% |
| 30 km | 14 | 93.333333% |
| 50 km | 14 | 93.333333% |
| 75 km | 14 | 93.333333% |

### Nearest eligible stations

| City | Climate ID | Station | Distance km | Daily first year | Daily last year | Second-nearest km |
|---|---|---|---:|---:|---:|---:|
| Calgary | 3031094 | CALGARY INT'L CS | 8.188 | 1999 | 2026 | 8.889 |
| Edmonton | 3012209 | EDMONTON BLATCHFORD | 4.414 | 1996 | 2026 | 25.655 |
| Kamloops | 1163842 | KAMLOOPS AUT | 7.576 | 2006 | 2026 | 8.239 |
| Lethbridge | 3033892 | LETHBRIDGE CDA 2 | 4.512 | 2004 | 2026 | 5.223 |
| Montreal | 7024745 | MCTAVISH | 2.246 | 1994 | 2026 | 10.521 |
| Moose Jaw | 4015322 | MOOSE JAW CS | 7.103 | 1998 | 2026 | 62.628 |
| Prince George | 1096454 | PRINCE GEORGE MASSEY AUTO | 3.270 | 2018 | 2026 | 5.558 |
| Prince Rupert | 1066488 | PRINCE RUPERT MONT CIRC | 2.425 | 1959 | 2026 | 7.863 |
| Red Deer | 3025484 | RED DEER REGIONAL A | 11.250 | 2020 | 2026 | 20.456 |
| Sarnia | 6127510 | SARNIA | 2.164 | 2009 | 2026 | 2.525 |
| Saskatoon | 4057152 | SASKATOON INTL A | 3.504 | 2018 | 2026 | 4.088 |
| Thunder Bay | 6048260 | THUNDER BAY | 5.201 | 2012 | 2026 | 5.201 |
| Toronto | 6158355 | TORONTO CITY | 8.257 | 2002 | 2026 | 8.857 |
| Vancouver | 110Q44V | VANCOUVER HARBOUR | 3.225 | 2023 | 2026 | 4.347 |
| Winnipeg | 5023262 | WINNIPEG THE FORKS | 1.327 | 1999 | 2026 | 7.282 |

## E. Prospective implications

- Intermodal-container dwell yields a source-defined single row per carrier-terminal-week when the frozen dimensions are applied; no commodity averaging is required.
- 2024–2025 remains a frozen preliminary Transport Canada snapshot, not a claim of final historical values.
- CGNDB matching permits accent-insensitive exact linguistic equivalence and requires Status=Official + Concise Term=CITY-City; no fuzzy geocoding.
- ECCC station support is based only on station inventory, coordinates and daily availability years; no weather values are opened.
- A final station-distance cap must be adopted from this structural coverage before any weather values.

Incremental monetary cost remained **0 USD**.
