# US-BRIDGE-F01 implementation integrity note

## Superseded technical run

GitHub Actions Run `34790222911` completed successfully at the workflow level and wrote an outcome-blind `HOLD_US_BRIDGE_F01_SOURCE_OR_IDENTITY_SUPPORT` result. That result is **not** the terminal scientific disposition because the runner applied the duplicate-key fail-closed rule at the wrong scope.

The annual source manifest showed only 1–4 duplicate canonical bridge keys among roughly 612k–624k annual records, but v3 discarded the entire annual contribution whenever any duplicate existed. This collapsed repeated-support counts to zero.

## Corrected interpretation

The frozen contract states that duplicate canonical bridge keys fail closed. The corrected implementation applies that rule to the ambiguous **canonical key-year** only:

- duplicated canonical key-year: excluded;
- unrelated unique bridge keys in the same annual official source: retained;
- no fuzzy or outcome-dependent repair;
- no source, date window, threshold, FEMA hazard set, or gate definition changes.

This is an identity-layer implementation correction, not a post-result scientific rescue.

## Outcome-blind integrity

Across the superseded run and corrected rerun:

- NBI condition-rating values are not parsed, converted, summarized, persisted, ranked, or compared;
- bytes corresponding to legacy condition Items 58/59/60/62 are not sliced;
- no disaster-linked bridge-condition relationship is computed;
- raw source bytes remain transient;
- incremental monetary cost remains 0 USD.

The corrected rerun supersedes Run `34790222911` only for the F01 terminal gate. Git history preserves the earlier derived result and this note preserves the reason it is not treated as scientifically terminal.
