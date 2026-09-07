# Research Operating Model / 연구 운영 모델
Date / 날짜: 2026-09-07. Decision / 결정: DEC-121.
Audit base / 감사 기준: main dafc97cb58921eb5662fec68769d03f9e9b283bf.

## Assessment / 진단
**KO:** 미션·증거등급·실험 전 규칙·중단규칙은 이미 강하다. 문제는 규칙 추가보다 실행과 기록의 연결이다. 실제 handoff는 #74, STATUS는 #88, MOC는 #8을 활성으로 표시한다. 기존 state-integrity는 두 문서를 대조하지만 last_decision 파일/로그 연결을 검사하지 않고, 활성 Issue가 하나 존재할 때 다른 open Issue를 허용한다. 반복 workflow 속 inline Python은 다음 gate가 활용할 identity map을 남기지 않아 같은 bytes를 다시 가져오게 한다.
**EN:** Mission, evidence classes, preregistration and stop rules are strong. The observed weaknesses concern execution and continuity: handoff #74, STATUS #88 and MOC #8 disagree. State integrity does not check the decision file/log linkage or enforce a sole open issue when one is declared. Inline workflow scripts omit reusable identity maps and encourage reacquisition.

**KO:** R08의 43/45는 선정 보조이며 실증적 혁신 가치가 아니다. F01은 데이터 결합 가능성을 확인할 뿐이다. CLM-129의 일본 항만 실험처럼 이미 관계 실험 증거는 있으므로 프로젝트를 “실험을 하나도 못 한 상태”로 평가해서도 안 된다. 각 성과의 신규성·외적 타당성·의사결정 효익은 별도 평가해야 한다.
**EN:** R08's 43/45 is a selection aid, not empirical innovation value. F01 qualifies a join. Prior association experiments exist (e.g. Japan ports, CLM-129), so this is not a project with no experiments. Novelty, external validity and decision utility require separate assessment.

## Minimal structure / 최소 구조
Retain existing directories and IDs. No new platform, database or global reorganization. / 기존 디렉터리·ID 유지, 새 플랫폼·DB·전면 재배치 없음.

| Layer / 계층 | Existing home / 기존 위치 | Required output / 필요한 결과 |
|---|---|---|
| Mission and portfolio / 미션·선정 | docs, registry, research/PORTFOLIO-* | Question, alternative, next uncertainty, stop boundary / 질문·대안·다음 불확실성·중단조건 |
| Source and join / source·결합 | research/<ID> + tools | Source hash, schema, deterministic mapping and exclusions / hash·schema·지도·제외사유 |
| Experiment / 실험 | research/<E-ID> | Frozen estimand, baseline, split, rejection rule, executable result / 추정대상·baseline·split·기각규칙·실행결과 |
| Innovation assessment / 혁신 평가 | same result + claim registry | Evidence, novelty, utility, scalability separately / 증거·신규성·실용성·확장성 분리 |
| Continuity / 연속성 | STATUS + SESSION_HANDOFF | One checkpoint payload, same commit, executable validation / 한 checkpoint 입력·동일 commit·자동검사 |

## Operating cycle / 진행 주기
1. Reconcile live state, source evidence and declared checkpoint before execution. / 실행 전 live·증거·checkpoint 정합.
2. State the smallest decision-relevant uncertainty and the artifact that resolves it. / 다음 의사결정 불확실성과 해결 산출물 명시.
3. Reuse an existing route before writing another workflow. Keep research-specific code in tools; workflows invoke it. / 새 workflow 전에 기존 경로 재사용, 코드는 tools에 두고 workflow에서 호출.
4. Execute within frozen boundaries and preserve machine-readable derived support alongside prose. / 동결 경계 내 실행, 서술과 파생 support 동시 보존.
5. Inspect outputs; CI success proves execution only. Decide PASS/PARTIAL/HOLD/REJECT from all acceptance conditions. / 출력 검사, CI 성공과 연구판정 분리.
6. Commit decision, result, index and synchronized checkpoint together. / 결정·결과·색인·checkpoint 동시 commit.

No new research ID for a parser retry. Existing >=2 infrastructure-descendant stop rule remains mandatory; log attempts inside the current gate. / parser 재시도에 새 연구 ID 금지, 기존 2회 인프라 descendant 중단규칙 유지·현재 gate에 시도 기록.
A fresh full portfolio scoring exercise is needed only at the existing governance triggers or material new evidence; do not restart R08 during routine F01 work. / 기존 trigger나 중요 새 증거 때 포트폴리오 비교, 일상 F01 작업에서 R08 재시작 금지.

