#!/usr/bin/env python3
"""Efficient outcome-blind USGS metadata qualification for US-WATERWAY-F01.

Uses the documented public DEMO_KEY and only metadata endpoints. No hydrologic
observation values and no lock-delay values are requested or parsed.
"""
from __future__ import annotations
import json, math, re, time, urllib.parse, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WATERWAY-F01'
UA='AI-Innovative-Research-Engine/US-WATERWAY-F01-fast-v2'
LOCK_QUERY='https://services7.arcgis.com/n1YM8pTrFmm7L4hs/ArcGIS/rest/services/Locks/FeatureServer/0/query?where=1%3D1&outFields=ID,NDCCODE,RIVERCD,LOCKCD,PMSDATA,PMSNAME,RIVER,STATE,DISTRICT&returnGeometry=true&f=json&outSR=4326'
LOC='https://api.waterdata.usgs.gov/ogcapi/v0/collections/monitoring-locations/items'
TS='https://api.waterdata.usgs.gov/ogcapi/v0/collections/time-series-metadata/items'
START='2018-01-01'; END='2020-12-31'; TARGET=25
PRIORITY=['MISSISSIPPI','OHIO','TENNESSEE','ARKANSAS','COLUMBIA','MONONGAHELA','ALLEGHENY','KANAWHA','MISSOURI','ILLINOIS','CUMBERLAND']

def get_json(url, attempts=2):
    last=None
    for i in range(attempts):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'application/json'})
            with urllib.request.urlopen(req,timeout=20) as r:
                return json.loads(r.read().decode('utf-8','replace'))
        except Exception as e:
            last=e
            if i+1<attempts: time.sleep(1+i)
    raise last

def norm(x):
    s=re.sub(r'[^A-Z0-9]+',' ',str(x or '').upper())
    return re.sub(r'\s+',' ',s).strip()

def river_match(river,name):
    r=norm(river); n=norm(name)
    if not r or not n: return False
    variants={r}
    if not r.endswith(' RIVER'): variants.add(r+' RIVER')
    if r.endswith(' WATERWAY'): variants.add(r[:-9].strip()+' RIVER')
    if r=='MISSISSIPPI': variants.add('MISSISSIPPI RIVER')
    if r=='OHIO': variants.add('OHIO RIVER')
    return any(len(v)>=5 and v in n for v in variants)

def covers(p):
    a=str(p.get('begin_utc') or p.get('begin') or '')[:10]
    b=str(p.get('end_utc') or p.get('end') or '')[:10]
    return a and b and a<=START and b>=END

def hav(a,b,c,d):
    R=6371.0088; p1=math.radians(a); p2=math.radians(c); dp=math.radians(c-a); dl=math.radians(d-b)
    x=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(x))

