#将元音字母转为t python
String_input = input('输入要转换的英文')
String_print = ''
for i in String_input:
    if i in ['a','e','i','o','u']:
        String_print += 't'
    else:
        String_print += i
print (String_print)