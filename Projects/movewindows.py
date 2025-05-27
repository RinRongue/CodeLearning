import time
import signal
import sys
import win32gui
import win32con
import win32api
from screeninfo import get_monitors
from pynput import mouse
import keyboard

# 全局变量
monitors = get_monitors()  # 获取所有监视器信息:contentReference[oaicite:5]{index=5}
for idx, m in enumerate(monitors):
    print(f"Monitor {idx}: x={m.x}, y={m.y}, resolution={m.width}x{m.height}")

last_click_monitor = None  # 最后一次鼠标点击所在的监视器索引
running = True            # 控制主循环

# 找到给定坐标所属的监视器索引
def find_monitor(x, y):
    for idx, m in enumerate(monitors):
        if m.x <= x < m.x + m.width and m.y <= y < m.y + m.height:
            return idx
    return None

# 鼠标点击回调
def on_click(x, y, button, pressed):
    global last_click_monitor
    if pressed:
        idx = find_monitor(x, y)
        if idx is not None:
            last_click_monitor = idx
            print(f"Mouse clicked at ({x}, {y}) on monitor {idx}")
        else:
            print(f"Mouse clicked at ({x}, {y}), no monitor found")
    # 返回 True 保持监听
    return True

# 注册鼠标监听（非阻塞）
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# 覆盖 Ctrl+C 信号处理，提示使用 Shift+F5 退出
def sigint_handler(signum, frame):
    print("请按 Shift+F5 终止程序 (Ctrl+C 被忽略)")
signal.signal(signal.SIGINT, sigint_handler)

# 使用 keyboard 注册 Shift+F5 热键以退出
def stop_program():
    global running
    print("检测到 Shift+F5，终止脚本。")
    running = False

keyboard.add_hotkey('shift+f5', stop_program)  # 按 Shift+F5 停止:contentReference[oaicite:6]{index=6}

# 获取当前所有可见顶层窗口的句柄集合
def get_top_windows():
    hwnds = []
    def enum_handler(hwnd, _):
        # 过滤：只要可见的顶层窗口，且无父窗口（跳过子窗口）
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetParent(hwnd) == 0:
            text = win32gui.GetWindowText(hwnd)
            if text:  # 忽略无标题窗口
                hwnds.append(hwnd)
    win32gui.EnumWindows(enum_handler, None)
    return set(hwnds)

# 初始已知窗口集合
known_windows = get_top_windows()

print("开始监听新窗口和鼠标点击事件...")

# 主循环：轮询新窗口
while running:
    current_windows = get_top_windows()
    # 发现新窗口
    new_windows = current_windows - known_windows
    for hwnd in new_windows:
        try:
            title = win32gui.GetWindowText(hwnd)
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
        except Exception:
            title = ""
            pid = None
        if title:
            print(f"检测到新窗口: '{title}' (PID={pid})")
            # 获取窗口位置和大小
            try:
                left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            except Exception:
                continue
            width = right - left
            height = bottom - top
            # 计算窗口中心点
            cx = left + width // 2
            cy = top + height // 2
            current_mon = find_monitor(cx, cy)
            target_mon = last_click_monitor
            if target_mon is not None:
                if current_mon != target_mon:
                    m = monitors[target_mon]
                    # 计算目标居中位置
                    new_x = m.x + (m.width - width) // 2
                    new_y = m.y + (m.height - height) // 2
                    # 移动窗口到目标监视器中央:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}
                    win32gui.MoveWindow(hwnd, new_x, new_y, width, height, True)
                    print(f" 移动窗口至监视器 {target_mon} 中心: ({new_x}, {new_y})")
                else:
                    print(" 窗口已在最后点击的屏幕，无需移动。")
            else:
                print(" 尚未记录鼠标点击，不移动窗口。")
    # 更新已知窗口集合
    known_windows = current_windows
    time.sleep(0.5)

mouse_listener.stop()
print("脚本已结束。")
