---
id: AMBENCH-E33-DESIGN-MAP-PREFLIGHT
type: process-input-preflight
created: 2026-08-23
numerical_outcome_values_emitted: false
process_input_values_only: true
incremental_monetary_cost_usd: 0
---

# AMBENCH-E33 Scan-Strategy Design Map Preflight / Scan-Strategy 설계 map 사전점검

## Boundary / 경계
- Scan-strategy process-input CSV only; no `Measurements.xlsx` numerical values, images, or outcomes. / scan-strategy 공정입력 CSV만 사용; `Measurements.xlsx` 숫자값·이미지·outcome 미사용.

## Source integrity / source 무결성
- dataset: `mds2-3662`
- version: `1.0.1`
- archive_size: `28583`
- sha256_nerdm: `f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee`
- sha256_local: `f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee`
- checksum_match: `True`

## `Scan Strategy Data/scanStrategyConverging.csv`
- line_count: `2981`
- first_lines_process_input_only:
  - `x (�m),y (�m),laser power (W),time (seconds)`
  - `2435,675,285,0`
  - `2435,685,285,0.00001`
  - `2435,694,285,0.00002`
  - `2435,709,285,0.00003`

## `Scan Strategy Data/scanStrategyDiverging.csv`
- line_count: `2966`
- first_lines_process_input_only:
  - `x (�m),y (�m),laser power (W),time (seconds)`
  - `2432,738,285,0`
  - `2432,747,285,0.00001`
  - `2431,757,285,0.00002`
  - `2431,767,285,0.00003`

## `Scan Strategy Data/singleTrack.csv`
- line_count: `3`
- first_lines_process_input_only:
  - `x (�m),y (�m),laser power (W),time (seconds)`
  - `500,500,285,0`
  - `500,2500,285,0.00208`

