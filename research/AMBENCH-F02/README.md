---
id: AMBENCH-F02
type: feasibility
state: FEASIBILITY_TEST
evidence_class: HYPOTHESIZED
region: us
domain: manufacturing
tags:
  - type/feasibility
  - state/experiment
  - evidence/hypothesized
  - region/us
  - domain/manufacturing
  - domain/additive-manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-001/README.md
  - docs/METADATA_SCHEMA.md
---

# AMBENCH-F02 — Raw Snapshot & Replicate Alignment Feasibility / AM Bench raw snapshot·반복 정렬 검증

**Issue / 이슈:** #11  
**State / 상태:** `FEASIBILITY_TEST`  
**Parent calibration / 상위 보정:** `AMBENCH-001`

## 1. Research Question / 연구 질문

**KO:** NIST AMB2022-03의 exact PDR snapshot과 raw identifier 체계만으로 thermography 3회 반복 track과 optical specimen/cross-section outcome을 어느 해상도까지 **추정 없이** 정렬할 수 있는가?  
**EN:** Using only exact NIST AMB2022-03 PDR snapshots and authoritative raw identifiers, to what resolution can three thermography repeat tracks be aligned with optical specimen/cross-section outcomes **without inference**?

## 2. Frozen Sources / 고정 소스

| Role | NIST PDR | DOI |
|---|---|---|
| thermography / 열화상 | `mds2-2716` | `10.18434/mds2-2716` |
| optical microscopy / 광학현미경 | `mds2-2718` | `10.18434/mds2-2718` |

Official NIST AMB2022-03 challenge documentation is used only to interpret experiment identity and published measurement design. / 공식 challenge 문서는 실험 ID·측정설계 해석에만 사용한다.

## 3. Frozen Relationship / 고정 관계

```text
process case
→ thermography track/repeat identity
→ optical specimen/cross-section identity
→ melt-pool depth/width outcome
```

Shared case identity alone is insufficient to prove repeat-level one-to-one pairing. / 공통 case ID만으로 반복수준 1:1 대응을 증명하지 않는다.

## 4. Required Lineage Record / 필수 계보 기록

For each PDR dataset: / 각 PDR dataset별
- snapshot/version identifier
- release/update history
- exact distribution manifest
- README/update-log file
- accessible file sizes and SHA-256
- `historical_version_retention`
- `snapshot_recoverability`
- `archive_or_mirror_status`
- `reproduction_risk`

Initial values remain `UNKNOWN` until machine inspection. / 기계검사 전 초기값은 `UNKNOWN`으로 유지한다.

## 5. Alignment Matrix / 정렬 행렬

Target schema: / 목표 schema

| process_case | thermo_track | thermo_repeat | optical_sample | optical_cross_section | evidence | alignment_state |
|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | `UNKNOWN` |

Allowed states: `EXACT`, `CASE_LEVEL_ONLY`, `MANY_TO_ONE`, `UNRESOLVED`. / 허용 상태.

## 6. Frozen Gate / 고정 게이트

### `PASS`
Authoritative NIST metadata/file naming provides reproducible track/repeat-level mapping to corresponding optical outcome identities. / 권위 있는 NIST metadata로 track/repeat 수준 대응이 재현 가능.

### `PARTIAL`
Exact snapshots are recoverable and case-level correspondence is authoritative, but optical outcomes cannot be linked one-to-one to thermography repeats. Only the validated aggregation level may be used downstream. / snapshot·case-level은 확정되지만 반복 1:1 대응은 불가하여 검증된 집계수준만 허용.

### `HOLD`
Required snapshots, manifests, or identifier semantics are unavailable or pairing requires speculative interpretation. / snapshot·manifest·식별자 의미가 비가용이거나 추정 pairing 필요.

No gate definition changes after inspecting the raw data. / raw 확인 후 게이트 변경 금지.

## 7. Execution Order / 실행 순서

1. inspect PDR landing/version metadata;
2. retrieve README/update history;
3. enumerate distributions and freeze fingerprints;
4. inspect only metadata/small structured files first;
5. extract naming conventions;
6. construct alignment matrix;
7. apply PASS/PARTIAL/HOLD;
8. only after a future PASS/PARTIAL decision consider raw-level modeling at the permitted resolution.

## 8. Current Evidence / 현재 증거

`OBSERVED`, official NIST documentation: / NIST 공식문서 관측
- 7 laser parameter cases × 3 repeats = 21 single tracks in the thermography design.
- optical challenge result tables report six melt-pool geometry measurements per condition and use Sample IDs such as `AMB2022-718-SH1-BP1-L1.2`.
- NIST directs users to dataset README files for periodic data/update/download changes.

These facts establish the feasibility question but **do not prove repeat pairing**. / 이 사실들은 feasibility 질문을 정당화하지만 반복 pairing을 증명하지 않는다.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and the v0.3 snapshot-lineage gate. / 관련 규약 준수.
