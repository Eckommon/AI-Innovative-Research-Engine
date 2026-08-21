---
id: AMBENCH-NEXT-TRIAGE
type: triage
state: COMPLETED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F02/README.md
  - research/AMBENCH-E03/README.md
  - research/AMBENCH-E03/RESULT.md
---

# AMBENCH Next-Hypothesis Triage / AMBENCH 다음 가설 선별

## Context / 배경

`AMBENCH-E03` closed as `NO_MATERIAL_GAIN`: ten preregistered raw-digital-level thermography summaries did not add robust process-case LOCO predictive value beyond process parameters. / `AMBENCH-E03`은 10개 사전고정 raw-DL thermography summary가 process parameter 대비 일반화 추가가치를 보이지 못해 `NO_MATERIAL_GAIN`으로 종료됐다.

The next step must add **new information or physical meaning**, not merely model/feature complexity. / 다음 단계는 단순 모델·feature 복잡도가 아니라 새로운 정보 또는 물리적 의미를 추가해야 한다.

## Ranking / 순위

| Rank | Candidate / 후보 | New information vs E03 | Semantic grounding | Generalization/sample benefit | Overfit risk | Disposition |
|---|---|---|---|---|---|---|
| 1 | **Calibrated temporal thermal representation / 보정 열동역학 표현** | High | High: NIST HDF5 calibration + 30 kfps metadata; AM Bench defines track cooling-rate quantities | Same n=21, but materially stronger physical representation | Medium | **PRIORITY — open feasibility gate** |
| 2 | Dynamic laser coupling `mds2-3842` alignment / 동적 레이저 결합 정렬 | High | Medium-High | Same nominal process-condition family; may add separate physical modality | Medium | feasibility first; do not assume BP4↔BP1 track identity |
| 3 | Microstructure `mds2-2775` alignment/outcome / 미세조직 정렬 | Medium-High | Medium-High | Adds outcome richness, not necessarily independent process cases | Medium | secondary feasibility |
| 4 | Additional compatible AM Bench experiments / 추가 독립 공정조건 확장 | **Very High** | Unknown until exact compatible source is identified | **Highest potential sample/generalization benefit** | Low-Medium | continue discovery; no direct compatible single-track expansion frozen yet |
| 5 | Spatial thermal morphology / 공간 열형상 | Medium | Incomplete: physical pixel/axis semantics not yet frozen | Same n=21 | High | `HOLD_SEMANTIC_GROUNDING` |
| 6 | Deep/high-capacity model on E03 representation / 고용량 모델 | Low | N/A | No new independent information | **Very High** | `REJECT_AS_NEXT_STEP` |

## Priority Decision / 우선 결정

**Select calibrated temporal thermal representation feasibility as the next official gate. / 다음 공식 게이트로 보정 열동역학 표현 feasibility를 선택한다.**

Rationale / 근거:
1. E03's failure could reflect representation weakness rather than absence of thermal information. / E03 실패가 열정보 부재가 아니라 표현 부족일 가능성을 분리할 수 있다.
2. NIST raw HDF5 already exposes calibration metadata and 30,000 fps acquisition metadata, so this direction is grounded in authoritative source semantics rather than post-hoc feature invention. / NIST 원본에 calibration·30 kfps 메타데이터가 있어 사후 임의 feature보다 근거가 강하다.
3. AM Bench publishes track solid/liquid cooling-rate benchmark concepts, making physically temporal quantities directly relevant to the benchmark domain. / AM Bench가 track solid/liquid cooling-rate benchmark를 정의하므로 시간 열동역학량이 benchmark 목적과 직접 연결된다.
4. It preserves low model complexity and changes primarily the **representation**, allowing a later experiment to isolate whether physically meaningful thermography improves over E03's raw-DL summaries. / 모델 복잡도를 유지하고 표현만 주로 바꿔 E03과 비교 가능하다.

## Important Boundary / 중요 경계

This triage does **not** authorize a new prediction model yet. The next item is a feasibility gate that must prove a deterministic, documented, track-level calibrated temporal representation without optical-outcome tuning. / 본 선별은 새 예측모델을 즉시 승인하지 않는다. 다음은 optical outcome tuning 없이 결정론적·문서화된 track-level 보정 열동역학 표현을 만들 수 있는지 검증하는 feasibility다.

Dynamic laser coupling is not merged with BP1 optical geometry unless a separate authoritative identity/alignment gate passes. / dynamic laser coupling은 별도 권위 식별자 정렬 게이트 통과 전 BP1 optical geometry와 결합하지 않는다.

## Next / 다음

Open `AMBENCH-F04 — Calibrated Thermal-Dynamics Representation Feasibility / 보정 열동역학 표현 가능성 검증`.
