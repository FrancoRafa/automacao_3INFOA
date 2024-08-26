import pyautogui
import time

def colocar(nome, nota, atividade, turma):
    #Registro
    cRegistro = pyautogui.locateCenterOnScreen('registro.png', grayscale=True, confidence=0.9)
    pyautogui.click(cRegistro, duration = 0.8)


    #localizar nome
    cAluno = pyautogui.locateCenterOnScreen('aluno.png', grayscale=True, confidence=0.9)
    #clicar
    pyautogui.click(cAluno, duration = 0.8)
    #Digitar
    pyautogui.write(nome)


    # atividade
    cAtividade = pyautogui.locateCenterOnScreen('atividade.png', grayscale=True, confidence=0.9)
    pyautogui.click(cAtividade, duration = 0.8)
    pyautogui.write(atividade)

    # nota
    cNota = pyautogui.locateCenterOnScreen('nota.png', grayscale=True, confidence=0.9)
    pyautogui.click(cNota, duration = 0.8)
    pyautogui.write(str(nota))


    #rolagem
    pyautogui.scroll(-300)

    if turma == '3INFOA':
        cInfo = pyautogui.locateCenterOnScreen('A.png', grayscale=True, confidence=0.9)
        pyautogui.click(cInfo, duration = 0.8)

    if turma == '3INFOB':
        cInfoB = pyautogui.locateCenterOnScreen('B.png', grayscale=True, confidence=0.9)
        pyautogui.click(cInfoB, duration = 0.8)
    

    #Enviar
    cEnviar = pyautogui.locateCenterOnScreen('enviar.png', grayscale=True, confidence=0.9)
    pyautogui.click(cEnviar, duration = 0.8)

    time.sleep(1)

    #EnviarOutra
    cEnviar2 = pyautogui.locateCenterOnScreen('enviarOutra.png', grayscale=True, confidence=0.9)
    pyautogui.click(cEnviar2, duration = 0.8)


    time.sleep(2)       
    
    
    
    
    


   