import pyautogui
import pyperclip
import time
import mss
import mss.tools
from PIL import Image, ImageChops, ImageStat # <-- Corrected import
import math
import sys

# --- 配置 ---
TARGET_PIXEL_X, TARGET_PIXEL_Y = 1023, 914 #识别颜色变化的区域
TARGET_COLORS_HEX = ["#FFF8F7", "#E5DFDE"] #识别的变化颜色，识别到该颜色则执行接下来的操作
CLICK_POS_1 = (1179, 897) #点击三次全选的地方
CLICK_POS_2 = (963, 1029) #点击输入框的地方
ALTERNATING_CLICK_POS_A = (1046, 936) #@第一个人的坐标
ALTERNATING_CLICK_POS_B = (1046, 983) #@第二个人的坐标

# 将十六进制颜色转换为 RGB 元组
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

TARGET_COLORS_RGB = [hex_to_rgb(c) for c in TARGET_COLORS_HEX]

# 颜色近似度检查 (使用欧氏距离)
# tolerance 值越小，要求颜色越接近。可以根据实际情况调整。
COLOR_TOLERANCE = 20 # 允许的颜色差异容差

def get_pixel_color(x, y, sct):
    """获取指定屏幕坐标的像素颜色 (RGB)"""
    monitor = {"top": y, "left": x, "width": 1, "height": 1}
    try:
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        return img.getpixel((0, 0))
    except Exception as e:
        print(f"  Error getting pixel color at ({x},{y}): {e}")
        return None # Return None or a default color if grabbing fails

def color_distance(rgb1, rgb2):
    """计算两个 RGB 颜色之间的欧氏距离"""
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)

def is_color_close(actual_rgb, target_rgbs, tolerance):
    """检查实际颜色是否与目标颜色列表中的任何一个足够接近"""
    if actual_rgb is None: # Handle cases where pixel grabbing failed
        return False
    for target_rgb in target_rgbs:
        if color_distance(actual_rgb, target_rgb) <= tolerance:
            return True
    return False

def capture_screen(sct):
    """捕获整个屏幕并返回 PIL Image 对象"""
    try:
        # Ensure using the primary monitor, adjust sct.monitors index if needed
        monitor = sct.monitors[1] 
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        return img
    except Exception as e:
         print(f"Error capturing screen: {e}")
         return None # Return None if capture fails

# --- 主逻辑 ---
print("脚本启动，开始监测屏幕变化...")
print(f"目标像素: ({TARGET_PIXEL_X}, {TARGET_PIXEL_Y})")
print(f"目标颜色 (RGB): {TARGET_COLORS_RGB}")
print(f"颜色容差: {COLOR_TOLERANCE}")
print("按 Ctrl+C 停止脚本。")

# pyautogui 配置
pyautogui.PAUSE = 0.05 # 轻微增加指令间的暂停时间，提高稳定性
pyautogui.FAILSAFE = True # Keep failsafe enabled (move mouse to corner to stop)

