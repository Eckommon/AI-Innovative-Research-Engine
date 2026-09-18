---
id: US-IRS-EO-N01-RESULT
type: outcome-blind-design-identifiability-result
created: 2026-09-18
issue: 164
research: US-IRS-EO-N01
disposition: HOLD
failed_gate: 5
contract_commit: 70898f12e1b1fb2ad233aaf0a1cb13ff49d73fe8
gate: HOLD_US_IRS_EO_N01_MATCHED_GOVERNANCE_INDEPENDENCE_DESIGN_NOT_IDENTIFIABLE
---

# US-IRS-EO-N01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_IRS_EO_N01_MATCHED_GOVERNANCE_INDEPENDENCE_DESIGN_NOT_IDENTIFIABLE`**

N01 terminates outcome-blind at **Gate 5** before any historical organization-return row or Automatic Revocation membership is opened.

N01은 historical organization-return row나 Automatic Revocation membership을 열기 전에 **Gate 5**에서 outcome-blind terminal HOLD로 종료됩니다.

## Why Gate 5 fails / Gate 5 실패 이유

The frozen contract requires every baseline eligibility concept to have one deterministic official-IRS 2019 XML mapping. In particular, the selected Form 990 baseline return requires `ApplicationPendingInd` not to be true.

Official IRS 2019v5.1 redacted-schema inspection establishes:

- `ApplicationPendingInd`: **no declaration/reference anywhere in the scanned 2019v5.1 package**;
- `ApplicationPending`: declared as `CheckboxType` for **IRS990EZ** and **IRS990PF** only;
- no `ApplicationPending` declaration was found in `TEGE/TEGE990/IRS990/IRS990.xsd`;
- the 2019 paper Form 990 itself includes an “Application pending” checkbox, so silently treating the missing XML concept as false would be an unsupported semantic inference.

Therefore the frozen Form-990-only cohort cannot deterministically enforce all of its own eligibility criteria from the authorized 2019 XML source. Dropping the criterion, substituting a proxy, changing the source year, admitting 990-EZ/PF, or treating schema absence as false would alter the frozen design after Issue binding and is prohibited.

## Preserved evidence / 보존 증거

- contract: `70898f12e1b1fb2ad233aaf0a1cb13ff49d73fe8`
- source/schema preflight: `e5ef1b4e6415a4fcd59a692da5d6d37e8a10b00d`
- name/ref schema preflight: `75fc78558e2911b970a23db9e2da754f7c90434f`
- exact application-pending schema map: `114c673aa2ddce5feeefdd5d24efa308c7bad783`
- official 2019 schema SHA-256: `32bc81b2767da3caf4700bfb90d015f17c670aa73bc481e7ac65410d1f03b9d7`
- 2019 index endpoint HEAD: HTTP **200**
- nine historical XML ZIP endpoints HEAD: **9/9 HTTP 200**

## Firewall / 방화벽

- historical 2019 index data rows opened by N01: **0**
- historical organization XML return rows opened by N01: **0**
- Automatic Revocation data rows opened: **0**
- Automatic Revocation entity-body bytes consumed: **0**
- relationship computed: **false**
- predictive metric computed: **false**
- exposure/matching thresholds changed: **false**
- source year changed: **false**
- incremental monetary cost: **0 USD**

Because one valid frozen requirement already fails, gates requiring full historical row ingestion, cohort cardinality, quartiles, matching, balance, and pair-manifest construction are **not run**. This is terminal early-stop, not missing evidence to be rescued inside N01.

## Consequence / 후속 조치

No E01 is authorized. The 2019 Form-990 governance-independence design is not rescued. The next authorized project action is an independent **PORTFOLIO-R40** outcome-blind reselection that treats this N01 HOLD as negative evidence.

E01은 허가되지 않습니다. 본 2019 Form-990 governance-independence 설계는 구조 변경으로 구제하지 않습니다. 다음 허가 작업은 이 HOLD를 negative evidence로 보존한 독립 **PORTFOLIO-R40** reselection입니다.
