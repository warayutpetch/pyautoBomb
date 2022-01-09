import pyautogui
import time
from check_function import *
# pyautogui.getWindowsWithTitle("Bombcrypto")[0].maximize()
while True:



    show_time = 0 
    work_time = 5
    wait_time = 30
    check_disconnect()
    check_login()
    check_mtm()
    open_hero()
    set_hero_work(2,1)
    wait_loading()
    enter_map()
    #ทำงาน
    for x in range(60) : 
        show_time += work_time
        time.sleep(work_time)
        print(show_time)
    show_time = 0
    back_button()
    open_hero()
    set_hero_rest()
    wait_loading()
    back_button()
    # #หยุดพัก
    for y in range(60) : 
        show_time += wait_time
        time.sleep(wait_time)
        print(show_time)

