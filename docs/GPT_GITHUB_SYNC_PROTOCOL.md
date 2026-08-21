# GPT ↔ GitHub Sync Protocol / GPT ↔ GitHub 동기화 규약

## Purpose / 목적

**한국어**  
이 규약은 GPT 기반 연구 작업이 `Eckommon/AI-Innovative-Research-Engine`의 지속적 상태와 어떻게 동기화되는지를 정의한다. GitHub는 공식 기준 기록이며 GPT 세션은 분석·조사·가설·검증을 수행하는 작업 공간이다.

**English**  
This protocol defines how GPT-assisted work remains synchronized with `Eckommon/AI-Innovative-Research-Engine`. GitHub is the official persistent system of record, while GPT sessions are analytical workspaces for research, synthesis, hypothesis generation, and validation.

## A. Session Start — READ BEFORE REASONING / 세션 시작 — 추론 전에 읽기

프로젝트 관련 실질 작업 전 GPT는 채팅 기억만 의존하지 않고 저장소 상태를 우선 확인한다.  
Before material project work, GPT should inspect repository state rather than rely only on chat memory.

Minimum read set / 최소 확인 대상:

1. `README.md`
2. `STATUS.md`
3. 관련 `docs/` / relevant `docs/`
4. 관련 `registry/` 및 `research/` 객체 / relevant registry and research objects
5. 관련 GitHub Issue와 최근 커밋 / relevant GitHub Issues and recent commits

현재 사용자 지시와 저장소가 충돌하면 이를 숨기지 않고 명시적 변경으로 해결한다.  
If current user instructions conflict with repository state, surface and resolve the conflict through an explicit change rather than silently assuming one side.

## B. During Work — CLASSIFY CLAIMS / 작업 중 — 주장 분류

중요한 주장은 다음 증거 등급으로 구분한다. / Material claims are conceptually classified as:

- `OBSERVED`
- `DERIVED`
- `HYPOTHESIZED`
- `VALIDATED`
- `REJECTED`
- `INCONCLUSIVE`

GPT는 가설을 검증 결과처럼 표현하지 않는다. / GPT must not present a hypothesis as a validated result.

## C. Language Gate / 언어 게이트

모든 공식 사람이 읽는 산출물은 `docs/LANGUAGE_POLICY.md`의 `LANG-001`을 적용한다.  
All official human-readable artifacts are governed by `LANG-001` in `docs/LANGUAGE_POLICY.md`.

Before write / 기록 전:

- 제목·핵심 설명·상태·판단·결론을 한국어/영어로 병기 / provide Korean-English bilingual titles, core descriptions, states, judgments, and conclusions;
- 두 언어에 동일한 중요한 제약·불확실성을 반영 / preserve material caveats and uncertainty in both languages;
- 데이터 필드명·코드·API·표준명·고유명은 원문 보존 / preserve native dataset fields, code, APIs, standards, and proper names.

## D. Before Repository Write / 저장소 기록 전

1. 현재 파일·Issue 상태를 다시 읽는다. / Fetch the current file or Issue state.
2. 의도적 교체가 아니면 기존 유효 내용을 보존한다. / Preserve valid existing content unless intentional replacement is required.
3. 새로운 증거·결정·불확실성을 반영한다. / Incorporate new evidence, decisions, and uncertainty.
4. `LANG-001`을 적용한다. / Apply `LANG-001`.
5. 설명 가능한 커밋 메시지를 사용한다. / Use a descriptive commit message.
6. 중복·모순 레지스트리를 만들지 않는다. / Avoid duplicate or contradictory registries.

## E. Session End — WRITE MATERIAL STATE / 세션 종료 — 실질 상태 기록

다음 중 하나 이상이 실질적으로 바뀌면 GitHub에 반영한다. / Write back when one or more of the following materially changes:

- 연구 방향 / research direction;
- 방법론 / methodology;
- 소재·소스·데이터셋 인벤토리 / topic, source, or dataset inventory;
- 평가·점수 / assessment or scoring;
- 가설 / hypothesis;
- feasibility 결과 / feasibility findings;
- 실험 결과 / experiment results;
- 프로젝트 상태 / project status;
- 다음 행동 / next action.

