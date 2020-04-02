"""
内容：斐波那契数列
        |n = 1, f(n) = 1
    f(n)|n = 2, f(n) = 1
        |n > 2, f(n) = f(n - 1) + f(n - 2)

data：2019.6.18
"""
def feibo(n):
    first, result = 1, 1
    for x in range(n):
        first, result = result, first + result
    return result
print("总共有个%d个兔崽子诞生" % feibo(20))
# 递归实现
def feb(n):
    # n伟月数
    if n<1:
        print('输入月份错误')
        return -1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        tz = feb(n-2)+feb(n-1)
        return tz
trer = feb(20)
if trer != -1:
    print(trer)

# 汉诺塔
temp = 0
def hanno(n, x, y, z):
    if n == 1:
        global temp
        temp += 1
        print(x, '-->', z)
    else:
        global temp
        temp += 1
        hanno(n-1,x, z, y)    # 将前n-1个盘子从x移动到y上
        print(x, '-->', z)    # 将最后一个盘子从x移动到z上
        hanno(n-1,y, x, z)    # 将y上的n-1个盘子移动到z上

hanno(4,'a','b','c')
print(temp)