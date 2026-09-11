#!/usr/bin/env python3
"""Inspect only string cells in the USACE Public Lock Usage workbook TOC.
No numeric delay, processing, hydrology, or relationship values are read/persisted.
"""
from __future__ import annotations
import hashlib, io, json, time, urllib.request
from pathlib import Path
from openpyxl import load_workbook

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WATERWAY-F01'
URL='https://usace.contentdm.oclc.org/utils/getfile/collection/p16021coll2/id/2958/filename/2959.xlsx'
UA='AI-Innovative-Research-Engine/US-WATERWAY-F01-toc-preflight'

def get(url):
    last=None
    for i in range(4):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':UA})
            with urllib.request.urlopen(req,timeout=120) as r:
                return r.read(),getattr(r,'status',200),r.geturl()
        except Exception as e:
            last=e; time.sleep(2*(i+1))
    raise last

def main():
    b,status,final=get(URL)
    wb=load_workbook(io.BytesIO(b),read_only=True,data_only=False)
    ws=wb['TOC']
    rows=[]
    strings=[]
    for r_idx,row in enumerate(ws.iter_rows(),start=1):
        vals=[]
        for c_idx,cell in enumerate(row,start=1):
            v=cell.value
            if isinstance(v,str) and v.strip():
                s=v.strip(); vals.append({'col':c_idx,'text':s}); strings.append(s)
        if vals: rows.append({'row':r_idx,'cells':vals})
    wb.close()
    # Structural identity estimate from TOC rows: rows containing at least one hyperlink target or named lock-like text
    # We do not infer from numeric cells.
    lock_like=[]
    stop={'Lock','Locks','Waterway','Table of Contents - Locks by Waterway'}
    for rec in rows:
        for c in rec['cells']:
            s=c['text']; u=s.upper()
            if s in stop: continue
            if any(tok in u for tok in ['LOCK','L/D','L & D','LOCKS & DAM','LOCK & DAM']) and len(s)<=120:
                lock_like.append(s)
    out={
      'boundary':{'numeric_outcome_cells_read':False,'delay_magnitudes_parsed':False,'hydrology_magnitudes_parsed':False,'relationship_computed':False},
      'url':URL,'http':status,'final_url':final,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
      'toc_sheet':'TOC','nonempty_string_rows':len(rows),'toc_rows_string_cells':rows,
      'lock_like_unique_strings':sorted(set(lock_like)),'lock_like_unique_count':len(set(lock_like)),
      'incremental_monetary_cost_usd':0
    }
    (OUT/'USAGE_TOC_PREFLIGHT.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
    md=['# US-WATERWAY-F01 Lock Usage TOC Identity Preflight','', 'String-cell only; no numeric outcome magnitudes read.', '',f'- HTTP: **{status}**',f'- bytes: **{len(b)}**',f'- SHA-256: `{out["sha256"]}`',f'- TOC nonempty string rows: **{len(rows)}**',f'- unique lock-like identity strings: **{len(set(lock_like))}**','', '## Lock-like identity strings']
    md += [f'- {x}' for x in sorted(set(lock_like))]
    md += ['', 'This is an identity-only diagnostic, not an effect analysis.', '', 'Incremental monetary cost: **0 USD**.']
    (OUT/'USAGE_TOC_PREFLIGHT.md').write_text('\n'.join(md)+'\n',encoding='utf-8')

if __name__=='__main__': main()
