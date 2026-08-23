---
id: AMBENCH-F22-AMENDMENT-02
type: classification-amendment
state: ACTIVE
created: 2026-08-23
source_of_truth: github
---

# AMBENCH-F22 Amendment 02 — All-Four Byte Integrity Ready, Header-Format Gate Unmet
# AMBENCH-F22 수정 02 — 4개 전체 byte 무결성 확보, header-format gate 미충족

## Why an amendment is required / 수정 필요 이유
The preregistered gates assumed the registered CSV files carried a textual 40-column header. Part 1 inspection established that the archive CSVs are headerless. No original gate exactly represents the observed combination:
- all four ZIP components are immutable-metadata qualified;
- all four ZIP bytes are locally SHA-256 verified;
- all four archives are valid and each contains exactly 250 CSVs with exact `L0001`–`L0250` filename coverage;
- but the frozen textual-header check is structurally inapplicable/unmet.

It would be misleading either to call full PASS or to call source access HOLD.

## Added descriptive gate / 추가 기술 gate
**`PARTIAL_F22_ALL_FOUR_IMMUTABLE_BYTES_READY__SCHEMA_HEADER_HOLD`**

This descriptive gate applies only when:
1. all four exact NERDm ZIP components have authoritative SHA-256 and NIST downloadURLs;
2. all four local ZIP SHA-256 values match exactly;
3. all four ZIPs validate structurally;
4. all four contain exactly 250 CSV members with deterministic layer filename coverage;
5. the frozen textual-header requirement is unmet because the CSV serialization is headerless;
6. no numerical experiment is authorized.

This gate does **not** weaken the original full PASS. `PASS_F22_REGISTERED_X4_IMMUTABLE_SOURCE_READY` remains failed because its header/schema condition was not met as written.

## Numerical-exposure state / numerical 노출 상태
`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED` remains in force from Amendment 01.

No additional CSV content lines were read during Parts 2–4 verification. The all-four byte/inventory result is therefore independent of further numerical outcome inspection.

## Consequence / 후속
- F22 can establish **all-four immutable source-byte readiness**.
- F22 cannot establish the preregistered textual-header schema condition.
- Do not model yet.
- Next work should be a separately preregistered **headerless serialization/schema mapping gate** using NIST AMS 100-69 as the authoritative 40-column semantic map, with numerical values suppressed and only structural field-count validation if needed.
