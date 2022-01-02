import pyautogui
import time

while True:
    time.sleep(70)
    pyautogui.press("esc")
    time.sleep(0.5)
    pyautogui.hotkey("win", "m")
