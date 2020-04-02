""" 第一种方法"""
import random
# 使用列表推到式来创建一个包含重复元素的列表
src_list = [random.randint(20, 30) for i in range(15)]
print(src_list)

# 用新列表收集，只收集不重复的元素
target_list = []    # 空列表

for ele in src_list:
    # 如果列表中不包含当前元素，新列表添加该元素即可
    if ele not in target_list:
        target_list.append(ele)
print(target_list)

"""第二种方式"""
src_list = [random.randint(20, 30) for i in range(15)]
print(src_list)
target_list = list(set(src_list))
print(target_list)

"""第三种方式"""
import itertools
src_list = [random.randint(20, 30) for i in range(15)]
print(src_list)
# 先对列表进行排序
src_list.sort()
# 进行分组（相同元素就分为同一组）
it = itertools.groupby(src_list)
for k, g in it:
    print(k)




