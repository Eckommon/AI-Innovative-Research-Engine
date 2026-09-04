---
id: JP-PORT-E01-JMA-PAYLOAD-SHAPE
created: 2026-09-04
weather_values_opened: false
relationship_outcome_computed: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-E01 JMA Payload Shape

- JS SHA-256: 01a025ef82e1eff3aaa68a8b03f6276adf382557e1c67e642d72623f984bb16c

## addElementList
~~~javascript
function addElementList() {
        elementList = getJsonLocalStorage("elementList");//再宣言が必要
        //console.log("elementList.length.start="+elementList.length);
        var myelem=[];//選択項目用配列

        $('input:enabled.elem').each(function() {
            if ($(this).prop('checked')) {
                $(this).next('span').addClass('checked');
                thispar = $(this).parent('div,td');
                //str=thispar.text();
                val = thispar.find('input.inumber,select.inumber').val(); //'value')
                if (val == undefined) {
                    val = "";
                }
                strkikan = getAggrgPeriod(aggrgPeriod);
                thispar.find("span.eltxt3").html(strkikan);
                str1 = thispar.find('span.eltxt1').text();
                str2 = thispar.find('span.eltxt2').text();
                switch ($(this).val()) {//例外
                    case '103':
                    case '403':
                        if (val == "0") {
                            pval = "0";
                            txval = "0.0";
                        } else if (val == "05") {
                            pval = "05";
                            txval = "0.5";
                        } else if (val == "01") {
                            pval = "01";
                            txval = "0.1";
                        } else {
                            pval = val;
                            txval = val;
                        }
                        break;
                    case '105':
                        if (val == 10) {
                            str2 = '分間' + str2;
                        } else {
                            str2 = '時間' + str2;
                        }
                        pval = val;
                        txval = pval;
                        break;
                    case '608':
                    case '609':
                        pval = val * 10;
                        txval = val;
                        break;
                    default:
                        pval = val;
                        txval = pval;
                }
                str = str1 + txval + str2;
                elflag = false;

                myelem.push( $(this).val() );//選択要素を記録する

                for (i = 0; i < elementList.length; i++) {
                    if ($(this).val() == elementList[i][1]) {
                        elementList[i] = [str, $(this).val(), pval];
                        elflag = true;
                        break;
                    }
                }
                if (!elflag) {
                    elementList.push([str, $(this).val(), pval]);
                }
            } else {
                $(this).next('span').removeClass('checked');
            }

        });

        elementList = elementList.filter( function (item) {
            const exists = myelem.includes(item[1]);
            return exists === true;
        });

        localStorage.setItem('obsdl_elementList', JSON.stringify(elementList));
        viewSelectedElement();
    }
~~~

## changePeriod
~~~javascript
function changePeriod(str) {
        const now = new Date();
        const yd = new Date(now.getFullYear(), now.getMonth(), now.getDate() - 1);

        // 期間の調整
        const periods = { "1y": [1, 0], "1m": [0, 1], "10y": [10, 0] };
        const [years, months] = periods[str] || [0, 0];
        const yd1 = new Date(yd.getFullYear() - years, yd.getMonth() - months, yd.getDate());

        const aggrgType = parseInt(aggrgPeriod[0]);
        ymdList[0] = yd1.getFullYear();
        ymdList[1] = yd.getFullYear();
        ymdList[2] = yd1.getMonth() + 1;
        ymdList[3] = yd.getMonth() + 1;
        ymdList[4] = calcDayValue(yd1.getDate(), aggrgType);
        ymdList[5] = calcDayValue(yd.getDate(), aggrgType);

        localStorage.setItem('obsdl_ymdList', JSON.stringify(ymdList));
        changeInputPeriod();
    }
~~~

## setform
~~~javascript
function setform(input, type, name, value) {
    input.setAttribute('type', type);
    input.setAttribute('name', name);
    input.setAttribute('value', value);
}
~~~

## getNum
~~~javascript
function getNum() {
        var nOfSt = 0;
        if (Object.keys) {
            nOfSt = Object.keys(stationList).length;
        } else {
            for (prop in stationList) {
                nOfSt++;
            }
        }
        var nOfEl = (elementList && elementList.length) ? elementList.length : 0;
        var opnum = (optionNumList && optionNumList.length) ? optionNumList.length : 0;
        var opkey = 0;

        // additional weight for options
        const weights = { op1: 1, op2: 1, op3: 2, op4: 2 };
        let nOfOp = 1; // obsの分
        let opyear = 1;
        for (const opt of optionNumList) {
            nOfOp += weights[opt[0]] ?? 0;
            if (opt[0] === 'op3' || opt[0] === 'op4') {
                opyear = 1 + opt[1] / 30;
            }
        }
        nOfOp *= opyear;

        var nOfPr = countPrNum(aggrgPeriod,interAnnualType,ymdList,jikantaiList);
        return [nOfSt, nOfEl, nOfPr, nOfOp];
    }
