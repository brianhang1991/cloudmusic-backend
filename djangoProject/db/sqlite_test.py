#!/usr/bin/python

import sqlite3


conn = sqlite3.connect('D:\work\cloudmusic-backend\djangoProject\db\music.db')

cursor = conn.cursor()
print("数据库打开成功")
# 执行查询语句
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# 获取查询结果
tables = cursor.fetchall()

# 打印所有表的名称
for table in tables:
    print(table[0])

conn.close()