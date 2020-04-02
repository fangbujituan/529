"""
内容：集合
data：2019.6.19
"""
# 1. 用{}括起来的，但是没有体现映射关系，集合中的元素是无序的，集合中的元素输出后都是唯一的
num1 = {}
print(num1)
num1 = {1,2,3,4,5}
print(num1)
set1 = {}
set2 = set([1,2,3,4,5,6])    # 用set（）创建集合参数为列表
print(set1)
print(set2)


list1 = [1, 2, 3, 4, 4, 2, 7, 8, 9]
list1 = list(set([1, 2, 3, 4, 4, 2, 7, 8, 9]))
print(list1)
print(0 in list1)
# 4. 访问集合
set2 = {1, 3, 2, 4, 5, 9, 5, 7, 6, 8}  # 集合中的元素是无序，如果元素是数字，输出时自动排序，如果有字符串，输出无序

for i in set2:
    print(i, end=' ')

set3 = frozenset({1,2,3,4})
