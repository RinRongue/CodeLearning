import os
import keyboard
try:
        os.system('taskkill /f /im gamemd.exe')
except:
    pass


if keyboard.is_pressed('ctrl+space'):
    try:
        os.system('taskkill /f /im gamemd.exe')
    except:
        pass
