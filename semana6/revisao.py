import pyautogui

#movimentar o mouse
pyautogui.moveTo(960,540, duration=.5)
pyautogui.moveRel(100, 100, duration=.5)

#Arrastar o mouse
pyautogui.dragTo(960,540, duration=.5)
pyautogui.dragRel(100,100, duration=.5)

#Clicar
pyautogui.click(960,540, clicks=2, button='RIGHT')

#Rolagem 
pyautogui.scroll(-2)

#Teclado
#escrever
pyautogui.write('Ola', interval=0.3)

#precionar uma tecla especifica
pyautogui.press('enter')

#precionar teclas simultâneas
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

#manter teclas precionadas
pyautogui.keyDown('a')
pyautogui.keyUp('a')