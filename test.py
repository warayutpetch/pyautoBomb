import pyautogui
import time
interval_check = 5
common = None
check_count = 0
time.sleep(3)
# for i in range(11) :
#     print(i)
#     for box in pyautogui.locateAllOnScreen('rare.png',grayscale=False,confidence=.95):
#         print(pyautogui.center(box))
#         pyautogui.moveTo(pyautogui.center(box))
#         pyautogui.moveRel(290,-20) #rest
#         pyautogui.click()
#         # pyautogui.moveRel(220,-20) #work
#         pyautogui.sleep(2)
#     for box in pyautogui.locateAllOnScreen('common.png',grayscale=False,confidence=.95):
#         print(pyautogui.center(box))
#         pyautogui.moveTo(pyautogui.center(box))
#         pyautogui.moveRel(290,-20) #rest
#         pyautogui.click()
#         # pyautogui.moveRel(220,-20) #work
#         pyautogui.sleep(2)
#     for box in pyautogui.locateAllOnScreen('super_rare.png',grayscale=False,confidence=.95):
#         print(pyautogui.center(box))
#         pyautogui.moveTo(pyautogui.center(box))
#         pyautogui.moveRel(290,-20) #rest
#         pyautogui.click()
#         # pyautogui.moveRel(220,-20) #work
#         pyautogui.sleep(2)
#     for box in pyautogui.locateAllOnScreen('epic.png',grayscale=False,confidence=.95):
#         print(pyautogui.center(box))
#         pyautogui.moveTo(pyautogui.center(box))
#         pyautogui.moveRel(290,-20) #rest
#         pyautogui.click()
#         # pyautogui.moveRel(220,-20) #work
#         pyautogui.sleep(2)
#     for scroll in range (4):
#         pyautogui.scroll(-50)
#     pyautogui.sleep(0.5)

# print("end")
while common == '' or common == None : 
    common = pyautogui.locateCenterOnScreen('disconnect.png',grayscale=False,confidence=.95)
    print(common)
    if common != None :
        pyautogui.moveTo(common)
        pyautogui.click()
        check_count = 0
    if check_count >= interval_check :
        check_count = 0
        print('break start')
        break
    else : 
        check_count +=1