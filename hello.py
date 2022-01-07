import pyautogui
import time
# pyautogui.getWindowsWithTitle("Bombcrypto")[0].maximize()
while True:
    start = ''
    mtm = ''
    hunt = ''
    open_hero = ''
    work = ''
    wait_work = ''
    go_work = ''
    hero = ''
    show_time = 0 
    work_time = 1 
    wait_time = 1
    check_count = 0
    interval_check = 3
    check_break = False
    while start == '' or start == None : 
        start = pyautogui.locateCenterOnScreen('wallet.png',grayscale=False)
        #print(start)
        if start != None :
            pyautogui.moveTo(start)
            time.sleep(2)
            pyautogui.click()
            time.sleep(5)
            check_count = 0
        if check_count >= interval_check :
            check_count = 0
            #print('break start')
            break
        else : 
            check_count +=1
            
    while mtm == '' or mtm == None : 
        mtm = pyautogui.locateCenterOnScreen('approve_mtm.png',grayscale=False)
        if mtm != None :
            #print(mtm)
            pyautogui.moveTo(mtm)
            time.sleep(2)
            pyautogui.click()
            check_count = 0
        if check_count >= interval_check :
            check_count = 0
            #print('break mtm')
            break
        else : 
            check_count +=1
    while hero == '' or hero == None : 
        hero = pyautogui.locateCenterOnScreen('hero.png',grayscale=False)
        if hero != None :
            #print(hero)
            pyautogui.moveTo(hero)
            pyautogui.click()
            check_count = 0
        if check_count == interval_check :
            #print('break map')
            check_count = 0
            break
        else : 
            check_count +=1 

    while work == '' or work == None : 
        work = pyautogui.locateCenterOnScreen('work.png',grayscale=False)
        if work != None :
            #print(work)
            pyautogui.moveTo(work)
            time.sleep(1)
            pyautogui.click()
            check_count = 0
        if check_count == interval_check :
            check_count = 0
            break
        else : 
            check_count +=1

    while wait_work == '' or wait_work == None : 
        wait_work = pyautogui.locateCenterOnScreen('close_hero.png',grayscale=False)
        #print('wait_work=',wait_work)
        if wait_work != None :
            while go_work == '' or go_work == None : 
                #print('go_work=',go_work)
                go_work = pyautogui.locateCenterOnScreen('btn_work.png',grayscale=False)
                if go_work != None :
                    #print(wait_work)
                    pyautogui.moveTo(wait_work)
                    time.sleep(0.5)
                    pyautogui.click()
                    time.sleep(0.5)
                    pyautogui.click()
                    check_count = 0
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

    while hunt == '' or hunt == None : 
        hunt = pyautogui.locateCenterOnScreen('hunt.png',grayscale=False)
        if hunt != None :
            #print(hunt)
            pyautogui.moveTo(hunt)
            time.sleep(1)
            pyautogui.click()
            check_count = 0
        if check_count == interval_check :
            check_count = 0
            break
        else : 
            check_count +=1
    #ทำงาน
    for x in range(60) : 
        show_time += work_time
        time.sleep(work_time)
        #print(show_time)
    show_time = 0
    bottom = ''
    go_rest = ''
    close = ''
    while bottom == '' or bottom == None : 
        bottom = pyautogui.locateCenterOnScreen('bottom.png',grayscale=False)
        #print(bottom)

        if bottom != None :
            #print(bottom)
            pyautogui.moveTo(bottom)
            pyautogui.moveRel(500,-50)
            pyautogui.click()
            pyautogui.click()
            while go_rest == '' or go_rest == None : 
                #print('go_rest=',go_rest)
                go_rest = pyautogui.locateCenterOnScreen('rest.png',grayscale=False)
                if go_rest != None :
                    #print(go_rest)
                    pyautogui.moveTo(go_rest)
                    pyautogui.click()
                    time.sleep(0.5)
                    while close == '' or close == None : 
                        #print('close_hero=',close)
                        close = pyautogui.locateCenterOnScreen('close.png',grayscale=False)
                        if close != None :
                            #print(close)
                            pyautogui.moveTo(close)
                            pyautogui.click()
                            time.sleep(0.5)
                            pyautogui.click()
                if check_count >= interval_check :
                    check_count = 0
                    while close == '' or close == None : 
                        #print('close_hero=',close)
                        close = pyautogui.locateCenterOnScreen('close.png',grayscale=False)
                        if close != None :
                            #print(close)
                            pyautogui.moveTo(close)
                            pyautogui.click()
                            time.sleep(0.5)
                            pyautogui.click()
                    break
                else : 
                    check_count +=1

    btn_back = ''
    while btn_back == '' or btn_back == None : 
        btn_back = pyautogui.locateCenterOnScreen('btn_back.png',grayscale=False)
        if btn_back != None :
            #print(btn_back)
            pyautogui.moveTo(btn_back)
            time.sleep(1)
            pyautogui.click()
            check_count = 0
        if check_count == interval_check :
            check_count = 0
            break
        else : 
            check_count +=1
                
    # #หยุดพัก
    for y in range(60) : 
        show_time += wait_time
        time.sleep(wait_time)
        #print(show_time)

