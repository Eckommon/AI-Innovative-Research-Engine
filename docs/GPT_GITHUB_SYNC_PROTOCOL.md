# GPT ↔ GitHub Sync Protocol / GPT ↔ GitHub 동기화 규약

## Purpose / 목적

GitHub는 공식 지속 Source of Truth이고 GPT 세션은 분석·조사·가설·검증 작업공간이다. Obsidian은 동일 Markdown에 대한 탐색 레이어이며 별도 권위 저장소가 아니다. **현재 live GitHub 상태를 먼저 확인한 뒤 지속문서를 읽고, 작업 종료 전에 다시 GitHub에 기록한다.**  
GitHub is the official persistent Source of Truth; GPT sessions are analytical workspaces. Obsidian is a navigation layer over the same Markdown, not a separate authority. **Read live GitHub state first, then durable context, and write material results back before declaring work complete.**

## A. Mandatory Session Start — `READ-001` + `STATE-001` / 의무 세션 시작

실질 프로젝트 작업 전 아래 순서를 수행한다. 채팅·모델 기억만으로 작업을 시작하지 않는다. / Before material work, perform the sequence below; never begin from chat/model memory alone.

### A0. Live State Read / live 상태 선확인
1. current open GitHub Issue(s) / 현재 open Issue;
2. latest relevant closed Issue/result / 최신 관련 closed Issue·result;
3. current default-branch/head state when materially relevant / 필요 시 main/head 최신상태.

### A1. Durable Read Set / 지속 컨텍스트 읽기
1. `README.md`
2. `STATUS.md`
3. `context/PROJECT_MEMORY.md`
4. `context/SESSION_HANDOFF.md`
5. relevant `knowledge/MOC_*.md` / 관련 MOC
6. relevant `research/` object / 관련 연구 객체
7. relevant active/recent GitHub Issue / 활성·최근 Issue
8. `registry/CLAIM_LEDGER.md` and `registry/DECISION_LOG.md` when claims/decisions are material / 중요 주장·결정 시 ledger/log
9. relevant governance/schema/cost files when changing rules, evidence, metadata, or execution / 관련 규약·스키마·비용문서.

### A2. State Reconciliation / 상태 정합
Compare live Issue state with `STATUS.md`, `SESSION_HANDOFF.md`, latest research artifact and Decision Log. / live 상태와 지속문서 대조.

- exact match → proceed / 일치 시 진행;
- mismatch → `STATE_DRIFT_DETECTED`, identify stale artifact, reconcile before research progression / 불일치 시 먼저 교정;
- no write access → `HOLD_STATE_RECONCILIATION` rather than assuming synchronization / 기록불가 시 HOLD.

If a mandatory artifact is missing, record the absence rather than infer its content. / 필수 문서 부재 시 내용을 추정하지 않고 부재를 기록한다.

## B. Evidence Discipline / 증거 규율

Material claims use: `OBSERVED`, `DERIVED`, `HYPOTHESIZED`, `VALIDATED`, `REJECTED`, `INCONCLUSIVE`. / 중요 주장 증거등급 구분.

Apply `docs/HALLUCINATION_CONTROL_PROTOCOL.md`: / 환각 방지 규약 적용
- `STATE-001` live state reconciliation / live 상태정합;
- `CHECKPOINT-001` synchronized operational checkpoint / 동기 checkpoint;
- `FACT-001` evidence-bound claims / 증거 결속;
- `UNKNOWN-001` unknown stays unknown / 미확인은 미확인;
- `CONFLICT-001` explicit conflict resolution / 충돌 명시 해결;
- `FRESH-001` dynamic facts reverified / 동적 사실 재검증;
- `MEMORY-001` durable GitHub memory / 지속 GitHub 메모리;
- `WRITEBACK-001` end-of-work writeback / 작업종료 기록;
- `VERIFY-001` automated state-integrity check / 자동 상태검사;
- `COST-001` zero-cost execution boundary / 무비용 실행경계.

A hypothesis is never presented as validated merely because it is plausible. / 그럴듯함만으로 가설을 검증결과처럼 표현하지 않는다.

## C. Cost Gate / 비용 게이트

Before any execution that may consume a paid or metered service: / 과금 가능 실행 전
1. verify incremental monetary cost is zero under current terms and repository/account state; or
2. classify `HOLD_COST_APPROVAL` and obtain explicit user approval **before execution**.

Unknown billing state is not permission. / 비용상태 미확인은 실행 허가가 아니다.

No blocked no-cost route may be silently replaced with a paid route. / 무비용 경로가 막혀도 유료경로로 묵시 전환 금지.

Canonical policy: `docs/NO_COST_POLICY.md`.

## D. Language Gate / 언어 게이트

All official human-readable artifacts comply with `LANG-001`. / 모든 공식 사람이 읽는 산출물은 `LANG-001` 준수.

- Korean-English semantic parity / 한·영 의미 동등성;
- preserve native fields/code/API/standards/proper names / 원천 필드·코드·API·표준·고유명 보존;
- material caveats and uncertainty appear in both languages / 중요 제약·불확실성 양언어 반영.

