# AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진

> **Public / Research Data → Data Relationships → Hypotheses → Experiments → Innovation**  
> **공공·연구 데이터 → 데이터 관계 → 가설 → 실험 → 혁신**

## Description / 프로젝트 설명

**한국어**  
AI 기반 혁신 탐색 연구 엔진은 국가·지역·공공기관·연구기관이 공개한 데이터를 발견·정규화·결합하고, AI가 데이터 간 관계에서 **검증 가능한 가설**을 생성한 뒤 실제 데이터 분석, 통계, 시뮬레이션, 모델링 및 통제된 실험을 통해 이를 검증하여 **산업·기술·사회 시스템의 혁신 기회와 잔존 병목을 체계적으로 발굴·평가·기록하는 연구 시스템**이다. 목표는 데이터 링크를 많이 수집하는 것이 아니라, 서로 분리되어 있던 데이터의 결합으로 새롭고 재현 가능하며 실용적인 통찰을 찾아내는 것이다.

**English**  
The AI-Innovative-Research-Engine is a research system that discovers, normalizes, and combines public and research datasets from governments, regions, public institutions, and research organizations; uses AI to generate **falsifiable hypotheses** from relationships among those datasets; and tests them through real-data analysis, statistics, simulation, modeling, and controlled experiments. Its purpose is to systematically discover, evaluate, and record **innovation opportunities and persistent bottlenecks in industrial, technological, and societal systems**. The goal is not to accumulate links, but to identify new, reproducible, and practically useful insights created by connecting previously separated data.

## Core Question / 핵심 질문

> **Which combinations of public/research data can produce a new, testable, reproducible, and practically useful insight?**  
> **어떤 공공·연구 데이터의 조합이 새롭고, 검증 가능하며, 재현 가능하고, 실용적인 통찰을 만들어낼 수 있는가?**

## Mission / 미션

**한국어**  
공공·연구 데이터를 단순 검색·요약하는 수준을 넘어, 데이터 간 연결 가능성을 탐색하고 검증 가능한 산업·사회적 명제를 생성하며, 성공·실패·보류 결과를 모두 축적하여 반복 가능한 혁신 탐색 체계를 구축한다.

**English**  
Move beyond simple search and summarization of public/research data by discovering relationships among datasets, generating testable industrial and societal propositions, and preserving validated, rejected, inconclusive, and held results as a reusable innovation-discovery system.

## Official Research Pipeline / 공식 연구 파이프라인

```text
Source Discovery / 소스 탐색
        ↓
Metadata Harvesting / 메타데이터 수집
        ↓
Dataset Triage / 데이터셋 선별
        ↓
Relationship Discovery / 관계 탐색
        ↓
Hypothesis Generation / 가설 생성
        ↓
Feasibility Test / 실행 가능성 검증
        ↓
Controlled Experiment / 통제 실험
        ↓
Innovation Registry / 혁신 레지스트리
```

## Research Levels / 연구 수준

| Level | 한국어 | English | Example / 예시 |
|---|---|---|---|
| L1 | 단일 데이터셋 혁신 | Dataset Innovation | NIST AM Bench → 제조 품질 예측 / manufacturing quality prediction |
| L2 | 데이터셋 간 혁신 | Cross-Dataset Innovation | 제조 + 로봇 + 소재 / manufacturing + robotics + materials |
| L3 | 기관 간 혁신 | Cross-Agency Innovation | NIST + DOE + EPA + NOAA |
| L4 | 국가·지역 간 혁신 | Cross-National Innovation | US + Korea + EU + Japan |
| L5 | 기계 보조 혁신 탐색 | Machine-Assisted Innovation Discovery | 유망 데이터 조합과 검증 가능한 가설의 반자동/자동 탐색 |

## Research Scope / 연구 소재 범위

연구 소재는 두 축을 모두 포함한다. / The research scope deliberately covers two complementary tracks.

1. **현대사회에서 성장성과 파급력이 큰 유망 영역 / High-potential frontier domains**  
   AI 인프라·데이터센터, 전력·그리드·저장, 첨단제조·로봇·디지털트윈, 핵심광물·순환자원, 바이오·공중보건, 공급망·물류, 기후·재난 회복력 등.

2. **이미 발전했지만 구조적 병목이 남은 영역 / Mature systems with persistent bottlenecks**  
   송배전·변압기, 건물 에너지 리트로핏, 상수도 누수, 항만·물류 지연, 제조 품질·인증, 자원 회수·재활용 등.

