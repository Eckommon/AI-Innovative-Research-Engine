# Wave 1 Synthesis & Next Experiment Selection / Wave 1 종합 및 다음 실험 선정

**Date / 기준일:** 2026-08-21  
**State / 상태:** `SYNTHESIS_COMPLETE`

## 1. Purpose / 목적

미국·한국·EU first-pass 결과를 동일한 관점에서 비교하여, 추정 IPS가 높다는 이유만으로 대규모 실험에 진입하지 않고 **가장 중요한 불확실성을 가장 낮은 비용으로 제거할 수 있는 다음 feasibility gate**를 선정한다.  
Compare U.S., Korean, and EU first-pass results under a common lens and select the next feasibility gate that removes the most important uncertainty at the lowest cost, rather than entering a large experiment solely because an estimated IPS is high.

## 2. Leading Candidates / 상위 후보

| Rank | Candidate | Region | Estimated Combination IPS | Principal Strength / 핵심 강점 | Critical Unknown / 핵심 미확인 |
|---:|---|---|---:|---|---|
| 1 | `C-KR-001` Grid Bottleneck Intelligence / 전력망 병목 지능화 | Korea | **97** | public 5-minute bus-level physical voltage/flow state + demand/renewable/weather/load joins | can `bus_number` be mapped defensibly to asset/geography? / 모선번호의 설비·지리 매핑 가능성 |
| 2 | `C-US-004` Registered Manufacturing Quality / 정렬 제조품질 | U.S. | **96** | NIST-registered process + in-situ + optical + XCT data in common coordinates | compute/data volume and incremental novelty beyond existing NIST work |
| 3 | `C-EU-001` Cross-National Grid Stress / 국가간 전력망 스트레스 | EU | **96** | harmonized multinational generation/load/transmission/outage/congestion + ERA5 | ENTSO-E auth/access and bidding-zone ↔ NUTS mapping |
| 4 | `C-EU-002` Industrial Energy–Emission Efficiency / 산업 에너지–배출 효율 | EU | **95** | >60k industrial sites with locations, emissions/waste; LCP energy-input data | reporting thresholds/completeness and production normalization |
| 5 | `C-KR-003` Port Weakest-Link Intelligence / 항만 최약고리 | Korea | **95** | event-level vessel timestamps + cargo/container + weather | derivation of defensible dwell/turnaround target from operational events |
| 6 | `C-US-001` Grid Bottleneck Intelligence / 전력망 병목 지능화 | U.S. | **93** | open EIA hourly grid + project-level interconnection queues + storm data | spatial/semantic alignment between queue projects and balancing-authority operations |

## 3. Feasibility Tournament / 실행가능성 토너먼트

This is a **selection matrix, not a new official scoring system**. / 이는 **선정용 비교표이며 새로운 공식 점수체계가 아니다**.

| Candidate | Open access / 공개접근 | Outcome signal / 결과신호 | Join certainty / 조인확실성 | Compute burden / 연산부담 | Cross-domain value / 교차분야 가치 | Immediate gate cost / 즉시 게이트 비용 |
|---|---|---|---|---|---|---|
| `C-KR-001` | High / 높음 | High / 높음 | **Unknown at bus mapping** / 모선 mapping 미확인 | Medium / 중간 | Very high / 매우 높음 | **Low** / 낮음 |
| `C-US-004` | High | Very high | Very high | **High** | Medium | Medium–high |
| `C-EU-001` | Medium (token/account) | High | Medium | Medium | Very high | Medium |
| `C-EU-002` | High | High | Medium–high | Medium | Very high | Medium |
| `C-KR-003` | High | Medium–high | High at vessel/event level | Medium | High | Medium |
| `C-US-001` | High | Medium | Medium | Medium | Very high | Medium |

## 4. Selection / 선정

### Next official feasibility gate / 다음 공식 feasibility gate

**`KR-GRID-F01 — KPX Bus Identifier Mapping Feasibility / KPX 모선 식별자 매핑 가능성 검증`**

**Why / 선정 이유**  
`C-KR-001` has the highest current Combination IPS estimate and uniquely exposes 5-minute physical bus-state estimates, but one semantic dependency can invalidate the intended localized bottleneck model: whether `bus_number` can be mapped to stable grid-asset or geographic semantics using public/authoritative sources. This question can be answered before downloading months of large data or training any model.  
`C-KR-001`은 현재 가장 높은 Combination IPS 추정값과 5분 물리계통 상태라는 독특한 장점을 갖지만, `bus_number`를 안정적 설비·지리 의미와 매핑할 수 있는지 여부가 지역 병목 모델 전체를 무효화할 수 있다. 이 질문은 대용량 수개월 데이터 다운로드나 모델학습 전에 검증 가능하다.

## 5. Falsifiable Gate / 반증 가능한 게이트

### Pass / 통과
At least one authoritative/public mapping path allows a meaningful share of KPX bus identifiers to be associated with stable asset, substation, voltage-level, or defensible geographic semantics, with documented identifier stability and no prohibited inference.  
권위 있는 공개 mapping 경로를 통해 의미 있는 비율의 KPX 모선 ID를 안정적인 설비·변전소·전압레벨 또는 방어 가능한 지리 의미와 연결할 수 있고 ID 안정성·제약을 문서화할 수 있다.

### Fail / 실패
Bus identifiers are effectively opaque, unstable, security-restricted, or only linkable by speculative inference such that localized stress interpretation would not be reproducible.  
모선 ID가 사실상 불투명·불안정·보안제한 상태이거나 추정에 의존해야 해서 지역 stress 해석이 재현 불가능하다.

### Hold / 보류
Partial mapping exists but is too incomplete to support localized modeling; retain KPX data for system-level/time-series research without geographic attribution.  
부분 mapping은 가능하지만 지역 모델에 부족하면 지리 귀속 없이 system-level/time-series 연구에만 유지한다.

## 6. If KR-GRID-F01 Passes / 통과 시

Proceed to `KR-GRID-E01`: / 다음 `KR-GRID-E01`로 진행:

```text
KPX bus-state 5min
+ demand forecast
+ renewable metering
+ KMA weather
+ KEPCO industry/regional load
→ stress/anomaly target
→ leakage-safe time split
→ simple baseline
→ controlled experiment
```

## 7. If KR-GRID-F01 Fails / 실패 시

Do not force geographic interpretation. Promote the next candidate by feasibility:
1. `C-EU-002` if cross-domain public-data innovation is prioritized; or
2. `C-US-004` if benchmark-grade model validation is prioritized.

지리 해석을 강제하지 않는다. 이후 우선순위는 교차도메인 혁신이면 `C-EU-002`, benchmark-grade 모델 검증이면 `C-US-004`로 이동한다.

## 8. Strategic Finding / 전략적 발견

**한국어**  
Wave 1은 국가별로 같은 데이터가 있어야 한다는 접근보다, 각 지역의 **비교우위 데이터 구조**를 활용한 뒤 공통 연구 schema로 결과를 연결하는 접근이 더 강하다는 점을 보여준다. 한국은 고빈도 계통/운영 데이터, 미국은 기관간 다양성과 benchmark 연구데이터, EU는 표준화·시설공간·국가간 조화성이 강하다.

**English**  
Wave 1 indicates that the engine should not require identical datasets in every jurisdiction. A stronger strategy is to exploit each region's **comparative data advantage** and connect results through a common research schema: Korea excels in high-frequency grid/operational data, the U.S. in cross-agency diversity and benchmark research data, and the EU in standardization, facility geospatial data, and cross-national harmonization.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
