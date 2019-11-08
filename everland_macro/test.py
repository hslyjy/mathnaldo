import pyautogui
# print(pyautogui.position())
# pyautogui.screenshot('./image/test.png', region=(942, 1045, 30,30))
item = pyautogui.locateCenterOnScreen("./image/test.PNG")
pyautogui.click(item)