소재는 유행성만으로 채택하지 않으며, **데이터 접근성·결합 가능성·검증 가능성·실질적 병목·확장성**을 함께 평가한다.  
Topics are not selected on trendiness alone; **data accessibility, joinability, falsifiability, bottleneck severity, and scalability** are assessed together.

## Geographic Waves / 지역 확장 단계

- **Wave 0** — NIST AM Bench: 방법론 보정 기준 / methodological calibration benchmark.
- **Wave 1** — United States / 미국, Korea / 한국, European Union / EU.
- **Wave 2** — Japan / 일본, United Kingdom / 영국, Singapore / 싱가포르.
- **Wave 3** — Canada / 캐나다, Australia / 호주, OECD, World Bank, additional regions / 기타 지역.

## Evidence Classes / 증거 등급

- `OBSERVED` — 원천 데이터·공식 문서·재현 가능한 직접 관측 / directly supported observation.
- `DERIVED` — 관측값에서 명시적 방법으로 계산·변환 / derived by documented computation or transformation.
- `HYPOTHESIZED` — 아직 검증되지 않은 시험 가능한 주장 / testable but unvalidated claim.
- `VALIDATED` — 사전 정의된 검증 기준 통과 / passed predefined validation criteria.
- `REJECTED` — 사전 정의된 기준에서 기각 / failed the predefined criteria.
- `INCONCLUSIVE` — 증거 부족 또는 모호 / insufficient or ambiguous evidence.

## Core Artifacts / 핵심 문서

- [`STATUS.md`](STATUS.md) — 현재 상태·Work Queue·다음 행동 / live state, work queue, and next actions.
- [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md) — 프로젝트 범위·의사결정 원칙 / governance and decision rules.
- [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) — 공식 연구 방법론 / official research methodology.
- [`docs/GPT_GITHUB_SYNC_PROTOCOL.md`](docs/GPT_GITHUB_SYNC_PROTOCOL.md) — GPT ↔ GitHub 동기화 규약 / synchronization protocol.
- [`docs/LANGUAGE_POLICY.md`](docs/LANGUAGE_POLICY.md) — 한글/영문 병기 규약 / Korean-English bilingual policy.
- [`docs/METADATA_SCHEMA.md`](docs/METADATA_SCHEMA.md) — 정규화 연구 메타데이터 스키마 / normalized research metadata schema.
- [`registry/GLOBAL_PUBLIC_DATA_SOURCE_REGISTRY.md`](registry/GLOBAL_PUBLIC_DATA_SOURCE_REGISTRY.md) — 글로벌 공공데이터 소스 레지스트리 / global public-data source registry.
- [`registry/INNOVATION_POTENTIAL_SCORE.md`](registry/INNOVATION_POTENTIAL_SCORE.md) — 혁신 잠재력 평가 / Innovation Potential Score.

## Repository Role / 저장소 역할

**한국어**  
이 저장소는 프로젝트의 **공식 지속 기록이자 기준 상태(Source of Truth)** 이다. GPT 세션은 분석·조사·가설 생성·비판적 검토를 수행하는 작업 공간이며, 중요한 연구 상태와 결정은 GitHub에 반영한다.

**English**  
This repository is the project's **official persistent system of record and source of truth**. GPT sessions are analytical workspaces for research, synthesis, hypothesis generation, experimentation, and critical review; material project state and decisions are persisted to GitHub.

## Language Rule / 언어 규칙

프로젝트의 향후 **사람이 읽는 모든 주요 연구·거버넌스·상태·Issue 산출물은 한국어와 영어를 병기**한다. 원천 데이터의 컬럼명, 코드, API 필드, 표준명, 고유명사는 정확성을 위해 원문을 보존한다. 자세한 규칙은 `docs/LANGUAGE_POLICY.md`를 따른다.  
All future **human-readable major research, governance, status, and Issue artifacts shall be maintained bilingually in Korean and English**. Native dataset fields, code, API keys, standards, and proper names remain in their authoritative original form for precision. See `docs/LANGUAGE_POLICY.md`.

## Current Baseline / 현재 베이스라인

**Baseline:** `v0.2-bilingual`  
**Current program:** Research-material landscape → `AMBENCH-001` calibration → Wave 1 US → Korea → EU.  
**현재 프로그램:** 연구 소재 탐색 → `AMBENCH-001` 보정 → Wave 1 미국 → 한국 → EU.
