# f = open()
# print(help(open))

# 读文件
# f = open('aaa.txt', 'r')

# 写文件
# f = open('aaa.txt', 'w')

# r+模式，抛异常
# f = open('aaa.txt', 'r+')

# a模式，追加模式，如果文件不存在，自动创建
f = open('aaa1.txt', 'a')
f.write('bbbbbbbb')
# f.write('jijnbujsnkdjf')
# print(f.read())
f.close()
