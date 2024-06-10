import pyautogui as pag
import keyboard as kb
import time

pag.PAUSE = 0
capslock = False

def mouseAutoClicker():
    while True:
        capslock = kb.is_pressed('capslock')

        if capslock:
            print('auto clicker stop!')
            exit()

        pag.moveTo(365, 650)
        pag.click()
        time.sleep(180)