## E. Before Write / 기록 전

1. fetch current file/Issue immediately before mutation / mutation 직전 현재 파일·Issue 조회;
2. preserve valid existing content and history / 유효 기존내용·역사 보존;
3. incorporate evidence, uncertainty, cost state and decision state / 증거·불확실성·비용·판단상태 반영;
4. check Claim Ledger/Decision Log to avoid contradiction / ledger/log 모순 확인;
5. apply `LANG-001` / 병기 적용;
6. use descriptive commit message / 설명 가능한 commit;
7. avoid duplicate truth stores / 중복 Source of Truth 금지.

## F. End-of-Work Writeback / 작업 종료 기록

Significant progress updates, as applicable, occur **before the chat says the work is complete**: / 완료 선언 전 기록

1. relevant `research/` artifact;
2. active/recent GitHub Issue;
3. `registry/CLAIM_LEDGER.md` for material claims;
4. `registry/DECISION_LOG.md` for material decisions;
5. `STATUS.md`;
6. `context/SESSION_HANDOFF.md`;
7. `context/PROJECT_MEMORY.md` **only for durable decision-relevant facts** / 지속사실 변경 시에만;
8. relevant MOC / 관련 MOC.

`STATUS.md` and `SESSION_HANDOFF.md` must receive the same `CHECKPOINT-001` fields in the same writeback cycle. / 두 파일 checkpoint 동시 갱신.

Chat-only conclusions remain provisional until recorded. / 채팅에만 있는 결론은 기록 전 잠정적이다.

## G. Repository / Obsidian Taxonomy / 저장소·Obsidian 구조

```text
README.md
STATUS.md
.gitignore

.github/workflows/
  state-integrity.yml

docs/
  GOVERNANCE.md
  LANGUAGE_POLICY.md
  METHODOLOGY.md
  GPT_GITHUB_SYNC_PROTOCOL.md
  HALLUCINATION_CONTROL_PROTOCOL.md
  NO_COST_POLICY.md
  OBSIDIAN_KNOWLEDGE_MANAGEMENT.md
  METADATA_SCHEMA.md

context/
  PROJECT_MEMORY.md
  SESSION_HANDOFF.md

knowledge/
  00_HOME.md
  MOC_RESEARCH.md
  MOC_DATASETS.md
  MOC_EXPERIMENTS.md
  MOC_DECISIONS.md
  TAG_TAXONOMY.md

registry/
  GLOBAL_PUBLIC_DATA_SOURCE_REGISTRY.md
  INNOVATION_POTENTIAL_SCORE.md
  RESEARCH_MATERIAL_LANDSCAPE.md
  CLAIM_LEDGER.md
  DECISION_LOG.md

research/
  <research-id>/...

templates/
  OBSIDIAN_NOTE_TEMPLATE.md
```

Open the repository root as the Obsidian Vault. Standard Markdown links are canonical for GitHub compatibility. / 저장소 루트를 Vault로 열며 표준 Markdown 링크를 canonical로 사용한다.

## H. Drift Reconciliation / 드리프트 조정

If `STATUS.md`, Issue state, research artifact, memory, or chat disagree: / 상태 불일치 시
1. inspect current live GitHub Issue/PR/repository state / live 상태 확인;
2. inspect latest committed decision and research artifact / 최신 결정·연구객체 확인;
3. identify the divergence explicitly / 차이 명시;
4. apply `CONFLICT-001` precedence / 우선순위 적용;
5. reconcile `STATUS.md` and `SESSION_HANDOFF.md` before continuing research / 연구진행 전 두 상태문서 교정;
6. update checkpoint fields and allow `state-integrity` to verify them / checkpoint 갱신·검사.

Do not silently average or merge contradictory states. / 충돌상태를 조용히 평균·혼합하지 않는다.

## I. Work Queue / 작업 큐

Proceed by dependency and information gain, normally following official Issue order. If a HOLD/FAIL makes the current path invalid, record the gate result and promote the next defensible candidate rather than forcing continuation. / 선행조건·정보이득 기준으로 진행하며 HOLD/FAIL 시 강제 진행 금지.

One-active-research-queue convention / 단일 활성 연구큐 원칙:
- normally maintain one active research Issue at a time;
- governance/admin PRs may coexist but may not silently redefine research state;
- opening/closing the active Issue requires a synchronized checkpoint update.

## J. Human/GPT Roles / 사용자·GPT 역할

Within authorization and `COST-001`, GPT may autonomously research, compare, score, generate hypotheses, critique, run feasibility analysis, design/execute permitted experiments, and update the repository. Records must let another GPT session or human reconstruct why a decision was made. / 권한·무비용 경계 내에서 자율 작업 가능하되 판단근거를 재구성 가능하게 기록한다.

Actions with possible monetary cost require prior explicit user approval even if technically executable. / 기술적으로 실행 가능해도 비용 가능 작업은 사전승인 필수.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `STATE-001`, `FACT-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
