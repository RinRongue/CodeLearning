- [re-正则表达式](#re)
   - [常用表达式](#常用表达式)
   - [常用通配符](#常用通配符)

# re
## 常用表达式
<span style='font-color:red;'>re.findall()</span>  
查找所有匹配的部分，返回一个列表  
```
result = re.findall(r'apple', 'I have an apple and another apple.')  
print(result)  #['apple', 'apple']
```
---
re.match()  
从字符串的**开头**匹配正则表达式。如果正则表达式能在字符串的开头匹配成功，就返回一个匹配对象；否则返回None  
```
text = "Hello, world!"
# 检查字符串是否以 "Hello" 开头
match = re.match(r'Hello', text)
if match:
    print("匹配成功:", match.group())
else:
    print("没有匹配成功") #匹配成功: Hello
```
---
re.search()
扫描整个字符串，返回第一个匹配的结果，否则返回None  
```
text = "My email is alice@example.com."
# 搜索字符串中的第一个邮箱地址
search = re.search(r'\w+@\w+\.\w+', text)
if search:
    print("找到邮箱:", search.group())
else:
    print("没有找到匹配的邮箱") #找到邮箱: alice@example.com
```
---
re.sub()   
用于替换匹配到的字符串。接受三个参数：要匹配的正则表达式、替换的内容、以及目标字符串。  
```
text = "My phone number is 123-456-7890."
# 将电话号码格式改为 'XXX-XXX-XXXX'
new_text = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
print("替换后的文本:", new_text) #替换后的文本: My phone number is XXX-XXX-XXXX.
```
---
re.split()   
用于根据正则表达式分割字符串。返回一个列表，包含所有分割出的部分。  
```
text = "apple,banana,orange,grape"
# 根据逗号分割字符串
split_text = re.split(r',', text)
print("分割后的列表:", split_text) #分割后的列表: ['apple', 'banana', 'orange', 'grape']
```
---
re.finditer()  
与 findall() 类似，区别在于它返回的是一个迭代器，迭代器中包含匹配对象，每个匹配对象都可以提供更多的信息（比如匹配的起始位置和结束位置）。
```
text = "I have 123 apples and 456 oranges."
# 使用 finditer 查找数字
matches = re.finditer(r'\d+', text)
for match in matches:
    print(f"匹配到的数字: {match.group()}, 起始位置: {match.start()}, 结束位置: {match.end()}")
#匹配到的数字: 123, 起始位置: 7, 结束位置: 10
 匹配到的数字: 456, 起始位置: 22, 结束位置: 25
```
---
re.compile()   
用来编译正则表达式的，返回一个正则表达式对象，可以复用这个正则表达式而不需要每次都调用 re 方法。通常用在你需要多次使用同一个正则表达式的场景中，性能会更好。  
```
# 编译一个正则表达式
pattern = re.compile(r'\d+')
# 使用编译后的正则表达式进行匹配
matches = pattern.findall("I have 123 apples and 456 oranges.")
print("找到的数字:", matches)  #找到的数字: ['123', '456']
```
---
re.fullmatch()   
用于判断整个字符串是否完全符合正则表达式。  
```
text = "12345"
# 检查整个字符串是否完全由数字组成
if re.fullmatch(r'\d+', text):
    print("字符串完全是数字！")
else:
    print("字符串不是完全由数字组成") #字符串完全是数字！
```
---
## 常用通配符
|匹配字符|含义|
|---|---|
|a|匹配字母 "a"（单个字符）|
|.|匹配任何单个字符（除了换行符）|
|\\ |转义字符，用来匹配特殊字符本身（如 \. 匹配一个点，\* 匹配星号）|
|$|匹配字符串结尾|
|*|	匹配前面的字符 0 次或多次|
|+|匹配前面的字符 1 次或多次|
|?|匹配前面的字符 0 次或 1 次|
|{n}|精确匹配 n 次|
|{n,}|匹配至少 n 次|
|{n,m}|匹配 n 到 m 次|
|[]|字符类，匹配括号内的任意字符|
|()|分组，用来分割或提取匹配的部分|
  
|常用字符|含义|
|---|---|
|\\d	|匹配任何数字（0-9）|
|\\D	|匹配任何非数字字符|
|\\w	|匹配任何字母、数字和下划线（a-z, A-Z, 0-9, _）|
|\\W	|匹配任何非字母、非数字、非下划线字符|
|\\s	|匹配任何空白字符（如空格、换行）|
|\\S	|匹配任何非空白字符|




