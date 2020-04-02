import sqlite3

# 获取数据库连接
conn = sqlite3.connect("test.db")

# 获取游标
cur = conn.cursor()

# 执行sql
cur.execute('select * from user_tb where _id > ?', (2,))

# 所有查询都通过游标来获取,description返回元组
for col in cur.description:
    print(col[0])
print()

for row in cur:
    for d in row:
        print(d,end='\t')
    print()
# 提交事务使修改生效
conn.commit()

# 关闭资源
cur.close()
conn.close()