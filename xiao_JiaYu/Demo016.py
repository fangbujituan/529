'''
* 内容：
    迭代器，生成器(generator)
* 用到的关键字：
    enumerate  lambda表达式
* data ：2019.06.26
* @author：fangbu
** 来自：https://www.cnblogs.com/wj-1314/p/8490822.html
'''
# 列表生成器
'''首先举个例子
现在有个需求，看列表 [0，1，2，3，4，5，6，7，8，9]，
要求你把列表里面的每个值加1，你怎么实现呢？
'''
# 方法一（简单）：
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
for index,i in enumerate(info):
    info[index] += 1
print("方法一",info)

# 方法二（一般）：
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = map(lambda x:x+1,info)
print("方法二",a)
for i in a:
    print(i,end=',')
print()

# 方法三（高级）：
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [i+1 for i in range(10)]
print("方法三",a)

lis = [x*x for x in range(10)]
print(lis)
generator_ex = (x*x for x in range(10))
for x in generator_ex:
    print(x,end=',')

# 用函数把斐波那契数列打印出来
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        a,b = b,a+b
        n =n + 1
        print(a)
    return 'done'
a = fib(10)