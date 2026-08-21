# Normalized Research Metadata Schema v0.2 / 정규화 연구 메타데이터 스키마 v0.2

## Purpose / 목적

서로 다른 미국·한국·EU 및 향후 글로벌 공공데이터 시스템에서 발견되는 데이터셋을 공통 연구 레이어로 표현한다. 이 스키마는 DCAT/DCAT-AP/CKAN 또는 기관 고유 메타데이터를 대체하지 않으며, 원본 메타데이터를 가능한 한 보존한 뒤 정규화 레이어에 매핑한다.  
Provide a common research-layer representation for datasets discovered from heterogeneous US, Korean, EU, and later global public-data systems. This schema does not replace native DCAT/DCAT-AP/CKAN or agency metadata; native metadata should be preserved where possible and mapped into this normalized layer.

**v0.2 calibration / v0.2 보정:** `AMBENCH-001` demonstrated that aggregate case IDs, replicate structures, measurement positions, and uncertainty must be represented explicitly. / `AMBENCH-001`을 통해 집계 case ID뿐 아니라 반복구조, 측정위치, 불확실성을 명시적으로 표현해야 함이 확인됨.

## 1. Source-Level Fields / 소스 수준 필드

| Field | Required | 한국어 / English |
|---|---|---|
| `source_id` | yes | 안정적 내부 소스 ID / stable internal source identifier |
| `source_name` | yes | 공식 소스·카탈로그명 / official source or catalog name |
| `jurisdiction` | yes | 국가·지역·글로벌 / country, region, or global |
| `publisher` | yes | 운영·발행기관 / operating publisher or agency |
| `canonical_url` | yes | 공식 URL / official URL |
| `catalog_api` | no | API·카탈로그 endpoint / catalog or API endpoint |
| `metadata_standard` | no | DCAT, DCAT-AP, CKAN, custom 등 / metadata standard |
| `access_auth` | yes | none/key/account/other / authentication |
| `license_policy` | no | 재사용·라이선스 요약 / reuse and licensing summary |
| `last_verified_at` | yes | 최종 검증일 / last verification date |

## 2. Dataset-Level Fields / 데이터셋 수준 필드

| Field | Required | 한국어 / English |
|---|---|---|
| `dataset_id` | yes | 내부 데이터셋 ID / stable internal identifier |
| `native_id` | no | 원천기관 ID / publisher-native identifier |
| `title` | yes | 데이터셋 제목 / dataset title |
| `publisher` | yes | 발행기관 / publisher |
| `description` | yes | 원문 설명 또는 충실한 요약 / source description or faithful summary |
| `landing_page` | yes | 공식 landing page / official landing page |
| `distributions` | yes | 파일/API/service endpoint / file, API, or service endpoints |
| `formats` | yes | CSV, JSON, XML, SHP, image, binary 등 / formats |
| `schema_url` | no | 스키마·data dictionary / schema or data dictionary URL |
| `license` | no | 라이선스·권리 / license or rights |
| `update_frequency` | no | 갱신주기 / update cadence |
| `temporal_start` | no | 시작시점 / coverage start |
| `temporal_end` | no | 종료시점 / coverage end |
| `spatial_scope` | no | 공간 범위 / geographic scope |
| `spatial_resolution` | no | facility/grid/admin/coordinate 등 / spatial granularity |
| `unit_system` | no | 주요 단위 / key units |
| `language` | no | 메타데이터·데이터 언어 / metadata/data language |
| `access_status` | yes | accessible/limited/unavailable/unknown / access status |

## 3. Observation & Replication Fields / 관측·반복 구조 필드

`AMBENCH-001`에서 신규 도입. / Added from `AMBENCH-001` calibration.

| Field | Required | 한국어 / English |
|---|---|---|
| `aggregation_level` | yes | raw/replicate/case/facility/region/etc.; 값이 어느 수준으로 집계되었는지 / level at which values are aggregated |
| `replicate_count` | no | 조건·개체별 반복 관측 수 / number of repeated observations per condition/entity |
| `replicate_alignment` | no | exact/partial/aggregate-only/unknown; 데이터셋 간 반복 대응 상태 / cross-dataset repeat pairing status |
| `native_sample_naming_convention` | no | 원천 sample/track/part ID 규칙 / publisher-native sample identifier convention |
| `measurement_position` | no | 단면·좌표·시설위치·센서위치 등 / cross-section, coordinate, facility or sensor position |
| `measurement_uncertainty` | no | 표준편차, CI, 측정오차·계측한계 / standard deviation, confidence interval, metrology error or limits |
| `benchmark_target_id` | no | 공식 benchmark/challenge target identifier / official benchmark or challenge target ID |

