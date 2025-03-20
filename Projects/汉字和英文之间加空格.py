#汉字和英文之间加空格
#半角字符的ASCII在0-127之间，全角字符的ASCII码大于127，用ord()函数可以查看字符的ASCII码
Len=input('输入要加入空格的文字')
x = 0 ; y = 0 #y存储上一个字符的ASCII码，x存储当前字符的ASCII码
Len1 = '' #存储最终结果
for i in Len:
    if i == " ":
        Len1 += i
        x = 32
    elif ord(i) > -1 and ord(i) <128 :
        x = ord(i)
        if y > -1 and y < 128:
            Len1 += i
            y=x
        else:
            Len1 += ' ' + i
            y=x
    elif ord(i) >127 or ord(i) < 0:
        x = ord(i)
        if y > 127 or y < 0 :
            Len1 += i
            y = x
        else:
            Len1 += ' ' + i 
            y = x

#如果第一个字符是空格，删除它，前提条件是输入的第一个字符不是空格
if Len1[0] == ' ' and Len[0] != ' ':
    Len1 = Len1[1:]

#copliot都帮我写完了，我要失业了
print(Len1)