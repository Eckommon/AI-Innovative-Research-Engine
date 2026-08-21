# Language Policy / 한글·영문 병기 규약

**Policy ID / 규약 ID:** `LANG-001`  
**Status / 상태:** `MANDATORY`  
**Effective / 시행일:** 2026-08-21

## 1. Rule / 기본 규칙

프로젝트의 사람이 읽는 주요 산출물은 **한국어와 영어를 병기**한다. 어느 한 언어만으로 작성하는 것은 원칙적으로 임시 작업 상태로만 허용하며, 공식 기록으로 승격될 때는 병기를 완료한다.  
Major human-readable project artifacts shall be **maintained in both Korean and English**. Single-language content is allowed only as temporary working material; bilingual completion is required before promotion to an official project record.

## 2. In Scope / 적용 대상

- `README.md`, `STATUS.md`
- `docs/`의 거버넌스·방법론·규약·설계 문서 / governance, methodology, protocol, and design documents under `docs/`
- `registry/`의 설명·평가 문서 / explanatory and assessment records under `registry/`
- `research/`의 연구 질문·가설·방법·결과·결론 / research questions, hypotheses, methods, results, and conclusions under `research/`
- GitHub Issue 제목·본문·중요 진행 코멘트 / GitHub Issue titles, bodies, and material progress comments
- 의사결정·HOLD·REJECTED·INCONCLUSIVE 사유 / rationale for decisions and terminal/hold states

## 3. Native Content Preservation / 원문 보존

다음은 번역으로 대체하지 않고 원문을 보존한다. 필요하면 설명만 병기한다.  
The following remain in their authoritative original form; bilingual explanation may be added, but the native token is not replaced.

- 데이터셋 컬럼명·필드명 / dataset column and field names
- API parameter, JSON/YAML key, schema identifier
- 코드, 명령어, 파일 경로, commit SHA
- 표준명, 규격번호, DOI, URL
- 기관·제품·프로그램의 공식 고유명 / official proper names of institutions, products, and programs
- 상태값과 증거등급 토큰 (`OBSERVED`, `VALIDATED`, etc.)

## 4. Recommended Format / 권장 형식

### 짧은 항목 / Short items
`한국어 / English`

### 설명형 문단 / Explanatory paragraphs
**한국어** 문단 후 **English** 문단을 배치한다.  
Place the Korean paragraph first, followed by its English counterpart.

### 표 / Tables
가능하면 `한국어 / English` 열 또는 셀 내 병기를 사용한다.  
Use parallel Korean/English columns or bilingual cell text when practical.

## 5. Fidelity Rule / 의미 충실성 규칙

한국어와 영어는 의미상 동등해야 하며, 한쪽 언어에만 중요한 판단·제약·불확실성을 남기지 않는다.  
The Korean and English versions must be semantically equivalent; material judgments, constraints, caveats, or uncertainty must not appear in only one language.

## 6. Source-Language Rule / 출처 언어 규칙

원천 자료가 특정 언어로만 존재할 경우, 원문 명칭과 핵심 용어를 보존하면서 다른 언어로 충실한 요약을 제공한다. 번역이 데이터 의미를 바꿀 위험이 있으면 원문을 우선한다.  
When a source exists in only one language, preserve its original names and critical terminology while providing a faithful summary in the other language. If translation risks changing technical meaning, the authoritative original takes precedence.

## 7. GPT Work Rule / GPT 작업 규칙

GPT는 프로젝트 관련 공식 산출물을 새로 만들거나 실질적으로 수정할 때 이 규약을 자동 적용한다. 기존 단일언어 문서를 발견하면 작업 범위와 관련된 문서는 병기 상태로 갱신한다.  
When GPT creates or materially revises an official project artifact, this policy is applied by default. If a relevant legacy artifact is single-language, GPT should update it to bilingual form when it falls within the active work scope.

## 8. Exception / 예외

대규모 원시 데이터, 자동 생성 로그, 실행 출력, 코드 내부 주석, 외부 원문 복제본에는 병기를 강제하지 않는다. 다만 이를 해석하는 공식 연구 문서는 병기해야 한다.  
Bilingual duplication is not mandatory for large raw datasets, machine-generated logs, execution outputs, source-code internals, or preserved external originals. Official research documents interpreting them remain subject to this policy.
