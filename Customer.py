from flask import Flask
from flask import Flask, render_template, request
from utils import *
import json
 
app = Flask(__name__, template_folder='customer_templates')

@app.route('/', methods = ["GET", "POST"])
def menu():
    if request.method == "POST":
        data = json.loads(request.data)
        items = data['item_list']
        # [{'id': '0', 'flavor': '011', 'qty': '2'}]
        order_itx = create_order(items)
        return render_template('order.html', order_itx=order_itx, state='製作ing')

    return render_template('menu.html')

@app.route('/order', methods = ['GET'])
def order():
    order_itx = request.args.get('idx')
    state = check_order_info()
    if state != 'error':
        return render_template('order.html', order_itx=order_itx, state=state)


if __name__ == '__main__':
    app.debug = True
    app.run()