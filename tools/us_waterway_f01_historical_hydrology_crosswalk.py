#!/usr/bin/env python3
"""Deterministic identity-only crosswalk for US-WATERWAY-F01.

Uses already persisted outcome-blind artifacts only. It does not fetch or parse
any delay, processing-time, or hydrology observation magnitude.
"""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WATERWAY-F01'


def norm(s:str)->str:
    s=str(s or '').upper().replace('&',' AND ')
    s=re.sub(r'\bL\s*/\s*D\b',' LOCK AND DAM ',s)
    s=re.sub(r'[^A-Z0-9]+',' ',s)
    s=re.sub(r'\s+',' ',s).strip()
    return s


def stripped_name(name:str)->str:
    toks=[t for t in norm(name).split() if t not in {'LOCK','LOCKS','DAM','AND'}]
    return ' '.join(toks)


def candidates(name:str,river:str):
    n=norm(name); r=norm(river)
    out={n,stripped_name(name)}
    nums=re.findall(r'\b(\d+[A-Z]?)\b',n)
    if nums:
        # USACE TOC convention for numbered river locks: "N RIVER".
        out.add(f'{nums[-1]} {r}')
    # common title words retained but structural LOCK/DAM wording removed.
    out.add(norm(re.sub(r'\b(?:LOCKS?|DAM|L/D)\b',' ',name,flags=re.I)))
    return {x for x in out if x}


def main():
    toc=json.loads((OUT/'USAGE_TOC_PREFLIGHT.json').read_text(encoding='utf-8'))
    hyd=json.loads((OUT/'HYDROLOGY_METADATA_PREFLIGHT_V2.json').read_text(encoding='utf-8'))
    toc_names=toc['lock_identity_unique']
    toc_norm={norm(x):x for x in toc_names}
    rows=[]
    for m in hyd['matches']:
        cands=sorted(candidates(m['lock_name'],m['river']))
        hits=[c for c in cands if c in toc_norm]
        rows.append({
          'lock_id':m['lock_id'],'lock_name':m['lock_name'],'river':m['river'],
          'usgs_id':m['usgs_id'],'candidate_keys':cands,
          'matched':bool(hits),'matched_key':hits[0] if hits else '',
          'toc_lock':toc_norm[hits[0]] if hits else '',
          'hydrology_interval':hyd['target_overlap'],
        })
    matched=[r for r in rows if r['matched']]
    out={
      'boundary':{'delay_magnitudes_parsed':False,'hydrology_values_parsed':False,'relationship_computed':False},
      'rule':'exact normalized name after structural LOCK/DAM token removal OR numbered-lock key <number> <river>; no fuzzy distance/name matching',
      'toc_lock_count':len(toc_names),'hydrology_qualified_count':len(hyd['matches']),
      'crosswalk_matched_count':len(matched),'crosswalk_unmatched_count':len(rows)-len(matched),
      'target_overlap':hyd['target_overlap'],'rows':rows,'incremental_monetary_cost_usd':0
    }
    (OUT/'HISTORICAL_HYDROLOGY_CROSSWALK.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
    md=['# US-WATERWAY-F01 Historical Lock ↔ USGS Crosswalk','',
        'Outcome-blind identity crosswalk only. No delay or hydrology magnitudes parsed.','',
        f'- archive TOC lock identities: **{len(toc_names)}**',
        f'- USGS-qualified locks: **{len(hyd["matches"])}**',
        f'- deterministically crosswalked to historical Lock Usage identities: **{len(matched)}**',
        f'- unmatched: **{len(rows)-len(matched)}**',
        f'- USGS metadata overlap: **{hyd["target_overlap"][0]}–{hyd["target_overlap"][1]}**','',
        'Rule: exact normalized name after removing structural LOCK/DAM wording, or numbered-lock key `<number> <river>`; no fuzzy name matching.','',
        '## Crosswalk']
    for r in rows:
        md.append(f"- `{r['lock_id']}` {r['lock_name']} / {r['river']} → {r['toc_lock'] or 'UNMATCHED'} → {r['usgs_id']} — {'PASS' if r['matched'] else 'NO_MATCH'}")
    md += ['', 'Incremental monetary cost: **0 USD**.']
    (OUT/'HISTORICAL_HYDROLOGY_CROSSWALK.md').write_text('\n'.join(md)+'\n',encoding='utf-8')

if __name__=='__main__': main()
