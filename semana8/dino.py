import pyautogui

#clica no chrome
pyautogui.click(200, 422, duration=.5)
pyautogui.keyDown('space')
while True:
     if not pyautogui.pixelMatchesColor(200, 422, [255,255,255], tolerance=0.1):
          pyautogui.keyDown('space')


