# Technical Adjudication — CA-GRAIN-E02 temporal identity

## Valid execution

Corrected Run `34689346777` supersedes the earlier invalid parser run and remains the valid E02 execution. It terminated before model fitting at **`HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL`**.

## Targeted provenance

Audit Run `34690867196` inspected no `Ktonnes` or dwell values. It found 120 matching structural rows at the collided normalized week: 60 components for each of two distinct 2024-25 source identities:

- Grain Week **44**, raw `08/06/2025`; official CGC week ending **2025-06-08**
- Grain Week **48**, raw `07/06/2025`; official CGC week ending **2025-07-06**

Thus the collision is a temporal-identity problem, not duplicated magnitude rows.

## Adjudication

Issue #110 froze explicit source-date normalization. After magnitude access was authorized, switching E02 to `grain_week`, dropping either identity, or selecting a slash-date interpretation would change the frozen design. No such repair is allowed. E02 is terminal HOLD.

Separate value-blind revalidation Run `34690978853` may correct historical F01/E01 structural counts because those gates did not depend on an effect estimate; it cannot rescue E02.

Incremental monetary cost: **0 USD**.
