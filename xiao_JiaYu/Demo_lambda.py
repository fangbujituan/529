"""
内容：lambda表达式(匿名函数),filter(过滤器)
    匿名函数的创建，lambda 变量 ：表达式
    filter语法：filter(函数，集合)
data：2019.6.17
"""
f = lambda x, y: x + y
print(f(3, 4))

# 过滤器filter
print(list(filter(lambda x : x % 2, range(10))))
def fun1(x, y = 3):
    return x * y
# 使用lambda表达式将下边函数转变为匿名函数
lambda x, y = 3 : x * y

# 3.用filter()函数和lambda表达式快速求出100以内所有3的倍数？  练习
print(list(filter(lambda x : (x % 3 == 0), range(1, 101))))
# 列表推导式代替filter()和lambda组合
print([x for x in range(1,100)if x%3==0])

# 5. 还记得zip吗？使用zip会将两数以元祖的形式绑定在一块
print(list(zip([1, 2, 3],[4, 5, 6, 7])))
# 但如果我希望打包的形式是灵活多变的列表而不是元祖（希望是[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]这种形式）
print(list(map(lambda x, y : [x, y], [1, 2, 3],[4, 5, 6, 7])))

def make_repeat(n):
    print(n)
    return lambda s:s*n
double=make_repeat(2)
print(double(8))
print(double('fishC'))