중요한 연구 진행은 최소한 해당 연구 객체와 `STATUS.md`를 갱신한다.  
Significant research progress should update at least the relevant research artifact and `STATUS.md`.

## F. Recommended Repository Taxonomy / 권장 저장소 구조

```text
README.md
STATUS.md

docs/
  GOVERNANCE.md
  LANGUAGE_POLICY.md
  METHODOLOGY.md
  GPT_GITHUB_SYNC_PROTOCOL.md
  METADATA_SCHEMA.md

registry/
  GLOBAL_PUBLIC_DATA_SOURCE_REGISTRY.md
  INNOVATION_POTENTIAL_SCORE.md
  RESEARCH_MATERIAL_LANDSCAPE.md

research/
  <research-id>/
    README.md
    SOURCES.md
    DATASET_PROFILE.md
    HYPOTHESES.md
    EXPERIMENT.md
    RESULTS.md

src/                  # 향후 자동화·분석 코드 / future automation and analysis code
tests/                # 재현성 테스트 / reproducibility tests
data/README.md         # 대용량·외부 데이터 취급 규칙 / external/large-data rules
```

## G. Synchronization Semantics / 동기화 의미

### `GitHub → GPT`
- 저장소가 지속적 프로젝트 컨텍스트를 정의한다. / Repository files define durable project context.
- 실질 작업 시작 시 관련 상태를 새로 읽는다. / Refresh relevant state before material work.

### `GPT → GitHub`
- 중요한 결정·조사 결과·검증 결과를 커밋 또는 Issue에 보존한다. / Persist material decisions and findings through commits or Issues.
- 채팅에만 남은 결론은 공식 기록되기 전까지 잠정적이다. / Chat-only conclusions remain provisional until recorded.

이는 모든 대화가 자동 복제된다는 의미가 아니라 **workflow synchronization / 작업 흐름 동기화**를 의미한다.

## H. Status Discipline / 상태 관리

`STATUS.md`는 다음을 유지한다. / `STATUS.md` should maintain:

- baseline/version / 베이스라인·버전;
- active wave / 활성 Wave;
- completed work / 완료 작업;
- active work / 진행 작업;
- blocked/hold items / 차단·보류 항목;
- official work queue / 공식 Work Queue;
- next actions / 다음 행동;
- relevant latest commits when useful / 필요 시 주요 최근 커밋.

## I. Drift Control / 드리프트 통제

저장소와 채팅이 불일치할 경우 / When repository and chat diverge:

1. 최신 저장소 상태를 확인 / inspect latest repository state;
2. 차이를 명시 / identify the divergence;
3. 기록된 결정을 미기록 가정보다 우선 / prefer explicit recorded decisions over unstored assumptions;
4. 사용자가 의도적으로 방향을 바꾼 경우 저장소를 갱신 / update the repository when the user intentionally changes direction.

## J. Work Queue Rule / Work Queue 규칙

공식 Issue가 존재하면 원칙적으로 번호·선행조건 순으로 진행한다. 단, 사용자가 명시적으로 선행 연구를 요청하거나 새 증거가 기존 순서를 무효화하면 그 이유를 기록한 뒤 순서를 조정할 수 있다.  
When official Issues exist, work proceeds in issue/dependency order by default. If the user explicitly requires precursor research or new evidence invalidates the order, the sequence may be changed after recording the rationale.

## K. Commit Message Convention / 커밋 메시지 규칙

- `docs: refine bilingual innovation discovery methodology`
- `registry: add research material landscape`
- `research: calibrate NIST AM Bench dataset profile`
- `experiment: record feasibility test results`
- `status: advance official work queue`

## L. Human/GPT Roles / 사용자와 GPT 역할

GPT는 사용자 권한 범위 내에서 자율적으로 조사, 비교, 점수화, 가설 생성, 비판적 검토, feasibility 분석 및 저장소 반영을 수행할 수 있다. 저장소는 다른 GPT 세션 또는 인간 검토자가 연구 의사결정의 근거를 재구성할 수 있을 정도의 증거를 보존해야 한다.  
Within user authorization, GPT may autonomously research, compare, score, generate hypotheses, critique results, perform feasibility analysis, and update the repository. The repository must preserve enough evidence for another GPT session or a human reviewer to reconstruct why a research decision was made.
