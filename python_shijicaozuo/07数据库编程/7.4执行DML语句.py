import sqlite3

# 获取数据库连接
conn = sqlite3.connect("test.db")

# 获取游标
cur = conn.cursor()

# 执行sql
cur.execute('insert into user_tb values (null, ?, ?, ?)', ('fkjava','33345', '23'))
cur.execute('insert into user_tb values (null, ?, ?, ?)', ('sdfs','33345', '24'))
cur.execute('insert into user_tb values (null, ?, ?, ?)', ('sdfsdfs','33345', '25'))
cur.executemany('insert into user_tb values (null, ?, ?, ?)',
                (('fkjava','33345', '23'),('fkjava','33345', '23'),('fkjava','33345', '23')))

# 提交事务使修改生效
conn.commit()

# 关闭资源
cur.close()
conn.close()