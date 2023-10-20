from flask import Flask
from flask import Flask, render_template, request
from utils import *
 
app = Flask(__name__, template_folder='customer_templates')

@app.route('/cashier', methods = ["GET", "POST"])
def cashier():
    if request.method == "POST":
        idx = request.form['id']
        state = request.form['state']
        upload_order_info(idx, state)

    return render_template('cashier.html')

@app.route('/cashier_refresh', methods = ["GET"])

#def cashier_refresh(): # download orders info
 #   orders = list(get_all_data())
  #  print(orders)
   # orders = [i for i in orders if i[13] != "3"] # 排除已完成訂單
    #orders = sorted(orders, key=lambda x: x[13]) # 從未付款的代號0的訂單開始排序
    
    #return orders

def cashier_refresh(): # download orders info
    orders = list(get_all_data())
    orders = [i for i in orders if i[13] != "3"] # 排除已完成訂單
    orders = sorted(orders, key=lambda x: x[13]) # 從未付款的代號0的訂單開始排序

    flavor_dict = {
        '1': ['香草', '草莓', '巧克力'],
        '2': ['香草', '草莓', '巧克力'],
        '3': ['香草', '草莓', '巧克力'],
        '4': ['原味', '蒜味'],
        '5': 'n',
        '6': ['可爾必思 35元', '石榴氣泡水 35元', '葡萄氣泡水 35元','水蜜桃棄泡水 35元','蘋果氣泡水 35元']
    }

    result = []

    for o in orders:
        order_dict = {}
        order_dict['id'] = o[0]

        i = 0
        for item in range(1, 13, 2):
            if o[item] != 'n' and o[item+1] != '0':
                i += 1
                if len(o[item]) == "1" and o[item] != '5':
                    o_item_text = flavor_dict[o[item]][int(o[item+1])-1]
                elif o[item] == '5':
                    o_item_text = '預設'
                else:
                    o_item_text = ''
                    for w in o[item].replace(' ','').split():
                        if w == '0':
                            o_item_text += '香草'
                        elif w == '1':
                            o_item_text += '草莓'
                        elif w == '2':
                            o_item_text += '巧克力'
                order_dict[str(int((item+1)/2))] = {'flavor': o_item_text, 'qty': o[item+1]}
        order_dict['total'] = int(o[14])
        order_dict['status'] = int(o[13])
        print(order_dict)
        result.append(order_dict)

    return result
@app.route('/kitchen', methods = ["GET", "POST"])
def kitchen():
    if request.method == "POST":
        idx = request.form['id']
        state = request.form['state']
        upload_order_info(idx, state)

    return render_template('kitchen.html')

@app.route('/kitchen_refresh', methods = ["GET"])
def kitchen_refresh():
    orders = check_order_info()
    orders = [i for i in orders if i['state'] == 1] # 只有需要製作的訂單
    orders = sorted(orders, key=lambda x: x['state']) # 從未付款的代號0的訂單開始排序

    return orders

if __name__ == '__main__':
    app.debug = True
    app.run()
