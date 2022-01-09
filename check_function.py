import pyautogui
import time

def check_login():
    start = None
    interval_check = 3
    check_count = 0
    while start == '' or start == None : 
        start = pyautogui.locateCenterOnScreen('wallet.png',grayscale=False,confidence=.9)
        print(start)
        if start != None :
            pyautogui.moveTo(start)
            time.sleep(2)
            pyautogui.click()
            time.sleep(5)
            check_count = 0
            return start
        if check_count >= interval_check :
            check_count = 0
            print('break start')
            return False
        else : 
            check_count +=1
def check_mtm():
    mtm = None
    interval_check = 3
    check_count = 0
    while mtm == '' or mtm == None : 
        mtm = pyautogui.locateCenterOnScreen('approve_mtm.png',grayscale=False,confidence=.9)
        if mtm != None :
            print(mtm)
            pyautogui.moveTo(mtm)
            time.sleep(2)
            pyautogui.click()
            check_count = 0
            return mtm
        if check_count >= interval_check :
            check_count = 0
            print('break mtm')
            return False
        else : 
            check_count +=1
def open_hero():
    hero = None
    interval_check = 10
    check_count = 0
    while hero == '' or hero == None : 
        hero = pyautogui.locateCenterOnScreen('hero.png',grayscale=False,confidence=.9)
        if hero != None :
            print(hero)
            pyautogui.moveTo(hero)
            pyautogui.click()
            check_count = 0
        if check_count >= interval_check :
            print('break map')
            check_count = 0
            break
        else : 
            check_count +=1 
        pyautogui.sleep(1)
def set_hero_work(max_class_work,action):
    for i in range(11) :
        print(i)
        if max_class_work >= 1 :
            for box in pyautogui.locateAllOnScreen('common.png',grayscale=False,confidence=.95):
                print(pyautogui.center(box))
                pyautogui.moveTo(pyautogui.center(box))
                if action == 1 :
                    pyautogui.moveRel(220,-20) #work
                else :
                    pyautogui.moveRel(290,-20) #rest
                pyautogui.click()
                pyautogui.sleep(2)
        
        if max_class_work >= 2 :
            for box in pyautogui.locateAllOnScreen('rare.png',grayscale=False,confidence=.95):
                print(pyautogui.center(box))
                pyautogui.moveTo(pyautogui.center(box))
                if action == 1 :
                    pyautogui.moveRel(230,-20) #work
                else :
                    pyautogui.moveRel(300,-20) #rest
                pyautogui.click()
                pyautogui.sleep(2)
        if max_class_work >= 3 :
            for box in pyautogui.locateAllOnScreen('super_rare.png',grayscale=False,confidence=.95):
                print(pyautogui.center(box))
                pyautogui.moveTo(pyautogui.center(box))
                if action == 1 :
                    pyautogui.moveRel(220,-20) #work
                else :
                    pyautogui.moveRel(290,-20) #rest
                pyautogui.click()
                pyautogui.sleep(2)
        if max_class_work >= 4 :    
            for box in pyautogui.locateAllOnScreen('epic.png',grayscale=False,confidence=.95):
                print(pyautogui.center(box))
                pyautogui.moveTo(pyautogui.center(box))
                if action == 1 :
                    pyautogui.moveRel(220,-20) #work
                else :
                    pyautogui.moveRel(290,-20) #rest
                pyautogui.click()
                pyautogui.sleep(2)
        for scroll in range (4):
            pyautogui.scroll(-50)
        pyautogui.sleep(0.5)

def set_hero_rest():
    go_rest = ''
    interval_check = 5
    check_count= 0
    while go_rest == '' or go_rest == None : 
        print('go_rest=',go_rest)
        go_rest = pyautogui.locateCenterOnScreen('rest.png',grayscale=False,confidence=.9)
        if go_rest != None :
            print(go_rest)
            pyautogui.moveTo(go_rest)
            pyautogui.click()
            time.sleep(0.5)
        if check_count >= interval_check :
            check_count = 0
            print('break set_hero_rest')
            break
        else : 
            check_count +=1

def check_disconnect():
    discon = None
    interval_check = 5
    check_count = 0
    while discon == '' or discon == None : 
        discon = pyautogui.locateCenterOnScreen('disconnect.png',grayscale=False,confidence=.95)
        print(discon)
        if discon != None :
            pyautogui.moveTo(discon)
            pyautogui.click()
            pyautogui.sleep(15)
            check_count = 0
        if check_count >= interval_check :
            check_count = 0
            print('break disconnect')
            break
        else : 
            check_count +=1

def back_button():
    btn_back = ''
    interval_check = 5
    check_count = 0
    while btn_back == '' or btn_back == None : 
        btn_back = pyautogui.locateCenterOnScreen('btn_back.png',grayscale=False,confidence=.8)
        if btn_back != None :
            print(btn_back)
            pyautogui.moveTo(btn_back)
            time.sleep(1)
            pyautogui.click()
            check_count = 0
        if check_count == interval_check :
            check_count = 0
            break
        else : 
            check_count +=1
def wait_loading():
    interval_check = 3
    wait_work = None
    check_count = 0
    go_work = None
    while wait_work == '' or wait_work == None : 
        wait_work = pyautogui.locateCenterOnScreen('close_hero.png',grayscale=False,confidence=.9)
        print('wait_work=',wait_work)
        if wait_work != None :
            while go_work == '' or go_work == None : 
                print('go_work=',go_work)
                go_work = pyautogui.locateCenterOnScreen('btn_work.png',grayscale=False,confidence=.9)
                if go_work != None :
                    print(wait_work)
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

def enter_map():
    interval_check = 5
    hunt = None
    check_count = 0
    while hunt == '' or hunt == None : 
        hunt = pyautogui.locateCenterOnScreen('hunt.png',grayscale=False,confidence=.9)
        if hunt != None :
            print(hunt)
            pyautogui.moveTo(hunt)
            time.sleep(1)
            pyautogui.click()
            check_count = 0
        if check_count == interval_check :
            check_count = 0
            break
        else : 
            check_count +=1 

def remap():
    back_button()
    enter_map()
                