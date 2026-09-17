#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import tempfile
import urllib.request
import zipfile
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUTDIR=ROOT/'research'/'US-EPA-XMEDIA-E01'; OUT=OUTDIR/'STAGING_RESULT.json'
CONTRACT='46938afda3fbeaf9349a3c508502f8d4a3c973a3'
MANIFEST_SHA='19e1b3a1963fe008811aa230336e12ec69a348b03cf37bd656ea9d3fba8e5aaf'
STATES=('AL','AR','CA','FL','GA','IN','KY','MD','MI','MO','MS','NC','NJ','NV','OH','OR','PA','SC','TN','TX','WI','WV')
BASE='https://echo.epa.gov/files/echodownloads/NPDES_by_state_year/{state}_NPDES_EFF_VIOLATIONS.zip'
G_POS='PASS_POSITIVE_MATERIAL_US_EPA_XMEDIA_E01_RELATIONSHIP'
G_SMALL='POSITIVE_BELOW_MATERIALITY_US_EPA_XMEDIA_E01_RELATIONSHIP'
G_NULL='NO_PREREGISTERED_POSITIVE_US_EPA_XMEDIA_E01_RELATIONSHIP'
REQ={'NPDES_ID','NPDES_VIOLATION_ID','VIOLATION_CODE','MONITORING_PERIOD_END_DATE'}


def norm(v): return (v or '').strip()

def canonical_sha(obj):
    raw=json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def parse_date(s):
    s=norm(s)
    if not s: return None
    for fmt in ('%m/%d/%Y','%Y-%m-%d','%d-%b-%Y','%d-%b-%y','%m/%d/%y','%Y%m%d'):
        try:
            d=datetime.strptime(s,fmt).date()
            return d if 1900<=d.year<=2100 else None
        except ValueError: pass
    return None

def download(url,dest):
    req=urllib.request.Request(url,headers={'User-Agent':'AI-Innovative-Research-Engine/US-EPA-XMEDIA-E01'})
    h=hashlib.sha256(); n=0
    with urllib.request.urlopen(req,timeout=240) as r, dest.open('wb') as f:
        while True:
            b=r.read(1024*1024)
            if not b: break
            f.write(b); h.update(b); n+=len(b)
    return n,h.hexdigest()
def member_for(z):
    ms=[n for n in z.namelist() if n.upper().endswith('.CSV') and 'NPDES_EFF_VIOLATIONS' in Path(n).name.upper()]
    if len(ms)!=1: raise RuntimeError(f'exactly one effluent violations CSV required: {ms}')
    return ms[0]
def exact_binom_two_sided(b,c):
    n=b+c
    if n==0: return 1.0
    k=min(b,c)
    tail=sum(math.comb(n,i) for i in range(k+1))/(2**n)
    return min(1.0,2.0*tail)

