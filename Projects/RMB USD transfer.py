'''人民币和美元是世界上通用的两种货币之一，写一个程序进行货币间币值转换，其中：
人民币和美元间汇率固定为：1美元 
程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用RMB表示，美元USD表示，符号和数值之间没有空格。'''
MMM=input()
if MMM[:3] == 'RMB':
    USD=eval(MMM[3:])/6.78
    print("USD{:.2f}".format(USD))
elif MMM[0:3] == 'USD':
    RMB=eval(MMM[3:])*6.78
    print("RMB{:.2f}".format(RMB))
