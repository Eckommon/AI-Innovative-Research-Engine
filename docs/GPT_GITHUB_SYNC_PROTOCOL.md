# GPT ↔ GitHub Sync Protocol / GPT ↔ GitHub 동기화 규약

## Purpose / 목적

GitHub는 공식 지속 Source of Truth이고 GPT 세션은 분석·조사·가설·검증 작업공간이다. Obsidian은 동일 Markdown에 대한 탐색 레이어이며 별도 권위 저장소가 아니다.  
GitHub is the official persistent Source of Truth; GPT sessions are analytical workspaces. Obsidian is a navigation layer over the same Markdown, not a separate authority.

## A. Mandatory Session Start — `READ-001` / 의무 세션 시작

실질 프로젝트 작업 전 아래 순서를 먼저 읽는다. 채팅·모델 기억만으로 작업을 시작하지 않는다. / Before material work, read the following sequence first; never begin from chat/model memory alone.

1. `README.md`
2. `STATUS.md`
3. `context/PROJECT_MEMORY.md`
4. `context/SESSION_HANDOFF.md`
5. relevant `knowledge/MOC_*.md` / 관련 MOC
6. relevant `research/` object / 관련 연구 객체
7. relevant active/recent GitHub Issue / 활성·최근 Issue
8. `registry/CLAIM_LEDGER.md` and `registry/DECISION_LOG.md` when claims/decisions are material / 중요 주장·결정 시 ledger/log
9. relevant governance/schema files when changing rules or metadata / 규약·스키마 변경 시 관련 문서

If a mandatory artifact is missing, record the absence rather than infer its content. / 필수 문서 부재 시 내용을 추정하지 않고 부재를 기록한다.

## B. Evidence Discipline / 증거 규율

Material claims use: `OBSERVED`, `DERIVED`, `HYPOTHESIZED`, `VALIDATED`, `REJECTED`, `INCONCLUSIVE`.  
중요 주장은 위 증거등급으로 구분한다.

Apply `docs/HALLUCINATION_CONTROL_PROTOCOL.md`: / 환각 방지 규약 적용:
- `FACT-001` evidence-bound claims / 증거 결속 주장;
- `UNKNOWN-001` unknown stays unknown / 미확인은 미확인 유지;
- `CONFLICT-001` explicit conflict resolution / 충돌 명시 해결;
- `FRESH-001` dynamic facts reverified / 동적 사실 재검증;
- `MEMORY-001` durable GitHub memory / 지속 GitHub 메모리;
- `WRITEBACK-001` end-of-work writeback / 작업종료 기록.

A hypothesis is never presented as validated merely because it is plausible. / 그럴듯함만으로 가설을 검증결과처럼 표현하지 않는다.

## C. Language Gate / 언어 게이트

All official human-readable artifacts comply with `LANG-001`. / 모든 공식 사람이 읽는 산출물은 `LANG-001` 준수.

- Korean-English semantic parity / 한·영 의미 동등성;
- preserve native fields/code/API/standards/proper names / 원천 필드·코드·API·표준·고유명 보존;
- material caveats and uncertainty appear in both languages / 중요 제약·불확실성 양언어 반영.

## D. Before Write / 기록 전

1. fetch current file/Issue / 현재 파일·Issue 조회;
2. preserve valid existing content / 유효 기존내용 보존;
3. incorporate evidence, uncertainty and decision state / 증거·불확실성·판단상태 반영;
4. check Claim Ledger/Decision Log to avoid contradiction / ledger/log 모순 확인;
5. apply `LANG-001` / 병기 적용;
6. use descriptive commit message / 설명 가능한 commit;
7. avoid duplicate truth stores / 중복 Source of Truth 금지.

## E. End-of-Work Writeback / 작업 종료 기록

Significant progress updates, as applicable: / 중요 진행 시 필요 항목 갱신:

1. relevant `research/` artifact;
2. active GitHub Issue;
3. `STATUS.md`;
4. `context/SESSION_HANDOFF.md`;
5. `context/PROJECT_MEMORY.md` **only for durable decision-relevant facts** / 지속 사실 변경 시에만;
6. `registry/CLAIM_LEDGER.md` for material claims;
7. `registry/DECISION_LOG.md` for material decisions;
8. relevant MOC / 관련 MOC.

Chat-only conclusions remain provisional until recorded. / 채팅에만 있는 결론은 기록 전 잠정적이다.

## F. Repository / Obsidian Taxonomy / 저장소·Obsidian 구조

```text
README.md
STATUS.md
.gitignore                 # excludes local .obsidian state

docs/
  GOVERNANCE.md
  LANGUAGE_POLICY.md
  METHODOLOGY.md
  GPT_GITHUB_SYNC_PROTOCOL.md
  HALLUCINATION_CONTROL_PROTOCOL.md
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

## G. Drift Reconciliation / 드리프트 조정

If `STATUS.md`, Issue state, research artifact, memory, or chat disagree: / 상태가 불일치하면:
1. inspect latest committed evidence and active Issue / 최신 commit 근거·Issue 확인;
2. identify the divergence explicitly / 차이 명시;
3. apply `CONFLICT-001` precedence / 충돌 우선순위 적용;
4. reconcile durable files in the same session when possible / 가능하면 같은 세션에서 지속파일 동기화.

Do not silently average or merge contradictory states. / 충돌상태를 조용히 평균·혼합하지 않는다.

## H. Work Queue / 작업 큐

Proceed by dependency and information gain, normally following official Issue order. If a HOLD/FAIL makes the current path invalid, record the gate result and promote the next defensible candidate rather than forcing continuation. / 선행조건·정보이득을 기준으로 공식 Issue 순서를 따르되 HOLD/FAIL이면 결과를 기록하고 강제 진행 대신 다음 방어 가능한 후보로 이동한다.

## I. Human/GPT Roles / 사용자·GPT 역할

Within authorization, GPT may autonomously research, compare, score, generate hypotheses, critique, run feasibility analysis, design/execute permitted experiments, and update the repository. Records must let another GPT session or human reconstruct why a decision was made. / 권한 범위에서 GPT는 조사·비교·점수화·가설·비판·feasibility·허용 실험·저장소 갱신을 수행할 수 있으며 기록은 다른 세션/사람이 판단근거를 재구성할 수 있어야 한다.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
