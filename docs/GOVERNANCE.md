# Governance / 거버넌스

## 1. Purpose / 목적

**한국어**  
AI-Innovative-Research-Engine은 공공·연구 데이터를 결합하고 검증 가능한 가설을 생성·시험하여 잠재적 혁신과 구조적 병목을 발견하며, 그 전체 증거 경로를 재현 가능한 형태로 보존하기 위해 존재한다.

**English**  
AI-Innovative-Research-Engine exists to discover potentially valuable innovations and structural bottlenecks from public/research data by combining datasets, generating falsifiable hypotheses, testing them, and preserving the full evidence trail in reproducible form.

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

## 8. Language Policy / 언어 정책

향후 주요 Markdown 문서, 연구 기록, 상태 기록, Issue 제목·본문, 핵심 결론과 의사결정은 **한글/영문 병기**를 원칙으로 한다. / Future major Markdown documents, research records, status records, Issue titles/bodies, core conclusions, and decisions shall be **bilingual in Korean and English**.

세부 규칙은 `docs/LANGUAGE_POLICY.md`를 따른다. / Detailed rules are defined in `docs/LANGUAGE_POLICY.md`.

## 9. Change Control / 변경 통제

미션, 방법론, 점수체계, 증거등급, 상태 생명주기, 언어정책 등 핵심 규칙의 변경은 설명 가능한 커밋으로 남기고 활성 작업에 영향을 주면 `STATUS.md`에 반영한다. / Material changes to mission, methodology, scoring, evidence classes, lifecycle, or language policy require descriptive commits and must be reflected in `STATUS.md` when they affect active work.
