
# from tkinter import *
  
# root = Tk()
# root.geometry("300x300")
# root.title(" AutoBomb by Wara ")

# def read_input():
#     work_val = work_time.get("1.0", "end-1c")
#     rest_time_val = rest_time.get("1.0", "end-1c")
#     max_class_val = max_class.get("1.0", "end-1c")
#     print(work_val)
#     print(rest_time_val)
#     print(max_class_val)

      
# lb1 = Label(text = "เวลาทำงาน (นาที)")
# work_time = Text(root, height = 1,
#                 width = 25,
#                 bg = "light yellow")
# lb2 = Label(text = "เวลาพัก (นาที)")
# rest_time = Text(root, height = 1,
#                 width = 25,
#                 bg = "light yellow")
# lb3 = Label(text = "ระดับของฮีโร่สูงสุดที่จะทำงาน")
# lb4 = Label(text = "1 = common , 2 = rare ,3= super rare, 4 = epic")
# max_class = Text(root, height = 1,
#                 width = 25,
#                 bg = "light yellow")
# Output = Text(root, height = 5, 
#               width = 25, 
#               bg = "light cyan")
# Display = Button(root, height = 1,
#                  width = 10, 
#                  text ="Run",
#                  command = lambda:read_input())
  
# lb1.pack()
# work_time.pack()
# lb2.pack()
# rest_time.pack()
# lb3.pack()
# lb4.pack()
# max_class.pack()
# Display.pack()
# Output.pack()
  
# mainloop()
import pyautogui
import time
# interval_check = 5
# common = None
# check_count = 0
# time.sleep(3)
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
# import win32gui
# import win32api
# import win32con


# def control_click(x, y, handle, button='left'):

#     l_param = win32api.MAKELONG(x, y)

#     if button == 'left':
#         win32gui.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
#         win32gui.PostMessage(handle, win32con.WM_LBUTTONUP, 0, l_param)
#         print('okkkk')
#     elif button == 'right':
#         win32gui.PostMessage(handle, win32con.WM_RBUTTONDOWN, 0, l_param)
#         win32gui.PostMessage(handle, win32con.WM_RBUTTONUP, 0, l_param)

# interval_check = 5
# check_count = 5
# common = None
# while common == '' or common == None : 

#     common = pyautogui.locateCenterOnScreen('hunt.png',grayscale=False,confidence=.95)
#     hWnd = win32gui.FindWindow(None, "Bombcrypto - Google Chrome",)
#     # print(hWnd)

#     if common != None :
#         # print(common.y)
#         # pyautogui.moveTo(common)
#         control_click(common.x,common.y,hWnd,"left")
#         # pyautogui.click(common)
#         check_count = 0
#     if check_count >= interval_check :
#         check_count = 0
#         print('break start')
#         break
#     else : 
#         check_count +=1

# common = pyautogui.getWindowsWithTitle('Bombcrypto')
# print(common[0])
def back_button(screen):
    btn_back = ''
    interval_check = 5
    check_count = 0
    while btn_back == '' or btn_back == None : 
        btn_back = pyautogui.locateCenterOnScreen('img/btn_back.png',region=(screen.left,screen.top,screen.width,screen.height),grayscale=False,confidence=.8)
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
browser = None
browser = pyautogui.getWindowsWithTitle('Bombcrypto')
print(browser)
screen_countX = 1
screen_countY = 1
cout_screen = 1
for list in browser :
    if list != None and list != [] :
        print(list)
        list.moveTo(screen_countX,screen_countY)
        screen_countX += 540
        cout_screen +=1
        if cout_screen > 3 :
            screen_countY += 500
            screen_countX = 1

        # screen_countY += 500
        # back_button(list)
