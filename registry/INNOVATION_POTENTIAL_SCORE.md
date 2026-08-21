# Innovation Potential Score (IPS) v0.1 / 혁신 잠재력 점수 v0.1

## Purpose / 목적

`IPS`는 실제 데이터셋, 데이터 조합, 프로젝트 후보를 우선순위화하기 위한 평가 도구다. 연구 소재 자체의 트렌드성 평가는 IPS와 분리한다.  
`IPS` is a triage framework for actual datasets, dataset combinations, and project candidates. Topic trend screening remains separate from IPS.

## 1. Dataset IPS / 데이터셋 IPS

| Criterion / 기준 | Max / 배점 |
|---|---:|
| Industrial / societal problem importance / 산업·사회 문제 중요도 | 15 |
| Raw-data granularity / 원시 데이터 세밀도 | 10 |
| Temporal / spatial resolution / 시간·공간 해상도 | 10 |
| Ground truth / outcome availability / 정답값·결과변수 존재 | 15 |
| Joinability with other datasets / 타 데이터셋 결합 가능성 | 15 |
| AI / ML applicability / AI·ML 적용 가능성 | 10 |
| Experimental / validation feasibility / 실험·검증 가능성 | 10 |
| API / machine readability / API·기계판독성 | 5 |
| License / reusability / 라이선스·재사용성 | 5 |
| Underexplored / novelty potential / 미개척·신규성 잠재력 | 5 |
| **Total / 합계** | **100** |

## 2. Suggested Bands / 권장 등급

- **85–100: Priority A / 우선 A** — 직접 feasibility 검증을 진행할 강한 후보 / strong candidate for direct feasibility testing.
- **70–84: Priority B / 우선 B** — 유망, 조인·target 정의 추가 검토 / promising; inspect joins and target definition.
- **55–69: Priority C / 우선 C** — 보조 데이터 또는 도메인 컨텍스트로 유용 / useful supporting dataset or context.
- **Below 55: Priority D / 우선 D** — 고가치 결합으로 역할이 바뀌지 않는 한 보관 / archive unless a high-value combination changes its role.

## 3. Mandatory Rationale / 필수 점수 근거

점수만 기록해서는 안 된다. / A numeric score alone is insufficient.

모든 평가에는 다음을 기록한다. / Every assessment records:
- criterion-level rationale / 기준별 근거;
- unknowns that may change the score / 점수를 바꿀 수 있는 미확인 요소;
- candidate target/outcome / 잠재 결과변수;
- candidate joins / 잠재 조합;
- evidence limitations / 증거 한계;
- next validation action / 다음 검증 행동.

## 4. Separate Scores / 점수 분리

1. **Dataset IPS / 데이터셋 IPS** — 단일 데이터셋 자체의 연구 잠재력 / intrinsic research potential of one dataset.
2. **Combination IPS / 조합 IPS** — 여러 데이터셋을 결합하면서 생성되는 추가 가치 / value created by joining datasets.
3. **Project IPS / 프로젝트 IPS** — 가설, feasibility, 신규성, 실용성까지 포함한 전체 프로젝트 가치 / full hypothesis, feasibility, novelty, and practical-use potential.

낮은 Dataset IPS가 높은 Combination IPS의 핵심 구성요소가 될 수 있다. / A low Dataset IPS may still participate in a high Combination IPS.

## 5. Combination IPS Guidance / 조합 IPS 가이드

Combination IPS는 다음을 별도 검토한다. / Combination IPS additionally examines:

- 실제 공통키와 의미적 조인 가능성 / real join keys and semantic compatibility;
- 시간·공간 정렬 품질 / temporal and spatial alignment quality;
- 단일 데이터로는 보이지 않던 새로운 설명·예측력 / incremental explanatory or predictive value;
- 데이터 누수·중복·교란 위험 / leakage, duplication, and confounding risks;
- 결합 후 실제 검증 가능한 target의 존재 / existence of a testable target after combination.

## 6. Project IPS Guidance / 프로젝트 IPS 가이드

Project IPS는 IPS 점수 외에도 다음을 독립적으로 기록한다. / Project IPS also records separately:

- evidence strength / 증거 강도;
- reproducibility / 재현성;
- novelty / 신규성;
- practical utility / 실용성;
- scalability / 확장성;
- implementation cost/risk / 구현 비용·위험.

## 7. Calibration Rule / 보정 규칙

NIST AM Bench는 초기 고품질 calibration case다. 그러나 평판을 근거로 높은 점수를 미리 부여하지 않으며, 파일·필드·Ground Truth·조인 구조·접근성을 실제로 확인한 뒤 항목별 점수를 확정한다.  
NIST AM Bench is the initial high-quality calibration case, but no high score is pre-assigned by reputation. Its exact score is finalized only after actual files, fields, ground truth, join structure, and access are inspected.

## 8. Language Rule / 언어 규칙

평가 근거와 결론은 `LANG-001`에 따라 한글/영문 병기한다. 원천 필드명·표준명은 원문을 유지한다.  
Assessment rationales and conclusions comply with `LANG-001`; native fields and standards remain in their original form.
