# KR-GRID-F01 — KPX Bus-Identifier Mapping Feasibility / KPX 모선 식별자 매핑 가능성 검증

**Issue / 이슈:** #5  
**State / 상태:** `HOLD_PENDING_IDENTIFIER_VALIDATION`  
**Date / 기준일:** 2026-08-21

## 1. Objective / 목적

**한국어**  
`C-KR-001`을 지역·설비 수준 Grid Bottleneck Intelligence로 승격하기 전에, 공개된 KPX `bus_number`가 현행 권위 있는 공개자료만으로 안정적인 설비·전압레벨 또는 방어 가능한 지리 의미와 연결되는지 검증한다. 본 연구는 중요 인프라의 정확한 위치나 토폴로지를 재구성·공개하는 것을 목표로 하지 않는다.

**English**  
Before promoting `C-KR-001` into localized or asset-level Grid Bottleneck Intelligence, determine whether public KPX `bus_number` identifiers can be associated with stable asset, voltage-level, or defensible geographic semantics using current authoritative public sources. This research does not attempt to reconstruct or expose precise critical-infrastructure locations or topology.

## 2. Current Observations / 현재 관측

### `OBSERVED` — current public-data metadata / 현행 공공데이터 메타데이터
The Public Data Portal describes the bus-state dataset as monthly 5-minute values containing time, bus number, state-estimated kV, and state-estimated MW-related flow values. It does not document a public current bus-number-to-substation/geography dictionary in the dataset metadata reviewed.  
공공데이터포털은 해당 자료를 시간, 모선번호, 상태추정 kV, 상태추정 MW 관련 조류값을 포함하는 월별 5분 자료로 설명한다. 이번에 검토한 현행 dataset metadata에는 모선번호를 변전소·지리와 연결하는 공개 사전이 설명되어 있지 않다.

### `OBSERVED` — historical technical documentation / 과거 기술문서
Historical KPX technical documents demonstrate that power-system modeling contexts have used relationships among bus number, bus name, and base voltage.  
과거 KPX 기술문서에서는 계통모델링 문맥에서 모선번호·모선명·Base kV 관계를 사용한 사례가 확인된다.

### `DERIVED` — validity limitation / 유효성 한계
Historical examples do **not** establish that the same numbering convention is current, complete, stable across releases, or appropriate as a mapping dictionary for the present public 5-minute state-estimation dataset.  
과거 사례만으로 현재 5분 상태추정 데이터의 번호체계가 동일·완전·안정적이거나 현행 mapping dictionary로 사용 가능하다고 볼 수 없다.

## 3. Gate Assessment / 게이트 평가

| Requirement / 요구사항 | Current finding / 현재 결과 | State |
|---|---|---|
| current dataset fields documented / 현행 필드 확인 | time, bus number, estimated kV/MW documented / 시간·모선번호·kV·MW 확인 | `PASS` |
| current authoritative public bus dictionary / 현행 공식 공개 모선사전 | not identified in reviewed metadata/search / 확인되지 않음 | `HOLD` |
| identifier stability across monthly raw releases / 월별 raw release ID 안정성 | not yet file-level validated / 파일 수준 미검증 | `HOLD` |
| voltage semantics / 전압 의미 | state-estimated kV is directly present, but bus-base-voltage classification mapping is not established / 상태추정 kV는 직접 존재하나 모선 base-voltage 분류 mapping은 미확립 | `PARTIAL` |
| safe geographic/asset attribution / 안전한 지리·설비 귀속 | no defensible current public path established / 방어 가능한 현행 공개 경로 미확립 | `HOLD` |

## 4. Decision / 판단

### `HOLD_PENDING_IDENTIFIER_VALIDATION`

**한국어**  
현재 근거로는 `bus_number`를 현행 지리·설비 ID로 해석해 지역별 병목을 주장할 수 없다. 따라서 `C-KR-001`의 **지역/설비 귀속 모델 승격은 HOLD**한다. 다만 모선별 5분 상태추정 자체는 공식 공개된 고해상도 시계열이므로, 지리 귀속이 필요하지 않은 **system-level anomaly/regime research**에는 계속 활용 가능하다.

**English**  
Current evidence does not justify interpreting `bus_number` as a current geographic or asset identifier for localized bottleneck claims. Promotion of `C-KR-001` into a **localized/asset-attributed model is therefore held**. The official 5-minute bus-state time series remains potentially usable for **system-level anomaly or regime research** that does not require geographic attribution.

## 5. Safety Boundary / 안전 경계

- Do not infer or publish precise infrastructure locations from indirect identifiers. / 간접 식별자에서 중요 인프라의 정확한 위치를 추정·공개하지 않는다.
- Do not reconstruct operational network topology from public fragments. / 공개 파편자료로 운영계통 topology를 재구성하지 않는다.
- Only use explicit current public mapping if later published by an authoritative source and necessary for benign aggregate research. / 향후 권위기관이 현행 공개 mapping을 명시적으로 제공하고 선의의 집계 연구에 필요한 경우에만 사용한다.

## 6. Next Action / 다음 행동

1. Keep Issue #5 open while checking whether a current official identifier schema/dictionary is explicitly published. / 현행 공식 식별자 schema/dictionary가 명시 공개되는지 확인하는 동안 Issue #5 유지.
2. Do not block the engine: open a parallel next feasibility candidate that does not depend on sensitive/opaque infrastructure mapping. / 엔진 전체를 정지시키지 않고 민감·불투명 인프라 mapping에 의존하지 않는 다음 feasibility 후보를 병렬 승격.
3. Preferred fallback: `C-EU-002` Industrial Energy–Emission Efficiency or `C-US-004` registered manufacturing quality. / 우선 fallback은 `C-EU-002` 또는 `C-US-004`.

## 7. Sources / 출처

- Public Data Portal — KPX bus-level 5-minute state-estimation metadata: https://www.data.go.kr/data/15051423/fileData.do
- KPX official archive for monthly bus-state releases: https://kpx.or.kr/board.es?bid=0067&mid=a10109020500
- Historical KPX technical documentation was used only to establish that bus-number/name/base-voltage relations existed in past modeling contexts; it is **not** treated as a current mapping dictionary. / 과거 KPX 기술문서는 과거 모델링 맥락의 번호·명칭·전압 관계 존재만 확인하는 데 사용했으며 현행 사전으로 취급하지 않는다.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
