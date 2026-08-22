---
id: AMBENCH-POST-D06-TRIAGE
type: triage
state: COMPLETED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D06/RESULT.md
  - research/AMBENCH-E05/RESULT.md
---

# AMBENCH Post-D06 Independent-Information Triage / D06 이후 독립정보 확대 후보 선별

## 1. Trigger / 선별 사유

`AMBENCH-D06` closed as `PROCESS_CASE_PROXY_DOMINANT`: all eight E05 thermal features were case-dominated and `PCA95_DIM=2`. / D06에서 E05 8개 feature가 모두 case 지배이고 유효차원 2로 확인됐다.

Therefore the next AM Bench step must add **independent process-condition information** or a **genuinely different physical sensing/data relationship**; simply increasing model capacity on the same 21 tracks is prohibited by `DEC-016`. / 다음 단계는 독립 공정조건 또는 실제 다른 sensing/data 관계를 추가해야 하며 동일 21-track 모델 고용량화는 금지한다.

This triage is outcome-blind with respect to any new candidate's target values. / 새 후보의 target 수치를 보지 않고 선별한다.

## 2. Official Source Facts Reverified 2026-08-22 / 공식 출처 재검증

### Candidate A — AMB2025-07 cross-cycle Alloy 718 pads / 2025 Alloy 718 pad

Official NIST AM Bench 2025 descriptions state: / NIST 공식 설명
- `AMB2025-07` uses arrays of adjacent laser tracks on **bare alloy 718 plate**;
- two pad geometries are used;
- **two laser turnaround / skywriting times** are varied while core laser parameters are otherwise held constant;
- challenge-associated measurements include **high-speed thermography-derived cooling/time-above-melting** and **melt-pool geometry** from cross-sections;
- detailed descriptions and solutions are posted;
- NIST's direct-data guidance currently lists `mds2-3707` as `AMB2025-06 and AMB2025-07 Challenge Problem Calibration Data`.

Authoritative sources / 권위 출처:
- NIST, `AM Bench 2025 Measurements and Challenge Problems`: https://www.nist.gov/ambench/am-bench-2025-measurements-and-challenge-problems
- NIST, `Short Descriptions of 2025 Benchmarks`: https://www.nist.gov/ambench/short-descriptions-2025-benchmarks
- NIST, `Direct AM Bench Data Links and Referencing Guidance`: https://www.nist.gov/ambench/direct-am-bench-data-links-and-referencing-guidance
- NIST PDR calibration identifier: https://doi.org/10.18434/mds2-3707

**Unresolved / 미확인:** the current direct-data guidance exposes the calibration publication, but this triage has **not yet established the exact public versioned raw thermography + geometry measurement manifests needed for a reproducible paired experiment**. This remains `UNKNOWN` and is the proposed feasibility target. / raw thermal·geometry paired manifest는 아직 확립하지 않음.

### Candidate B — `mds2-3842` Dynamic Laser Coupling / 동적 레이저 결합

NIST's direct-data guidance lists `Dynamic Laser Coupling of Scanned Single Tracks on Bare IN718 with Varying Beam Diameter, Scan Speed, and Power` under `AMB2022-03`, identifier `mds2-3842`. / AMB2022-03의 별도 물리 sensing dataset으로 공식 등재.

The AMB2022-03 measurement description uses the same seven nominal process cases and three repeats per case for the dynamic-coupling single-track design. / 동적 결합 측정은 동일한 7개 nominal process case × 3 repeat 설계를 사용한다.

Authoritative sources / 권위 출처:
- NIST direct-data guidance above;
- `AMB2022-03 Benchmark Measurements and Challenge Problems` official PDF;
- NIST PDR: https://data.nist.gov/od/id/mds2-3842

**Boundary / 경계:** same nominal case design does **not** establish BP4↔BP1 physical track identity. It adds a distinct physical modality but does not automatically expand the number of independent process conditions. / nominal case 일치가 physical track 조인을 뜻하지 않는다.

### Candidate C — AMB2018-02 single-track thermography / 2018 single-track 열화상

NIST documents AMB2018-02 as single laser scans on bare IN625 with in-situ thermography and melt-pool/cooling-rate benchmark measurements. NIST publications report seven laser power/scan-speed combinations with multiple replications. / IN625 bare plate single-track, 7개 power/speed 조합·다수 반복.

Authoritative sources / 권위 출처:
- NIST, `AMB2018-02 Description`: https://www.nist.gov/ambench/amb2018-02-description
- NIST, `Thermography of Single Line Scans ... AM-Bench 2018`: https://www.nist.gov/publications/thermography-single-line-scans-performed-commercial-powder-bed-fusion-machine-additive
- NIST, `Measurement of the Melt Pool Length During Single Scan Tracks ...`: https://www.nist.gov/publications/measurement-melt-pool-length-during-single-scan-tracks-commercial-laser-powder-bed

**Boundary / 경계:** material (`IN625` vs `IN718`), machine/camera/calibration, and test-cycle differences create substantial domain shift. / 재료·장비·calibration domain shift 큼.

## 3. Post-D06 Ranking / D06 이후 순위