def main():
    assert not OUT.exists(),'immutable E01 staging already exists'
    cp=json.loads((ROOT/'context/checkpoint.json').read_text())
    assert cp=={'checkpoint_id':'CHK-20260917-US-EPA-XMEDIA-E01-ACTIVE','active_issue':152,'active_research':'US-EPA-XMEDIA-E01','last_completed_issue':151,'last_completed_research':'US-EPA-XMEDIA-N01','last_decision':'DEC-216','updated':'2026-09-17'}
    m=json.loads((ROOT/'research/US-EPA-XMEDIA-N01/DESIGN_MANIFEST.json').read_text())
    core={k:v for k,v in m.items() if k!='canonical_core_sha256'}
    assert canonical_sha(core)==MANIFEST_SHA==m['canonical_core_sha256']
    assert len(m['pairs'])==307 and m['outcome_membership_included'] is False

    frozen_ids=set(); id_state={}
    for p in m['pairs']:
        h,l=p['high'],p['low']
        assert h['exposure_eval_count']>l['exposure_eval_count']
        for u in (h,l):
            pid=u['npdes_id']; st=u['state_code']
            assert st in STATES
            assert pid not in frozen_ids
            frozen_ids.add(pid); id_state[pid]=st
    assert len(frozen_ids)==614 and set(id_state.values())==set(STATES)

    positive_ids=set(); source_meta={}; total_rows=0; matched_rows=0; malformed_candidate_dates=0
    required_schema_all=True
    with tempfile.TemporaryDirectory(prefix='epa-xmedia-e01-') as td0:
        td=Path(td0)
        for st in STATES:
            url=BASE.format(state=st); p=td/f'{st}.zip'
            n,digest=download(url,p)
            if not zipfile.is_zipfile(p): raise RuntimeError(f'not zip: {st}')
            state_rows=state_matched=state_e90_2024=0
            with zipfile.ZipFile(p) as z:
                member=member_for(z)
                raw=z.open(member,'r'); text=io.TextIOWrapper(raw,encoding='utf-8-sig',errors='replace',newline='')
                reader=csv.DictReader(text); fields={norm(x) for x in (reader.fieldnames or [])}
                schema_ok=REQ<=fields; required_schema_all &= schema_ok
                if not schema_ok: raise RuntimeError(f'{st} missing required fields: {sorted(REQ-fields)}')
                for row in reader:
                    state_rows+=1
                    pid=norm(row.get('NPDES_ID'))
                    if pid not in frozen_ids or id_state[pid]!=st: continue
                    state_matched+=1
                    if norm(row.get('VIOLATION_CODE')).upper()!='E90': continue
                    vid=norm(row.get('NPDES_VIOLATION_ID'))
                    ds=norm(row.get('MONITORING_PERIOD_END_DATE'))
                    if not vid: continue
                    d=parse_date(ds)
                    if d is None:
                        if ds: malformed_candidate_dates+=1
                        continue
                    if d.year==2024:
                        positive_ids.add(pid); state_e90_2024+=1
            total_rows+=state_rows; matched_rows+=state_matched
            source_meta[st]={'url':url,'bytes':n,'sha256':digest,'member':Path(member).name,'rows_scanned':state_rows}

    hh=hl=lh=ll=0
    high_y=low_y=0
    for p in m['pairs']:
        yh=int(p['high']['npdes_id'] in positive_ids); yl=int(p['low']['npdes_id'] in positive_ids)
        high_y+=yh; low_y+=yl
        if yh and yl: hh+=1
        elif yh and not yl: hl+=1
        elif not yh and yl: lh+=1
        else: ll+=1
    n=len(m['pairs']); risk_h=high_y/n; risk_l=low_y/n; rd=risk_h-risk_l
    b,c=hl,lh; pval=exact_binom_two_sided(b,c)
    if rd>=0.05 and pval<0.05 and b>c: gate=G_POS
    elif 0<rd<0.05 and pval<0.05 and b>c: gate=G_SMALL
    else: gate=G_NULL

    result={
      'research':'US-EPA-XMEDIA-E01','issue':152,'contract_commit':CONTRACT,
      'activation_decision':'DEC-216','n01_staging_commit':'78f0f0f1458463c79c326c016d415dc5533af026',
      'n01_manifest_sha256':MANIFEST_SHA,'generated_utc':datetime.utcnow().replace(microsecond=0).isoformat()+'Z',
      'source_scope':{'states':list(STATES),'state_count':len(STATES),'source_table':'NPDES_EFF_VIOLATIONS','required_fields':sorted(REQ)},
      'source_fingerprints':source_meta,
      'integrity':{'frozen_pairs':307,'frozen_npdes_ids':614,'required_schema_all_states':required_schema_all,'total_source_rows_scanned':total_rows,'rows_for_frozen_ids':matched_rows,'malformed_nonblank_candidate_e90_dates_excluded':malformed_candidate_dates,'facility_level_outcome_labels_persisted':False,'pair_membership_changed':False,'endpoint_changed':False,'window_changed':False,'threshold_changed':False},
      'primary':{'high_event_facilities':high_y,'low_event_facilities':low_y,'risk_high':risk_h,'risk_low':risk_l,'risk_difference':rd,'both_event':hh,'b_high1_low0':b,'c_high0_low1':c,'neither_event':ll,'discordant_pairs':b+c,'exact_two_sided_mcnemar_binomial_p':pval,'materiality_floor':0.05},
      'gate':gate,
      'interpretation_boundary':{'observational_noncausal':True,'negative_estimate_not_protective_claim':True,'facility_ranking_computed':False,'enforcement_targeting_score_computed':False,'secondary_endpoint_computed':False,'dmr_values_or_limits_opened':False,'rcra_outcomes_opened':False},
      'incremental_monetary_cost_usd':0,
    }
    OUTDIR.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'gate':gate,'n':n,'risk_high':risk_h,'risk_low':risk_l,'rd':rd,'b':b,'c':c,'p':pval},sort_keys=True))
if __name__=='__main__': main()
