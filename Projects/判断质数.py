while True:
    num =  input("输入数字")
    if num.lower() == 'q' :
        break
    else:
        pass
    
    for i in num :
        if i == '.' :
            print('请输入整数');exit()
    if i not in ['1','2','3','4','5','6','7','8','9','0'] :
            print('请输入数字');exit()
    
    num=int(num)
    if num%2 == 0:
        print('不是质数')
    else:
        for i in range(3,int((num+1)/2),2):
            if num%i == 0:
                print(f'不是质数,{i}');break
        else: 
            print('是质数')
