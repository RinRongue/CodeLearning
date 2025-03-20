import secrets
num=secrets.randbelow(101)
time=0

while True:
    guess=input('臭大叔0-100数字捏：')
    time+=1
    try:
        guess=int(guess)
    except ValueError:
        print('你要不要玩了啊臭杂鱼❤')
        continue
    else:
        guess=int(guess)

    if guess<0 or guess>100:
        print('你要不要玩了啊臭杂鱼❤')
    elif guess>num:
        print('杂鱼，大了捏❤')
    elif guess<num:
        print('杂鱼，小了捏❤')
    else:
        print(f'猜对了捏❤，用了{time}次捏')
        break