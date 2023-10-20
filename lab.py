import pymysql

# 连接到MySQL数据库
connection = pymysql.connect(
    host="vultr-prod-0735f93d-5e03-4e4b-b1ae-878c590715ab-vultr-prod-7d22.vultrdb.com",     # MySQL服务器的主机名或IP地址
    user="vultradmin", # MySQL用户名
    password="AVNS_PcAfxyST1X5nxEzfYSq", # MySQL密码
    database="order",
    port=16751
)

# 创建一个游标对象，用于执行SQL查询
cursor = connection.cursor()

# prompt = '''
# CREATE TABLE master(id VARCHAR(100) PRIMARY KEY,total INT,status TINYINT)'''

prompt = '''SELECT `COLUMN_NAME` 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='order' 
    AND `TABLE_NAME`='example';'''
#sql = "INSERT INTO example (item,flavor,qty) VALUES (%s,%s,%s)"
sql = "SELECT * FROM example"
values = ('2',"011","0")


cursor.execute(sql)
connection.commit()
result = cursor.fetchall()

print(result)