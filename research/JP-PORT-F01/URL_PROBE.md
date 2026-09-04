---
id: JP-PORT-F01-URL-PROBE
created: 2026-09-04
relationship_outcome_computed: false
weather_values_opened: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-F01 Official URL Probe

## C02 metadata page

- page result: {'ok': True, 'status': 200, 'url': 'https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-C02-v3_2.html', 'type': 'text/html; charset=UTF-8', 'length': None}
- page SHA-256: 8b6fa8e06f920256d8263c3a898e4e4515c260a8fd2cb55c876bf13579807217

### Relevant raw HTML snippets

- <li><a href="/kokjo/inspect/landclassification/download.html">GISデータのダウンロード</a></li>
- <i class="material-icons">file_download</i>
- <i class="material-icons">file_download</i>
- <td class="txtCenter">C02-14_GML.zip</td>
- onclick="javascript:DownLd('0.57MB', 'C02-14_GML.zip',  '../data/C02/C02-14/C02-14_GML.zip' ,this);">
- <span id="C02-14_GML.zip-open" style="display: block">
- <i class="material-icons">file_download</i>
- <span id="C02-14_GML.zip-close" style="display: none">
- <li><a class="grey-text text-darken-3 font95 footer__grid-contents" href="/kokjo/inspect/landclassification/download.html">国土調査 GISデータのダウンロード</a></li>

## Candidate C02 download routes

| URL | HEAD/GET result |
|---|---|
| https://nlftp.mlit.go.jp/ksj/gml/data/C02/C02-2014/C02-14_GML.zip | {'ok': False, 'error': "<HTTPError 404: 'Not Found'>"} |
| https://nlftp.mlit.go.jp/ksj/gml/data/C02/C02-14/C02-14_GML.zip | {'ok': True, 'status': 200, 'url': 'https://nlftp.mlit.go.jp/ksj/gml/data/C02/C02-14/C02-14_GML.zip', 'type': 'application/zip', 'length': '601717'} |
| https://nlftp.mlit.go.jp/ksj/gml/data/C02/C02-14_GML.zip | {'ok': False, 'error': "<HTTPError 404: 'Not Found'>"} |
| https://nlftp.mlit.go.jp/ksj/gml/data/C02/C02-2014/C02-14.zip | {'ok': False, 'error': "<HTTPError 404: 'Not Found'>"} |

## JMA station-list route

| URL | result |
|---|---|
| https://www.jma.go.jp/jma/kishou/know/amedas/ame_master.zip | {'ok': True, 'status': 200, 'url': 'https://www.jma.go.jp/jma/kishou/know/amedas/ame_master.zip', 'type': 'application/zip', 'length': '53494'} |