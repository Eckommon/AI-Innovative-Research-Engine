# Normalized Research Metadata Schema v0.3 / 정규화 연구 메타데이터 스키마 v0.3

## Purpose / 목적

서로 다른 미국·한국·EU 및 향후 글로벌 공공데이터 시스템에서 발견되는 데이터셋을 공통 연구 레이어로 표현한다. 이 스키마는 DCAT/DCAT-AP/CKAN 또는 기관 고유 메타데이터를 대체하지 않으며, 원본 메타데이터를 가능한 한 보존한 뒤 정규화 레이어에 매핑한다.  
Provide a common research-layer representation for datasets discovered from heterogeneous US, Korean, EU, and later global public-data systems. This schema does not replace native DCAT/DCAT-AP/CKAN or agency metadata; native metadata should be preserved where possible and mapped into this normalized layer.

**v0.2 calibration / v0.2 보정:** `AMBENCH-001` demonstrated that aggregate case IDs, replicate structures, measurement positions, and uncertainty must be represented explicitly.  
**v0.3 calibration / v0.3 보정:** `EU-STEEL-R01` demonstrated that a still-citable dataset identifier or landing page does not guarantee recovery of the exact historical snapshot used by a published analysis. Snapshot/version lineage is therefore a first-class reproducibility object. / dataset ID·landing page가 남아 있어도 발표 분석에 사용된 exact historical snapshot의 복구가 보장되지 않으므로 snapshot/version 계보를 1급 재현성 객체로 추가한다.

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
| `access_status` | yes | accessible/limited/unavailable/unknown / current access status |

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

## 6. Snapshot & Version Lineage / Snapshot·버전 계보

`EU-STEEL-R01`에서 신규 도입. / Added from `EU-STEEL-R01` reproduction calibration.

| Field | Required | 한국어 / English |
|---|---|---|
| `snapshot_identifier` | for historical claims | 분석에 사용된 exact snapshot/version ID / exact snapshot or version used by an analysis |
| `snapshot_retrieved_at` | when retrieved | snapshot 실제 확보시각 / actual snapshot retrieval time |
| `snapshot_hash` | when bytes available | SHA-256 등 byte fingerprint / byte-level fingerprint such as SHA-256 |
| `historical_version_retention` | yes | strong/partial/none/unknown; 발행기관의 과거 버전 보존성 / publisher retention of historical versions |
| `snapshot_recoverability` | yes | exact/current_only/archive_only/unavailable/unknown / ability to recover the required snapshot |
| `discontinued_at` | no | dataset/API 배포중단 시점 / discontinuation date if known |
| `replacement_dataset_id` | no | 공식 후속·대체 dataset ID / official successor or replacement dataset ID |
| `replacement_correspondence_evidence` | if replacement used | authoritative/partial/weak/none / evidence that replacement is historically equivalent |
| `archive_or_mirror_status` | yes | official_archive/official_current/third_party_mirror/none/unknown |
| `reproduction_risk` | yes | low/medium/high/blocked / reproducibility risk from lineage/access |

### Controlled vocabulary / 통제 어휘

**`historical_version_retention`**
- `strong`: exact prior versions/snapshots are officially retained and retrievable.
- `partial`: some historical artifacts remain, but not all periods/versions.
- `none`: historical versions required for reproduction are not retained through official dissemination.
- `unknown`: not yet verified.

**`snapshot_recoverability`**
- `exact`: required snapshot can be retrieved and fingerprinted.
- `current_only`: current data are accessible but the required historical snapshot is not.
- `archive_only`: exact or near-exact historical snapshot is available only through an official archive path.
- `unavailable`: required snapshot could not be recovered through tested authoritative paths.
- `unknown`: not yet tested.

**`replacement_correspondence_evidence`**
- `authoritative`: publisher explicitly documents one-to-one or valid historical correspondence.
- `partial`: publisher documents some continuity but not enough for all required fields/periods.
- `weak`: similarity exists without authoritative correspondence; cannot support substitution.
- `none`: no correspondence evidence.

### Gate / 게이트

A current accessible landing page, API, or successor dataset is **not sufficient** to label a historical claim strongly reproducible. Historical reproduction requires `snapshot_recoverability=exact|archive_only` or authoritative replacement correspondence covering the required semantics, geography, units, classifications, and periods. / 현재 접근 가능한 landing/API/후속 dataset만으로 historical claim에 강한 재현성을 부여하지 않는다.

Missing values must retain native semantics. `null`, confidential/suppressed, not-applicable, and explicit zero are distinct until authoritative rules establish otherwise. / `null`, 비공개·억제, 해당없음, 명시적 0을 권위 규칙 없이 동일시하지 않는다.

## 7. Combination Record / 데이터 결합 기록

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
snapshot_alignment:
combination_ips:
reproduction_risk:
mechanism_or_rationale_ko:
mechanism_or_rationale_en:
hypothesis_ids: []
state:
```

각 데이터셋의 개별 기록과 조합 기록을 분리한다. / Combination records remain separate from individual dataset records.

## 8. Hypothesis Record / 가설 기록

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

## 9. Experiment Record / 실험 기록

```yaml
experiment_id:
hypothesis_id:
data_snapshot_or_version:
input_snapshot_hashes: []
snapshot_recoverability:
replacement_correspondence_evidence:
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

## 10. Cross-National Normalization / 국가 간 정규화 필드

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

## 11. Language Fields / 언어 필드

공식 연구 해석·가설·결론은 `*_ko` / `*_en` 또는 병기 가능한 구조를 사용한다. 데이터 원문 필드명은 번역하여 덮어쓰지 않는다.  
Official interpretations, hypotheses, and conclusions use `*_ko` / `*_en` or equivalent bilingual structures. Native dataset field names are never overwritten by translations.

## 12. IPS Interaction / IPS 연계

`reproduction_risk` is initially a **gating/modifier field, not a reweighting of the 100-point IPS**. / `reproduction_risk`는 우선 100점 IPS의 재가중 항목이 아니라 게이트·modifier로 운용한다.

- `low/medium`: IPS may be interpreted normally with documented caveats.
- `high`: promotion to controlled experiment requires explicit snapshot mitigation.
- `blocked`: a historical reproduction claim cannot be promoted to `VALIDATED` until the blocked lineage is resolved or the research question is reformulated prospectively.

IPS weights should be changed only after calibration across multiple reproduction cases. / IPS 가중치는 복수 재현사례 보정 후에만 변경한다.

## 13. Schema Evolution Rule / 스키마 진화 규칙

`v0.3` incorporates two empirical calibrations: `AMBENCH-001` for observation/replication structure and `EU-STEEL-R01` for snapshot/version-lineage reproducibility. New fields are added because real research objects require them, and future cases should test whether the controlled vocabularies are sufficient before promoting the schema toward stable. / `v0.3`은 AMBENCH 반복구조와 EU-STEEL snapshot 계보의 두 실증 보정을 반영하며, 실제 연구 객체 필요에 따라 필드를 추가하고 stable 승격 전 후속 사례에서 어휘 충분성을 검증한다.

공식 산출물은 `LANG-001`을 따른다. / Official artifacts comply with `LANG-001`.
