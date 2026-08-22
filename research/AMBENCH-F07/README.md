---
id: AMBENCH-F07
type: feasibility
state: PREREGISTERED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D06/RESULT.md
  - research/AMBENCH-POST-D06-TRIAGE.md
  - Issue #21
---

# AMBENCH-F07 — AMB2025-07 Independent-Condition Expansion Feasibility / AMB2025-07 독립 공정조건 확장 가능성 검증

**State / 상태:** `PREREGISTERED — SOURCE/IDENTITY FEASIBILITY`  
**Issue / 이슈:** #21  
**Parent / 상위:** `AMBENCH-D06 — PROCESS_CASE_PROXY_DOMINANT`

## 1. Research Question / 연구 질문

**KO:** NIST AMB2025-07의 공개 자료가 D06에서 확인된 기존 7개 process-case 정보제약을 완화할 수 있도록, **새로운 독립 공정조건**과 thermal measurement 및 melt-pool geometry를 권위 있고 version-identifiable한 source/identifier로 재현 가능하게 구성할 수 있는가?  
**EN:** Can public NIST AMB2025-07 resources be assembled reproducibly, with authoritative version-identifiable sources and identifiers, to provide **new independent process conditions** together with thermal measurements and melt-pool geometry, thereby addressing the seven-process-case information limitation diagnosed by D06?

This is a source/identity/manifest feasibility gate, not a prediction experiment. / 본 단계는 source·identity·manifest feasibility이며 예측실험이 아니다.

## 2. Outcome-Blind Boundary / outcome 비사용 경계

During candidate/source/identity freezing: / 후보·source·identity 고정 중
- do not inspect new AMB2025-07 geometry answer values;
- do not use new thermal/geometry target values to select sources, IDs, joins, thresholds, or conditions;
- metadata, filenames, units, experiment-design descriptions, file sizes, hashes/checksums, identifiers, and schema are eligible;
- any later outcome use requires this feasibility gate to be resolved first and a separate predictive/external-validation preregistration.

## 3. Authoritative Candidate Facts Frozen Before Deeper Inspection / 심층검사 전 고정 공식 사실

Current official NIST AM Bench 2025 documentation describes `AMB2025-07` as: / 현행 NIST 공식 설명
- arrays of adjacent laser tracks on **bare Alloy 718 plate**;
- two pad geometries;
- two laser turnaround / skywriting times while core laser parameters are otherwise held constant;
- challenge-associated high-speed thermography quantities including cooling/time-above-melting;
- melt-pool geometry from cross-sections;
- current direct-data guidance identifies `mds2-3707` for AMB2025-06/07 challenge calibration data.

These facts establish a plausible independent-condition expansion candidate, but they do **not** establish that exact raw thermal↔geometry measurement manifests are public or deterministically pairable. / 독립정보 후보 가능성은 지지하지만 exact raw paired manifest 존재·조인을 의미하지 않는다.

## 4. Primary Unknown / 핵심 미확인

`UNKNOWN`: exact authoritative public versioned records for the raw or analysis-ready AMB2025-07 thermal measurement and melt-pool geometry measurement datasets, plus deterministic pairing semantics. / raw 또는 분석가능 thermal·geometry 측정 dataset의 exact 공개 version/record와 pairing semantics.

Do not substitute `mds2-3707` calibration/answer materials for missing measurement publications. / calibration·answer 자료를 누락 measurement source의 대체물로 사용하지 않는다.

## 5. Frozen Feasibility Gate / 고정 feasibility 게이트

### A. `PASS_INDEPENDENT_EXPANSION_READY`
All conditions must hold / 모두 충족:
1. authoritative, public, version-identifiable NIST source(s) expose the required thermal measurement and geometry/response artifacts or an authoritative exact correspondence to them;
2. unit of observation, pad/location/condition identifiers, and repeat structure are explicit enough for deterministic pairing without invented IDs;
3. at least one experimental condition axis is demonstrably independent of the 2022 seven-case design, such as turnaround/skywriting time or pad scenario;
4. snapshot/version provenance is recoverable and relevant files can be checksum-frozen;
5. access/execution remain `COST-001` compliant;
6. a future validation question can be defined without treating 2022 and 2025 rows as direct track-level joins.

### B. `PARTIAL_SOURCE_READY`
Authoritative experiment/calibration/answer metadata are public and independent conditions are explicit, but exact raw thermal↔geometry paired measurement manifests remain incomplete or not yet publicly exposed. / 실험·독립조건은 명확하나 exact raw paired manifest 불완전.

### C. `HOLD_DATA_OR_IDENTITY_GAP`
Required raw measurement publication, identifiers, or pairing semantics cannot be established from current authoritative public evidence without unsupported substitution. / 데이터·식별자·pairing gap.

### D. `REJECT_NO_INDEPENDENT_INFORMATION`
Candidate does not actually add an independent condition/modality relevant to D06's controlling failure mode. / D06 문제에 독립정보를 추가하지 않음.

Only one gate outcome is assigned. No threshold or condition may be changed after outcome-value inspection. / 단일 판정만 허용하며 outcome 확인 후 gate 변경 금지.

## 6. Frozen Work Order / 고정 작업순서

1. resolve current NIST PDR records/versions for AMB2025-07 calibration, thermography/thermal measurements/results, and optical/melt-pool geometry using metadata first;
2. enumerate public files, stable identifiers, sizes, hashes/checksums where exposed;
3. recover experiment hierarchy: pad geometry, turnaround/skywriting time, bare/powder state, locations, repeats, measurement IDs;
4. determine deterministic thermal↔geometry pairing semantics without inspecting outcome values;
5. quantify **independent condition count**, not merely row count;
6. assess snapshot/version lineage and `reproduction_risk`;
7. apply `COST-001` before any large download/compute;
8. assign exactly one frozen feasibility outcome;
9. only after `PASS_INDEPENDENT_EXPANSION_READY` may a separate predictive/external-validation experiment be preregistered.

## 7. Explicit Non-Actions / 명시 비행동

- no post-hoc tuning of E03/E05/D06;
- no higher-capacity model on the same 2022 21-track representation;
- no assumption of 2022↔2025 row-level or track-level identity;
- no invented cross-publication IDs;
- no outcome-driven candidate or file selection;
- no paid API/data/cloud/GPU/larger runner;
- unknown billing or possible monetary overage => `HOLD_COST_APPROVAL` before execution.

## 8. COST-001 / 비용 규약

Zero incremental monetary cost is mandatory. / 추가 금전비용 0원 의무.

Metadata-first investigation is preferred. Large files are downloaded only when necessary to decide the frozen gate and after their public/free path is verified. / metadata 선확인, 대용량 파일은 gate 판정에 필요한 경우에만 무료 경로 확인 후 사용.

## 9. Success Does Not Mean Model Success / PASS의 의미 경계

`PASS_INDEPENDENT_EXPANSION_READY` would mean only that the **data/source/identity structure is defensible enough to preregister a later experiment**. It does not mean AMB2025-07 improves prediction, validates E05, or establishes a causal thermal mechanism. / PASS는 후속실험 자격만 의미하며 예측향상·E05 검증·인과기제를 의미하지 않는다.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `STATE-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and frozen-gate controls. / 관련 규약 준수.
