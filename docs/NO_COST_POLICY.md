# COST-001 — No-Cost Execution Policy / 무비용 실행 규약

**State / 상태:** `MANDATORY`  
**Effective / 적용일:** 2026-08-22  
**Authority / 권위:** `docs/GOVERNANCE.md`, `registry/DECISION_LOG.md`

## 1. Default Rule / 기본 규칙

**KO:** 프로젝트의 모든 연구·검증·개발·자동화 작업은 기본적으로 **추가 금전비용(incremental monetary cost) 0원** 조건에서 수행한다. 비용이 발생하거나 발생할 합리적 가능성이 있는 작업은 실행 전에 사용자의 명시적 승인을 받아야 한다.  
**EN:** All project research, validation, development, and automation work defaults to **zero incremental monetary cost**. Any action that incurs, or has a reasonable possibility of incurring, monetary cost requires the user's explicit approval **before execution**.

## 2. Allowed Without Additional Approval / 추가 승인 없이 허용

The following are allowed only when they do not create incremental monetary charges: / 다음은 추가 금전비용을 만들지 않는 경우 허용한다.

- public web research and official public-data access / 공개 웹 조사·공식 공공데이터 접근;
- existing repository read/write operations through already connected GitHub/API tooling / 기존 연결 GitHub/API를 통한 저장소 읽기·쓰기;
- local or already-provided compute/storage that does not create a new charge / 신규 과금이 없는 로컬·기제공 compute/storage;
- reuse and inspection of already-created workflow artifacts, logs, and downloaded evidence / 이미 생성된 workflow artifact·log·증거 재사용·검사;
- open-source/free tools with no paid tier activation, paid token, or billable hosted resource required / 유료 tier·token·hosted resource를 요구하지 않는 OSS·무료도구.

## 3. Prior Approval Required / 사전승인 필수

Explicit user approval is required before any of the following if they can generate monetary cost: / 금전비용 가능성이 있으면 아래는 사용자 명시승인 전 실행 금지.

- paid APIs, datasets, subscriptions, SaaS, licenses, or marketplace fees / 유료 API·데이터·구독·SaaS·라이선스·마켓플레이스 비용;
- cloud compute, GPU, storage, database, hosting, domain, network egress, or managed-service charges / 클라우드 compute·GPU·storage·DB·hosting·domain·egress·managed service;
- GitHub Actions/CI or other metered automation when zero monetary overage cannot be established / 0원 과금 여부를 확립할 수 없는 GitHub Actions/CI·metered automation;
- purchases, paid trials requiring billing details, or any action that may auto-convert to paid usage / 구매·결제정보가 필요한 trial·자동유료전환 가능 작업;
- any third-party service whose billing state or remaining free allowance is unknown and whose execution may create a charge / billing/free allowance가 불명확하고 실행 시 과금될 수 있는 제3자 서비스.

## 4. Uncertainty Rule / 불확실성 규칙

If cost status cannot be verified confidently, classify the action as **`HOLD_COST_APPROVAL`** and do not execute it. / 비용 상태를 신뢰성 있게 검증할 수 없으면 **`HOLD_COST_APPROVAL`**로 두고 실행하지 않는다.

Before requesting approval, report when knowable: / 승인 요청 전 가능한 범위에서 다음을 제시한다.
- why the paid action is needed / 비용행동 필요 이유;
- expected or maximum cost / 예상·최대 비용;
- billing unit or quota consumed / 과금단위·소모 quota;
- no-cost alternatives already considered / 검토한 무비용 대안;
- decision impact if the action is not approved / 미승인 시 연구판단 영향.

## 5. No Silent Paid Substitution / 묵시적 유료대체 금지

A blocked no-cost route must not be silently replaced with a paid route. / 무비용 경로가 막혔다고 유료 경로로 임의 대체하지 않는다.

Research may instead end in `HOLD`, `PARTIAL`, or `INCONCLUSIVE` when evidence cannot be obtained under the no-cost boundary. / 무비용 경계에서 필요한 증거를 얻지 못하면 `HOLD`, `PARTIAL`, `INCONCLUSIVE`가 올바른 결과일 수 있다.

## 6. Automation-Specific Rule / 자동화 규칙

Do not trigger a new metered workflow merely for convenience when equivalent evidence can be recovered from existing artifacts, repository records, public official sources, or zero-cost local analysis. / 기존 artifact·저장소 기록·공식 공개출처·무비용 로컬분석으로 동등 근거를 확보할 수 있으면 편의를 위해 새로운 metered workflow를 실행하지 않는다.

Any active research Issue should inherit `COST-001` unless an explicitly approved exception is recorded. / 모든 활성 연구 Issue는 명시 승인된 예외가 없는 한 `COST-001`을 상속한다.

## 7. Recordkeeping / 기록

Approved paid exceptions, if any, must record scope, approval, expected cost, actual known cost, and the research object that required it. / 향후 유료 예외가 승인되면 범위·승인·예상비용·확인 가능한 실제비용·관련 연구객체를 기록한다.

Official artifacts comply with `LANG-001` and `COST-001`. / 공식 산출물은 관련 규약을 따른다.
