#!/usr/bin/env python3
from __future__ import annotations

import csv, hashlib, io, json, math, re, urllib.request, zipfile
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'CA-GRAIN-E02'; OUT.mkdir(parents=True,exist_ok=True)
TC_URL='https://tdih-cdit.tc.canada.ca/sites/default/files/ferroviaire-rail.zip'
GSW_URLS={
 '2023-24':'https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2023-24/gsw-shg-en.csv',
 '2024-25':'https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2024-25/gsw-shg-en.csv'}
START=date(2023,8,1); END=date(2025,7,31)
GRAINS=('Amber Durum','Barley','Beans','Canaryseed','Canola','Chick Peas','Corn','Flaxseed','Lentils','Mustard Seed','Oats','Peas','Rye','Soybeans','Wheat')
REGIONS=('Alberta','British Columbia','Manitoba','Saskatchewan')
CARRIERS=('CN','CPKC'); COMPONENTS={(g,r) for g in GRAINS for r in REGIONS}
MIN_N=75; HAC_LAG=2; MATERIALITY=1.0
UA='AI-Innovative-Research-Engine/CA-GRAIN-E02 date-corrected preregistered runner'
INITIAL_INVALID_RUN=34689155367
OFFICIAL_CALENDAR='https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/archived.html'

def fetch(url):
 req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'*/*'})
 with urllib.request.urlopen(req,timeout=120) as r:
  b=r.read(); return b,{'requested_url':url,'final_url':r.geturl(),'status':getattr(r,'status',200),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'content_type':r.headers.get('Content-Type')}

def decode(b):
 for enc in ('utf-8-sig','utf-8','cp1252','latin-1'):
  try:return b.decode(enc)
  except UnicodeDecodeError:pass
 raise RuntimeError('decode failure')

def norm(s):return re.sub(r'\s+',' ',(s or '').strip()).casefold()
def hnorm(s):return re.sub(r'[_\-\s]+',' ',(s or '').strip()).casefold()
def header(headers,*names):
 m={hnorm(h):h for h in headers}
 for n in names:
  if hnorm(n) in m:return m[hnorm(n)]
 return None

def gsw_date(raw):
 s=(raw or '').strip()
 for fmt in ('%Y-%m-%d','%Y/%m/%d','%d/%m/%Y'):
  try:return datetime.strptime(s,fmt).date()
  except ValueError:pass
 return None

def tc_date(raw):
 s=(raw or '').strip()
 if re.match(r'^20\d\d-\d\d-\d\d',s):s=s[:10]
 for fmt in ('%Y-%m-%d','%Y/%m/%d','%d/%m/%Y'):
  try:return datetime.strptime(s,fmt).date()
  except ValueError:pass
 return None

def monday(d):return d-timedelta(days=d.weekday())
def number(raw):
 s=(raw or '').strip().replace(',','')
 if not s:raise ValueError('blank numeric value')
 x=float(s)
 if not math.isfinite(x):raise ValueError('nonfinite numeric value')
 return x

def inv2(a,b,c,d):
 det=a*d-b*c
 if abs(det)<1e-15:raise RuntimeError('singular XTX')
 return ((d/det,-b/det),(-c/det,a/det))
def mm(A,B):return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]),(A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]))

