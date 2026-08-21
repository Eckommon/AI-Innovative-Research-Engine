# Claim Ledger / 주장·증거 레저

**Purpose / 목적:** 중요한 프로젝트 주장을 증거등급·검증수준·출처와 함께 추적하여, 다음 세션이 문장 자체보다 **근거 상태**를 먼저 확인하도록 한다. / Track material claims with evidence class, verification level, and source so future sessions inspect **evidence state** rather than trusting prose alone.

| Claim ID | Claim / 주장 | Evidence Class | Verification | Source / 출처 | verified_at | Status |
|---|---|---|---|---|---|---|
| `CLM-001` | NIST AM Bench is suitable as a calibration benchmark but high Dataset IPS does not imply every ML hypothesis succeeds. / NIST AM Bench는 보정 benchmark로 적합하지만 높은 Dataset IPS가 모든 ML 가설 성공을 의미하지 않는다. | `DERIVED` | `V3_REPRODUCED` | `research/AMBENCH-001/` | 2026-08-21 | active |
| `CLM-002` | Current public evidence does not establish a defensible KPX `bus_number → geography/asset` mapping for localized claims. / 현행 공개 근거로 KPX 모선번호의 안정적 지리·설비 mapping은 확립되지 않았다. | `OBSERVED/DERIVED` | `V2_PRIMARY_VERIFIED` | Issue #5; `research/KR-GRID-F01/README.md` | 2026-08-22 | active |
| `CLM-003` | EU-27 industrial GVA rose while six tracked major industrial pollutant families declined ≥20% from 2010 to 2024 under the EEA indicator relationship. / 2010–2024 EU-27 산업 GVA 증가와 동시에 추적 6개 주요 산업오염물질군이 20% 이상 감소했다. | `OBSERVED` | `V2_PRIMARY_VERIFIED` | EEA industrial pollutant releases indicator; `research/EU-IEE-E01/README.md` | 2026-08-22 | active |
| `CLM-004` | `EU-IEE-E01` passes the predefined material-decoupling gate but is not independently novel. / `EU-IEE-E01`은 사전 decoupling gate를 통과하지만 독립 신규성은 낮다. | `DERIVED/VALIDATED` | `V3_REPRODUCED` | Issue #6; `research/EU-IEE-E01/README.md` | 2026-08-22 | active |
| `CLM-005` | Sector-level E-PRTR × PRODCOM normalization is feasible for explicitly mapped activities/products; EEA has published a steel-mercury precedent. / 명시 mapping된 sector에서 E-PRTR × PRODCOM 정규화가 가능하며 EEA 철강-수은 선례가 있다. | `OBSERVED` | `V2_PRIMARY_VERIFIED` | EEA mercury-per-steel chart/report; Issue #7 | 2026-08-22 | active |
| `CLM-006` | A generic facility-level emissions-per-output metric is not justified by country/sector production denominators alone. / 국가·sector 생산분모만으로 일반 시설단위 배출효율을 정당화할 수 없다. | `DERIVED` | `V2_PRIMARY_VERIFIED` | EEA methodology notes; Issue #7 | 2026-08-22 | active |

## Rule / 규칙

- New material claims should receive a stable ID when they influence scoring, promotion, HOLD/REJECT decisions, or downstream experiments. / 점수·승격·HOLD/REJECT·후속 실험에 영향을 주는 중요 주장은 안정적 ID 부여.
- When a claim is superseded, retain the old row and mark it superseded; do not erase history. / 주장이 대체되면 삭제하지 않고 superseded 표시.
- `V0_UNSOURCED` claims cannot be used as official evidence. / `V0_UNSOURCED`는 공식 근거 사용 금지.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
