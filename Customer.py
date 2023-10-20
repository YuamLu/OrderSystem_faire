from flask import Flask
from flask import Flask, render_template, request
from utils import *
import json
 
app = Flask(__name__, template_folder='websites')

@app.route('/', methods = ["GET", "POST"])
def menu():
    if request.method == "POST":
        data = json.loads(request.data)
        items = data['item_list']
        # [{'id': '0', 'flavor': '011', 'qty': '2'}]
        order_itx = create_order(items)
        return render_template('orderNum.html', order_itx=order_itx, state='製作ing')

    return render_template('index.html')

@app.route('/order', methods = ['GET'])
def order():
    order_idx = request.args.get('idx')
    print('he:','#'+order_idx)

    state = check_order_info('#'+order_idx)

    if state != 'error':
        if state == "0":
            state = "未付款"
        elif state == "1":
            state = "製作中"
        elif state == "2":
            state = "待取餐"
        else:
            state = "已完成取餐"
        return render_template('orderNum.html', order_idx=order_idx, state=state)
    else:
        return "Error with order info"


if __name__ == '__main__':
    app.debug = True
    app.run()