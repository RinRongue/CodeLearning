inp=input('输入开始年月日+天数，如2024.01.01+130')
a,b=[],[]
if inp.count('+')==1:
    a=inp.split('+')
elif inp.count('-')==1:
    b=inp.split('-')
else:
    print('输入格式错误，请重新输入')
    exit()

def try1(aa):
    global y,m,d,days
    try:
        date=(aa[0])
        days=int(aa[1])
        y,m,d=map(int,str(date).split('.'))
    except:
        print('输入格式错误，请重新输入2')
        exit()
    return y,m,d,days

if a != []:
    y,m,d,days = try1(a)
else :
    y,m,d,days = try1(b)
md=[31,0,31,30,31,30,31,31,30,31,30,31]
if y%4==0:
    md[1]=29
else:
    md[1]=28
    
if a != []:
    for i in range(days):
        d+=1
        if d>md[m-1]:
            d=1
            m+=1
            if m>12:
                m=1
                y+=1
else:
    for i in range(days):
        d-=1
        if d<1:
            m-=1
            if m<1:
                m=12
                y-=1
            d=md[m-1]
print(f'计算结果为：{y}.{m:02d}.{d:02d}')
    