# 初始化屏幕捕获和状态
click_next_pos_A = True # 控制交替点击的位置，True表示下次点A
last_screen_img = None
try:
    with mss.mss() as sct:
        # Initial screen capture
        last_screen_img = capture_screen(sct)
        if last_screen_img is None:
             print("无法获取初始屏幕截图，脚本退出。")
             sys.exit(1) # Exit if initial capture fails

        while True:
            current_screen_img = capture_screen(sct)
            if current_screen_img is None:
                 print("无法获取当前屏幕截图，跳过此次检测。")
                 time.sleep(1) # Wait longer if capture fails
                 continue # Skip to the next loop iteration

            # 1. 检测屏幕变化 (比较当前屏幕和上一帧)
            screen_changed = False
            if last_screen_img.size == current_screen_img.size: # Ensure images are comparable
                try:
                    diff = ImageChops.difference(current_screen_img, last_screen_img)
                    diff_stat = ImageStat.Stat(diff)
                    # sum is a list of sums for each band (R, G, B)
                    change_magnitude = sum(diff_stat.sum) / (current_screen_img.width * current_screen_img.height * len(diff_stat.sum)) * 100
                    # 设置一个变化阈值，例如 0.05%，避免微小噪声触发 (adjust as needed)
                    screen_changed = change_magnitude > 0.05 
                except Exception as e:
                    print(f"Error comparing images: {e}")
                    # Decide how to handle comparison errors, maybe assume change or no change
                    screen_changed = False # Assume no change if comparison fails
            else:
                 print("屏幕尺寸发生变化，无法比较。")
                 # Treat size change as a significant change? Or ignore?
                 screen_changed = True # Let's assume size change is a trigger

            if screen_changed:
                print(f"检测到屏幕变化 (幅度: {change_magnitude:.4f}%)，检查目标像素颜色...")

                # 2. 获取目标像素颜色
                # Re-grab the specific pixel for maximum accuracy at this moment
                current_pixel_color = get_pixel_color(TARGET_PIXEL_X, TARGET_PIXEL_Y, sct)

                if current_pixel_color: # Check if pixel color was obtained successfully
                    print(f"  坐标 ({TARGET_PIXEL_X}, {TARGET_PIXEL_Y}) 的颜色: {current_pixel_color}")

                    # 3. 检查颜色是否近似匹配
                    if is_color_close(current_pixel_color, TARGET_COLORS_RGB, COLOR_TOLERANCE):
                        print(f"  颜色匹配！执行操作序列...")

                        # --- 执行操作 ---
                        try:
                            # a. 连续点击 (1179, 897) 三次，间隔 0.1s
                            print(f"  - 点击 {CLICK_POS_1} 三次")
                            for _ in range(3):
                                pyautogui.click(CLICK_POS_1[0], CLICK_POS_1[1])
                                time.sleep(0.1)

                            # b. 执行 Ctrl+C
                            print("  - 按下 Ctrl+C")
                            pyautogui.hotkey('ctrl', 'c')
                            time.sleep(0.2) # Slightly longer wait for clipboard

                            # c. 读取剪切板，处理内容
                            clipboard_content = pyperclip.paste()
                            print(f"  - 读取剪切板: '{clipboard_content[:50]}...'")
                            space_index = clipboard_content.find(' ')
                            if space_index != -1:
                                modified_content = clipboard_content[space_index + 1:]
                                pyperclip.copy(modified_content)
                                print(f"  - 修改后剪切板: '{modified_content[:50]}...'")
                            else:
                                print("  - 剪切板内容中未找到空格，未修改。")
                                # Ensure clipboard still contains original content if needed for paste
                                pyperclip.copy(clipboard_content) 

                            # d. 间隔 0.3s
                            time.sleep(0.3)

                            # e. 点击 (963, 1029)
                            print(f"  - 点击 {CLICK_POS_2}")
                            pyautogui.click(CLICK_POS_2[0], CLICK_POS_2[1])
                            time.sleep(0.1) # Small delay after click

                            # f. 输入 '@' 键
                            print("  - 输入 @")
                            pyautogui.write('@') # Use write for better compatibility sometimes
                            time.sleep(0.1) # Small delay after typing

                            # g. 交替点击 (1046, 936) 或 (1046, 983)
                            if click_next_pos_A:
                                target_click_pos = ALTERNATING_CLICK_POS_A
                                print(f"  - 点击 {target_click_pos} (A)")
                                pyautogui.click(target_click_pos[0], target_click_pos[1])
                                click_next_pos_A = False # 下次点击 B
                            else:
                                target_click_pos = ALTERNATING_CLICK_POS_B
                                print(f"  - 点击 {target_click_pos} (B)")
                                pyautogui.click(target_click_pos[0], target_click_pos[1])
                                click_next_pos_A = True # 下次点击 A
                            time.sleep(0.1) # Small delay after click

                            # h. 执行 Ctrl+V
                            print("  - 按下 Ctrl+V")
                            pyautogui.hotkey('ctrl', 'v')

                            # i. 间隔 0.2s
                            time.sleep(0.2)

                            # j. 执行 Alt+S
                            print("  - 按下 Alt+S")
                            pyautogui.hotkey('alt', 's')

                            print("  操作序列完成。")
                            # 短暂暂停，避免操作刚完成就立即触发下一次检测
                            time.sleep(0.5)

                        except Exception as action_e:
                             print(f"  --- 执行操作时发生错误: {action_e} ---")
                             # Decide if you want to stop or continue monitoring
                             # For robustness, we'll continue monitoring here
                             time.sleep(1) # Pause after error before next check

            # 更新上一帧图像，用于下次比较
            last_screen_img = current_screen_img

            # 短暂休眠，避免 CPU 占用过高
            time.sleep(0.5) # 检测间隔，可以调整 (e.g., 0.2 or 0.5)

except KeyboardInterrupt:
    print("\n脚本被用户中断。")
except Exception as e:
    print(f"\n发生未处理的错误: {e}")
finally:
    print("脚本退出。")