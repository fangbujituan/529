# 1、使用循环计算阶乘
# 2、运用递归计算阶乘
# 3、调用reduce函数计算


# 循环函数
def frat(n):
    r = 1

    if n< 1:
        return
    else:
        # i从1循环到n
        for i in range(1, n+1):
            r *= i
        return r
print(frat(9))

# 递归函数
def frat2(n):
    if n == 1:
        return 1
    else:
        return n * frat2(n - 1)
print(frat2(9))

# functools函数
import functools
def fn(x, y):
    return x * y
def frat3(n):
    if n == 1:
        return 1
    else:
        return functools.reduce(fn, range(1, n + 1))
print(frat3(9))