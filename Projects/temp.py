#tempcovert.py
Temp = input('输入温度')
if Temp[-1] in ['c' , 'C']:
	print('输出温度为{:.2f}F'.format(1.8 * eval(Temp[0:-1]) + 32))
elif Temp[-1] in ['f' , 'F']:
    print(f'输出温度为{(eval(Temp[:-1])-32)/1.8:.2f}C')
else :
	print('错误')