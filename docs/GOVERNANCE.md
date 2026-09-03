# Governance / 거버넌스

## 1. Purpose / 목적

**한국어**  
AI-Innovative-Research-Engine은 공공·연구 데이터를 결합하고 검증 가능한 가설을 생성·시험하여 잠재적 혁신과 구조적 병목을 발견하며, 그 전체 증거 경로를 재현 가능한 형태로 보존하기 위해 존재한다.

**English**  
AI-Innovative-Research-Engine exists to discover potentially valuable innovations and structural bottlenecks from public/research data by combining datasets, generating falsifiable hypotheses, testing them, and preserving the full evidence trail in reproducible form.

### Mission Anchor / 목적 고정

**KO:** 특정 데이터셋·실험·도구·시뮬레이터·재현 경로의 완주는 프로젝트 목적이 아니다. 최상위 목적은 **공공·연구 데이터의 관계에서 새롭고 반증 가능하며 재현 가능하고 실용적인 혁신 기회 또는 구조적 병목 통찰을 발견·검증·축적하는 것**이다.

**EN:** Completing any particular dataset, experiment, tool, simulator, or reproduction route is not the project mission. The highest-level objective is to **discover, test, and accumulate new, falsifiable, reproducible, and practically useful innovation opportunities or structural-bottleneck insights from relationships among public/research data**.

Durable mission memory: `context/MEM-054-MISSION-ANCHOR.md`. / 지속 목적 기억은 `MEM-054`를 따른다.

## 2. Repository Authority / 저장소 권한

GitHub는 다음 항목의 지속적 기준 저장소다. / GitHub is the persistent system of record for:

- 프로젝트 범위와 아키텍처 / project scope and architecture;
- 연구 방법론 / research methodology;
- 소스 및 데이터셋 레지스트리 / source and dataset registries;
- 평가·점수·가설·실험 / evaluations, scores, hypotheses, and experiments;
- 결정·상태·Work Queue / decisions, status, and work queue;
- 가능한 경우 재현 코드와 산출물 / reproducible code and outputs where practical.

채팅 세션은 작업 환경이며 최종 기준 기록이 아니다. / Chat sessions are working environments, not the final source of truth.

## 3. Core Principles / 핵심 원칙

1. **Evidence before narrative / 서사보다 증거** — 매력적인 설명은 데이터보다 우선하지 않는다. / Attractive explanations do not outrank data.
2. **Hypothesis is not conclusion / 가설은 결론이 아님** — 검증 전 주장은 명시적으로 잠정 상태를 유지한다. / Untested claims remain explicitly provisional.
3. **Reproducibility / 재현성** — 변환, 조인, 가정, 평가 기준을 기록한다. / Transformations, joins, assumptions, and evaluation criteria are recorded.
4. **Negative results are assets / 부정적 결과도 자산** — 기각·불확정 결과도 연구 레저에 보존한다. / Rejected and inconclusive results remain in the research ledger.
5. **Source provenance / 출처 추적성** — 공식·1차 출처를 우선하고 URL·메타데이터·버전을 보존한다. / Prefer official or primary sources and preserve URLs, metadata, and versions.
6. **Join discipline / 조인 규율** — 조인키, 시간·공간 정렬, 의미적 호환성을 문서화한다. / Document join keys, temporal/spatial alignment, and semantic compatibility.
7. **No forced innovation / 혁신 강제 금지** — 증거가 약하면 `HOLD`, `REJECTED`, `INCONCLUSIVE`가 올바른 결과다. / If evidence is weak, `HOLD`, `REJECTED`, or `INCONCLUSIVE` is the correct result.
8. **Progressive scaling / 단계적 확장** — 고품질 사례에서 방법론을 검증한 뒤 대규모 수집·자동화로 확장한다. / Validate the method on strong cases before broad harvesting and automation.
9. **Bilingual traceability / 한·영 병기 추적성** — 사람이 읽는 주요 산출물은 한국어와 영어를 병기한다. / Major human-readable artifacts are maintained in both Korean and English.
10. **Native-term preservation / 원문 용어 보존** — 데이터 필드명·코드·표준·API·고유명사는 정확성을 위해 원문을 유지한다. / Native field names, code, standards, APIs, and proper names remain in their authoritative original form.
11. **No-cost by default / 기본 무비용** — 모든 연구·검증·개발·자동화는 추가 금전비용 0원을 기본 조건으로 한다. 비용이 발생하거나 발생할 합리적 가능성이 있는 작업은 실행 전에 사용자의 명시적 승인을 받아야 하며, 비용 상태가 불명확하면 `HOLD_COST_APPROVAL`로 둔다. / All research, validation, development, and automation defaults to zero incremental monetary cost. Any action that incurs or may reasonably incur monetary cost requires explicit user approval before execution; uncertain billing status is `HOLD_COST_APPROVAL`.
12. **Mission over branch completion / Branch 완주보다 목적 우선** — 특정 연구 branch의 기술적 완주보다 프로젝트 수준의 혁신·병목 발견 정보가치를 우선한다. Route dependency를 mission dependency로 승격하지 않는다. / Mission-level innovation/bottleneck information value outranks technical completion of a particular research branch. A route dependency must not be promoted into a mission dependency.
13. **Portfolio opportunity cost / 포트폴리오 기회비용** — descendant gate를 열 때는 같은 시간에 더 높은 Combination/Project IPS 후보를 놓치는 비용을 명시적으로 고려한다. / Every descendant gate must consider the opportunity cost of deferring higher-value Combination/Project IPS candidates.

