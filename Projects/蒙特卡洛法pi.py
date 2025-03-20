import random
import time

t, round = map(int, input('请输入次数和轮次（用空格分隔）: ').split())
round1=0 #计数轮次
#random.seed()
while True:
    time1=0 #计数落在圆内的次数
    time2=0 #计数循环次数
    while time2 < t:
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        if pow(x,2)+pow(y,2)<=1:
            time1+=1
        time2+=1
    print(f'{(time1 /t)*4:.4f}    ',end="")
    round1 +=1
    #time.sleep(0.1)
    if round1 == round:
        break