# 字符串
使用' '或" "
使用''' '''创建多行字符串
## 索引和切片
正向递增序号0\~a  
反向递减序号a\~-1  
`<字符串>[M,N,K]` M开始，N结束，以步长K获取字符  
`<字符串>[M,N,-1]` 把M到N的字符串倒过来  
## 转义符
```
\b #回退
\n #换行
\r #回车
```
## 字符串格式化
槽{}  
![](string0.png)
```python

```

## 字符串操作符
```python
x+y #连接xy
x*n ; n*x #复制n次x
x in s #判断x是否为s子串，返回布尔值
```
## 字符串处理函数
```python
len(x) #返回x长度

str(x) #将任意内容x变成字符串
eval(x) #将字符串x变成语句

chr(x) #unicode转字符
ord(x) #字符转unicode (0x10FFFF)

hex(x) #十进制整数转16进制字符串
oct(x) #十进制整数转8进制字符串
```
## 字符串处理方法
```python
#str用于表示字符串
str.lower() #str小写 'AbC' > 'abc'
str.upper() #str大写

str.split(sep=None) #按照sep分隔str 'A,BC:D'.split(':') >['A,BC','D']
str.count(sub) #返回str出现sub的次数
str.replace(old,new) #'ABC'.replace('A','a') > 'aBC'
str.strip(chars) #去除两侧的chars列出的字符 'ABCDCDCBA'.strip('ABC') > 'DCD'
str.join(iter) #在str除最后一个元素外每个元素后加一个iter，用于分隔 'abc'.join('+') > 'a+b+c'
str.center(width[,fillchar]) #在width宽度中居中，两侧用fillchar填充
```
# 数据运算
```python
pow(x,y) #x^y
```
# 循环
## if loop
```python
if a:
elif b:
else:
```
`if a else b #单行if`

```python
if a in []:
if a not in []: #检查元素是否在序列（如列表、字符串、字典）中
if a is/not is []: #用于比较对象是否是同一个（内存地址 是否相同）
```
### match-case
```python
match a:
  case 1:
    b
  case 2:
    c
#用于模式匹配
```
# for loop
` for i in range(): `
```python
for :
  print(a,end="") #每次输出后不换行
```

# while loop

# try-except



# 自定义函数
```python
def factor(a):
  ...
return factor
```
# 官方库

# time库

## turtle库
```python
turtlre.setup(width,height,startx,starty) #设置窗体大小位置，后两项非必须
turtle.pensize(len)
turtle.pencolor(a,b,c) #可用整数或小数或名称  
turtle.colormode(mode) #mode=1.0 或 255  
turtle.penup()  
turtle.pendown()
turtle.fd(len) #往前爬len像素  
turtle.goto(x,y)  
turtle.circle(len,angle)  #画angle度直径len的圆  
turtle.seth(angle) #逆时针  
turtle.left(angle) #往左转  
turtle.right(angle)  
turtle.done()
```
![](/PythonDCIM/turtle0.jpg)