~~~

## getErrMseg
~~~javascript
function getErrMseg() {
        var str = "";
        var errMseg = [];
        if ($.isEmptyObject(stationList)) {
            errMseg.push("地点が選択されていません");
        }
        if (!(elementList && elementList.length)) {
            errMseg.push("項目が選択されていません");
        }
        var nOf = getNum();
        if (getErr(nOf[0], nOf[1], nOf[2], nOf[3])) {
            errMseg.push("選択要素が多すぎます。地点、データ、期間のいずれかを減らしてください");
        }
        if (errMseg.length > 0) {
            for (i = 0; i < errMseg.length; i++) {
                str = str + errMseg[i] + '\n';
            }
            return str;
        } else {
            return false;
        }
    }
~~~

## CSV form construction
~~~javascript
orm = function(form, name, element) {
        var input = document.createElement('input');
        setform(input, 'hidden', name, element);
        form.appendChild(input);
    };

    $('body').on('click', '#csvdl', function() {
        // Wait dialogを表示
        openDialog("#wait");

        var str = getErrMseg();
        if (str) {
            closeDialog("#wait");
            alert(str);
            location.hash = "";
        } else {
            // ダウンロード完了Cookieを削除
            document.cookie = 'downloadComplete=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';

            var stationNumList = [];
            var elementNumList = [];
            $.each(stationList, function(key) {
                stationNumList.push($(this)[1]);
            });
            $.each(elementList, function() {
                elementNumList.push([$(this)[1], $(this)[2]]);
            });
            var form = document.createElement('form');
            document.body.appendChild(form);
            createForm(form, 'stationNumList',  JSON.stringify(stationNumList));
            createForm(form, 'aggrgPeriod',     aggrgPeriod);
            createForm(form, 'elementNumList',  JSON.stringify(elementNumList));
            createForm(form, 'interAnnualType', interAnnualType);
            createForm(form, 'ymdList',         JSON.stringify(ymdList));
            createForm(form, 'optionNumList',   JSON.stringify(optionNumList));
            createForm(form, 'downloadFlag',    true);
            createForm(form, 'rmkFlag',         rmkFlag);
            createForm(form, 'disconnectFlag',  disconnectFlag);
            createForm(form, 'youbiFlag',       youbiFlag);
            createForm(form, 'fukenFlag',       fukenFlag);
            createForm(form, 'kijiFlag',        kijiFlag);
            //createForm(form, 'huukouFlag',      huukouFlag);
            createForm(form, 'csvFlag',         csvFlag);
            createForm(form, 'jikantaiFlag',    jikantaiFlag);
            createForm(form, 'jikantaiList',    JSON.stringify(jikantaiList));//配列はJSON.stringifyで
            createForm(form, 'ymdLiteral',      ymdLiteral);
            form.setAttribute('method', 'post');
            form.setAttribute('action', 'show/table');
            form.submit();

            // Cookieをポーリングしてダウンロード完了を検知
            var downloadCheckInterval = setInterval(function() {
                if (document.cookie.indexOf('downloadComplete') !== -1) {
                    clearInterval(downloadCheckInterval);
                    closeDialog("#wait");
                    // Cookieを削除
                    document.cookie = 'downloadComplete=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
                }
            }, 100); // 100msごとにチェック

            // 安全のため2分後にタイムアウト
            setTimeout(function() {
                clearInterval(downloadCheckInterval);
                closeDialog("#wait");
            }, 120000);
        }
    });

});

// non-DOM functions

function getAggrgPeriod(aggrgPeriod) {
    const aggrgType = parseInt(aggrgPeriod[0]);
    return (aggrgType !== 8) ? aggrgChar[aggrgType] : aggrgPeriod.slice(2) + '日間';
}

function calcAcrossYearMaxYear(aggrgNum, endMonth, endDay, latestday) {
    var maxy, latestYear, latestMonth, latestDay;
    latestYear  = latestday.getFullYear();
    latestMonth = latestday.getMonth();
    latestDay   = latestday.getDate();
    if (endMonth == latestMonth + 1) {
        if (aggrgNum === 2) { //暦日半旬 endDay = 1, 2, .., 6
            maxy = (latestDay >= 5 * (endDay - 1)) ? latestYear : latestYear - 1;
        } else if (aggrgNum === 4) { //旬 endDay = 1, 2, 3
            maxy = (latestDay >= 10 * (endDay - 1)) ? latestYear : latestYear - 1;
        } else if ([1, 8, 9].includes(aggrgNum)){
            maxy = (latestDay >= endDay) ? latestYear : latestYear - 1;
        } else {
            maxy = latestYear;
        }
    } else if (endMonth > latestMonth + 1) {
        maxy= latestYear - 1;
    } else {
        maxy = latestYear;
    }

    return maxy;
}

~~~