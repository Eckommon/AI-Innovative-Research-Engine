# Normalized Research Metadata Schema v0.1

Purpose: provide a common representation for datasets discovered from heterogeneous US, Korean, EU, and later global public-data systems.

This is a research-layer schema, not a replacement for native DCAT/DCAT-AP/CKAN or agency metadata. Native metadata should be preserved where possible and mapped into this normalized layer.

## 1. Source-Level Fields

| Field | Required | Description |
|---|---|---|
| `source_id` | yes | Stable internal source identifier |
| `source_name` | yes | Official source/catalog name |
| `jurisdiction` | yes | Country/region/global |
| `publisher` | yes | Operating agency/organization |
| `canonical_url` | yes | Official source URL |
| `catalog_api` | no | API/catalog endpoint |
| `metadata_standard` | no | DCAT, DCAT-AP, CKAN, custom, etc. |
| `access_auth` | yes | none/key/account/other |
| `license_policy` | no | Reuse/license summary |
| `last_verified_at` | yes | Verification date |

## 2. Dataset-Level Fields

| Field | Required | Description |
|---|---|---|
| `dataset_id` | yes | Stable internal dataset identifier |
| `native_id` | no | Publisher/catalog native ID |
| `title` | yes | Dataset title |
| `publisher` | yes | Dataset publisher |
| `description` | yes | Source description or faithful summary |
| `landing_page` | yes | Official dataset page |
| `distributions` | yes | File/API/service endpoints |
| `formats` | yes | CSV, JSON, XML, SHP, image, binary, etc. |
| `schema_url` | no | Schema/data dictionary link |
| `license` | no | Dataset-specific license/rights |
| `update_frequency` | no | Update cadence |
| `temporal_start` | no | Coverage start |
| `temporal_end` | no | Coverage end |
| `spatial_scope` | no | Geographic coverage |
| `spatial_resolution` | no | Facility/grid/admin/coordinate/etc. |
| `unit_system` | no | Key measurement units |
| `language` | no | Metadata/data language |
| `access_status` | yes | accessible/limited/unavailable/unknown |

## 3. Research Qualification Fields

| Field | Required | Description |
|---|---|---|
| `domain` | yes | Manufacturing, energy, climate, logistics, etc. |
| `data_structure_class` | yes | experiment, time-series, panel, image, geospatial, event, administrative, etc. |
| `input_candidates` | no | Possible predictors/features |
| `outcome_candidates` | no | Ground truth/targets/outcomes |
| `ground_truth_strength` | yes | none/weak/moderate/strong |
| `candidate_join_keys` | no | Entity/time/space/classification/material/etc. |
| `join_constraints` | no | Semantic/alignment caveats |
| `dataset_ips` | no | 0–100 once assessed |
| `ips_rationale` | no | Written criterion-level rationale |
| `research_state` | yes | DISCOVERED/SCREENING/CANDIDATE/etc. |

## 4. Provenance and Evidence Fields

| Field | Required | Description |
|---|---|---|
| `evidence_class` | yes | OBSERVED/DERIVED/HYPOTHESIZED/VALIDATED/REJECTED/INCONCLUSIVE |
| `retrieved_at` | yes | Retrieval/inspection timestamp |
| `source_citations` | yes | Official pages/docs supporting the record |
| `transformations` | no | Any parsing/normalization/derivation performed |
| `assumptions` | no | Explicit research assumptions |
| `known_limitations` | no | Missingness, bias, coverage, semantic limits |

## 5. Combination Record

A dataset relationship should be represented separately from the individual dataset records.

Minimum fields:

```yaml
combination_id:
datasets: []
relationship_type:
join_keys: []
temporal_alignment:
spatial_alignment:
semantic_alignment:
combination_ips:
mechanism_or_rationale:
hypothesis_ids: []
state:
```

## 6. Hypothesis Record

```yaml
hypothesis_id:
combination_id:
claim:
target:
mechanism:
scope:
baseline:
primary_metric:
rejection_criterion:
evidence_class: HYPOTHESIZED
state:
```

## 7. Experiment Record

```yaml
experiment_id:
hypothesis_id:
data_snapshot_or_version:
method:
train_test_or_evaluation_design:
metrics:
sensitivity_checks:
result:
limitations:
evidence_class:
final_state:
reproducibility_reference:
```

## 8. Cross-National Normalization Fields

When multiple jurisdictions are involved, add as applicable:

- `classification_system_native`
- `classification_mapping`
- `currency_native`
- `currency_normalization_method`
- `price_basis_year`
- `timezone`
- `statistical_methodology_notes`
- `geographic_level_mapping`
- `unit_conversion`

## 9. Schema Evolution Rule

This v0.1 schema should be calibrated against `AMBENCH-001` and at least one dataset from each Wave 1 jurisdiction before being treated as stable. New fields should be added because real research objects require them, not merely to maximize metadata coverage.
