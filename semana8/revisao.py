import pyautogui 
import time

#clica no campo login
pyautogui.click(539, 220, duration=.10)

pyautogui.write("rafaela.guimaraes@alunos.ifsuldeminas.edu.br", interval=0.1)

#clica no botão avançar
pyautogui.click(864, 443, duration=1)

time.sleep(5)
pyautogui.write("Rafaela", interval=0.1)

pyautogui.click(864, 443, duration=1)
