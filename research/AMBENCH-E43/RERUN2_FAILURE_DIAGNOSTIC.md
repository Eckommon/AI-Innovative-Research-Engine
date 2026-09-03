---
id: AMBENCH-E43-RERUN2-FAILURE-DIAGNOSTIC
type: exact-rerun-error-diagnostic
created: 2026-09-03
historical_run_id: 32648786267
run_attempt: 2
performance_output_accessed: false
experiment_contract_changed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E43 Rerun Attempt 2 Failure Diagnostic / 재실행 2차 실패 진단

```text
[0_execute.txt] 2026-09-03T08:26:39.2006020Z [36;1m            if len(row)!=4:[0m
[0_execute.txt] 2026-09-03T08:26:39.2007174Z [36;1m                malformed+=1; continue[0m
[0_execute.txt] 2026-09-03T08:26:39.2008351Z [36;1m            try:[0m
[0_execute.txt] 2026-09-03T08:26:39.2009459Z [36;1m                vals=tuple(map(float,row))[0m
[0_execute.txt] 2026-09-03T08:26:39.2010715Z [36;1m            except Exception:[0m
[0_execute.txt] 2026-09-03T08:26:39.2011942Z [36;1m                malformed+=1; continue[0m
[0_execute.txt] 2026-09-03T08:26:39.2013302Z [36;1m            if not all(math.isfinite(v) for v in vals):[0m
[0_execute.txt] 2026-09-03T08:26:39.2014953Z [36;1m                malformed+=1; continue[0m
[0_execute.txt] 2026-09-03T08:26:39.2016217Z [36;1m            rows.append(vals)[0m
[0_execute.txt] 2026-09-03T08:26:39.2142784Z [36;1mprint(json.dumps(info,indent=2))[0m
[0_execute.txt] 2026-09-03T08:26:39.2144022Z [36;1mPY[0m
[0_execute.txt] 2026-09-03T08:26:39.2171953Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
[0_execute.txt] 2026-09-03T08:26:39.2173343Z ##[endgroup]
[0_execute.txt] 2026-09-03T08:28:20.5503202Z Traceback (most recent call last):
[0_execute.txt] 2026-09-03T08:28:20.5503929Z   File "<stdin>", line 31, in <module>
[0_execute.txt] 2026-09-03T08:28:20.5504383Z   File "<stdin>", line 20, in fetch
[0_execute.txt] 2026-09-03T08:28:20.5505032Z   File "/usr/lib/python3.12/http/client.py", line 500, in read
[0_execute.txt] 2026-09-03T08:28:20.5508030Z     s = self._safe_read(self.length)
[0_execute.txt] 2026-09-03T08:28:20.5508670Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0_execute.txt] 2026-09-03T08:28:20.5509404Z   File "/usr/lib/python3.12/http/client.py", line 663, in _safe_read
[0_execute.txt] 2026-09-03T08:28:20.5510410Z     raise IncompleteRead(data.getvalue(), amt - data.tell())
[0_execute.txt] 2026-09-03T08:28:20.5511699Z http.client.IncompleteRead: IncompleteRead(7651036 bytes read, 10428540 more expected)
[0_execute.txt] 2026-09-03T08:28:20.5667036Z ##[error]Process completed with exit code 1.
[0_execute.txt] 2026-09-03T08:28:20.5801534Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
[0_execute.txt] 2026-09-03T08:28:20.5803100Z Post job cleanup.
[0_execute.txt] 2026-09-03T08:28:20.6551770Z [command]/usr/bin/git version
[0_execute.txt] 2026-09-03T08:28:20.6587732Z git version 2.55.0
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2006016Z [36;1m            if len(row)!=4:[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2007171Z [36;1m                malformed+=1; continue[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2008348Z [36;1m            try:[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2009455Z [36;1m                vals=tuple(map(float,row))[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2010712Z [36;1m            except Exception:[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2011938Z [36;1m                malformed+=1; continue[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2013286Z [36;1m            if not all(math.isfinite(v) for v in vals):[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2014942Z [36;1m                malformed+=1; continue[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2016214Z [36;1m            rows.append(vals)[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2142781Z [36;1mprint(json.dumps(info,indent=2))[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2144013Z [36;1mPY[0m
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2171917Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:26:39.2173339Z ##[endgroup]
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5502986Z Traceback (most recent call last):
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5503918Z   File "<stdin>", line 31, in <module>
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5504377Z   File "<stdin>", line 20, in fetch
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5505025Z   File "/usr/lib/python3.12/http/client.py", line 500, in read
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5508018Z     s = self._safe_read(self.length)
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5508661Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5509394Z   File "/usr/lib/python3.12/http/client.py", line 663, in _safe_read
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5510318Z     raise IncompleteRead(data.getvalue(), amt - data.tell())
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5511690Z http.client.IncompleteRead: IncompleteRead(7651036 bytes read, 10428540 more expected)
[execute/3_Reconstruct and verify frozen F42 inputs.txt] 2026-09-03T08:28:20.5667003Z ##[error]Process completed with exit code 1.
```
