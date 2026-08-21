# AMBENCH-001 Dataset Profile / 데이터셋 프로파일

## 1. Process Cases / 공정 조건

| Case | Power [W] | Scan speed [mm/s] | Spot size D4σ [µm] | VEDσ [J/mm³] | VED/VEDbase |
|---|---:|---:|---:|---:|---:|
| 0 | 285 | 960 | 67 | 1058 | 1.00 |
| 1.1 | 285 | 960 | 49 | 1978 | 1.87 |
| 1.2 | 285 | 960 | 82 | 706 | 0.67 |
| 2.1 | 285 | 1200 | 67 | 847 | 0.80 |
| 2.2 | 285 | 800 | 67 | 1270 | 1.20 |
| 3.1 | 325 | 960 | 67 | 1207 | 1.14 |
| 3.2 | 245 | 960 | 67 | 910 | 0.86 |

Each case has three single-track thermography repeats for 21 tracks. / 각 case는 열화상 단일트랙 3회 반복으로 총 21개 track을 구성한다.

## 2. Thermography Measurements / 열화상 측정

| Variable | Meaning / 의미 | Unit |
|---|---|---|
| `TTAM` | Track Time Above Melting / 용융온도 이상 지속시간 | s |
| `TSCR` | Track Solid Cooling Rate / 응고 후 고상 냉각률 | °C/s |
| `TLCR` | Track Liquid Cooling Rate / 응고 전 액상 냉각률 | °C/s |
| `TTCR` | Track Transition Cooling Rate / 전이 냉각률 | °C/s |

NIST reports these thermal values as averages across three tracks/case. / NIST 공개 결과는 조건별 3개 track의 평균 열지표를 제공한다.

| Case | TTAM [s] | TSCR [°C/s] | TLCR [°C/s] | TTCR [°C/s] |
|---|---:|---:|---:|---:|
| 0 | 1.22E-03 | 6.99E+05 | 4.14E+05 | 1.93E+05 |
| 1.1 | 1.30E-03 | 7.32E+05 | 4.06E+05 | 1.38E+05 |
| 1.2 | 1.04E-03 | 5.11E+05 | 3.65E+05 | 1.93E+05 |
| 2.1 | 8.96E-04 | 7.85E+05 | 5.06E+05 | 3.01E+05 |
| 2.2 | 1.59E-03 | 6.11E+05 | 3.25E+05 | 1.46E+05 |
| 3.1 | 1.38E-03 | 7.05E+05 | 3.81E+05 | 1.57E+05 |
| 3.2 | 1.03E-03 | 7.49E+05 | 4.33E+05 | 2.32E+05 |

## 3. Optical Geometry Outcomes / 광학 형상 결과

NIST reports six geometry measurements per condition. / NIST는 조건별 6개 형상 측정을 보고한다.

| Case | Mean depth [µm] | SD depth [µm] | Mean width [µm] | SD width [µm] |
|---|---:|---:|---:|---:|
| 0 | 139.7 | 1.9 | 136.3 | 2.9 |
| 1.1 | 227.2 | 3.2 | 106.2 | 3.6 |
| 1.2 | 102.4 | 1.1 | 141.7 | 1.8 |
| 2.1 | 109.7 | 1.7 | 112.9 | 1.7 |
| 2.2 | 176.5 | 2.6 | 156.1 | 4.9 |
| 3.1 | 166.1 | 2.0 | 134.3 | 2.5 |
| 3.2 | 116.9 | 1.2 | 129.4 | 1.6 |

## 4. Join Semantics / 조인 의미

### Aggregate level / 집계수준
`case_number` is a verified join key across published process, thermography and geometry result tables. / 공개 공정·열화상·형상 결과표 사이에서는 `case_number`가 검증된 조인키다.

### Replicate level / 반복수준
`case_number` does **not** prove one-to-one pairing between the three thermography tracks and the six geometry measurements. Raw filenames, track IDs, cross-section positions and measurement provenance must be inspected before paired-sample modeling.  
`case_number`는 열화상 3회 반복과 형상 6회 측정 간 1:1 대응을 보장하지 않는다. paired-sample 모델링 전 raw filename, track ID, 단면 위치와 측정 provenance를 검증해야 한다.

## 5. Data Structure Classes / 데이터 구조 유형

- process-design table / 공정설계 표
- high-speed thermographic image/time-series data / 고속 열화상·시계열
- scan strategy / 스캔전략
- optical TIFF images / 광학 TIFF 영상
- tabular measurement outcomes / 표형 측정 결과
- microstructure SEM/EBSD/EDS candidates / 미세조직 후보

## 6. Ground Truth Strength / 정답값 강도

**`STRONG` at benchmark aggregate level / benchmark 집계수준에서 `STRONG`.**  
Measured depth/width are explicitly defined benchmark quantities with repeated measurements and reported variability. Thermography quantities also have explicit measurement/analysis definitions, but NIST notes systematic measurement uncertainty related to apparent temperature, emissivity, radiating process byproducts, and the largest spot-size case.  
깊이·폭은 반복측정과 변동성이 제공되는 명시적 benchmark 값이다. 열화상 지표 역시 정의되어 있으나 NIST는 apparent temperature, emissivity, 방사성 공정부산물 및 큰 spot-size 조건에서의 측정오차 가능성을 명시한다.

## 7. Schema Calibration Finding / 스키마 보정 발견

Add to the normalized research schema when next revised: / 차기 스키마 개정 시 추가 권고:

- `replicate_count`
- `replicate_alignment`
- `measurement_position`
- `measurement_uncertainty`
- `aggregation_level`
- `benchmark_target_id`
- `native_sample_naming_convention`

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
