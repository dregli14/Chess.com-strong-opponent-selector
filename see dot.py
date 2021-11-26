from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import numpy as np

time.sleep(5)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    
#In the region domain you should modify it so it can match your particular needs
                         
while not keyboard.is_pressed ('q'):
    start= pyautogui.locateCenterOnScreen('dot.png', region=(1142,384,250,100), confidence=0.8) 
    if start is not None:
        pyautogui.moveTo(start)
        pyautogui.click(start)
    
