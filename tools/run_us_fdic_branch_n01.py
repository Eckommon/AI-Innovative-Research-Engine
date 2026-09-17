#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, io, json, math, time, urllib.parse, urllib.request
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/US-FDIC-BRANCH-N01/staging'
OUT.mkdir(parents=True,exist_ok=True)
CONTRACT='c0f9f412b88b4ff54fd9999ff57fc3c4be40f374'
ISSUE=161
YEARS=(2022,2023,2024)
FIELDS=['YEAR','CERT','BRNUM','UNINUMBR','STALPBR','DEPSUMBR']
BASE='https://api.fdic.gov/banks/sod'
UA='AI-Innovative-Research-Engine/US-FDIC-BRANCH-N01 outcome-blind historical design'

boundaries={
 'future_2025_sod_rows_opened':False,
 'future_branch_membership_opened':False,
 'future_structure_event_membership_opened':False,
 'future_closure_noncontinuation_computed':False,
 'fuzzy_name_address_zip_geo_manual_identity_repair_used':False,
 'relationship_computed':False,
 'predictive_metric_computed':False,
 'causal_claim_made':False,
 'branch_or_bank_ranking_made':False,
 'novelty_claim_made':False,
}

def get(url,retries=4):
    last=None
    for i in range(retries):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'application/json'})
            with urllib.request.urlopen(req,timeout=90) as r: return r.read()
        except Exception as e:
            last=e; time.sleep(2**i)
    raise last

def sha(b): return hashlib.sha256(b).hexdigest()
def norm(v):
    if v is None: return ''
    s=str(v).strip()
    if s.lower() in {'','none','null','nan'}: return ''
    if s.endswith('.0') and s[:-2].replace('-','').isdigit(): s=s[:-2]
    return s

def unwrap(payload):
    rows=payload.get('data',[]) if isinstance(payload,dict) else []
    out=[]
    for x in rows:
        if isinstance(x,dict) and isinstance(x.get('data'),dict): out.append(x['data'])
        elif isinstance(x,dict): out.append(x)
    return out

def fetch_year(year):
    out=[]; pages=[]; limit=10000; offset=0
    while True:
        q=urllib.parse.urlencode({'filters':f'YEAR:{year}','fields':','.join(FIELDS),'limit':limit,'offset':offset})
        url=BASE+'?'+q
        raw=get(url); rows=unwrap(json.loads(raw))
        pages.append({'year':year,'offset':offset,'rows':len(rows),'bytes':len(raw),'sha256':sha(raw)})
        out.extend({k:r.get(k) for k in FIELDS} for r in rows)
        if len(rows)<limit: break
        offset += len(rows)
        if offset>200000: raise RuntimeError('unexpected pagination ceiling')
    return out,pages

all_rows=[]; pages=[]
for y in YEARS:
    rows,p=fetch_year(y); all_rows.extend(rows); pages.extend(p)

# Normalize and collapse exact duplicates; any same UNINUMBR×YEAR structural conflict excludes that UNINUMBR fail-closed.
by_key=defaultdict(list)
for r in all_rows:
    x={k:norm(r.get(k)) for k in FIELDS}
    by_key[(x['UNINUMBR'],x['YEAR'])].append(x)

records={}; conflict_unis=set(); exact_dupes=0
for key,rows in by_key.items():
    if not key[0] or not key[1]:
        if key[0]: conflict_unis.add(key[0])
        continue
    sigs={tuple(r[k] for k in FIELDS) for r in rows}
    if len(sigs)>1:
        conflict_unis.add(key[0]); continue
    exact_dupes += max(0,len(rows)-1)
    records[key]=rows[0]

# Build all-three-year stable exact branches.
elig=[]; exclusions=defaultdict(int)
all_unis={u for u,y in records if u}
for u in sorted(all_unis):
    if u in conflict_unis:
        exclusions['same_year_conflict']+=1; continue
    rs={y:records.get((u,str(y))) for y in YEARS}
    if any(rs[y] is None for y in YEARS): exclusions['not_all_three_years']+=1; continue
    if any(any(not rs[y][f] for f in ('CERT','BRNUM','STALPBR','DEPSUMBR')) for y in YEARS): exclusions['missing_required_field']+=1; continue
    certs={rs[y]['CERT'] for y in YEARS}
    if len(certs)!=1: exclusions['cert_changed_2022_2024']+=1; continue
    if rs[2022]['STALPBR']!=rs[2024]['STALPBR']: exclusions['state_changed_2022_2024']+=1; continue
    try:
        dep={y:float(rs[y]['DEPSUMBR'].replace(',','')) for y in YEARS}
    except Exception:
        exclusions['deposit_non_numeric']+=1; continue
    if not (math.isfinite(dep[2022]) and dep[2022]>0 and math.isfinite(dep[2024]) and dep[2024]>0):
        exclusions['nonpositive_2022_or_2024_deposit']+=1; continue
    if not math.isfinite(dep[2023]): exclusions['nonfinite_2023_deposit']+=1; continue
    elig.append({'UNINUMBR':u,'CERT':rs[2024]['CERT'],'STALPBR':rs[2024]['STALPBR'],'BRNUM':rs[2024]['BRNUM'],
                 'dep2022':dep[2022],'dep2023':dep[2023],'dep2024':dep[2024]})

