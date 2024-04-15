import pyautogui as screen
import time
import random
import pyautogui
x,y = screen.size()
while True:
    x1= random.randint(0,x)
    y1= random.randint(0,y)
    pyautogui.moveTo(x1,y1)
    pyautogui.click()
    time.sleep(59)