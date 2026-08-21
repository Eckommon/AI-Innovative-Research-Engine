---
id: KM-TAGS
type: taxonomy
state: ACTIVE
tags:
  - type/moc
  - domain/knowledge-management
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# Tag Taxonomy / 태그 체계

## Principle / 원칙

태그는 탐색과 필터링을 위한 통제 vocabulary다. 새로운 의미가 기존 namespace로 표현 가능하면 새 synonym을 만들지 않는다. / Tags are a controlled vocabulary for navigation and filtering. Do not create synonyms when an existing namespace can express the meaning.

## Namespaces / Namespace

| Namespace | Purpose / 목적 | Examples / 예시 |
|---|---|---|
| `type/*` | 문서·객체 유형 / object type | `type/dataset`, `type/source`, `type/hypothesis`, `type/experiment`, `type/decision`, `type/moc`, `type/memory` |
| `state/*` | 연구 생명주기 / research lifecycle | `state/discovered`, `state/feasibility`, `state/validated`, `state/rejected`, `state/inconclusive`, `state/hold` |
| `evidence/*` | 증거등급 / evidence class | `evidence/observed`, `evidence/derived`, `evidence/hypothesized`, `evidence/validated` |
| `region/*` | 국가·지역 / jurisdiction | `region/us`, `region/kr`, `region/eu`, `region/global` |
| `domain/*` | 연구분야 / domain | `domain/grid`, `domain/manufacturing`, `domain/industry`, `domain/climate`, `domain/logistics`, `domain/minerals` |
| `wave/*` | 확장 Wave | `wave/wave0`, `wave/wave1`, `wave/wave2` |
| `priority/*` | 우선순위 / priority | `priority/p0`, `priority/p1`, `priority/a`, `priority/b` |
| `risk/*` | 핵심 위험 / risk | `risk/data-gap`, `risk/mapping`, `risk/classification`, `risk/license`, `risk/freshness`, `risk/safety` |

## Mandatory Tags / 권장 필수 태그

Durable research objects should normally include at least / 지속 연구객체는 원칙적으로 최소 다음을 포함:
- one `type/*`;
- one `state/*`;
- one `region/*` where applicable;
- one `domain/*`;
- one `evidence/*` when the note contains a central empirical claim.

## State vs Evidence / 상태와 증거 구분

`state/*`는 연구 객체의 workflow 위치이고 `evidence/*`는 주장 근거의 성격이다. 둘을 혼동하지 않는다.  
`state/*` describes workflow position; `evidence/*` describes claim evidence. Do not conflate them.

Example / 예시: an experiment note may have `state/validated` and contain some `evidence/hypothesized` next-step claims. / 검증 완료 실험 문서에도 후속 가설은 `evidence/hypothesized`일 수 있다.

## Change Rule / 변경 규칙

새 namespace 또는 대규모 태그 구조 변경은 `KM-001` 변경으로 보고 `docs/OBSIDIAN_KNOWLEDGE_MANAGEMENT.md`와 이 문서를 함께 갱신한다.  
A new namespace or material taxonomy change is treated as a `KM-001` change and requires coordinated updates to this file and the knowledge-management policy.

`LANG-001` compliant / 한글·영문 병기 규약 준수.
