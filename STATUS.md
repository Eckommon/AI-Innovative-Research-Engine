---
checkpoint_id: CHK-20260907-US-AIR-F01-AUDITED
active_issue: 88
active_research: US-AIR-F01
last_completed_issue: 87
last_completed_research: PORTFOLIO-R08
last_decision: DEC-121
updated: 2026-09-07
---

# Project Status / 프로젝트 상태

**State / 상태:** `CONTINUE_US_AIR_F01_2025_DATE_SUPPORT_VERIFICATION`

## Mission / 목적
Public/research data relationships → falsifiable, reproducible, practically useful innovation and bottleneck evidence. / 공공·연구 데이터 관계에서 반증 가능하고 재현 가능하며 실용적인 혁신·병목 증거를 발견한다. MEM-054 remains mandatory / 의무 유지.

## Verified checkpoint / 검증 상태
Issue #87 PORTFOLIO-R08 is closed; Issue #88 US-AIR-F01 is the sole open research issue. / #87 완료, #88 단일 활성 연구.
Source run: 7,736,770 flight identity rows; 349 AirportIDs present in all 12 months. / 연중 349개 공항.
Mapping run 33959662982 succeeded: January exact SeqID 352/352; mapped airports/stations 340/340; reachable 2025 files 322; intersection lower bounds 337 spatial and 319 file-supported. / 1월 exact 매핑 352, 공간 340, 파일 322; 연중 집합 하한 각각 337·319.
These are January-map bounds, not proof of full-year time-valid mapping or weather completeness. / 1월 지도 기반 하한이며 연중 유효 매핑·기상 완전성 증명이 아니다.
Evidence: research/US-AIR-F01/MASTER_COORDINATE_MAPPING_PREFLIGHT.md; registry/CLM-134.md.

## Improvement applied / 적용 개선
DEC-121 and docs/RESEARCH_OPERATING_MODEL.md define evidence-to-utility progression, reusable execution and atomic checkpoint discipline. / 증거→실용성 단계, 재사용 실행, 원자적 checkpoint 동기화를 적용한다.
The stale #74 handoff is superseded by this checkpoint. / 과거 #74 인수인계를 본 checkpoint로 대체한다.

## Exact next action / 정확한 다음 행동
Validate all 2025 SeqIDs and deterministic station mapping, then inspect only NOAA DATE support; persist derived mapping and support manifests. / 2025 전체 SeqID·결정론적 매핑 후 NOAA DATE만 검사하고 파생 매핑·지원도 manifest를 보존한다.
Resolve CSV time semantics, local-calendar boundary interpretation, and status/duplicate eligibility before any final F01 PASS. / 최종 PASS 전 CSV 시간 의미·날짜 경계·status/duplicate 규칙을 확정한다.
No weather/delay magnitude, effect, ranking, propagation or causal analysis is authorized. / 기상·지연 크기, 효과·순위·전파·인과 분석 금지.

## Preserved boundaries / 보존 경계
2025; 10.0 km; tie tolerance 0.001 km; >=50 airports; >=40 distinct stations; station × local date; DepDelayMinutes only as future primary outcome. / 기존 기간·거리·지원도·단위·outcome 유지.
Distinct stations do not prove statistical independence. DATE presence does not prove measurement completeness. / 별도 관측소는 독립성 증명이 아니며 DATE 존재는 측정 완전성 증명이 아니다.
AU-NEM join asset remains preserved without automatic E01. / AU-NEM 조인 자산 보존, 자동 E01 금지.
Incremental cost: 0 USD; COST-001 and RAW-001 remain mandatory. / 추가비용 0원·원천자료 일시 처리 유지.
