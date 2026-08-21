# Innovation Discovery Methodology / 혁신 탐색 연구 방법론

## 1. Objective / 목적

**한국어**  
엔진은 공공·연구 데이터를 통제된 증거 파이프라인을 통해 검증 가능한 혁신 후보로 전환한다. 연구 대상은 단일 데이터셋 자체보다, 데이터 간 관계가 새로운 예측·최적화·스트레스테스트·벤치마크·의사결정도구·산업 통찰로 연결되는 구조다.

**English**  
The engine converts public/research data into testable innovation candidates through a controlled evidence pipeline. The higher-value target is not merely a useful dataset, but a relationship among datasets that supports a new prediction, optimization, stress test, benchmark, decision tool, or industrial insight.

## 2. Official Pipeline / 공식 파이프라인

### Stage 1 — Source Discovery / 소스 탐색
권위 있는 데이터 발행기관·카탈로그를 국가·지역·기관·도메인별로 식별한다. / Identify authoritative data publishers and catalogs by jurisdiction, agency, region, and domain.

Minimum / 최소 기록: source name / 소스명, jurisdiction / 관할, publisher / 발행기관, URL, API/access mode / 접근방식, metadata standard / 메타데이터 표준, license/reuse / 라이선스·재사용, priority domains / 우선 도메인.

### Stage 2 — Metadata Harvesting / 메타데이터 수집
선별과 재현에 필요한 데이터셋 수준 메타데이터를 수집한다. / Capture dataset-level metadata sufficient for triage and reproducibility.

Recommended / 권장: identifier, publisher, description, temporal/spatial coverage, update frequency, distributions/formats, API/download endpoint, license/rights, schema/documentation, quality statement, candidate join keys, candidate outcomes.

### Stage 3 — Dataset Triage / 데이터셋 선별
`registry/INNOVATION_POTENTIAL_SCORE.md`에 따라 평가한다. / Score using `registry/INNOVATION_POTENTIAL_SCORE.md`.

별도로 유지 / Keep separate:
- `Dataset IPS` — 단일 데이터셋 잠재력 / intrinsic dataset potential;
- `Combination IPS` — 데이터 결합 잠재력 / value from joining datasets;
- `Project IPS` — 가설·실행가능성·실용성 포함 프로젝트 잠재력 / full project potential.

### Stage 4 — Relationship Discovery / 관계 탐색
엔티티·시설·기업, 지리, 시간, 산업분류, 제품·소재, 인프라 자산, 물리측정, 이벤트 ID, 정책·규제체계 등을 기준으로 조인 가능한 관계를 탐색한다. / Search for joinable relationships across entity/facility/company, geography, time, industry classification, product/material, infrastructure asset, physical measurement, event ID, and policy/regulatory regime.

필드명이 같다는 이유만으로 조인을 인정하지 않는다. 의미적 호환성을 반드시 기록한다. / Matching field names alone do not prove joinability; semantic compatibility must be documented.

### Stage 5 — Hypothesis Generation / 가설 생성
관계로부터 반증 가능한 주장을 만든다. / Generate a falsifiable claim from the relationship.

```text
Given [datasets/evidence] / [데이터·증거]가 주어졌을 때,
we hypothesize that [relationship/mechanism] / [관계·메커니즘]이
can predict/optimize/explain [target] / [대상]을 예측·최적화·설명할 수 있으며,
under [scope/conditions] / [범위·조건]에서,
measured by [metric/rejection criterion] / [평가지표·기각기준]으로 검증한다.
```

### Stage 6 — Feasibility Test / 실행 가능성 검증
본 실험 전에 실제 접근, 스키마, 조인키, 시간·공간 정렬, 결측·표본수, 누수(leakage), 라이선스, baseline 정의 가능성을 확인한다. / Before full experimentation, verify real access, schema usability, join keys, temporal/spatial alignment, missingness/sample size, leakage risk, licensing, and baseline definability.

### Stage 7 — Controlled Experiment / 통제 실험
최종 결과를 보기 전에 target, baseline, evaluation split/design, primary metric, sensitivity checks, rejection criteria, reproducibility steps를 정의한다. / Predefine target, baseline, evaluation design, primary metrics, sensitivity checks, rejection criteria, and reproducibility steps before final evaluation.