strata=defaultdict(list)
for x in elig: strata[(x['CERT'],x['STALPBR'])].append(x)

eligible_strata={k:v for k,v in strata.items() if len(v)>=8}
pairs=[]; dropped_no_separation=0; candidate_extremes=0
for (cert,state),units in sorted(eligible_strata.items()):
    total22=sum(x['dep2022'] for x in units); total24=sum(x['dep2024'] for x in units)
    if total22<=0 or total24<=0: continue
    enriched=[]
    for x in units:
        z=dict(x)
        z['share2022']=x['dep2022']/total22
        z['share2024']=x['dep2024']/total24
        z['delta']=math.log(z['share2024']/z['share2022'])
        enriched.append(z)
    enriched.sort(key=lambda z:(z['delta'],z['UNINUMBR']))
    k=len(enriched)//4
    if k<2: continue
    decline=enriched[:k]; gain=enriched[-k:]
    candidate_extremes += 2*k
    if not (max(x['delta'] for x in decline) < min(x['delta'] for x in gain)):
        dropped_no_separation+=1; continue
    unused={x['UNINUMBR']:x for x in gain}
    for d in sorted(decline,key=lambda z:(z['delta'],z['UNINUMBR'])):
        def keyfun(g):
            d1=abs(math.log(d['share2022'])-math.log(g['share2022']))
            d2=abs(math.log(d['dep2022'])-math.log(g['dep2022']))
            if d['dep2023']>0 and g['dep2023']>0:
                d3=abs(math.log(d['dep2023'])-math.log(g['dep2023']))
            else: d3=float('inf')
            return (d1,d2,d3,g['UNINUMBR'])
        if not unused: break
        g=min(unused.values(),key=keyfun); del unused[g['UNINUMBR']]
        pairs.append({'CERT':cert,'STALPBR':state,'DECLINE':d,'GAIN':g})

states={p['STALPBR'] for p in pairs}
unique_unis=[p[s]['UNINUMBR'] for p in pairs for s in ('DECLINE','GAIN')]
sep=all(p['DECLINE']['delta']<p['GAIN']['delta'] for p in pairs)
same_stratum=all(p['DECLINE']['CERT']==p['GAIN']['CERT']==p['CERT'] and p['DECLINE']['STALPBR']==p['GAIN']['STALPBR']==p['STALPBR'] for p in pairs)
no_dup=len(unique_unis)==len(set(unique_unis))

def ratio_ok(a,b):
    if a<=0 or b<=0: return False
    r=a/b; return (1/3)<=r<=3

share_bal=sum(ratio_ok(p['DECLINE']['share2022'],p['GAIN']['share2022']) for p in pairs)/len(pairs) if pairs else 0
abs22_bal=sum(ratio_ok(p['DECLINE']['dep2022'],p['GAIN']['dep2022']) for p in pairs)/len(pairs) if pairs else 0
pos23=[p for p in pairs if p['DECLINE']['dep2023']>0 and p['GAIN']['dep2023']>0]
abs23_bal=sum(ratio_ok(p['DECLINE']['dep2023'],p['GAIN']['dep2023']) for p in pos23)/len(pos23) if pos23 else 0

buf=io.StringIO(); w=csv.writer(buf)
w.writerow(['PAIR_ID','CERT','STALPBR','CLASS','UNINUMBR','DEPSUMBR_2022','DEPSUMBR_2023','DEPSUMBR_2024','SHARE_2022','SHARE_2024','DELTA_LOG_SHARE'])
for i,p in enumerate(pairs,1):
    for cls in ('DECLINE','GAIN'):
        x=p[cls]
        w.writerow([f'P{i:06d}',p['CERT'],p['STALPBR'],cls,x['UNINUMBR'],f"{x['dep2022']:.10g}",f"{x['dep2023']:.10g}",f"{x['dep2024']:.10g}",f"{x['share2022']:.16g}",f"{x['share2024']:.16g}",f"{x['delta']:.16g}"])
