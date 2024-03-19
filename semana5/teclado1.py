import pyautogui

#clica no campo usuário
pyautogui.click(880, 393, duration=0.2)
#digita a matrícula no campo
pyautogui.write('2022190029', interval=0.5)

#clica no campo senha
pyautogui.click(880, 500, duration=0.2)
#digita a matrícula no campo
pyautogui.write('123456Rafa!', interval=0.5)


#clica no botão acessar
pyautogui.click(880, 500, duration=0.2)

