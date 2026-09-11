#!/usr/bin/env python3
"""Search persisted USACE Lock Usage TOC identities for three unresolved names.
Identity-only; no outcome/hydrology magnitudes.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WATERWAY-F01'

def main():
    toc=json.loads((OUT/'USAGE_TOC_PREFLIGHT.json').read_text(encoding='utf-8'))
    names=toc['lock_identity_unique']
    needles=['PRICE','MELD','MYERS']
    hits={n:[x for x in names if n in x.upper()] for n in needles}
    out={'boundary':{'outcome_magnitudes_parsed':False,'hydrology_values_parsed':False},'needles':needles,'hits':hits,'incremental_monetary_cost_usd':0}
    (OUT/'NAMED_LOCK_ALIAS_DIAGNOSTIC.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    lines=['# US-WATERWAY-F01 Named Lock Alias Diagnostic','', 'Identity strings only; no magnitudes parsed.','']
    for n in needles: lines.append(f'- `{n}` → {hits[n]}')
    lines+=['','Incremental monetary cost: **0 USD**.']
    (OUT/'NAMED_LOCK_ALIAS_DIAGNOSTIC.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
if __name__=='__main__': main()
