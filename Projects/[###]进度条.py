import time
scale = 10
print("------执行开始------")
for i in range(scale + 1):
    a = '#' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)
a="执行结束"
print(f"{a:-^12}")

#单行动态刷新
for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.1)