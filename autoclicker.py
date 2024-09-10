import pyautogui, time
time.sleep(5)
pyautogui.click()    # Click to make the window active. 
pyautogui.FAILSAFE = False
for i in range(100):
    pyautogui.click()
pyautogui.FAILSAFE = True