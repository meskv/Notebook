import pyautogui
import webbrowser as wb
import time

wb.open("web.whatsapp.com")
time.sleep(30)

for i in range(5):
    pyautogui.press("Hello")