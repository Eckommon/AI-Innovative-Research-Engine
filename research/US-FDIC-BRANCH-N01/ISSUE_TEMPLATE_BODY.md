## Mission
Execute the outcome-blind matched-design contract frozen **before Issue creation** at commit `c0f9f412b88b4ff54fd9999ff57fc3c4be40f374` in `research/US-FDIC-BRANCH-N01/README.md`.

N01 must determine whether exact-`UNINUMBR` historical SOD 2022–2024 data support a deterministic matched design comparing within-bank/state branch deposit-network position trajectories, without opening any 2025 SOD row or future branch/event membership.

## Frozen design
- exact physical identity: `UNINUMBR` only;
- historical stable ownership required: same `CERT` in 2022–2024;
- strata: exact `CERT × STALPBR`, minimum n=8;
- exposure: bottom vs top quartile of `delta_log_share = ln(share_2024/share_2022)`;
- deterministic within-stratum matching on baseline 2022 share/deposit proximity;
- no name/address/ZIP/geospatial/fuzzy/manual identity repair;
- 2025 SOD and future BankFind event membership remain sealed;
- E01 remains unauthorized;
- incremental monetary cost = 0 USD.

## Frozen gate
All 18 N01 requirements must pass for:

`PASS_US_FDIC_BRANCH_N01_MATCHED_NETWORK_POSITION_TRAJECTORY_DESIGN_IDENTIFIABLE`

Otherwise a valid scientific design run terminates as:

`HOLD_US_FDIC_BRANCH_N01_MATCHED_NETWORK_POSITION_TRAJECTORY_DESIGN_NOT_IDENTIFIABLE`

Implementation/network/parser defects before a valid structural design run are not scientific HOLD and may be transparently corrected without changing the frozen contract.

A PASS authorizes only a separately activated E01 under the prospectively frozen future adjudication/paired-analysis section of the N01 contract.
