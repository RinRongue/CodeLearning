import random
import turtle
while True:
    time=input('模拟次数：')
    try:
        time=int(time)
    except:
        time=input('模拟次数：')
    else:
        break
    
#画画乌龟
turtle.setup(400,400)
turtle.speed(0)
turtle.pensize(1)
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.goto(100,-100);turtle.goto(-100,-100);turtle.goto(-100,100);turtle.goto(100,100)
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)

#写字乌龟
text_turtle = turtle.Turtle()
text_turtle.speed(0)
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(-150, 150)

#循环
time1 =0
count =0
while time1<time:
    x = random.uniform(-100,100)
    y = random.uniform(-100,100)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    if pow(x,2)+pow(y,2)<=10000:
        count+=1
        turtle.dot(3,'green')
    else:
        turtle.dot(3,'red')
    time1+=1

    text_turtle.clear()
    text_turtle.goto(-150, 150)
    text_turtle.write(f'绿色点数量: {count}', font=("Microsoft YaHei UI", 12, "normal"))
    text_turtle.goto(-150, 130)
    text_turtle.write(f'红色点数量: {time1-count}', font=("Microsoft YaHei UI", 12, "normal"))
    text_turtle.goto(-150, 110)
    text_turtle.write(f'pi ≈ {((count / time1) * 4):.2f}', font=("Microsoft YaHei UI", 12, "normal"))
    text_turtle.goto(-150, 150)

print(f'pi≈{(count/time)*4:.2f}')

turtle.done()