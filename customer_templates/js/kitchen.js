
/*
    status:
    0 = 未付款
    1 = 已付款，製作中
    2 = 餐點準備完成
    3 = 訂單已完成(變成歷史訂單)
*/
XHR = createXHR()
setInterval(()=>{
    XHR.open("GET","http://example.com/",true)
    XHR.onreadystatechange = function () {
        if (XHR.readyState === 4) {
            if (XHR.status === 200) {
                // Successful response
                var response = XHR.responseText;
                order_list = [
                    {
                        "id":"example1",
                        "order_num":"#AR326",
                        "item_list":[
                            {"name":"冰淇淋(一球)","qty":1},
                            {"name":"炸薯條","qty":1}
                        ],
                        "total":75,
                        "status":1    
                    },
                    {
                        "id":"example2",
                        "order_num":"#AR326",
                        "item_list":[
                            {"name":"冰淇淋(兩球)","qty":1},
                            {"name":"烤香腸","qty":1}
                        ],
                        "total":70,
                        "status":0 
                    }
                ]
                /*----顯示每筆訂單----*/
                for(let i = 0;i < order_list.length;i++){
                    //
                    let id = order_list[i]["id"];
                    let htmlText = "<div id='"+order_list[i]["id"]+"' class='item' onclick='defaultLg(\""+order_list[i]["id"]+"\")'><div id='"+order_list[i]["id"]+"_default' class='item_default'><div class='order_num'>";
                    htmlText += "<h1>"+order_list[i]["order_num"]+"</h1>";
                    htmlText += "</div><div class='item_list'>";
                    for(let j = 0;j < order_list[i]["item_list"].length;j++){
                        htmlText += "<h4>-"+order_list[i]["item_list"][j]["name"]+"</h4>";
                    }
                    htmlText += "</div><div class='money'>";
                    htmlText += "<h1 style='color: red;'>$"+order_list[i]["total"]+"</h1>";
                    htmlText += "</div></div><div id='"+order_list[i]["id"]+"_lg'><div class='lg_upper'><div class='order_num_lg'>";
                    htmlText += "<h1>"+order_list[i]["order_num"]+"</h1>";
                    htmlText += "</div><div class='money_lg'>";
                    htmlText += "<h1 style='color: red;'' align='right'>$"+order_list[i]["total"]+"</h1>";
                    htmlText += "</div></div><div class='lg_middle'>";
                        for(let j = 0;j < order_list[i]["item_list"].length;j++){
                        htmlText += "<h4>-"+order_list[i]["item_list"][j]["name"]+"</h4>";
                    }
                    htmlText += "</div><div class='lg_footer'><span id='"+order_list[i]["id"]+"_buttons'></span></div></div></div>";
                    document.getElementById("items").innerHTML = document.getElementById("items").innerHTML + htmlText;
                
                    document.getElementById(id + "_default").style.display = "flex";
                    document.getElementById(id + "_lg").style.display = "none";
                    //分辨訂單種類
                    if(order_list[i]["status"] == 1){
                        document.getElementById(id + "_buttons").innerHTML = "<button type='button'>餐點準備完成</button>";
                    }
                }
                // You can parse and work with the response data here
                console.log(response);
            } else {
                // Error handling
                console.error("Request failed with status: " + xhr.status);
            }
        }
    };

    
},20000)
