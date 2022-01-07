import pyautogui
import time
# pyautogui.getWindowsWithTitle("Bombcrypto")[0].maximize()
start = ''
mtm = ''
hunt = ''
open_hero = ''
# while start == '' or start == None : 
#     start = pyautogui.locateCenterOnScreen('wallet.png',grayscale=False)
#     print(start)
# if start != None :
#     pyautogui.moveTo(start)
#     time.sleep(2)
#     pyautogui.click()
#     time.sleep(5)
# while mtm == '' or mtm == None : 
#     mtm = pyautogui.locateCenterOnScreen('approve_mtm.png',grayscale=False)
#     print(mtm)
#     pyautogui.moveTo(mtm)
#     time.sleep(2)
#     pyautogui.click()
while hunt == '' or hunt == None : 
    hunt = pyautogui.locateCenterOnScreen('hunt.png',grayscale=False)
    if hunt != None :
        print(hunt)
        pyautogui.moveTo(hunt)
        time.sleep(2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveRel(0,270)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.moveRel(0,-350)
        time.sleep(3)
        pyautogui.scroll(-100000)




# while open_hero == '' or open_hero == None : 
#     open_hero = pyautogui.locateCenterOnScreen('open_hero.png',grayscale=False)
#     print(open_hero)
#     pyautogui.moveTo(open_hero)
#     time.sleep(2)
#     pyautogui.click()