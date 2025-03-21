import sys

# 设置递归深度限制
sys.setrecursionlimit(2000)

count = 0

def hanoi(n, a, b, c):  # n个盘子，a是初始柱子，b是中间柱子，c是目标柱子
    global count
    if n == 1:
        count += 1
        print('第', count, '次移动:', a, '-->', c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)

input_num = int(input('请输入汉诺塔的层数:'))
try:
    hanoi(input_num, 'A', 'B', 'C')
except RecursionError:
    print('输入的层数过大，无法计算')
except MemoryError:
    print('内存不足，无法计算')