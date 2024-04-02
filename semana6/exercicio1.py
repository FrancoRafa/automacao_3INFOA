'''fazer uma pesquisa no google clique no campo de pesquisa, 
após digite o texto 'como automatizar o whatsapp' após precione enter'''

import pyautogui
pyautogui.moveTo(425,402, duration=.5)
pyautogui.click(425,402, clicks=2, interval=0.3, button='LEFT')
pyautogui.write ('como automatizar o whatsapp', interval=0.3)
pyautogui.press('enter')




pyautogui.moveTo(31, 342, duration=.5)
pyautogui.dragTo(401, 481, duration=.2)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1036, 593, duration=.5)
pyautogui.hotkey('ctrl', 'v')