import webbrowser, pyautogui
from time import sleep

# 1. Abrir browsser
webbrowser.open('https://www.tiktok.com/')
sleep(8)

# 2. Cliclar em login
#pyautogui.click(770,495,duration=2)
#sleep(5)

# 3. Clicar em logar com email
pyautogui.click(1003,296,duration=2)
sleep(2)

# 4. Clicar em logar com email/username
pyautogui.click(1068,222,duration=2)
sleep(3)

# 5. Digitar email ou usuário
pyautogui.click(975,260,duration=2)
pyautogui.write('usuario')
sleep(1)

#6. Digitar senha
pyautogui.click(905,321,duration=2)
pyautogui.write('senha')
sleep(1)

# 7. Clicar em Entrar
pyautogui.click(1000,415,duration=2)
sleep(50)

# 8. Navegar até a página
webbrowser.open('página a ser curtida')
sleep(8)

# 9. Clica na postagem mais recente
pyautogui.click(876,663,duration=2)
sleep(5)

# 10. Verifica se o vídeo já foi curtido 
# 11. Repetir 2 vezes
for video in range(2):
    imagem = pyautogui.locateOnScreen('curtida.png')
    sleep(5)
    if imagem:
        # Se não foi curtindo, curtir este video e passar para o próximo video
        pyautogui.click(1332,279,duration=2)
        pyautogui.press('down')
        sleep(5)
    else:
        # Se foi curtido, passar para o próximo vídeo       
        sleep(5)       
        pyautogui.press('down')



