data = [[3, 5, 1],[10, 2],[8, 9, 7, 6]]

len_max=0
for i in range(len(data)):
    len_max = len(data[i]) if len(data[i]) > len_max else len_max
    #print(len_max)

for i in range(len(data)): #没有负数的话
    while len(data[i]) < len_max:
        data[i].append(0)
    #print(data[i])
row=[]
for i in range(len(data[0])):
    r=0
    for j in range(len(data)):
        if data[j][i] > r:
            r = data[j][i]
    row.append(r)
print(row)

'''2.0'''
# 找出最长行的长度
len_max = max(len(row) for row in data)

result = []
for i in range(len_max):
    max_val = None
    for row in data:
        if i < len(row):  # 如果这一行有第i列
            if max_val is None or row[i] > max_val:
                max_val = row[i]
    result.append(max_val)

print(result)  # 输出：[10, 9, 7, 6]