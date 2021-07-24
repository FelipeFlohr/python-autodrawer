import pyautogui

print("EN: Monitor's X size | PT-BR: Tamanho X do monitor: {}\nEN: Monitor's Y size | PT-BR: Tamanho Y do monitor: {}\n".format(pyautogui.size()[0], pyautogui.size()[1]))
input("EN: Press enter to exit | PT-BR: Aperte enter para sair ")