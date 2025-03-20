'''获得用户输入的一个正整数输入，输出该数字对应的中文字符表示。
0到9对应的中文字符分别是：零一二三四五六七八九'''

num = input('输入罗马数字：')
num_str = str(num)
#num_digits = len(num_str)
b = ""
a = ['零','一','二','三','四','五','六','七','八','九']
for i in num_str:
    b += a[int(i)]
print(b)
