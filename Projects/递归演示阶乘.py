def fact(a):
    if a == 1:
        return 1 # 递归终止条件
    else:
        return a * fact(a - 1) # 递归调用自身
print(fact(5)) # 120