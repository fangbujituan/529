import matplotlib.pyplot as plt

# 创建一组数字
# squares = [1, 4, 9, 16, 25]
# input_valus = [1, 2, 3, 4, 5]
# plt.plot(input_valus, squares, linewidth = 5)
#
# # 设置图表标题，并给坐标轴加上标签
# plt.title("fangbu", fontsize = 24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)
