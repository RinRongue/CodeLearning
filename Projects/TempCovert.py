#转换温度
#C和F在后面
TempStr = input("输入温度：")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) -32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
#C和F在前面
elif TempStr[0] in ['f' , 'F']:
    C = (eval(TempStr[1:]) -32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[0] in ['c' ,'C']:
    F = 1.8*eval(TempStr[1:])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输错")  
