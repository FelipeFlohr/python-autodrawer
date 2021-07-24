import keyboard
import pyautogui
from time import sleep

def getpos():
    while True:
        sleep(0.01)
        if keyboard.is_pressed('ctrl'):
            print(pyautogui.position())

getpos()