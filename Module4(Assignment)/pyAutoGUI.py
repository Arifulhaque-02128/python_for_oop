import pyautogui
import time

n = int(input())

time.sleep(2)

for i in range(n+1) :
    for j in range(i) :
        pyautogui.write("#", interval=0.25)
    pyautogui.press('enter')






