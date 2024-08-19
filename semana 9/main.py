import pyautogui
import time

def cadastrar(atleta, modalidade, medalha, comite):

    #localizar Atleta
    cAtleta = pyautogui.locateCenterOnScreen('atleta.png', grayscale=True, confidence=0.9)
    #clicar
    pyautogui.click(cAtleta, duration = 0.8)
    #Digitar
    pyautogui.write(atleta)


    # Modalidade
    cModalidade = pyautogui.locateCenterOnScreen('modalidade.png', grayscale=True, confidence=0.9)
    pyautogui.click(cModalidade, duration = 0.8)
    pyautogui.write(modalidade)


    # Modalidade
    cMedalha = pyautogui.locateCenterOnScreen('medalha.png', grayscale=True, confidence=0.9)
    pyautogui.click(cMedalha, duration = 0.8)
    pyautogui.write(medalha)


    #rolagem
    pyautogui.scroll(3)


    #Comite
    cComite = pyautogui.locateCenterOnScreen('comite.png', grayscale=True, confidence=0.9)
    pyautogui.click(cComite, duration = 0.8)
    pyautogui.write(comite)


    #rolagem
    #pyautogui.scroll(-200)


    #Enviar
    cEnviar = pyautogui.locateCenterOnScreen('enviar.png', grayscale=True, confidence=0.9)
    pyautogui.click(cEnviar, duration = 0.8)

    time.sleep(1)

    #EnviarOutra
    cEnviar2 = pyautogui.locateCenterOnScreen('enviarOutra.png', grayscale=True, confidence=0.9)
    pyautogui.click(cEnviar2, duration = 0.8)


    time.sleep(2)       

