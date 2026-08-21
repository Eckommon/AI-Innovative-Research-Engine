# AMBENCH-001 — NIST AM Bench Methodological Calibration / NIST AM Bench 방법론 보정

**Research ID / 연구 ID:** `AMBENCH-001`  
**State / 상태:** `CALIBRATION_COMPLETE`  
**Wave:** 0  
**Calibration date / 보정일:** 2026-08-21  
**Topic track / 소재 트랙:** `PERSISTENT_BOTTLENECK` — additive-manufacturing quality, qualification, and interoperability / 적층제조 품질·인증·상호운용성

## 1. Purpose / 목적

**한국어**  
NIST AM Bench 2022 `AMB2022-03`을 이용해 엔진의 메타데이터, IPS, 데이터 결합, 가설, feasibility gate가 실제 실험·측정 데이터에서 작동하는지 보정한다.

**English**  
Use NIST AM Bench 2022 `AMB2022-03` to calibrate whether the engine's metadata schema, IPS, dataset-combination logic, hypothesis discipline, and feasibility gate work on real experimental and measurement data.

## 2. Verified Experimental Structure / 검증된 실험 구조

```text
Laser power + scan speed + spot size / 레이저 출력 + 주사속도 + spot size
                ↓
21 single tracks = 7 cases × 3 repeats / 7개 조건 × 3회 반복
                ↓
In-situ thermography / 실시간 열화상
TTAM + TSCR + TLCR + TTCR
                ↓
Ex-situ optical microscopy / 사후 광학현미경
melt-pool depth + width
                ↓
NIST benchmark challenge results / NIST 벤치마크 결과
```

NIST challenge documentation states that seven combinations of power, scan speed, and spot size were tested with three thermography repeats per condition. Optical microscopy reports six melt-pool geometry measurements per condition.  
NIST challenge 문서에 따르면 power·scan speed·spot size의 7개 조합을 조건별 3회 열화상 반복으로 시험했고, 광학현미경 결과는 조건별 6개 melt-pool geometry 측정을 보고한다.

## 3. Primary Datasets / 핵심 데이터셋

| Internal ID | NIST PDR | Role / 역할 | State |
|---|---|---|---|
| `AMB03-THERMO-2716` | DOI `10.18434/mds2-2716` | In-situ thermography + scan strategy / 열화상 + 스캔전략 | `SCREENED` |
| `AMB03-OPTICAL-2718` | DOI `10.18434/mds2-2718` | optical microscopy + melt-pool geometry / 광학현미경 + 용융풀 형상 | `CALIBRATED` |
| `AMB03-MICRO-2775` | DOI `10.18434/mds2-2775` | SEM/EBSD/EDS cross-sectional microstructure / 단면 미세조직 | `JOIN_CANDIDATE` |
| `AMB03-COUPLING-3842` | PDR `mds2-3842` | dynamic laser coupling / 동적 레이저 결합 | `JOIN_CANDIDATE` |

## 4. Join Keys / 조인 키

**Verified / 확인됨:** shared `AMB2022-03` experiment identity and case numbers `0`, `1.1`, `1.2`, `2.1`, `2.2`, `3.1`, `3.2`; specimen/sample naming embeds material/plate/part/line identity such as `AMB2022-718-SH1-BP1-L1.2`.  
**확인됨:** 공통 `AMB2022-03` 실험 ID와 case 번호 `0`, `1.1`, `1.2`, `2.1`, `2.2`, `3.1`, `3.2`; 표본명에는 `AMB2022-718-SH1-BP1-L1.2`처럼 소재·plate·part·line 정보가 내장된다.

**Caveat / 주의:** thermography repeats and optical cross-sectional measurements are not assumed to be one-to-one observations merely because they share a case. Replicate-level pairing must be validated from raw-file metadata before a paired model is claimed.  
열화상 반복과 광학 단면 측정은 같은 case를 공유한다고 해서 1:1 관측치로 간주하지 않는다. raw-file metadata에서 replicate-level pairing을 확인하기 전에는 paired model을 주장하지 않는다.

## 5. Calibration Scores / 보정 점수

### Dataset IPS — `AMB03-OPTICAL-2718`: **91/100 — Priority A**

| Criterion / 기준 | Score | Rationale / 근거 |
|---|---:|---|
| Problem importance / 문제 중요도 | 13/15 | AM 품질·인증은 광범위 채택의 지속 병목 / quality and qualification remain adoption bottlenecks |
| Raw granularity / 원시 세밀도 | 10/10 | TIFF micrographs + measured geometry + replicate structure |
| Temporal/spatial resolution / 시간·공간 해상도 | 8/10 | high spatial detail, but optical dataset itself is ex-situ and not time-resolved |
| Ground truth/outcomes / 결과·정답값 | 15/15 | measured melt-pool depth/width with mean/std and benchmark definitions |
| Joinability / 결합 가능성 | 14/15 | common experiment/case/sample semantics with thermography and microstructure |
| AI/ML applicability / AI·ML 적용성 | 9/10 | image, regression, multimodal and uncertainty-aware tasks possible |
| Validation feasibility / 검증 가능성 | 10/10 | explicit benchmark challenges and metrics/results exist |
| Machine readability / 기계판독성 | 3/5 | XLSX + TIFF + README; rich but heterogeneous and no simple analysis API |
| License/reuse / 재사용성 | 5/5 | NIST public data/open license path verified |
| Underexplored potential / 미개척 잠재력 | 4/5 | rich multimodal joins remain possible, while AM Bench already has active research use |
| **Total** | **91/100** | `Priority A` |