Detailed cost controls are defined in `docs/NO_COST_POLICY.md` (`COST-001`). / 세부 비용 통제는 `COST-001`을 따른다.

## 4. Research Object States / 연구 객체 상태

- `DISCOVERED` — 발견 / discovered
- `SCREENING` — 선별 / screening
- `CANDIDATE` — 후보 / candidate
- `FEASIBILITY_TEST` — 실행 가능성 검증 / feasibility test
- `EXPERIMENT` — 실험 / experiment
- `VALIDATED` — 검증 / validated
- `REJECTED` — 기각 / rejected
- `INCONCLUSIVE` — 불확정 / inconclusive
- `HOLD` — 보류 / hold
- `ARCHIVED` — 보관 / archived

## 5. Evidence Classes / 증거 등급

- `OBSERVED` — 원천 데이터·공식 문서 또는 재현 가능한 직접 관측 / directly supported by source data, official documentation, or reproducible observation.
- `DERIVED` — 관측 근거에서 명시적 방법으로 계산·변환 / computed or transformed from observed evidence using a documented method.
- `HYPOTHESIZED` — 검증 대기 중인 시험 가능한 주장 / testable claim awaiting validation.
- `VALIDATED` — 정의된 검증 기준 통과 / passed defined validation criteria.
- `REJECTED` — 정의된 기준에서 기각 / failed defined criteria.
- `INCONCLUSIVE` — 증거가 부족하거나 모호 / insufficient or ambiguous evidence.

## 6. Decision Rule / 의사결정 규칙

가설은 다음 조건이 충족되기 전 프로젝트 결론으로 승격되지 않는다. / No hypothesis is promoted to a project claim until:

- 출처와 버전이 기록됨 / source provenance and version are recorded;
- 실제 데이터 접근이 확인됨 / data access is confirmed;
- 주요 변수와 결과변수가 식별됨 / key variables and outcomes are identifiable;
- 조인 또는 모델링 가능성이 실증됨 / feasibility of joining or modeling is demonstrated;
- 최종 평가 전에 검증·기각 기준이 정의됨 / validation and rejection criteria are defined before final evaluation;
- `OBSERVED` / `DERIVED` / `HYPOTHESIZED`가 명확히 분리됨 / evidence states are clearly separated.

## 7. Research Scope / 연구 범위

연구 소재는 다음 두 트랙을 동등하게 포함한다. / The engine maintains two equal research tracks:

