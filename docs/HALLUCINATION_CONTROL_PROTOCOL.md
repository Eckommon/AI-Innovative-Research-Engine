# Hallucination & Context-Drift Control / 환각·컨텍스트 드리프트 방지 규약

**Policy family / 규약군:** `READ-001`, `STATE-001`, `CHECKPOINT-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `MEMORY-001`, `WRITEBACK-001`, `VERIFY-001`, `COST-001`  
**Status / 상태:** `MANDATORY`  
**Effective / 시행일:** 2026-08-22

## 1. Purpose / 목적

**한국어**  
GPT가 과거 대화 기억, 오래된 상태, 모델 일반지식 또는 그럴듯한 추정을 프로젝트 사실처럼 사용하는 것을 방지한다. 프로젝트의 '메모리'는 모델 내부 기억이 아니라 **검증 가능한 GitHub 지속 컨텍스트 + 현재 live repository state + 재현 가능한 검증기록**으로 관리한다.

**English**  
Prevent GPT from treating remembered conversation context, stale state, general model knowledge, or plausible inference as project fact. Project 'memory' is maintained through **verifiable durable GitHub context + current live repository state + reproducible verification records**, not by reliance on opaque model memory.

## 2. `READ-001` — Read Before Reasoning / 추론 전 선읽기

Material project work MUST begin by reading the minimum durable context. / 실질 프로젝트 작업은 아래 최소 지속 컨텍스트를 먼저 읽은 뒤 시작한다.

### Mandatory minimum read set / 의무 최소 읽기
1. current repository/open-Issue state / 현재 저장소·open Issue 상태
2. `README.md`
3. `STATUS.md`
4. `context/PROJECT_MEMORY.md`
5. `context/SESSION_HANDOFF.md`
6. relevant `knowledge/MOC_*.md` / 관련 MOC
7. relevant `research/` object / 관련 연구 객체
8. relevant active/most-recent GitHub Issue / 활성·최근 Issue
9. `registry/CLAIM_LEDGER.md` and `registry/DECISION_LOG.md` when claims/decisions are material / 중요 주장·결정 시 ledger/log
10. relevant policy/schema if the work changes governance, scoring, evidence, metadata, or cost / 관련 규약·스키마·비용정책

If any mandatory artifact does not yet exist, note the absence rather than inventing its content. / 필수 문서가 없으면 내용을 추정하지 않고 부재를 명시한다.

## 3. `STATE-001` — Live State Reconciliation Gate / live 상태 정합 게이트

**KO:** 선읽기는 파일을 단순 열람하는 것으로 끝나지 않는다. 실질 추론·실험·새 Issue 착수 전에 **현재 GitHub live state와 요약문서가 서로 일치하는지 확인**해야 한다.  
**EN:** Read-before-reasoning is not satisfied by merely opening files. Before material reasoning, experimentation, or opening a new Issue, the **live GitHub state must be reconciled with summary artifacts**.

Mandatory comparison / 필수 대조:
- currently open GitHub Issue(s) / 현재 open Issue;
- most recent relevant closed Issue/result / 최신 관련 closed Issue·result;
- `STATUS.md` active/last-completed state;
- `context/SESSION_HANDOFF.md` checkpoint and active state;
- latest relevant `research/` state;
- latest `registry/DECISION_LOG.md` direction-changing decision.

If they disagree: / 불일치 시
1. declare `STATE_DRIFT_DETECTED` / 상태 drift 명시;
2. apply `CONFLICT-001` precedence / 충돌 우선순위 적용;
3. identify which artifact is stale / stale 문서 식별;
4. correct durable state before progressing with the next research action when write access exists / write 권한이 있으면 다음 연구 진행 전 지속상태 교정;
5. if correction cannot be written, keep the work `HOLD_STATE_RECONCILIATION` rather than pretending the state is synchronized / 기록 불가 시 동기화된 것으로 가정하지 않고 HOLD.

A stale summary is never allowed to supersede a newer completed Issue/result merely because it appears in `STATUS.md`. / STATUS에 있다는 이유만으로 stale 요약이 더 최신 Issue/result를 덮을 수 없다.

## 4. `CHECKPOINT-001` — Synchronized Operational Checkpoint / 동기 운영 checkpoint

`STATUS.md` and `context/SESSION_HANDOFF.md` MUST carry the same machine-readable operational checkpoint fields: / 두 문서는 동일 checkpoint 필드를 가져야 한다.

- `checkpoint_id`
- `active_issue`
- `active_research`
- `last_completed_issue`
- `last_completed_research`
- `last_decision`
- `updated`

Rules / 규칙:
- change the checkpoint whenever a material Issue is opened, closed, superseded, held, or promoted / 중요 Issue 상태변화마다 checkpoint 갱신;
- update both files in the same writeback cycle / 두 파일 같은 writeback cycle에서 갱신;
- never silently reuse an old checkpoint after a newer Issue/result exists / 최신 결과 후 과거 checkpoint 재사용 금지;
- checkpoint equality proves only **state synchronization**, not scientific truth / checkpoint 일치는 상태정합만 증명하며 연구결론 진실성을 증명하지 않음.

## 5. `FACT-001` — Evidence-Bound Claims / 증거 결속 주장

A material `OBSERVED` claim requires at least one of: / 중요한 `OBSERVED` 주장은 다음 중 하나 이상을 요구한다.
- authoritative/primary source / 권위·1차 출처;
- repository-recorded source with current provenance / 출처가 기록된 저장소 근거;
- reproducible computation from preserved inputs / 보존 입력에서 재현 가능한 계산.

A statement supported only by reasoning becomes `DERIVED`; a testable but unverified proposition becomes `HYPOTHESIZED`. / 추론만으로 지지되는 진술은 `DERIVED`, 검증 전 명제는 `HYPOTHESIZED`로 분류한다.

## 6. `UNKNOWN-001` — Unknown Stays Unknown / 미확인은 미확인으로 유지

Missing information is never silently filled. / 빈 정보를 조용히 메우지 않는다.

Use explicit states when appropriate: / 필요 시 명시 상태 사용:
- `UNKNOWN`
- `NOT_VERIFIED`
- `DATA_GAP`
- `HOLD`
- `INCONCLUSIVE`
- `HOLD_STATE_RECONCILIATION`
- `HOLD_COST_APPROVAL`

Do not infer a geographic identifier, classification mapping, license permission, causal mechanism, measurement meaning, current Issue state, or billing state merely because it would make the analysis convenient. / 분석 편의를 위해 지리 ID·분류 mapping·라이선스 권한·인과기제·측정 의미·Issue 상태·비용상태를 추정하지 않는다.

## 7. `CONFLICT-001` — Conflict Resolution / 충돌 해결

When sources disagree, do not blend them silently. / 근거가 충돌하면 조용히 혼합하지 않는다.

Default precedence for project state / 프로젝트 상태의 기본 우선순위:
1. current explicit user instruction / 현재 사용자의 명시 지시;
2. current authoritative external evidence for external facts / 외부 사실에 대한 최신 권위근거;
3. current live GitHub Issue/PR/repository state for operational state / 운영상태에 대한 현재 live GitHub 상태;
4. latest committed explicit project decision / 최신 commit된 명시 결정;
5. latest committed research artifact / 최신 연구객체;
6. synchronized `STATUS`/`SESSION_HANDOFF` checkpoint / 동기 checkpoint;
7. older repository context / 과거 저장소 컨텍스트;
8. chat/model memory / 채팅·모델 기억.

A conflict that affects conclusions or work order must be recorded and reconciled. / 결론·작업순서에 영향을 주는 충돌은 기록·조정한다.

## 8. `FRESH-001` — Freshness Gate / 최신성 게이트

Dynamic facts must be reverified when material to the answer or decision. / 동적 사실은 결론에 중요하면 재검증한다.

Examples / 예시:
- current dataset availability/API/access terms;
- current laws/regulations/standards;
- current source versions;
- current project/open-Issue/PR state;
- current billing/free-tier status when execution may consume a metered service;
- current market/technology/infrastructure claims.

Durable records should capture `verified_at` or equivalent date when freshness matters. / 최신성이 중요한 지속 기록은 `verified_at` 또는 동등 날짜를 기록한다.

## 9. `MEMORY-001` — Durable Project Memory / 지속 프로젝트 메모리

`context/PROJECT_MEMORY.md` is a compact index of **durable, decision-relevant facts only**. / `context/PROJECT_MEMORY.md`는 **지속적이며 의사결정에 중요한 사실만** 담는 압축 인덱스다.

Each memory item should state: / 각 메모리 항목 권장 필드:
- stable memory ID / 안정적 ID;
- statement in Korean and English / 한·영 진술;
- evidence/status / 증거·상태;
- source/reference / 출처·참조;
- `verified_at` / 검증일;
- supersedes/superseded-by if applicable / 변경 관계.

Maintenance / 유지:
- add only durable facts that change future interpretation or action / 후속 판단·행동에 영향을 주는 지속사실만 추가;
- compact or supersede stale memory explicitly; never silently rewrite history / stale 메모리는 명시적으로 supersede;
- `SESSION_HANDOFF` stores operational detail; `PROJECT_MEMORY` stores durable conclusions/policies / 운영세부와 지속메모리 역할 분리;
- every session start revalidates dynamic memory against live GitHub state / 동적 메모리는 세션 시작 시 live state와 재검증.

Do NOT put speculative brainstorming into durable memory. / 아이디어 브레인스토밍은 지속 메모리에 넣지 않는다.

## 10. `WRITEBACK-001` — End-of-Work Writeback / 작업 종료 기록

After material work, update as applicable **before declaring the work complete in chat**: / 실질 작업 후 채팅에서 완료 선언하기 전에 필요 항목 갱신
1. relevant research artifact / 관련 연구객체;
2. GitHub Issue / Issue;
3. `registry/CLAIM_LEDGER.md` for material claims / 중요 주장 ledger;
4. `registry/DECISION_LOG.md` for material decisions / 중요 결정 log;
5. `STATUS.md`;
6. `context/SESSION_HANDOFF.md`;
7. `context/PROJECT_MEMORY.md` only if a durable fact changed / 지속 사실 변경 시 프로젝트 메모리;
8. relevant MOC / 관련 MOC.

Chat-only conclusions remain provisional until material writeback completes. / 채팅에만 존재하는 결론은 지속 기록 전 잠정적이다.

## 11. `VERIFY-001` — Automated State Integrity / 자동 상태 무결성 검사

A zero-cost repository check, `.github/workflows/state-integrity.yml`, validates the operational checkpoint whenever relevant state files change. / 관련 상태파일 변경 시 무비용 repo check가 checkpoint 정합성을 검사한다.

Minimum checks / 최소검사:
- `STATUS.md` and `SESSION_HANDOFF.md` checkpoint fields match exactly;
- declared `active_issue` is actually open when not `none`;
- when `active_issue=none`, no open research Issue may silently remain unresolved under the one-active-queue convention;
- declared `last_completed_issue` is closed;
- declared `last_completed_research` artifact exists;
- malformed/missing checkpoint fields fail the check.

Boundary / 경계:
- this check detects **state drift**, not scientific hallucination by itself;
- a green check cannot promote `HYPOTHESIZED` to `VALIDATED`;
- evidence claims still require `FACT-001` and the Claim Ledger;
- if branch rules/status-check enforcement cannot be configured through the current authorized interface, the workflow remains detective/advisory until an administrator enables it as a required check. / 현재 권한 인터페이스에서 ruleset 설정이 불가하면 required check 강제 전까지 탐지·경고 장치로 운용.

## 12. `COST-001` — Cost Gate Coupling / 비용 게이트 연동

`docs/NO_COST_POLICY.md` is mandatory for all work. / 모든 작업에 무비용 규약 적용.

Before a potentially metered action: / 과금 가능 실행 전
1. establish that incremental monetary cost is zero; or
2. classify `HOLD_COST_APPROVAL` and obtain explicit user approval before execution.

A blocked no-cost route is never silently replaced by a paid one. / 무비용 경로 차단 시 유료경로로 묵시 전환 금지.

## 13. Claim Verification Levels / 주장 검증수준

| Level | Meaning / 의미 | Allowed use / 허용 사용 |
|---|---|---|
| `V0_UNSOURCED` | 근거 미기록 / unsourced | scratch only / 임시 메모만 |
| `V1_SOURCE_FOUND` | 출처 확인 / source identified | screening / 선별 |
| `V2_PRIMARY_VERIFIED` | 1차·공식 출처 검증 / primary verified | `OBSERVED` project claim |
| `V3_REPRODUCED` | 계산·추출 재현 / reproduced | strong `OBSERVED/DERIVED` |
| `V4_INDEPENDENTLY_VALIDATED` | 독립 데이터/실험 확인 / independent validation | candidate `VALIDATED` conclusion |

Do not confuse citation count with verification level. / 인용 수와 검증수준을 혼동하지 않는다.

## 14. Session Handoff Rule / 세션 인수인계 규칙

`context/SESSION_HANDOFF.md` is overwritten/updated as the **latest operational checkpoint**, not an accumulating diary. / `SESSION_HANDOFF.md`는 누적 일기가 아니라 최신 운영 checkpoint로 갱신한다.

It must include: / 필수 포함
- synchronized checkpoint fields / 동기 checkpoint;
- current state / 현재 상태;
- last completed work / 최근 완료;
- active issue/research ID / 활성 Issue·연구 ID;
- known HOLD/UNKNOWN/data gaps / 보류·미확인·공백;
- exact next actions / 정확한 다음 행동;
- required read set for next session / 다음 세션 필수 읽기.

## 15. Safety-Critical Interpretation / 안전 중요 해석

For critical infrastructure, health, legal, financial or other high-impact interpretations, use the most conservative defensible semantic level. / 중요 인프라·의료·법률·금융 등 고영향 해석은 방어 가능한 가장 보수적인 의미수준을 사용한다.

For this project specifically, do not reconstruct precise critical-infrastructure locations/topology from indirect identifiers. / 본 프로젝트에서는 간접 식별자로 중요 인프라의 정확한 위치·토폴로지를 재구성하지 않는다.

## 16. Relationship to ChatGPT Memory / ChatGPT 메모리와의 관계

ChatGPT product memory, when available, may improve convenience but **must never be the sole authority for project facts**. / ChatGPT 제품 메모리는 편의에 도움될 수 있으나 프로젝트 사실의 단독 권위가 될 수 없다.

If remembered context and GitHub disagree, apply `STATE-001` and `CONFLICT-001`; GitHub durable evidence/live state controls the project record. / 기억과 GitHub가 다르면 상태 정합·충돌 규칙을 적용한다.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
