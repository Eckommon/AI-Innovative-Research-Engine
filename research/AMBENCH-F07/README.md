---
id: AMBENCH-F07
type: feasibility
state: COMPLETED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D06/RESULT.md
  - research/AMBENCH-POST-D06-TRIAGE.md
  - research/AMBENCH-F07/RESULT.md
  - Issue #21
---

# AMBENCH-F07 — AMB2025-07 Independent-Condition Expansion Feasibility / AMB2025-07 독립 공정조건 확장 가능성 검증

**State / 상태:** `COMPLETED — PARTIAL_SOURCE_READY`  
**Issue / 이슈:** #21  
**Parent / 상위:** `AMBENCH-D06 — PROCESS_CASE_PROXY_DOMINANT`  
**Detailed result / 상세 결과:** [`RESULT.md`](RESULT.md)

## 1. Research Question / 연구 질문

**KO:** NIST AMB2025-07의 공개 자료가 D06에서 확인된 기존 7개 process-case 정보제약을 완화할 수 있도록, **새로운 독립 공정조건**과 thermal measurement 및 melt-pool geometry를 권위 있고 version-identifiable한 source/identifier로 재현 가능하게 구성할 수 있는가?  
**EN:** Can public NIST AMB2025-07 resources be assembled reproducibly, with authoritative version-identifiable sources and identifiers, to provide **new independent process conditions** together with thermal measurements and melt-pool geometry, thereby addressing the seven-process-case information limitation diagnosed by D06?

This is a source/identity/manifest feasibility gate, not a prediction experiment. / 본 단계는 source·identity·manifest feasibility이며 예측실험이 아니다.

## 2. Outcome-Blind Boundary / outcome 비사용 경계

During candidate/source/identity freezing: / 후보·source·identity 고정 중
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

## 4. Frozen Feasibility Gate / 고정 feasibility 게이트

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

## 5. Final Gate Result / 최종 게이트 결과

**`PARTIAL_SOURCE_READY`**

Observed source/identity facts / 확인된 source·identity:
- detailed NIST design defines `0.75 ms` and `5.0 ms` turnaround conditions on bare IN718;
- design has three repeat plates per turnaround condition and two pad geometries within the experiment;
- NIST optical microscopy/melt-pool measurement publication is directly identified as **`mds2-4103`**;
- NIST calibration/challenge publication is **`mds2-3707`**;
- high-speed thermography is explicitly documented as an experimental modality;
- an exact version-identifiable public raw/analysis-ready AMB2025-07 thermography measurement PDR publication was **not established** through the authoritative NIST routes investigated.

Therefore exact thermal↔geometry paired manifests cannot yet be checksum-frozen or deterministically joined. / exact paired manifest 미고정.

## 6. Decision Consequence / 후속 결정

- do not open a predictive AMB2025-07 experiment yet;
- preserve `mds2-4103` and the specimen hierarchy as future-qualified assets;
- treat the missing thermal PDR as `NOT_VERIFIED_PUBLICATION`, not proof of permanent absence;
- move to the next no-cost candidate with public measurement data, `mds2-3842` dynamic laser coupling, under a separate identity/information feasibility gate;
- do not infer BP4↔BP1 physical-track identity from nominal process-case similarity.

## 7. COST-001 / 비용 규약

F07 was resolved metadata-first without large raw measurement download or paid compute. / 대용량 raw 다운로드·유료 compute 없이 판정.

Unknown future billing or possible monetary overage => `HOLD_COST_APPROVAL` before execution. / 비용 불명확 시 사전승인.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `STATE-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and frozen-gate controls. / 관련 규약 준수.