def fit(x,y):
 n=len(x); sx=sum(x); sy=sum(y); sxx=sum(v*v for v in x); sxy=sum(a*b for a,b in zip(x,y))
 inv=inv2(n,sx,sx,sxx); alpha=inv[0][0]*sy+inv[0][1]*sxy; beta=inv[1][0]*sy+inv[1][1]*sxy
 u=[yy-alpha-beta*xx for xx,yy in zip(x,y)]; z=[(1.,xx) for xx in x]
 S=[[0.,0.],[0.,0.]]
 for t in range(n):
  q=u[t]*u[t]; a=z[t]
  S[0][0]+=q*a[0]*a[0]; S[0][1]+=q*a[0]*a[1]; S[1][0]+=q*a[1]*a[0]; S[1][1]+=q*a[1]*a[1]
 for ell in range(1,HAC_LAG+1):
  w=1-ell/(HAC_LAG+1)
  for t in range(ell,n):
   q=w*u[t]*u[t-ell]; a=z[t]; b=z[t-ell]
   S[0][0]+=q*(a[0]*b[0]+b[0]*a[0]); S[0][1]+=q*(a[0]*b[1]+b[0]*a[1]); S[1][0]+=q*(a[1]*b[0]+b[1]*a[0]); S[1][1]+=q*(a[1]*b[1]+b[1]*a[1])
 cov=mm(mm(inv,(tuple(S[0]),tuple(S[1]))),inv); fsc=n/(n-2)
 vb=cov[1][1]*fsc
 if vb < -1e-12:raise RuntimeError('negative HAC variance')
 se=math.sqrt(max(vb,0.)); zstat=beta/se if se else (math.inf if beta else 0.); p=math.erfc(abs(zstat)/math.sqrt(2)) if se else (0. if beta else 1.)
 return {'n':n,'alpha':alpha,'beta':beta,'se_hac_lag2_fsc':se,'z':zstat,'p_two_sided_normal':p,'ci95_normal':[beta-1.96*se,beta+1.96*se],'hac_lag':HAC_LAG,'finite_sample_multiplier':fsc}

provenance={'gsw':{},'transport_canada':{},'date_semantics':{'gsw_slash_format':'DD/MM/YYYY','official_archive':OFFICIAL_CALENDAR,'supersedes_initial_run':INITIAL_INVALID_RUN}}
struct={'expected_components_per_week':60,'gsw_source_weeks':0,'gsw_complete_weeks':0,'gsw_incomplete_weeks':[],'gsw_duplicate_component_weeks':[],'tc_carrier_week_counts':{},'tc_complete_two_carrier_weeks':0,'tc_units':[],'final_model_observations':0}
weekvals=defaultdict(dict); counts=defaultdict(Counter); source_weeks=set(); raw_date_examples=set()

for crop,url in GSW_URLS.items():
 b,meta=fetch(url); provenance['gsw'][crop]=meta; rd=csv.DictReader(io.StringIO(decode(b))); hs=rd.fieldnames or []
 H={'date':header(hs,'week_ending_date','Week Ending Date'),'worksheet':header(hs,'worksheet'),'metric':header(hs,'metric'),'period':header(hs,'period'),'grain':header(hs,'grain'),'grade':header(hs,'grade'),'region':header(hs,'region'),'value':header(hs,'Ktonnes')}
 if not all(H.values()):raise RuntimeError(f'GSW schema {crop}: {H}')
 for row in rd:
  if norm(row.get(H['worksheet']))!=norm('Primary') or norm(row.get(H['metric']))!=norm('Deliveries') or norm(row.get(H['period']))!=norm('Current Week'):continue
  if (row.get(H['grade']) or '').strip()!='':continue
  grain=(row.get(H['grain']) or '').strip(); region=(row.get(H['region']) or '').strip()
  if grain not in GRAINS or region not in REGIONS:continue
  raw=(row.get(H['date']) or '').strip(); d=gsw_date(raw)
  if not d or not START<=d<=END:continue
  raw_date_examples.add(raw); wk=monday(d); source_weeks.add(wk); k=(grain,region); counts[wk][k]+=1
  v=number(row.get(H['value']))
  if k not in weekvals[wk]:weekvals[wk][k]=v

struct['gsw_source_weeks']=len(source_weeks); provenance['date_semantics']['gsw_raw_date_examples']=sorted(raw_date_examples)[:5]
for wk in sorted(source_weeks):
 c=counts[wk]; dup=[f'{g}|{r}' for (g,r),n in c.items() if n!=1]; miss=[f'{g}|{r}' for g,r in COMPONENTS if c.get((g,r),0)==0]
 if dup:struct['gsw_duplicate_component_weeks'].append({'week':wk.isoformat(),'key_count':len(dup)})
 if miss or len(c)!=60:struct['gsw_incomplete_weeks'].append({'week':wk.isoformat(),'missing_count':len(miss),'observed_component_count':len(c)})