Experiment classes / 실험 유형: prediction / 예측, classification / 분류, anomaly detection / 이상탐지, optimization / 최적화, causal/quasi-causal / 인과·준인과, simulation/digital twin / 시뮬레이션·디지털트윈, stress testing / 스트레스테스트, index/ranking / 지수·랭킹, computer vision/signal analysis / 비전·신호분석, benchmark construction / 벤치마크 구축.

### Stage 8 — Innovation Registry / 혁신 레지스트리
성공뿐 아니라 실패·불확정·보류도 기록한다. / Record validated, rejected, inconclusive, and held outcomes.

Minimum result / 최소 결과: research ID, datasets, hypothesis, experiment design, result, evidence class, limitations, practical utility, novelty assessment, next action, final state.

## 3. Research Material Discovery Gate / 연구 소재 탐색 게이트

`AMBENCH-001` 이후 대규모 확장을 하기 전에, 엔진은 연구 소재를 다음 두 축에서 정기적으로 탐색한다. / Before broad scaling after `AMBENCH-001`, the engine periodically scans two topic tracks:

1. **Frontier Opportunity / 현대 유망 영역** — 빠른 수요 성장·기술변화·사회적 파급력 / rapid demand growth, technological change, and societal impact.
2. **Persistent Bottleneck / 잔존 병목 영역** — 성숙한 시스템이지만 인프라·품질·표준·비용·공급망·운영 병목 지속 / mature systems with persistent infrastructure, quality, standardization, cost, supply-chain, or operational constraints.

소재 탐색 점수는 IPS와 분리된 선별 도구로 사용하며, 실제 데이터셋이 확인된 뒤에만 Dataset/Combination/Project IPS를 부여한다. / Topic-screening scores remain separate from IPS; Dataset/Combination/Project IPS is assigned only after actual datasets are inspected.

## 4. NIST AM Bench Reference Pattern / NIST AM Bench 기준 패턴

```text
Process Conditions / 공정 조건
  → Physical Experiment / 실제 제조·실험
  → Measurement & Imaging / 측정·영상
  → Material or Geometry Outcome / 소재·형상 결과
  → Benchmark / Ground Truth / 벤치마크·정답값
```

이 패턴은 `X_process + X_measurement → Y_quality` 같은 명시적 검증 구조를 지원한다. 엔진은 단일 데이터 또는 데이터 조합으로 이와 유사한 입력–측정–결과 구조를 만들 수 있는 대상을 우선 탐색한다.  
This pattern supports explicit test mappings such as `X_process + X_measurement → Y_quality`. The engine preferentially searches for datasets—or combinations—that can construct similarly explicit input–measurement–outcome structures.

## 5. Evidence, Novelty, Utility Separation / 증거·신규성·실용성 분리

최종 평가는 최소한 다음을 별도로 평가한다. / Final evaluation separately assesses:
1. evidence strength / 증거 강도;
2. reproducibility / 재현성;
3. novelty / 신규성;
4. practical utility / 실용성;
5. scalability / 확장성;
6. implementation cost/risk / 구현 비용·위험.

통계적으로 유의하다고 상업적으로 유용한 것은 아니며, 새롭다고 검증된 것도 아니다. / Statistical significance does not imply practical value, and novelty does not imply validation.

## 6. Cross-National Rule / 국가 간 분석 규칙

국가 간 비교에서는 classification, units, currency/inflation, timezone/period, spatial granularity, methodology changes, sampling/coverage, missing/censored observations를 명시적으로 점검한다.  
Cross-national work explicitly checks classification systems, units, currency/inflation treatment, time zones/periods, spatial granularity, methodology changes, sampling/coverage, and missing/censored observations.

## 7. Promotion Gates / 승격 게이트

```text
DISCOVERED / 발견
→ SCREENING / 선별
→ CANDIDATE / 후보
→ FEASIBILITY_TEST / 실행가능성 검증
→ EXPERIMENT / 실험
→ VALIDATED / REJECTED / INCONCLUSIVE / HOLD
```

AI가 그럴듯한 아이디어를 만들었다는 이유만으로 승격하지 않는다. / No candidate advances solely because an AI-generated idea sounds plausible.

## 8. Language Compliance / 언어 준수

공식 산출물은 `LANG-001` (`docs/LANGUAGE_POLICY.md`)을 따른다. / Official artifacts comply with `LANG-001` in `docs/LANGUAGE_POLICY.md`.
