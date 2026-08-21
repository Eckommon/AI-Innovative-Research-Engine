# KR-GRID-F01 — KPX Bus-Identifier Mapping Feasibility / KPX 모선 식별자 매핑 가능성 검증

**Issue / 이슈:** #5  
**State / 상태:** `HOLD`  
**Date / 기준일:** 2026-08-22  
**Issue disposition / Issue 처리:** `COMPLETED`

## 1. Objective / 목적

**한국어**  
`C-KR-001`을 지역·설비 수준 Grid Bottleneck Intelligence로 승격하기 전에, 공개된 KPX `bus_number`가 현행 권위 있는 공개자료만으로 안정적인 설비·전압레벨 또는 방어 가능한 지리 의미와 연결되는지 검증했다. 본 연구는 중요 인프라의 정확한 위치나 토폴로지를 재구성·공개하지 않는다.

**English**  
Before promoting `C-KR-001` into localized or asset-level Grid Bottleneck Intelligence, this feasibility task tested whether public KPX `bus_number` identifiers can be associated with stable asset, voltage-level, or defensible geographic semantics using current authoritative public sources. This research does not reconstruct or expose precise critical-infrastructure locations or topology.

## 2. Observations / 관측

### `OBSERVED` — current public-data metadata / 현행 공공데이터 메타데이터
The Public Data Portal describes monthly 5-minute values containing time, bus number, state-estimated kV, and state-estimated MW-related flow values. The reviewed metadata does not document a current public bus-number-to-substation/geography dictionary.  
공공데이터포털은 시간, 모선번호, 상태추정 kV, 상태추정 MW 관련 조류값을 포함하는 월별 5분 자료로 설명하지만, 검토한 metadata에는 현행 공개 모선번호→변전소·지리 사전이 설명되어 있지 않다.

### `OBSERVED` — continued publication / 지속 공개
Official KPX listings include 2026 May and June monthly bus-state releases. / KPX 공식 게시물에서 2026년 5월·6월 월별 자료의 지속 공개를 확인했다.

### `OBSERVED` — historical technical context / 과거 기술문맥
Historical KPX technical documents show that bus number, bus name, and base-voltage relationships existed in past power-system modeling contexts. / 과거 KPX 기술문서에서는 모선번호·모선명·Base kV 관계 사용 사례가 존재한다.

### `DERIVED` — limitation / 한계
Historical examples do **not** prove that the present public 5-minute dataset uses the same numbering, that identifiers are stable across current releases, or that historical mappings are safe/current dictionaries. Continued monthly publication alone also does not prove identifier stability.  
과거 사례는 현행 5분 데이터의 동일 번호체계·월간 ID 안정성·현행 mapping dictionary를 증명하지 않으며 월별 공개 지속만으로 ID 안정성을 입증할 수도 없다.

## 3. Gate Assessment / 게이트 평가

| Requirement / 요구사항 | Finding / 결과 | State |
|---|---|---|
| current dataset fields / 현행 필드 | time, bus number, estimated kV/MW documented | `PASS` |
| current authoritative public bus dictionary / 현행 공식 공개 모선사전 | not established / 미확립 | `HOLD` |
| identifier stability across monthly raw releases / 월별 ID 안정성 | not proven / 미증명 | `HOLD` |
| voltage semantics / 전압 의미 | estimated kV present; base-voltage class mapping unestablished | `PARTIAL` |
| safe geographic/asset attribution / 안전한 지리·설비 귀속 | no defensible current public path established | `HOLD` |

## 4. Final Decision / 최종 판단

### `HOLD`

**한국어**  
`bus_number`를 현행 지리·설비 ID로 해석해 지역별 병목이나 설비별 결론을 주장할 근거가 부족하다. 따라서 `C-KR-001`의 **지역/설비 귀속 모델은 승격하지 않는다**. 다만 모선별 5분 상태추정 자체는 공식 공개된 고해상도 시계열이므로, 정확한 지리·설비를 추정하지 않는 **system-level anomaly/regime research**에는 계속 사용할 수 있다.

**English**  
Evidence is insufficient to interpret `bus_number` as a current geographic or asset identifier for localized bottleneck or asset-specific claims. `C-KR-001` is therefore **not promoted to a localized/asset-attributed model**. The official high-resolution 5-minute bus-state series remains eligible for **system-level anomaly/regime research** that does not infer precise geography or assets.

## 5. Safety Boundary / 안전 경계

- Do not infer or publish precise infrastructure locations from indirect identifiers. / 간접 식별자로 중요 인프라의 정확한 위치 추정·공개 금지.
- Do not reconstruct operational network topology from public fragments. / 공개 파편자료로 운영 topology 재구성 금지.
- Historical identifier examples are not current mapping dictionaries. / 과거 식별자 사례는 현행 mapping 사전이 아님.

## 6. Disposition / 처리

Issue #5 feasibility work is complete with a `HOLD` outcome. The fallback path was executed through `EU-IEE-E01` and subsequent EU normalization/reproduction work. / Issue #5 feasibility는 `HOLD` 결과로 완료되었으며 fallback 경로는 `EU-IEE-E01` 이후 EU 정규화·재현 연구로 진행됐다.

Reopen only if new authoritative public evidence materially changes the identifier-mapping question. / 새로운 권위 공개근거가 식별자 mapping 문제를 실질적으로 바꾸는 경우에만 재개한다.

## 7. Sources / 출처

- Public Data Portal — KPX bus-level 5-minute state-estimation metadata: https://www.data.go.kr/data/15051423/fileData.do
- KPX official monthly archive: https://kpx.or.kr/board.es?bid=0067&mid=a10109020500

Official artifacts comply with `LANG-001`, `READ-001`, and `FACT-001`. / 공식 산출물은 관련 규약을 따른다.
