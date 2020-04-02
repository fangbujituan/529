# coding=utf-8
# 1、只有函数执行才会开启一个作用域。
if (2 > 1):
    x = 1
print(x)

x = 2
print(vars()["x"])  # 使用vars()函数可以访问当前作用域包含的变量。

x = 9
def func():     # 使用locals()函数可以访问局部作用域。
    print(globals()["x"])
func()
'''
每个函数定义时都会记住所在的作用域。
    函数执行的时候会开启一个新的作用域
    函数内变量访问的规则是：先访问当前作用域，
    如果没有就访问函数定义时的作用域，递归直到全局作用域。'''
print("当前x = ",x)
x = 1
def func():
    y = 2
    print(x, y)
func()

# 变量赋值始终访问的是当前作用域。
x = 1
print("当前x = ",x)

def func():
    x = 2
    y = 2
    print(x, y) # 输出2， 2
# 调用函数func
func()

# 局部变量会覆盖隐藏全局变量，想访问全局变量可以采用global关键字或globals()函数。
print("global")
x = 1

def func():
    global x    # 这是是指的全局变量
    x = 2
    y = 2
    print(x, y)    # 输出2 2

func()
print(x)    # 输出 2

# python支持闭包
print("----------------------------")
def func(x):
    def inner_func(y):
        print(x + y)

    return inner_func
inner_func = func(10)
inner_func(1)
inner_func(2)

# 函数作为对象
def func(fn, arg):
    fn(arg)

func(print, 'hello')
func(lambda arg:print(arg),'hello')

