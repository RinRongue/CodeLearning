digit=int(input('前多少个质数？'))
a=0
b=3
output=f"2"
while True:
    if b%2 ==0:
        pass
    else:
        for i in range(3,int((b**0.5) + 1),2):
            if b%i == 0:
                break
        else:
            output += f"    {b}"
            a+=1
    b+=1
    if a==digit:
        break

with open("primes.txt", "w") as f:
    f.write(output)

print(f"前{digit}个质数已保存到 primes.txt 文件中。")
#print(output)