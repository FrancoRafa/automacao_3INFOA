import pyautogui


#localizar x, y de uma imagem na tela
nome_XY = pyautogui.locateCenterOnScreen('./semana7/campo_nome.png', confidence=0.9)
pyautogui.click(nome_XY, duration=0.5) #clica
pyautogui.write('Rafaela Guimarães Franco da Silva')


cpf_XY = pyautogui.locateCenterOnScreen('./semana7/campo_cpf.png', confidence=0.9)
pyautogui.click(cpf_XY, duration=0.5) #clica
pyautogui.write('114.606.156-03')


sim_XY = pyautogui.locateCenterOnScreen('./semana7/campo_sim.png', confidence=0.9)
pyautogui.click(sim_XY, duration=0.5) #clica

enviar_XY = pyautogui.locateCenterOnScreen('./semana7/campo_enviar.png', confidence=0.9)
pyautogui.click(enviar_XY, duration=0.5) #clica