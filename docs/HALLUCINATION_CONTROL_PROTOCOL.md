# Hallucination & Context-Drift Control / 환각·컨텍스트 드리프트 방지 규약

**Policy family / 규약군:** `READ-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `MEMORY-001`, `WRITEBACK-001`  
**Status / 상태:** `MANDATORY`  
**Effective / 시행일:** 2026-08-22

## 1. Purpose / 목적

**한국어**  
GPT가 과거 대화 기억, 오래된 상태, 모델 일반지식 또는 그럴듯한 추정을 프로젝트 사실처럼 사용하는 것을 방지한다. 프로젝트의 '메모리'는 모델 내부 기억이 아니라 **검증 가능한 GitHub 지속 컨텍스트**로 관리한다.

**English**  
Prevent GPT from treating remembered conversation context, stale state, general model knowledge, or plausible inference as project fact. Project 'memory' is maintained as **verifiable durable GitHub context**, not as reliance on opaque model memory.

## 2. `READ-001` — Read Before Reasoning / 추론 전 선읽기

Material project work MUST begin by reading the minimum durable context. / 실질 프로젝트 작업은 아래 최소 지속 컨텍스트를 먼저 읽은 뒤 시작한다.

### Mandatory minimum read set / 의무 최소 읽기
1. `README.md`
2. `STATUS.md`
3. `context/PROJECT_MEMORY.md`
4. `context/SESSION_HANDOFF.md`
5. relevant `knowledge/MOC_*.md` / 관련 MOC
6. relevant `research/` object / 관련 연구 객체
7. relevant open/most-recent GitHub Issue / 관련 활성·최근 Issue
8. relevant policy/schema if the work changes governance, scoring, evidence, or metadata / 규약·점수·증거·스키마 변경 시 관련 문서

If any mandatory file does not yet exist, note the absence rather than inventing its content. / 필수 파일이 없으면 내용을 추정하지 않고 부재를 명시한다.

## 3. `FACT-001` — Evidence-Bound Claims / 증거 결속 주장

A material `OBSERVED` claim requires at least one of: / 중요한 `OBSERVED` 주장은 다음 중 하나 이상을 요구한다.
- authoritative/primary source / 권위·1차 출처;
- repository-recorded source with current provenance / 출처가 기록된 저장소 근거;
- reproducible computation from preserved inputs / 보존 입력에서 재현 가능한 계산.

A statement supported only by reasoning becomes `DERIVED`; a testable but unverified proposition becomes `HYPOTHESIZED`. / 추론만으로 지지되는 진술은 `DERIVED`, 검증 전 명제는 `HYPOTHESIZED`로 분류한다.

## 4. `UNKNOWN-001` — Unknown Stays Unknown / 미확인은 미확인으로 유지

Missing information is never silently filled. / 빈 정보를 조용히 메우지 않는다.

Use explicit states when appropriate: / 필요 시 명시 상태 사용:
- `UNKNOWN`
- `NOT_VERIFIED`
- `DATA_GAP`
- `HOLD`
- `INCONCLUSIVE`

Do not infer a geographic identifier, classification mapping, license permission, causal mechanism, or measurement meaning merely because it would make the analysis convenient. / 분석 편의를 위해 지리 ID·분류 mapping·라이선스 권한·인과기제·측정 의미를 추정하지 않는다.

## 5. `CONFLICT-001` — Conflict Resolution / 충돌 해결

When sources disagree, do not blend them silently. / 근거가 충돌하면 조용히 혼합하지 않는다.

Default precedence for project state / 프로젝트 상태의 기본 우선순위:
1. current explicit user instruction / 현재 사용자의 명시 지시;
2. current authoritative external evidence for external facts / 외부 사실에 대한 최신 권위근거;
3. latest committed explicit project decision / 최신 commit된 명시 결정;
4. latest research artifact/Issue evidence / 최신 연구객체·Issue 근거;
5. older repository context / 과거 저장소 컨텍스트;
6. chat/model memory / 채팅·모델 기억.

A conflict that affects conclusions must be recorded and reconciled. / 결론에 영향을 주는 충돌은 기록·조정해야 한다.

## 6. `FRESH-001` — Freshness Gate / 최신성 게이트

Dynamic facts must be reverified when material to the answer or decision. / 동적 사실은 결론에 중요하면 재검증한다.

Examples / 예시:
- current dataset availability/API/access terms;
- current laws/regulations/standards;
- current source versions;
- current project/open-Issue state;
- current market/technology/infrastructure claims.

Durable records should capture `verified_at` or equivalent date when freshness matters. / 최신성이 중요한 지속 기록은 `verified_at` 또는 동등 날짜를 기록한다.

## 7. `MEMORY-001` — Durable Project Memory / 지속 프로젝트 메모리

`context/PROJECT_MEMORY.md` is a compact index of **durable, decision-relevant facts only**. / `context/PROJECT_MEMORY.md`는 **지속적이며 의사결정에 중요한 사실만** 담는 압축 인덱스다.

Each memory item should state: / 각 메모리 항목 권장 필드:
- stable memory ID / 안정적 ID;
- statement in Korean and English / 한·영 진술;
- evidence/status / 증거·상태;
- source/reference / 출처·참조;
- `verified_at` / 검증일;
- supersedes/superseded-by if applicable / 변경 관계.

Do NOT put speculative brainstorming into durable memory. / 아이디어 브레인스토밍은 지속 메모리에 넣지 않는다.

## 8. `WRITEBACK-001` — End-of-Work Writeback / 작업 종료 기록

After material work, update as applicable: / 실질 작업 후 필요 시 갱신:
1. relevant research artifact / 관련 연구객체;
2. GitHub Issue / Issue;
3. `STATUS.md`;
4. `context/SESSION_HANDOFF.md`;
5. `context/PROJECT_MEMORY.md` only if a durable fact changed / 지속 사실이 바뀐 경우에만 프로젝트 메모리;
6. `registry/CLAIM_LEDGER.md` for material claims / 중요 주장 ledger;
7. `registry/DECISION_LOG.md` for material decisions / 중요 결정 log;
8. relevant MOC / 관련 MOC.

## 9. Claim Verification Levels / 주장 검증수준

| Level | Meaning / 의미 | Allowed use / 허용 사용 |
|---|---|---|
| `V0_UNSOURCED` | 근거 미기록 / unsourced | scratch only / 임시 메모만 |
| `V1_SOURCE_FOUND` | 출처 확인 / source identified | screening / 선별 |
| `V2_PRIMARY_VERIFIED` | 1차·공식 출처 검증 / primary verified | `OBSERVED` project claim |
| `V3_REPRODUCED` | 계산·추출 재현 / reproduced | strong `OBSERVED/DERIVED` |
| `V4_INDEPENDENTLY_VALIDATED` | 독립 데이터/실험 확인 / independent validation | candidate `VALIDATED` conclusion |

Do not confuse citation count with verification level. / 인용 수와 검증수준을 혼동하지 않는다.

## 10. Session Handoff Rule / 세션 인수인계 규칙

`context/SESSION_HANDOFF.md` is overwritten/updated as the **latest operational checkpoint**, not an accumulating diary. / `SESSION_HANDOFF.md`는 누적 일기가 아니라 **최신 운영 checkpoint**로 갱신한다.

It must include: / 필수 포함:
- current state / 현재 상태;
- last completed work / 최근 완료;
- active issue/research ID / 활성 Issue·연구 ID;
- known HOLD/UNKNOWN/data gaps / 보류·미확인·공백;
- exact next actions / 정확한 다음 행동;
- required read set for next session / 다음 세션 필수 읽기.

## 11. Safety-Critical Interpretation / 안전 중요 해석

For critical infrastructure, health, legal, financial or other high-impact interpretations, use the most conservative defensible semantic level. / 중요 인프라·의료·법률·금융 등 고영향 해석은 방어 가능한 가장 보수적인 의미수준을 사용한다.

For this project specifically, do not reconstruct precise critical-infrastructure locations/topology from indirect identifiers. / 본 프로젝트에서는 간접 식별자로 중요 인프라의 정확한 위치·토폴로지를 재구성하지 않는다.

## 12. Relationship to ChatGPT Memory / ChatGPT 메모리와의 관계

ChatGPT product memory, when available, may improve convenience but **must never be the sole authority for project facts**. / ChatGPT 제품 메모리는 편의에 도움될 수 있으나 **프로젝트 사실의 단독 권위가 될 수 없다**.

If remembered context and GitHub disagree, apply `CONFLICT-001`. / 기억과 GitHub가 다르면 `CONFLICT-001`을 적용한다.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
