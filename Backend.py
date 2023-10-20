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
def cashier_refresh(): # download orders info
    orders = list(get_all_data())
    orders = [i for i in orders if i['13'] != "3"] # 排除已完成訂單
    orders = sorted(orders, key=lambda x: x['13']) # 從未付款的代號0的訂單開始排序

    for o in orders:
        print(o)

    return orders

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