### Dataset IPS — `AMB03-THERMO-2716`: **92/100 — Priority A (provisional / 잠정)**
High temporal/spatial measurement value, direct scan strategy, multiple thermography outputs, and strong joinability; exact file-level scoring remains subject to raw distribution parsing.  
시간·공간 측정 밀도, scan strategy, 열화상 결과, 높은 조인성을 반영한 잠정 점수이며 raw distribution 세부 파싱 후 재확인한다.

### Combination IPS — `2716 + 2718`: **95/100 — Priority A (calibration estimate / 보정 추정)**
The pair directly constructs `process → thermal history → geometry outcome`, with shared cases and public benchmark outputs. Replicate-level semantic alignment remains the principal uncertainty.  
두 데이터셋은 직접 `공정 → 열이력 → 형상 결과` 구조를 만들며 공통 case와 공개 benchmark 결과가 존재한다. 핵심 불확실성은 replicate-level 의미 정렬이다.

## 6. Feasibility Result / 실행가능성 검증 결과

Published NIST result tables were joined at the seven-case aggregate level. A deliberately simple leave-one-condition-out linear test was used to avoid claiming high-capacity ML performance from only seven aggregated observations.  
NIST 공개 결과표를 7개 case 집계수준에서 조인했고, 단 7개 관측으로 고용량 ML 성능을 주장하지 않기 위해 의도적으로 단순한 leave-one-condition-out 선형 검증을 사용했다.

- **Depth / 깊이:** process-only (`power + speed + spot size`) RMSE ≈ **19.71 µm**; `VED`-only ≈ **19.32 µm**; best single thermal feature (`TTAM`) ≈ **38.96 µm**.
- **Width / 폭:** process-only RMSE ≈ **14.63 µm**; `VED`-only ≈ **28.36 µm**; best single thermal feature (`TLCR`) ≈ **13.71 µm**.
- `TLCR` improves width RMSE by ≈ **6.3%** versus the full process-only baseline, below the predefined 10% material-improvement threshold; it improves ≈ **51.6%** versus the weaker VED-only baseline.

**Decision / 판단:** the data combination is feasible, but the blanket claim that aggregated thermography metrics necessarily improve geometry prediction is **not validated**. Aggregate-level evidence is `INCONCLUSIVE` for a general multimodal-gain claim; a raw/replicate-level study is required.  
데이터 결합 자체는 실행 가능하지만, 집계 열화상 지표가 항상 형상 예측을 개선한다는 포괄 가설은 **검증되지 않았다**. 일반적인 multimodal 개선 주장은 집계수준에서 `INCONCLUSIVE`이며 raw/replicate-level 검증이 필요하다.

## 7. What the Engine Learned / 엔진 보정 결과

1. `case_id` alone is insufficient; a separate `replicate_alignment` field is required. / `case_id`만으로는 부족하고 `replicate_alignment` 필드가 필요하다.
2. Dataset IPS can be high even when a simplistic AI hypothesis fails. / 단순 AI 가설이 실패해도 데이터셋 IPS는 높을 수 있다.
3. Ground truth quality and benchmark design deserve high weighting. / 정답값 품질과 benchmark 설계는 높은 가중치가 타당하다.
4. Aggregate and raw-level evidence must be separated. / 집계수준과 raw-level 증거를 분리해야 한다.
5. `process → measurement → outcome` generalizes well as a cross-domain discovery pattern. / `공정 → 측정 → 결과`는 타 도메인으로 일반화 가능한 패턴이다.

## 8. Issue #1 Gate / Issue #1 게이트

Calibration requirements are satisfied at the benchmark/calibration level: authoritative sources, variables, join semantics, IPS, hypothesis, baseline, metric, rejection threshold, and preliminary feasibility test are documented.  
benchmark/calibration 수준에서 공식 출처, 변수, 조인 의미, IPS, 가설, baseline, 지표, 기각기준 및 예비 feasibility 검증이 모두 문서화되었다.

**Issue #1 disposition / 처리:** `COMPLETED`  
**Next official queue / 다음 공식 큐:** Issue #2 — Wave 1 United States dataset discovery / 미국 데이터셋 탐색.

See / 참조: `SOURCES.md`, `DATASET_PROFILE.md`, `HYPOTHESES.md`, `EXPERIMENT.md`, `RESULTS.md`.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
