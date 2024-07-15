import pyautogui

#clica na barra 
pyautogui.click(777,1052)
#escreve calculadora
pyautogui.write('calculadora', interval=0.2)
#aperta na calculadora
pyautogui.click(863,440, duration=0.4)
#aperta no 7
pyautogui.click(88,376, duration=0.4)
#aperta no X
pyautogui.click(324,377, duration=0.4)
#aperta no 7
pyautogui.click(88,376, duration=0.4)
#aperta no igual do teclado
pyautogui.press('=')