## Mission completion ladder / 목적 달성 단계
- JOIN_READY: source and semantic join qualified; no effect claim. / 결합 자격, 효과 주장 없음.
- RELATIONSHIP_TESTED: prespecified baseline comparison with uncertainty, including null results. / 사전 baseline 대비 검증·불확실성·음성결과.
- GENERALIZATION_TESTED: untouched temporal/spatial evaluation and dependence-aware uncertainty. / 미사용 시공간 평가·종속성 반영.
- NOVELTY_ASSESSED: prior work and existing operational practice compared against the exact contribution. / 선행연구·현행 운영과 구체적 기여 비교.
- UTILITY_TESTED: named user, decision, information available at decision time, measurable benefit/cost and failure case. / 사용자·결정·결정시점 정보·측정 효익/비용·실패조건.
- INNOVATION_CANDIDATE: evidence sufficient for the intended use, with limits stated. / 용도에 맞는 증거와 한계가 있는 후보.

These are assessment fields, not replacement lifecycle states or automatic promotion rules. / 기존 lifecycle의 대체가 아닌 평가항목이다.
Report completed falsifiable tests, incremental value against baseline, generalization status, novelty/utility status and reusable evidence. Do not optimize document count, row volume, favorable p-values or branch throughput. / 반증실험·baseline 추가가치·일반화·신규성/실용성·재사용 증거로 진척 보고, 문서수·행수·유리한 p값·branch 처리량 최적화 금지.
No numerical mission KPI target is invented before a reliable historical denominator exists. / 신뢰성 있는 과거 분모 없이 KPI 목표 수치 생성 금지.

## US-AIR application / 항공 적용
**KO:** 우선 연중 SeqID와 DATE 지원을 끝낸다. 164개 AirportID의 복수 SeqID가 있으므로 1월 좌표를 연중으로 확장하지 않는다. 같은 station을 공유하는 공항은 같은 노출 cluster다. 다른 station도 같은 폭풍의 영향을 받으므로 station 개수는 독립성 증명이 아니다.
**EN:** Finish annual SeqID and DATE support first. Multiple SeqIDs occur for 164 AirportIDs; January coordinates cannot certify the year. Shared stations are one exposure cluster, and distinct stations may share storms.

**KO:** DATE가 365일 존재해도 선택할 기상 변수의 유효 관측값·품질이 365일 존재하는 것은 아니다. 일별 집계가 CSV 시각의 의미를 입증하지 않으며 LST와 DST 적용 현지 날짜의 24시간 창도 자동으로 같지 않다. 현재 contract는 그대로 보존하고 의미 차이를 별도 판정한다.
**EN:** 365 DATE labels do not prove 365 usable weather values or quality coverage. Daily aggregation does not establish CSV timestamp semantics or identical LST/civil-day windows. Preserve the existing contract and adjudicate the difference explicitly.

**KO:** 향후 질문은 운영·달력 baseline에 비해 결합 데이터가 무엇을 추가하는지여야 한다. 관측된 당일 기상으로 당일 지연을 설명하는 분석을 사전 예측이라고 부르지 않는다. 전파를 주장하려면 항공기 회전·시간적 선후·연결망과 confounding을 별도 설계해야 한다.
**EN:** A future question must identify what the joined data add beyond operational/calendar baselines. Same-day observed weather cannot be relabeled advance prediction. Propagation requires a separate design for aircraft rotations, time order, network links and confounding.

E01 remains unapproved. Before it opens: freeze one primary scientific question, aggregation/denominator/status handling, predictor/quality semantics, baseline, evaluation split, dependence-aware uncertainty, falsification and minimum useful improvement. Novelty and utility are UNKNOWN until assessed. / E01 미승인; primary 질문·집계/분모/status·변수/품질·baseline·split·종속성·반증·최소 효익을 먼저 동결. 신규성·실용성은 검토 전 UNKNOWN.

## Reuse and evidence / 재사용·증거
Persist code, hashes, derived identity maps, coverage summaries, missing dates and exclusion reasons under RAW-001. Do not persist raw CSV/ZIP files. Current source hashes are recorded against earlier hashes; revisions are disclosed, not silently treated as identical snapshots. / 코드·hash·파생 지도·지원도·결측날짜·제외사유 보존, 원천 파일 비저장, source revision 명시.
Historical workflow migration is deferred until actual reuse warrants it. / 과거 workflow 일괄 이관은 실제 재사용 필요 때 수행.

## Acceptance of this improvement / 개선 수용기준
- STATUS/HANDOFF match and identify live #88 / live #88과 checkpoint 일치.
- DEC-121 is linked from the decision log / 결정 로그 연결.
- Existing contracts unchanged / 과학 계약 보존.
- Reusable support execution emits outcome-blind manifests / 결과 비사용 재사용 실행.
- Full F01 PASS remains blocked until every scientific requirement is met / 모든 과학 요건 전 최종 PASS 금지.