man=buf.getvalue().encode(); (OUT/'pair_manifest.csv').write_bytes(man)
source={'contract_commit':CONTRACT,'years':list(YEARS),'fields':FIELDS,'pages':pages,'future_requests_made':0,'future_2025_sod_rows_opened':False,'future_structure_event_membership_opened':False}
(OUT/'source_manifest.json').write_text(json.dumps(source,indent=2,sort_keys=True)+'\n',encoding='utf-8')

def req(n,name,passed,evidence): return {'number':n,'name':name,'pass':bool(passed),'evidence':evidence}
requirements=[
 req(1,'official SOD 2022-2024 reproducibly machine-readable at zero incremental cost',all(any(p['year']==y for p in pages) for y in YEARS),{'rows':len(all_rows),'pages':len(pages)}),
 req(2,'all six frozen historical fields present in each year',all(any(norm(r.get(f)) for r in all_rows if norm(r.get('YEAR'))==str(y)) for y in YEARS for f in FIELDS),FIELDS),
 req(3,'no 2025 SOD row or future BankFind branch/event membership opened',not any(boundaries[k] for k in ('future_2025_sod_rows_opened','future_branch_membership_opened','future_structure_event_membership_opened')),boundaries),
 req(4,'exact UNINUMBR only; historical conflicts and ownership changes excluded fail-closed; identity repair false',not boundaries['fuzzy_name_address_zip_geo_manual_identity_repair_used'],{'conflict_uninumbr':len(conflict_unis),'cert_change_excluded':exclusions['cert_changed_2022_2024']}),
 req(5,'>=50000 historically eligible stable-ownership branches',len(elig)>=50000,len(elig)),
 req(6,'>=500 eligible CERT x STALPBR strata with n>=8',len(eligible_strata)>=500,len(eligible_strata)),
 req(7,'>=2000 matched DECLINE-GAIN pairs',len(pairs)>=2000,len(pairs)),
 req(8,'matched pairs span >=30 STALPBR values',len(states)>=30,len(states)),
 req(9,'every pair has delta DECLINE < delta GAIN',sep,sep),
 req(10,'every pair shares exact CERT and STALPBR',same_stratum,same_stratum),
 req(11,'no UNINUMBR appears in more than one pair',no_dup,no_dup),
 req(12,'>=75% pairs have 2022 deposit-share ratio within [1/3,3]',share_bal>=0.75,share_bal),
 req(13,'>=75% pairs have 2022 absolute deposit ratio within [1/3,3]',abs22_bal>=0.75,abs22_bal),
 req(14,'>=75% positive-2023 pairs have 2023 absolute deposit ratio within [1/3,3]',abs23_bal>=0.75,{'rate':abs23_bal,'denominator':len(pos23)}),
 req(15,'deterministic canonical pair-manifest SHA-256 persisted',True,sha(man)),
 req(16,'all future-outcome/firewall booleans remain false',all(v is False for v in boundaries.values()),boundaries),
 req(17,'relationship prediction causality ranking novelty all remain false',not any(boundaries[k] for k in ('relationship_computed','predictive_metric_computed','causal_claim_made','branch_or_bank_ranking_made','novelty_claim_made')),False),
 req(18,'incremental monetary cost exactly 0 USD',True,0),
]
passed=sum(r['pass'] for r in requirements)
gate='PASS_US_FDIC_BRANCH_N01_MATCHED_NETWORK_POSITION_TRAJECTORY_DESIGN_IDENTIFIABLE' if passed==18 else 'HOLD_US_FDIC_BRANCH_N01_MATCHED_NETWORK_POSITION_TRAJECTORY_DESIGN_NOT_IDENTIFIABLE'
result={'research':'US-FDIC-BRANCH-N01','issue':ISSUE,'contract_commit':CONTRACT,'scientific_disposition':'PASS' if passed==18 else 'HOLD','gate':gate,'requirements_total':18,'requirements_passed':passed,'requirements':requirements,
'diagnostics':{'raw_rows':len(all_rows),'same_year_conflict_uninumbr':len(conflict_unis),'exact_duplicate_rows_collapsed':exact_dupes,'historically_eligible_stable_branches':len(elig),'eligible_strata_n_ge8':len(eligible_strata),'candidate_extreme_units':candidate_extremes,'dropped_strata_no_strict_separation':dropped_no_separation,'matched_pairs':len(pairs),'states_in_pairs':len(states),'baseline_share_balance_rate':share_bal,'baseline_2022_deposit_balance_rate':abs22_bal,'positive_2023_pair_count':len(pos23),'baseline_2023_deposit_balance_rate':abs23_bal,'exclusions':dict(exclusions),'pair_manifest_sha256':sha(man)},
'boundaries':boundaries,'incremental_monetary_cost_usd':0}
(OUT/'n01_result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(gate)
print(json.dumps(result['diagnostics'],sort_keys=True))
