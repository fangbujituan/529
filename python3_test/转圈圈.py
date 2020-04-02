
def maini(size):
    # 主函数

    # 得到一个size * size的二维数组
    array = [[0] * size]
    for i in range(size - 1):
        array += [[0] * size]

    # 给二维数组赋值
    git_num(size, array)

    # 打印二维数组的方法
    print_arr(array)


# 给二维数组赋值
def git_num(size, array):
    # 控制方向：0代表向下，1代表向右，2代表向左，3代表向上
    orient = 0

    # j控制行，k控制列
    j, k = 0, 0
    # 控制程序将1~size*size-1的数字填到矩阵中
    for i in range(1, size * size + 1):
        array[j][k] = i
        # ①号转弯线
        if j + k == size - 1:
            # 行大于列 位于下半
            if j > k:
                orient = 1
            # 位于下半
            else:
                orient = 2
        # 位于②号转弯线
        elif j == k and j >= size / 2:
            orient = 3
        # 位于三号转弯线
        elif j + 1 == k and k <= size / 2:
            orient = 0

        if orient == 0:  # 0代表向下
            j += 1
        elif orient == 1:  # 1代表向右
            k += 1
        elif orient == 2:  # 2代表向左
            k -= 1
        elif orient == 3:  # 3代表向上
            j -= 1

# 打印二维数组的方法
def print_arr(array):
    # 打印二位列表array
    for ele in array:
        for e in ele:
            print('%03d' % e, end=' ')
        print()

maini(15)