struct_fail=bool(struct['gsw_duplicate_component_weeks'] or struct['gsw_incomplete_weeks'])
P={}
if not struct_fail:
 for wk in sorted(source_weeks):P[wk]=sum(weekvals[wk][k] for k in COMPONENTS)
 struct['gsw_complete_weeks']=len(P)

tcb,tcmeta=fetch(TC_URL); provenance['transport_canada']=tcmeta; carrier={c:{} for c in CARRIERS}; cc=Counter(); units=set()
with zipfile.ZipFile(io.BytesIO(tcb)) as zf:
 members=[n for n in zf.namelist() if n.lower().endswith('.csv')]; chosen=[]
 for yr in (2023,2024,2025):
  hits=[n for n in members if re.search(rf'(^|/)weekly_rail_system_performance_indicators_eng_{yr}\.csv$',n,re.I)]
  if len(hits)!=1:raise RuntimeError(f'TC member {yr}: {hits}')
  chosen.append(hits[0])
 provenance['transport_canada']['selected_members']=chosen
 for member in chosen:
  rd=csv.DictReader(io.StringIO(decode(zf.read(member)))); hs=rd.fieldnames or []
  H={'date':header(hs,'Reference_Date'),'carrier':header(hs,'Carrier'),'measure':header(hs,'Measure'),'unit':header(hs,'Unit_of_Measure'),'geo':header(hs,'Geography'),'commodity':header(hs,'Commodity'),'value':header(hs,'Measure_Value')}
  if not all(H.values()):raise RuntimeError(f'TC schema: {H}')
  for row in rd:
   if norm(row.get(H['commodity']))!=norm('All Western grain') or norm(row.get(H['measure']))!=norm('Average Dwell Time at Origin') or norm(row.get(H['geo']))!=norm('Canada'):continue
   c=(row.get(H['carrier']) or '').strip()
   if c not in CARRIERS:continue
   d=tc_date(row.get(H['date']))
   if not d or not START<=d<=END:continue
   wk=monday(d); cc[(c,wk)]+=1; unit=(row.get(H['unit']) or '').strip()
   if unit:units.add(unit)
   v=number(row.get(H['value']))
   if cc[(c,wk)]==1:carrier[c][wk]=v
struct['tc_units']=sorted(units); struct['tc_carrier_week_counts']={c:len(carrier[c]) for c in CARRIERS}
tcdup=[(c,wk,n) for (c,wk),n in cc.items() if n!=1]; struct['tc_duplicate_carrier_weeks']=len(tcdup)
if tcdup or len(units)!=1 or norm(next(iter(units),'')) not in {'hour','hours'}:struct_fail=True
D={}
if not struct_fail:
 for wk in sorted(set(carrier['CN']) & set(carrier['CPKC'])):D[wk]=(carrier['CN'][wk]+carrier['CPKC'][wk])/2
 struct['tc_complete_two_carrier_weeks']=len(D)

model_dates=[]; x=[]; y=[]
if not struct_fail:
 for t in sorted(D):
  t1=t-timedelta(days=7); t2=t-timedelta(days=14)
  if t1 in D and t1 in P and t2 in P:
   model_dates.append(t); x.append((P[t1]-P[t2])/100.); y.append(D[t]-D[t1])
struct['final_model_observations']=len(model_dates); struct['first_model_week']=model_dates[0].isoformat() if model_dates else None; struct['last_model_week']=model_dates[-1].isoformat() if model_dates else None

if struct_fail or len(model_dates)<MIN_N:
 gate='HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL'; primary=None; diagnostics=None