| Rank | Candidate / 후보 | Independent condition gain | New physical information | Semantic comparability to 2022 IN718 | Public reproducibility status | Primary risk | Disposition |
|---|---|---:|---:|---:|---:|---|---|
| **1** | **AMB2025-07 Alloy 718 pad cross-cycle feasibility** | **High** | High | High material/process-family, different pad task | `UNKNOWN/PARTIAL` until raw paired manifests verified | measurement-publication/identity availability | **SELECT F07 FEASIBILITY** |
| 2 | `mds2-3842` dynamic laser coupling | Low for process cases | **Very High** | **Very High nominal case family** | official PDR dataset identified | BP4↔BP1 track identity not established; may remain case proxy | fallback feasibility |
| 3 | AMB2018-02 IN625 single-track thermography | High | Medium-High | Medium-Low | strong archival/public precedent | alloy/machine/calibration domain shift | external-validation candidate after harmonization |

## 4. Selection Decision / 선택 결정

**Select `AMBENCH-F07 — AMB2025-07 Independent-Condition Expansion Feasibility` as the next official Work Queue item. / 다음 공식 Work Queue로 AMB2025-07 독립 공정조건 확장 feasibility를 선택한다.**

Rationale / 근거:
1. D06's controlling failure mode is insufficient independent process-case information in the current 21-track representation. / D06의 지배 문제를 직접 겨냥.
2. AMB2025-07 retains **alloy 718 + bare-plate laser scanning + high-speed thermal measurement + melt-pool geometry** while introducing a different experimental factor, **turnaround/skywriting time**, and a multi-track pad context. / 동일 material/process family에서 새로운 공정조건 축 추가.
3. This is better aligned with external-information gain than another same-21-track representation or model-capacity change. / 동일 21-track 복잡도 증가보다 정보이득 큼.
4. The main uncertainty is data-manifest/public pairing feasibility, so the correct next step is a **source/identity feasibility gate**, not a predictive model. / 핵심 불확실성이 데이터 공개·정렬이므로 feasibility가 우선.

## 5. Frozen F07 Feasibility Gate / F07 고정 feasibility 게이트

F07 must remain outcome-blind while establishing source/identity semantics. / source·identity 확인 중 target 수치 미사용.

### `PASS_INDEPENDENT_EXPANSION_READY`
All must hold / 모두 필요:
1. authoritative, public, version-identifiable NIST source(s) expose the required thermal measurement and geometry/response measurement artifacts or an authoritative exact correspondence to them;
2. unit of observation, pad/location/condition identifiers, and repeat structure are explicit enough for deterministic pairing without invented IDs;
3. at least one experimental condition axis is demonstrably independent of the 2022 seven-case design (e.g., turnaround/skywriting time / pad scenario) rather than only another repeat of the same case grid;
4. snapshot/version provenance is recoverable and files can be checksum-frozen;
5. access and execution remain `COST-001` compliant;
6. the future validation question can be defined without treating 2022 and 2025 rows as direct track-level joins.

### `PARTIAL_SOURCE_READY`
Authoritative experiment/calibration/answer metadata are public and independent conditions are explicit, but exact raw thermal↔geometry paired measurement manifests remain incomplete or not yet publicly exposed. / 실험은 명확하나 raw paired manifest 불완전.

### `HOLD_DATA_OR_IDENTITY_GAP`
Required raw measurement publication, identifiers, or pairing semantics cannot be established from current authoritative public evidence without unsupported substitution. / 데이터·ID gap으로 HOLD.

### `REJECT_NO_INDEPENDENT_INFORMATION`
Candidate turns out not to add an independent condition/modality relevant to D06's failure mode. / D06 문제에 새 정보 미추가.

## 6. Frozen F07 Work Order / F07 고정 작업순서

1. resolve current NIST PDR records/versions for `AMB2025-07` calibration, thermography/thermal results, and optical/melt-pool geometry using metadata only where possible;
2. enumerate files, sizes, hashes/checksums if publicly exposed, and stable identifiers;
3. recover experiment hierarchy: pad geometry, turnaround time, bare/powder state, locations, repeats, measurement IDs;
4. determine deterministic thermal↔geometry pairing semantics without reading outcome values;
5. quantify **independent condition count**, not merely row count;
6. assess snapshot/version lineage and `reproduction_risk`;
7. apply `COST-001` before any large download/compute;
8. assign one frozen F07 gate outcome;
9. only after `PASS_INDEPENDENT_EXPANSION_READY` may a separate predictive/external-validation hypothesis be preregistered.

## 7. Explicit Non-Actions / 명시 비행동

- do not tune E05/D06 on the same 21 tracks;
- do not inspect AMB2025-07 geometry answer values during source/identity freezing;
- do not assume 2022↔2025 row-level identity;
- do not substitute `mds2-3707` calibration/answer content for missing raw measurement data;
- do not use paid data/API/cloud/GPU; billing uncertainty => `HOLD_COST_APPROVAL`.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `STATE-001`, `FACT-001`, `UNKNOWN-001`, and frozen-gate controls. / 관련 규약 준수.
