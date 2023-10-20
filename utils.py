import random
import pymysql

# 连接到MySQL数据库
conn = pymysql.connect(
    host="vultr-prod-0735f93d-5e03-4e4b-b1ae-878c590715ab-vultr-prod-7d22.vultrdb.com", 
    user="vultradmin",
    password="AVNS_PcAfxyST1X5nxEzfYSq",
    database="order",
    port=16751
)

cursor = conn.cursor()




def create_order(data):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    random_letters = ''.join(random.choice(letters) for _ in range(2))
    random_numbers = ''.join(random.choice(numbers) for _ in range(3))

    order_idx = '#'+random_letters+random_numbers
    total_price = 0
    price_dict = {'1':20, '2':40, '3':50, '4':30, '5':35, '6': {'1': 35, '2': 40, '3': 40, '4': 40, '5': 40}}
    for i in data:
        if i['id'] == '6':
            total_price += price_dict[i['id']][i['flavor']] * int(i['qty'])
        else:
            total_price += price_dict[i['id']] * int(i['qty'])

    # 寫入mysql dataset
    '''html格式:
    create table master
    (
        id   varchar(10)         not null,
        1_favor varchar(10)  not null,
        1_number varchar(10)  not null,
        2_favor varchar(10)  not null,
        2_number varchar(10)  not null,
        3_favor varchar(10)  not null,
        3_number varchar(10)  not null,
        4_favor varchar(10)  not null,
        4_number varchar(10)  not null,
        5_favor varchar(10)  not null,
        5_number varchar(10)  not null,
        6_favor varchar(10)  not null,
        6_number varchar(10)  not null,
        status  varchar(10)          not null,
        total varchar(10)  not null,
        primary key (id)
    );'''

    ordered_data = [0]*12 # 根據id填入相對應的6個品項，若該項qty為0則填入n
    for i in range(len(data)):
        ordered_data[2*int(data[i]['id'])-2] = data[i]['flavor']
        ordered_data[2*int(data[i]['id'])-1] = data[i]['qty']

    # write to sql
    prompt = '''INSERT INTO master (id, 1_favor, 1_number, 2_favor, 2_number, 3_favor, 3_number, 4_favor, 4_number, 5_favor, 5_number, 6_favor, 6_number, status, total) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(order_idx, ordered_data[0], ordered_data[1], ordered_data[2], ordered_data[3], ordered_data[4], ordered_data[5], ordered_data[6], ordered_data[7], ordered_data[8], ordered_data[9], ordered_data[10], ordered_data[11], '0', str(total_price))
    print(prompt)
    cursor.execute(prompt)
    conn.commit()
    return order_idx

# 測試
# data = [{'id': '6', 'flavor': '1', 'qty': '1'}]
# create_order(data)

def get_all_data():
    # 從mysql中讀取data
    prompt = '''SELECT * FROM master'''
    cursor.execute(prompt)
    result = cursor.fetchall()
    return result

def check_order_info(target_id):
    for i in get_all_data():
        print(i[0])
        if i[0] == target_id: # id 對應到第0個數據
            print(i)
            return i[13]
    return 'error'

def upload_order_info(target_id, target_state):
    # 更新訂單資訊
    prompt = '''UPDATE master SET status = '{}' WHERE id = '{}' ;'''.format(target_state, target_id)
    print(prompt)
    cursor.execute(prompt)
    conn.commit()
    return 'success'
