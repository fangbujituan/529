"""
方法的练习
data：2019.6.13
"""
# 1、函数文档
def Myfuntion01(name):
    '这是我写的第一个函数文档'
    # 函数文档占一个参数位置
    print('传递进来的参数是', name, '叫做实参')

# 调用参数
print(Myfuntion01.__doc__)
print(help(Myfuntion01),'--------------------')

# 2、关键字参数
def MyFuntion(name,age):
    print(name, '->', age)

MyFuntion(age = 18, name = "fangbu")    # 关键字实现

# 3、默认参数
'''
&& 在函数定义的时候，给形式参数赋予一个默认值；调用函数的时候，如果没有给该参数赋新值，则使用函数定义时的默认值
&& 如果位置参数和默认参数都存在，则必须将位置参数放在默认参数前
'''
def MyFuntion02(age, name = '方步'):  # 默认参数后面不能有非默认参数
    print(name, '->', age)
MyFuntion02(18,'123')

# 4、可变参数
def test(age, *params, b= 'ggg'):
    print("参数的长度是：", len(params))
    print("第二个参数是：", params[1])
    print('默认参数是：', b)

test(1, 2, 'dsd', 6)