def priority(lock):
    r=norm(lock['river'])
    for i,p in enumerate(PRIORITY):
        if p in r: return i
    return 99

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    obj=get_json(LOCK_QUERY)
    locks=[]
    for f in obj.get('features',[]):
        a=f.get('attributes') or {}; g=f.get('geometry') or {}
        if str(a.get('PMSDATA','')).upper()!='Y' or g.get('x') is None or g.get('y') is None: continue
        locks.append({'id':a.get('ID'),'name':a.get('PMSNAME'),'river':a.get('RIVER'),'state':a.get('STATE'),'lon':float(g['x']),'lat':float(g['y'])})
    locks.sort(key=lambda x:(priority(x),norm(x['river']),norm(x['name'])))
    matches=[]; errors=[]; reqs=1; attempts=0
    for lock in locks:
        if len(matches)>=TARGET: break
        attempts+=1
        deg=.35
        bbox=f"{lock['lon']-deg:.6f},{lock['lat']-deg:.6f},{lock['lon']+deg:.6f},{lock['lat']+deg:.6f}"
        q=LOC+'?'+urllib.parse.urlencode({'f':'json','bbox':bbox,'limit':500,'api_key':'DEMO_KEY'})
        try:
            loc=get_json(q); reqs+=1
        except Exception as e:
            errors.append(f"loc lock {lock['id']}: {type(e).__name__}: {e}"); continue
        cands=[]
        for f in loc.get('features',[]):
            p=f.get('properties') or {}; g=f.get('geometry') or {}; co=g.get('coordinates') or []
            mid=f.get('id') or p.get('id') or p.get('monitoring_location_id'); name=p.get('monitoring_location_name') or ''
            if str(p.get('agency_code') or '')!='USGS' or not mid or len(co)<2 or not river_match(lock['river'],name): continue
            d=hav(lock['lat'],lock['lon'],float(co[1]),float(co[0])); cands.append((d,str(mid),str(name)))
        for d,mid,name in sorted(cands):
            q2=TS+'?'+urllib.parse.urlencode({'f':'json','monitoring_location_id':mid,'limit':250,'api_key':'DEMO_KEY'})
            try:
                ts=get_json(q2); reqs+=1
            except Exception as e:
                errors.append(f"ts {mid}: {type(e).__name__}: {e}"); continue
            supports=[]
            for f in ts.get('features',[]):
                p=f.get('properties') or {}
                if str(p.get('parameter_code')) not in {'00060','00065'}: continue
                if str(p.get('computation_period_identifier','')).lower()!='daily': continue
                if covers(p):
                    supports.append({'parameter_code':p.get('parameter_code'),'statistic_id':p.get('statistic_id'),'start':str(p.get('begin_utc') or p.get('begin'))[:10],'end':str(p.get('end_utc') or p.get('end'))[:10]})
            if supports:
                matches.append({'lock_id':lock['id'],'lock_name':lock['name'],'river':lock['river'],'state':lock['state'],'usgs_id':mid,'usgs_name':name,'distance_km':round(d,3),'daily_metadata_support':supports[:12]})
                break
        time.sleep(.03)
    result={'boundary':{'delay_magnitudes_parsed':False,'hydrology_values_requested':False,'hydrology_values_parsed':False,'relationship_computed':False,'incremental_monetary_cost_usd':0},'target_overlap':[START,END],'national_lock_features':len(obj.get('features',[])),'pmsdata_y_geometry_locks':len(locks),'locks_attempted':attempts,'qualified_matches':len(matches),'metadata_requests':reqs,'errors':errors[:100],'matches':matches}
    (OUT/'HYDROLOGY_METADATA_PREFLIGHT_V2.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    lines=['# US-WATERWAY-F01 Hydrology Metadata Preflight v2','', 'No delay magnitudes or hydrologic observation values were requested or parsed.','',f'- national lock features: **{len(obj.get("features",[]))}**',f'- `PMSDATA=Y` locks with geometry: **{len(locks)}**',f'- target overlap: **{START}–{END}**',f'- locks attempted before stop: **{attempts}**',f'- qualified lock↔USGS metadata matches: **{len(matches)} / {TARGET}**',f'- metadata requests: **{reqs}**','', 'Qualification requires coordinate proximity <= ~0.35° search envelope, full reported river/waterbody identity in the USGS monitoring-location name, and Daily `00060`/`00065` time-series metadata covering the full target interval.','', '## Qualified matches']
    for m in matches:
        pcs=','.join(sorted({str(x['parameter_code']) for x in m['daily_metadata_support']}))
        lines.append(f"- `{m['lock_id']}` {m['lock_name']} / {m['river']} ↔ `{m['usgs_id']}` {m['usgs_name']} — {m['distance_km']} km; {pcs}")
    lines+=['','Incremental monetary cost: **0 USD**.']
    (OUT/'HYDROLOGY_METADATA_PREFLIGHT_V2.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'pms_locks':len(locks),'attempted':attempts,'qualified':len(matches),'requests':reqs,'errors':len(errors)}))
if __name__=='__main__': main()
