# AMBENCH-E27 Amendment 01 — Encoding-only schema-preflight repair / Encoding 전용 schema preflight 보정

## Trigger / 발생
The first preregistered schema preflight verified the frozen primary component identity, NERDm size and SHA-256, then failed before header/schema inspection with `UnicodeDecodeError` because the CSV was not decodable as UTF-8-sig.

## Integrity / 무결성
- primary component identity: PASS;
- local SHA-256 match: PASS;
- numerical outcome values emitted/read for analysis: NO;
- endpoint, location, groups, hypothesis, statistic and gates: UNCHANGED.

## Amendment / 보정
Permit deterministic text-encoding detection/selection for schema parsing only:
1. detect BOM when present;
2. otherwise try a fixed non-outcome-driven encoding order (`utf-8-sig`, `utf-16`, `cp1252`, `latin-1`);
3. select the first encoding that decodes the complete file and yields a CSV header;
4. report encoding/header/identifier coverage only during preflight;
5. do not emit numerical outcome cells.

Each frozen component is handled independently so a sensitivity decoding issue cannot erase an already verified primary metadata result.

This amendment repairs serialization handling only and does not authorize any scientific redesign or outcome-driven choice.