**Rule / 규칙:** matching aggregate keys do not prove replicate-level one-to-one joinability. / 집계 조인키 일치가 반복수준 1:1 조인 가능성을 증명하지 않는다.

## 4. Research Qualification Fields / 연구 적격성 필드

| Field | Required | 한국어 / English |
|---|---|---|
| `domain` | yes | 제조·전력·기후·물류 등 / manufacturing, energy, climate, logistics, etc. |
| `topic_track` | yes | `FRONTIER` 또는 `PERSISTENT_BOTTLENECK` |
| `data_structure_class` | yes | experiment, time-series, panel, image, geospatial, event, administrative 등 |
| `input_candidates` | no | 잠재 입력·predictor / possible predictors or features |
| `outcome_candidates` | no | 결과·정답값 / ground truth or target candidates |
| `ground_truth_strength` | yes | none/weak/moderate/strong |
| `candidate_join_keys` | no | entity/time/space/classification/material/etc. |
| `join_constraints` | no | 의미·정렬 제약 / semantic and alignment caveats |
| `dataset_ips` | no | 실제 데이터 검토 후 0–100 / 0–100 after inspection |
| `ips_rationale` | no | 기준별 점수 근거 / criterion-level rationale |
| `research_state` | yes | DISCOVERED/SCREENING/CANDIDATE/etc. |

## 5. Provenance and Evidence / 출처·증거 필드

| Field | Required | 한국어 / English |
|---|---|---|
| `evidence_class` | yes | OBSERVED/DERIVED/HYPOTHESIZED/VALIDATED/REJECTED/INCONCLUSIVE |
| `retrieved_at` | yes | 조회·검토 시각 / retrieval or inspection timestamp |
| `source_citations` | yes | 공식 출처·문서 / official source references |
| `source_version` | no | 데이터·문서 버전 / source version or snapshot |
| `transformations` | no | 파싱·정규화·파생 / parsing, normalization, derivation |
| `assumptions` | no | 명시적 가정 / explicit assumptions |
| `known_limitations` | no | 결측·편향·범위·의미 한계 / missingness, bias, coverage, semantic limits |

## 6. Combination Record / 데이터 결합 기록

```yaml
combination_id:
datasets: []
relationship_type:
join_keys: []
aggregation_level:
replicate_alignment:
temporal_alignment:
spatial_alignment:
semantic_alignment:
combination_ips:
mechanism_or_rationale_ko:
mechanism_or_rationale_en:
hypothesis_ids: []
state:
```

각 데이터셋의 개별 기록과 조합 기록을 분리한다. / Combination records remain separate from individual dataset records.

## 7. Hypothesis Record / 가설 기록

```yaml
hypothesis_id:
combination_id:
claim_ko:
claim_en:
target:
mechanism:
scope:
baseline:
primary_metric:
material_improvement_threshold:
rejection_criterion:
evidence_class: HYPOTHESIZED
state:
```

## 8. Experiment Record / 실험 기록

```yaml
experiment_id:
hypothesis_id:
data_snapshot_or_version:
aggregation_level:
method:
train_test_or_evaluation_design:
metrics:
sensitivity_checks:
result_ko:
result_en:
limitations_ko:
limitations_en:
evidence_class:
final_state:
reproducibility_reference:
```

## 9. Cross-National Normalization / 국가 간 정규화 필드

필요 시 / As applicable:

- `classification_system_native`
- `classification_mapping`
- `currency_native`
- `currency_normalization_method`
- `price_basis_year`
- `timezone`
- `statistical_methodology_notes`
- `geographic_level_mapping`
- `unit_conversion`

## 10. Language Fields / 언어 필드

공식 연구 해석·가설·결론은 `*_ko` / `*_en` 또는 병기 가능한 구조를 사용한다. 데이터 원문 필드명은 번역하여 덮어쓰지 않는다.  
Official interpretations, hypotheses, and conclusions use `*_ko` / `*_en` or equivalent bilingual structures. Native dataset field names are never overwritten by translations.

## 11. Schema Evolution Rule / 스키마 진화 규칙

`v0.2`는 `AMBENCH-001` 보정을 반영했으며 Wave 1 미국·한국·EU 최소 1개 데이터셋씩에 적용한 뒤 `v0.3` 또는 stable 후보 여부를 판단한다. 실제 연구 객체가 요구할 때만 필드를 추가한다.  
`v0.2` incorporates `AMBENCH-001` calibration and will be tested against at least one Wave 1 dataset from each of the US, Korea, and EU before considering `v0.3` or a stable candidate. New fields are added because real research objects require them.

공식 산출물은 `LANG-001`을 따른다. / Official artifacts comply with `LANG-001`.
