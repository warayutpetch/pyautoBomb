import pyautogui
import time
# pyautogui.getWindowsWithTitle("Bombcrypto")[0].maximize()
start = ''
mtm = ''
hunt = ''
open_hero = ''
work = ''
wait_work = ''
go_work = ''
show_time = 0 
work_time = 1 
wait_time = 1
check_count = 0
interval_check = 10
check_break = False
while start == '' or start == None : 
    start = pyautogui.locateCenterOnScreen('wallet.png',grayscale=False)
    print(start)
    if start != None :
        pyautogui.moveTo(start)
        time.sleep(2)
        pyautogui.click()
        time.sleep(5)
    if check_count >= interval_check :
        check_count = 0
        print('break start')
        break
    else : 
        check_count +=1
        
while mtm == '' or mtm == None : 
    mtm = pyautogui.locateCenterOnScreen('approve_mtm.png',grayscale=False)
    print(mtm)
    pyautogui.moveTo(mtm)
    time.sleep(2)
    pyautogui.click()
    if check_count >= interval_check :
        check_count = 0
        print('break mtm')
        break
    else : 
        check_count +=1
while hunt == '' or hunt == None : 
    hunt = pyautogui.locateCenterOnScreen('hunt.png',grayscale=False)
    if hunt != None :
        print(hunt)
        pyautogui.moveTo(hunt)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveRel(0,270)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
    if check_count == interval_check :
        print('break map')
        check_count = 0
        break
    else : 
        check_count +=1

while work == '' or work == None : 
    work = pyautogui.locateCenterOnScreen('work.png',grayscale=False)
    if work != None :
        print(work)
        pyautogui.moveTo(work)
        time.sleep(1)
        pyautogui.click()
    if check_count == interval_check :
        check_count = 0
        break
    else : 
        check_count +=1

while wait_work == '' or wait_work == None : 
    wait_work = pyautogui.locateCenterOnScreen('close.png',grayscale=False)
    print('wait_work=',wait_work)
    if wait_work != None :
        while go_work == '' or go_work == None : 
            print('go_work=',go_work)
            go_work = pyautogui.locateCenterOnScreen('rest.png',grayscale=False)
            if go_work != None :
                print(wait_work)
                pyautogui.moveTo(wait_work)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
            if check_count >= interval_check :
                check_count = 0
                break
            else : 
                check_count +=1
    if check_count >= interval_check :
        check_count = 0
        break
    else : 
        check_count +=1
#ทำงาน
for x in range(60) : 
    show_time += work_time
    time.sleep(work_time)
    print(show_time)
show_time = 0
while back == '' or back == None : 
    back = pyautogui.locateCenterOnScreen('btn_back.png',grayscale=False)
    if back != None :
        print(back)
        pyautogui.moveTo(back)
        while go_work == '' or go_work == None : 
            print('go_work=',go_work)
            go_work = pyautogui.locateCenterOnScreen('rest.png',grayscale=False)
            if go_work != None :
                print(wait_work)
                pyautogui.moveTo(wait_work)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
              
#หยุดพัก
for y in range(60) : 
    show_time += wait_time
    time.sleep(wait_time)
    print(show_time)







# while open_hero == '' or open_hero == None : 
#     open_hero = pyautogui.locateCenterOnScreen('open_hero.png',grayscale=False)
#     print(open_hero)
#     pyautogui.moveTo(open_hero)
#     time.sleep(2)
#     pyautogui.click()