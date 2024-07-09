import pyautogui

def obterEstadoCenario():
     if pyautogui.pixelMatchesColor(100,600,[255,255,255],50):
          return 'DIA'
     else
          return 'NOITE'

#clica no chrome
pyautogui.click(200, 422, duration=.5)
pyautogui.keyDown('space')
while True:
#pega cor dino
    #corDino= pyautogui.pixel(70,718)
     if obterEstadoCenario())== DIA:
           if pyautogui.pixelMatchesColor(235,439,[83,83,83], 50) 
           print(pyautogui.pixel(235,439))
           pyautogui.keyDown('space')
   
     else
          if  pyautogui.pixelMatchesColor(235, 439, [172,172,172]):
          pyautogui.keyDown('space')
    



