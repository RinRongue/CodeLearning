import tkinter as tk
import pyautogui
import keyboard

x, y = None, None

def update_position():
    """更新鼠标位置并显示在窗口中"""
    global x, y
    x, y = pyautogui.position()
    label.config(text=f"X: {x}  Y: {y}")
    root.after(100, update_position)  # 每100毫秒更新一次

def check_keyboard():
    """检查键盘输入"""
    global x, y
    if keyboard.is_pressed('enter'):
        print(f"X: {x}  Y: {y}，比例：{x/2560:.2f}  {y/1440:.2f}")  # 打印鼠标坐标和比例
    if keyboard.is_pressed('esc'):
        root.destroy()  # 关闭窗口并退出程序
        return
    root.after(100, check_keyboard)  # 每100毫秒检查一次键盘输入

# 创建 Tkinter 窗口
root = tk.Tk()
root.title("鼠标坐标")
root.geometry("250x50+21+1571")
root.overrideredirect(True)  # 去边框
root.attributes("-topmost", True)  # 总在最上
root.wm_attributes("-transparentcolor", "white")
root.configure(bg='white')

# 创建标签用于显示鼠标坐标
label = tk.Label(root, text="", font=("微软雅黑", 14), bg='white', fg='black')
label.pack(expand=True)

# 启动鼠标位置更新和键盘检查
update_position()
check_keyboard()

# 启动 Tkinter 主事件循环
root.mainloop()