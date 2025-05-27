import readfolder
file_name=readfolder.readfile()
while True:
    if file_name[-3:] not in ['csv', 'txt']:
        print('文件格式不正确，请输入csv或txt文件')
        file_name = readfolder.readfile()
    else:
        break

with open(file_name,'r',encoding='utf-8')as f1:
    old=list()
    for i in f1.readlines():
        row = [x for x in i.strip().split(',')]
        old.append(row)
print(old)

with open('new.csv','w',encoding='utf-8')as f2:
    i = 0
    while i<len(old):
        new=""
        for j in range(len(old)):
            if j+1 < len(old[j]):
                new+= f"{old[j][i]},"
            else:
                new+= f"{old[j][i]}"
        i+=1
        f2.write(f'{new}\n')