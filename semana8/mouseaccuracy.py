import pyautogui

while True:
    try:
     ponto= pyautogui.locateCenterOnScreen('bolinha.php', grayscale=True region=[0,89,846,591], confidence=0.5)

     pyautogui.click(ponto, duration=0.1)
    except:
        print("Não encontra bolinha")