---
id: JP-PORT-F01-SOURCE-PREFLIGHT
type: outcome-blind-source-preflight
created: 2026-09-04
relationship_outcome_computed: false
weather_values_opened: false
throughput_values_persisted: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-F01 Source Preflight / 소스 사전검증

No weather-throughput relationship, port ranking, weather observation value or throughput magnitude was calculated/persisted.

## A. e-Stat mature Port Survey annual port-aggregate workbooks

| Year | Bytes | SHA-256 | Sheets |
|---:|---:|---|---:|
| 2019 | 1056222 | c9b52effc6939080290f9cd2d1eaad894769d5a0af8f5c268bd18dce5218bebf | 6 |
| 2020 | 1048653 | 9ee04b6f968fa475f004c7e397cb74303d6bd3498972ef040c12f3414b1fbe46 | 4 |
| 2021 | 1045142 | de510a1510a178a9dc3d3d0dce9ed5ea8da165929ccb0d381458f2005571dd68 | 4 |
| 2022 | 1045714 | f5e1402c0fba0afa2b8a74f8e463638c9dc6ef141ed9c08355f39125b6fa61c4 | 4 |
| 2023 | 1044224 | 4670b2ac230cae5b2bdc6a50ae03c72001137ca24b9c023a6f90e28e77156d04 | 4 |
| 2024 | 1056705 | 830c2173b19f9ea106596e043730bd93616dafe93ef0c6a385d633335cef0200 | 4 |

### Sheet identities

- 2019: ['港別集計値の取り扱い', '受付状況', '入港船舶', '海上出入貨物', '自動車航送車両', 'コンテナ個数']
- 2020: ['入港船舶', '海上出入貨物', '自動車航送車両', 'コンテナ個数']
- 2021: ['入港船舶', '海上出入貨物', '自動車航送車両', 'コンテナ個数']
- 2022: ['入港船舶', '海上出入貨物', '自動車航送車両', 'コンテナ個数']
- 2023: ['入港船舶', '海上出入貨物', '自動車航送車両', 'コンテナ個数']
- 2024: ['入港船舶', '海上出入貨物', '自動車航送車両', 'コンテナ個数']

### Text/schema diagnostics

- port-name-like union 2019–2024: **0**
- exact normalized port labels present in all six mature workbooks: **0**

- 2019: **0** port-name-like labels
- 2020: **0** port-name-like labels
- 2021: **0** port-name-like labels
- 2022: **0** port-name-like labels
- 2023: **0** port-name-like labels
- 2024: **0** port-name-like labels

#### 2024 first text structures

- sheet 入港船舶: approx 1010×82; text=['【入港船舶表】', '2025年12月25日現在', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)']
- sheet 海上出入貨物: approx 1010×74; text=['【海上出入貨物表】', '2025年12月25日現在', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)']
- sheet 自動車航送車両: approx 843×74; text=['【車種別自動車航送車両台数表】', '2025年12月25日現在', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)']
- sheet コンテナ個数: approx 175×73; text=['【ｺﾝﾃﾅ個数表】', '2025年12月25日現在', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)', '(166／166港)']

First 100 six-year-stable port labels:




## B. MLIT C02 official port-point snapshot

- URL: https://nlftp.mlit.go.jp/ksj/gml/data/C02/C02-14/C02-14_GML.zip
- bytes: **601717**
- SHA-256: 5dfda41a2b1b622f328312c437e0d3c4f9bda7bbf276572631e128af70d0af0b
- PortAndHarbor records: **994**
- unique normalized C02 port names: **929**
- six-year-stable e-Stat labels with exactly one C02 point: **0**
- ambiguous C02-name matches: **0**
- unmatched stable e-Stat labels: **0**


## C. JMA AMeDAS detailed station-history snapshot

- URL: https://www.data.jma.go.jp/stats/data/mdrr/chiten/meta/amdmaster.index4
- bytes: **2095768**
- SHA-256: 5e8c212c433fd0322bc1045f4995c24b13949d4d438f902cdf930a6c3b86a9e9
- parsed >=33-field history rows: **7938**
- stable 2019–2024 precip+wind metadata segments: **0**
- unique stable station IDs: **0**
- ambiguous multiple stable segments: **0**

Eligibility here means a single JMA metadata-history segment spans the entire 2019-01-01..2024-12-31 period and both precipitation and wind statistics are present. No observation values are opened.

## D. Structural nearest-station support (distance only)

| Max distance | Ports supported | Share of exact C02 ports |
|---:|---:|---:|
| 10 km | 0 | 0.000000% |
| 20 km | 0 | 0.000000% |
| 30 km | 0 | 0.000000% |
| 40 km | 0 | 0.000000% |
| 50 km | 0 | 0.000000% |

### 30-km structural candidate

- candidate ports: **0** / 0 exact-C02 ports
- nearest-station assignment is deterministic by geodesic distance; exact distance ties are excluded.
- 30 km is evaluated as the prospective upper bound because JMA documents ~21 km spacing for the ~840 four-element stations; it is not selected from throughput-weather outcomes.

First 120 candidate identities and distances (non-outcome metadata only):

| Port | C02 code | JMA station | Distance km | Second-nearest km |
|---|---|---|---:|---:|

## E. Prospective implications

- Mature source window candidate is 2019–2024, using annual e-Stat port aggregate workbooks only; current preliminary/partially revised months are excluded.
- Future primary throughput family remains total maritime cargo if the next schema adjudication confirms one consistent monthly total field/unit across the frozen files; otherwise F01 must fall back prospectively to vessel arrivals or HOLD.
- C02 location is 2014 vintage; only exact normalized one-to-one names appearing in every 2019–2024 mature workbook are eligible. No manual geocoding or alias repair after outcomes.
- JMA station eligibility requires one metadata-history segment spanning the whole 2019–2024 window with precipitation+wind statistics present.
- A final port→station rule still requires formal adoption of the maximum distance and exact-tie handling after reviewing this structural coverage only.

Incremental monetary cost remained **0 USD**.
