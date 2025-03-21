import turtle
import time

def drawgap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawline(draw):  # 绘制单个数字
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawdigit(digit):  # 根据数字绘制七段数码管
    drawline(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20) # 为绘制后续数字确定位置

def drawdate(date):  # 获得要输出的数字
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年', font=('Arial', 18, 'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=('Arial', 18, 'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=('Arial', 18, 'normal'))
        else:
            drawdigit(eval(i))  # 通过eval()函数将数字变为整数  

def main():
    turtle.speed(0)
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()

main()