# -coding=utf-8

# 1、你好，世界！
print("世界 您好！")

# 2、乘方
print(2 ** 10)

# 3、变量
var = 1
print(var)
var = '闫得超'   # 注：这里的var = xxxx不叫变量赋值，而叫变量绑定，python维护了一个符号表（变量名）以及符合对应的值，这个对应关系就叫做绑定，一个符号可以绑定任意类型的值。
print(var)

# 4、获取用户输入
# x = input("x:")
# y = input("y:")
# print(x * y)    # 注：input接受的是Python代码，输入中可以访问当前执行环境中的变量，如果想获取原始输入需要使用 raw_input。

# 5、函数定义
def say_b():
    print("b")

# 6、强类型        Javascript和Php是弱类型的，Python和Ruby是强类型的。弱类型允许不安全的类型转换，强类型则不允许。
print(1 + int('1'))
print(str(1) + '1')

# 7、字符串
print('''
闫
得
超''')
print(r'c:\log.txt')
print('c:\log.txt')

# 8、序列
seq = "0123456789"
print(seq[0])    # 从0开始编码。
print(seq[-1])    # 支持倒着数数，-1代表倒数第一。
print(seq[1:5])    # 支持分片操作，seq[start:end]，start会包含在结果中，end不会包含在结果中。
print(seq[7:])     # seq[start:end]中的end可以省略。
print(seq[-3:])    # 分片也支持负数。
print(seq[:3])    # seq[start:end]中的start也可以省略。
print(seq[:])    # 全部省略会复制整个序列。
print(seq[::2])    # 支持步长。
print(seq[::-2])    #支持负步长。
print(seq[::-2]) #支持负步长。
print([1, 2, 3] + [4, 5, 6])    # 序列支持相加，这解释了为啥字符串可以相加。
print([1, 2, 3] * 5)#序列支持相乘，这解释了为啥字符串可以相称。
print([None] * 10)     # 生成一个空序列。
print(1 in [1, 2, 3, 4])#成员判断。

# 9、可变的列表
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data[0] = "a"   # 修改元素
print(data)
del data[10]    # 删除元素
print(data)
del data[8:]      # 分片删除
print(data)
data[8:] = [9, 99]
print(data)

# 10、不可变的元祖
print((1,2,3))    # 元祖以小括号形式声明。
print((1,))

# 11、字符串格式化
print("% 10s" % "0000900-()---")
print ('')
# %(title)s
# %(body)s
# ''' % {"title": "标题", "body": "内容"}

# 12、字典
dic = {"title": "title", "body": "body"}
print(dic)
print(dict(title = "title", body = "body"))
print(dict([("title", "title"), ("body", "body")]))
print(dic["title"])
del dic["title"]
print(dic)

# 13、print 语句
print('a', 'b')

# 14、序列解包
x, y, z = 1, 2, 3
print(x, y, z)
(x, y, z) = [1, 2, 3]
print(x, y, z)

# 15、bool值
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(''))
# 虽然这些值在条件运算中会当做False，但是本身不等于False。
print(True and "")
print(not "")
print(False == "")
print(False == 0)

# 16、bool运算
print(0 < 1 < 10)
print(0 < 1 and 1 < 10)
print(0 > 1 < 100)

# 17、语句块
if (10 > 1):
    print("10 > 1")
else:
    print("不会发生的事情")

# 18、三元运算符
print("10 > 1" if 10 > 1 else "不可能发生")

# 19、相等比较    == 和 is的差别，==比较的是内容，is比较的是引用。
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x == y)
print(x == z)
print(x is y)
print(x is z)

# 20、循环        #for循环类似C#的foreach，注意for后面是没有括号的，python真是能简洁就尽量简洁。
for x in range(1,10):
    print(x,end=' ')

for key in {'x':'xxx'}:
    print(key)


for key, value in {'x':'xxx'}.items():  # items()以列表返回可遍历的(键, 值) 元组数组
    print(key, value)

for x, y, z in [["a", 1, "A"],["b", 2, "B"]]:
    print(x, y, z)
# 带索引的遍历
for index, value in enumerate(range(0, 10)):    # enumerate 对一个可遍历的数据对象(如列表、元组或字符串)，enumerate 会将该数据对象组合为一个索引序列，同时列出数据和数据下标
    print(index, value)


# 好用的zip方法
print("好用的zip方法")
for x, y in zip(range(1,9),range(1,10)):
    print(x, y)

# 循环中的的else子句
from math import sqrt
for item in range(99, 1, -1):
    root = sqrt(item)
    if(root == int(root)):
        print("item=", item)
        break
else:
    print("没有执行break语句。")

# 21、pass、exec和eval
print("21、pass、exec和eval")
if(1 == 1):
    pass

exec('print(x)', {"x": "abc"})
print(eval('x*2', {"x": 5}))

# 22、函数部分
def func():     # 基本函数定义。
    print("func")
func()

def func_with_return():     # 带返回值的函数
    return ("func_with_return")
print(func_with_return())

def func_with_muti_return():
    return ("func_with_muti_return", "func_with_muti_return")
print(func_with_muti_return())

def func_with_parameters(x, y):     # 位置参数
    print(x, y)
func_with_parameters(1, 2)

def func_with_collection_rest_parameters(x, y, *rest1):      # 收集多余的位置参数
    print(x, y)
    print(rest1)
func_with_collection_rest_parameters(1, 2, 3, 4, 5)

print("命名参数")
def func_with_named_parameters(x, y, z):    # 命名参数
    print(x, y, z)
func_with_named_parameters(z = 1, y = 2, x = 3)

def func_with_default_value_parameters(x, y, z = 3):    # 默认值参数
    print(x, y, z)
func_with_default_value_parameters(x = 1,y = 8)

def func_with_collection_rest_naned_parameters(*args, **named_agrs):    # 收集命名参数
    print(args, named_agrs)
func_with_collection_rest_naned_parameters(1, 2, 3, x = 4, y = 5, z = 6)
'''
函数传参时有多种：
位置参数，默认参数，可变参数，关键字参数，命名关键字参数，参数组合
'''