else:
 primary=fit(x,y); beta=primary['beta']; lo,hi=primary['ci95_normal']
 if beta>=MATERIALITY and lo>0:gate='PASS_POSITIVE_MATERIAL_CA_GRAIN_E02_RELATIONSHIP'
 elif 0<beta<MATERIALITY and lo>0:gate='POSITIVE_BELOW_MATERIALITY_CA_GRAIN_E02_RELATIONSHIP'
 else:gate='NO_PREREGISTERED_POSITIVE_CA_GRAIN_E02_RELATIONSHIP'
 primary.update({'x_scale':'+100 Ktonnes weekly change in Primary deliveries at t-1','y_unit':'hours weekly change in equal-weight CN/CPKC origin dwell at t','materiality_floor_beta':MATERIALITY,'signed_hypothesis':'beta > 0','gate':gate})
 diagnostics={}
 for c in CARRIERS:
  yc=[carrier[c][t]-carrier[c][t-timedelta(days=7)] for t in model_dates]; diagnostics[c]=fit(x,yc); diagnostics[c]['non_rescuing']=True

payload={'id':'CA-GRAIN-E02-STAGE-B-PRIMARY','issue':110,'execution_revision':2,'supersedes_invalid_technical_run':INITIAL_INVALID_RUN,'date_semantics_correction':'GSW slash dates parsed DD/MM/YYYY per official CGC archive','preregistration_unchanged':True,'provenance':provenance,'structural_gate':struct,'primary':primary,'diagnostics':diagnostics,'gate':gate,'raw_source_bytes_persisted':False,'incremental_monetary_cost_usd':0}
(OUT/'STAGE_B_PRIMARY_RESULT.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
if primary is None:
 result=f'''---\nid: CA-GRAIN-E02-RESULT\ntype: preregistered-relationship-test\nissue: 110\nexecution_revision: 2\ngate: {gate}\nrelationship_computed: false\nincremental_monetary_cost_usd: 0\n---\n\n# CA-GRAIN-E02 Result\n\n**`{gate}`**\n\nDate-corrected execution supersedes invalid technical Run `{INITIAL_INVALID_RUN}`. The frozen preregistration was unchanged.\n\n- GSW DD/MM/YYYY source weeks: **{struct['gsw_source_weeks']}**; complete weeks: **{struct['gsw_complete_weeks']}**.\n- incomplete weeks: **{len(struct['gsw_incomplete_weeks'])}**; duplicate-component weeks: **{len(struct['gsw_duplicate_component_weeks'])}**.\n- TC weeks: CN **{struct['tc_carrier_week_counts'].get('CN',0)}**, CPKC **{struct['tc_carrier_week_counts'].get('CPKC',0)}**.\n- final model observations: **{struct['final_model_observations']}** (required >= {MIN_N}).\n- No relationship model fitted. Raw source bytes not persisted. Cost **0 USD**.\n'''
else:
 lo,hi=primary['ci95_normal']; result=f'''---\nid: CA-GRAIN-E02-RESULT\ntype: preregistered-relationship-test\nissue: 110\nexecution_revision: 2\ngate: {gate}\nrelationship_computed: true\nincremental_monetary_cost_usd: 0\n---\n\n# CA-GRAIN-E02 Result\n\n**`{gate}`**\n\nDate-corrected execution supersedes invalid technical Run `{INITIAL_INVALID_RUN}`; the frozen preregistration was unchanged.\n\n- N: **{primary['n']}**\n- beta: **{primary['beta']:.9f} hours per +100 Ktonnes**\n- HAC(2) SE: **{primary['se_hac_lag2_fsc']:.9f}**\n- 95% CI: **[{lo:.9f}, {hi:.9f}]**\n- two-sided normal p: **{primary['p_two_sided_normal']:.9g}**\n- materiality floor: **+1.0 hour per +100 Ktonnes**\n- model window: **{struct['first_model_week']} through {struct['last_model_week']}**\n\nThis is a preregistered association/predictive bottleneck test, not a causal estimate. Diagnostics cannot rescue the primary gate. Raw source bytes were not persisted. Cost **0 USD**.\n'''
(OUT/'RESULT.md').write_text(result,encoding='utf-8')
print(json.dumps({'gate':gate,'n':struct['final_model_observations'],'beta':None if primary is None else primary['beta'],'ci95':None if primary is None else primary['ci95_normal'],'p':None if primary is None else primary['p_two_sided_normal'],'cost_usd':0}))
