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

    # 寫入mysql dataset(未完成)

    return order_idx

def get_all_data():
    # 從mysql中讀取data
    prompt = '''SELECT * FROM master'''
    cursor.execute(prompt)
    result = cursor.fetchall()
    for i in result:
        print(i)

def check_order_info(target_id):
    # 查詢訂單資訊
    target_order = [i for i in get_all_data() if i['id'] == target_id]
    for i in get_all_data():
        if i['id'] == target_id:
            return i['state']
        return 'error'

def upload_order_info(target_id, target_state):
    # 更新訂單資訊
    pass
