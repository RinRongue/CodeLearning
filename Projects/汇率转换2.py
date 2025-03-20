#RMB USD Transfer Python
import requests as r
from forex_python.converter import CurrencyRates as c

#从forex_python请求汇率
def forex_get_rate():
    try:
        ratea = c().get_rate('USD', 'CNY')
        return ratea
    except Exception as e:
        print(f'请求失败，错误信息: {e}, 使用默认值6.78')
        return 6.78

#从API请求汇率
def API_get_rate():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=CNY"
    response = r.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            return data["rates"]["CNY"]
        except:
            print(f"API请求失败，无Access Key，尝试使用forex_rate请求汇率")
            return forex_get_rate()
    else:
        print(f"API请求失败，状态码：{response.status_code}，尝试使用forex_rate请求汇率")
        return forex_get_rate()
 
Rate = API_get_rate()
print (f"当前汇率{Rate}")

while True :
    Dollar = input("输入以“RMB“或“USD”开头+数字，退出输入“exit”")

    if Dollar.lower()  == "exit":
        break
    elif Dollar[:3].upper() == "RMB":
        USD = float(Dollar[3:])/Rate
        print('USD{:.2f}'.format(USD))
    elif Dollar[:3].upper() == 'USD':
        RMB = float(Dollar[3:])*Rate
        print(f'RMB{RMB:.2f}')
    else:
        print("输入错误")