import pyautogui as pag
import random
import time

def mouseMoveAround():
    while True: 
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        
        print('mouse move!')
        pag.moveTo(x, y, 0.5)
        time.sleep(180)
        # 300(5 Min), 1800(30 Min)