### A. Frontier Opportunity / 현대 유망 영역
성장성·사회적 파급력·기술변화 속도가 크고 공공·연구데이터로 검증 가능한 영역. / Fast-growing, high-impact domains where public/research data can support falsifiable investigation.

### B. Persistent Bottleneck / 기존 혁신의 잔존 병목
기술·산업이 이미 성숙했지만 비용, 품질, 인프라, 표준화, 공급망, 효율 또는 접근성 병목이 지속되는 영역. / Mature systems where cost, quality, infrastructure, standards, supply-chain, efficiency, or access bottlenecks persist.

소재 선정은 유행성보다 데이터 접근성·결합 가능성·검증 가능성·병목의 실재성·확장성을 우선한다. / Topic selection prioritizes data access, joinability, falsifiability, real bottleneck evidence, and scalability over trendiness.

## 8. Mission-ROI / Branch-Stop Control / 목적-ROI 및 Branch 중단 통제

`DEC-093` and `MEM-054` are mandatory. / `DEC-093`와 `MEM-054`는 의무 적용한다.

Before opening any descendant after `HOLD`, `REJECT`, runtime failure, source-access failure, or failed feasibility, the work record must answer:

1. **Scientific vs tooling uncertainty / 과학 vs 도구 불확실성** — 다음 gate가 과학·혁신 불확실성을 줄이는가, 아니면 transport/runtime/parser/tooling만 해결하는가?
2. **Mission necessity / 미션 필수성** — 막힌 source/route가 프로젝트 수준 가설에 유일하게 필요한가, 아니면 한 구현경로에만 필요한가?
3. **Alternative portfolio value / 대체 포트폴리오 가치** — 더 높은 Combination/Project IPS 또는 더 직접적인 독립 후보가 있는가?
4. **Infrastructure streak / 인프라 연속성** — 새 과학 증거 없이 infrastructure/runtime/source-transfer descendant가 두 번 이상 연속됐는가?
5. **Loss if stopped / 중단 손실** — branch를 멈추면 고유한 검증 claim을 잃는가, 아니면 하나의 시험만 연기되는가?

### Default branch-stop rule / 기본 branch 중단 규칙

If the next work is primarily tooling/infrastructure, the blocked route is not uniquely mission-critical, a credible alternative exists, and there have been **>=2 consecutive infrastructure/runtime/source-transfer descendants without new scientific evidence**, default to:

**`HOLD_BRANCH / ARCHIVE_ROUTE → RETURN_TO_PORTFOLIO`**.

Do not open another numbered descendant solely because another workaround is technically possible. / 또 다른 우회방법이 기술적으로 가능하다는 이유만으로 descendant를 자동 생성하지 않는다.

### Continuation override / 계속 진행 예외

Continuation requires explicit written justification that at least one is true:
- the source/route is uniquely necessary to a high-value project claim;
- no credible independent alternative exists;
- the next gate has clearly superior mission-level expected information value;
- the user explicitly prioritizes completion of that branch.

## 9. Language Policy / 언어 정책

향후 주요 Markdown 문서, 연구 기록, 상태 기록, Issue 제목·본문, 핵심 결론과 의사결정은 **한글/영문 병기**를 원칙으로 한다. / Future major Markdown documents, research records, status records, Issue titles/bodies, core conclusions, and decisions shall be **bilingual in Korean and English**.

세부 규칙은 `docs/LANGUAGE_POLICY.md`를 따른다. / Detailed rules are defined in `docs/LANGUAGE_POLICY.md`.

## 10. Change Control / 변경 통제

미션, 방법론, 점수체계, 증거등급, 상태 생명주기, 언어정책, 비용정책, Mission-ROI/Branch-Stop 규칙 등 핵심 규칙의 변경은 설명 가능한 커밋과 Decision record로 남기고 활성 작업에 영향을 주면 `STATUS.md`에 반영한다. / Material changes to mission, methodology, scoring, evidence classes, lifecycle, language policy, cost policy, or Mission-ROI/Branch-Stop controls require descriptive commits and a Decision record, and must be reflected in `STATUS.md` when they affect active work.
