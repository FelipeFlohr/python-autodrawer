import os
import pyautogui
import keyboard
from PIL import Image
from time import sleep
from threading import Thread
from ini_parser import Parameters as Pm

# Pega o valor RGB de um pixel de uma imagem
# imagem = Image.open('imagemteste.png')
# pixel = imagem.load()
# tamanho = imagem.size
# print(imagem.size)
# print('0, 0', pixel[0, 0])

# quadro no paint
# -> x=434 y=315------------------ <- x=1273 y=315
#               |                |
#               |     CANVAS     |
#               |                |
# -> x=434 y=862------------------ <- x=1273 y=862

# tamanho da tela = 1370x886
# centro do canvas = x=856px y=592px


class Debug(Pm):
    def __init__(self, monitor_x=1920, monitor_y=1080):
        '''
        -> Constructor
        :param monitor_x: The X size of your monitor
        :param monitor_y: The Y size of your monitor
        '''
        Pm.__init__(Pm, 'config.ini')
        self.monitor_x = monitor_x
        self.monitor_y = monitor_y

    def verificar_imagem_tamanho(self, imagem_tamanho):
        """
        -> Verifies if the image's size is equal or smaller than the canvas' size. If not, then it will ask if you want to continue anyways.
        :param imagem_tamanho: A tuple with two values. The first one is the X size of the image, and the second one is the Y size of the image
        :return: No return
        """
        if imagem_tamanho[0] > (Pm.canvas_bottomrightx(self) - Pm.canvas_topleftx(self)):
            print('Tamanho X =', imagem_tamanho[0])
            print('Tamanho X Canvas =', (Pm.canvas_bottomrightx(self) - Pm.canvas_topleftx(self)))
            print("The X size of the image is bigger than the canvas' size.")
            while True:
                pergunta = str(input('Do you want to continue anyway (WARNING: Errors may occur)[Y/N]?')).strip().upper()[0]
                if pergunta != 'N' and pergunta != 'Y':
                    pergunta = str(input('Invalid answer. Do you want to continue anyway (WARNING: Errors may occur)[Y/N]?')).strip().upper()[0]
                if pergunta == 'N':
                    print('Encerrando programa...')
                    sleep(1.5)
                    os._exit()
                elif pergunta == 'Y':
                    pass
        elif imagem_tamanho[1] > (Pm.canvas_bottomrighty(self) - Pm.canvas_toplefty(self)):
            print('Tamanho Y =', imagem_tamanho[1])
            print('Tamanho Y Canvas =', (Pm.canvas_bottomrighty(self) - Pm.canvas_toplefty(self)))
            print("The X size of the image is bigger than the canvas' size.")
            while True:
                pergunta = str(input('Do you want to continue anyway (WARNING: Errors may occur)[Y/N]?')).strip().upper()[0]
                if pergunta != 'N' and pergunta != 'Y':
                    pergunta = str(input('Invalid answer. Do you want to continue anyway (WARNING: Errors may occur)[Y/N]?')).strip().upper()[0]
                if pergunta == 'N':
                    print('Encerrando programa...')
                    sleep(1.5)
                    os._exit()
                elif pergunta == 'Y':
                    pass
        else:
            print('Tamanho da Foto: OK')

    def desenhar4cantos(self):
        """
        -> Will draw a rectangle, showing the total size of the canvas
        :return:
        """
        pyautogui.moveTo(Pm.canvas_topleftx(self), Pm.canvas_toplefty(self), _pause=False)
        pyautogui.dragTo(Pm.canvas_bottomrightx(self), Pm.canvas_toplefty(self), button='left', _pause=False)
        pyautogui.dragTo(Pm.canvas_bottomrightx(self), Pm.canvas_bottomrighty(self), button='left', _pause=False)
        pyautogui.dragTo(Pm.canvas_topleftx(self), Pm.canvas_bottomrighty(self), button='left', _pause=False)
        pyautogui.dragTo(Pm.canvas_topleftx(self), Pm.canvas_toplefty(self), _pause=False, button='left')

    def centralizar_canvas(self, debug=False): # Bug -> Esse método não funciona se o NumLock estiver ligado
        """
        -> This will centralize the canvas based on the specified zoom
        :param debug: This will print the debug things
        :return: No return
        """
        print('Abra o paint em 5 segundos')
        sleep(5)
        pyautogui.moveTo(self.monitor_x//2, self.monitor_y//2)
        pyautogui.click(button='right')
        pyautogui.move(20, 210)
        pyautogui.click(button='left')
        pyautogui.click(button='left')
        pyautogui.moveTo(x=1576, y=102)
        pyautogui.click(button='left')
        pyautogui.write(str(Pm.canvas_zoom(self)))
        pyautogui.press('enter')
        if debug:
            print('Canvas centralizado!')

    def mover_cursor_4cantos(self, delay=False):
        """
        -> This will move your cursor to all the edges of your canvas. It is just for debugging
        :param delay: Turn on/off the delay for moving the cursor
        :return: No return
        """
        if delay:
            print('Movendo o cursor do Mouse para os quatro quantos do canvas em 5...')
            sleep(5)
        else:
            print('Movendo o cursor do Mouse para os quatro quantos do canvas...')
        posoriginal_x, posoriginal_y = pyautogui.position()
        pyautogui.moveTo(Pm.canvas_topleftx(self), Pm.canvas_toplefty(self))
        sleep(1)
        pyautogui.moveTo(Pm.canvas_topleftx(self), Pm.canvas_bottomrighty(self))
        sleep(1)
        pyautogui.moveTo(Pm.canvas_bottomrightx(self), Pm.canvas_toplefty(self))
        sleep(1)
        pyautogui.moveTo(Pm.canvas_bottomrightx(self), Pm.canvas_bottomrighty(self))
        pyautogui.moveTo(posoriginal_x, posoriginal_y) # Retorna para a oposição original

    def tamanho_monitor(self):
        """
        -> Just get the resolution of your monitor
        :return: Return a string with your monitor's resolution
        """
        return 'DEBUG: O tamanho do seu monitor é: {}x{}'.format(pyautogui.size()[0], pyautogui.size()[1])

    def centro_canvas(self):
        """
        -> Will return a tuple with the center position of the Canvas
        :return: A tuple with two values. The first one is the X position of the canvas' center. The second one is the Y position of the canvas' center
        """
        pos_a = (Pm.canvas_topleftx(self), Pm.canvas_toplefty(self))
        pos_b = (Pm.canvas_bottomrightx(self), Pm.canvas_toplefty(self))
        pos_c = (Pm.canvas_topleftx(self), Pm.canvas_bottomrighty(self))
        dist_x = pos_a[0] + ((pos_b[0] - pos_a[0]) / 2)
        dist_y = pos_a[1] + ((pos_c[1] - pos_a[1]) / 2)
        return (dist_x, dist_y)

    def fechar_programa(self):
        """
        -> A method to exit the program
        :return: No return
        """
        tecla = Pm.keyboard_interruptionKey(self)
        while True:
            if keyboard.is_pressed(tecla):
                print(f'Tecla {tecla} apertada. Encerrando o programa')
                os._exit(0)
            else:
                sleep(0.5)


class Imagem(Pm):
    def __init__(self):
        '''
        -> Constructor
        '''
        Pm.__init__(Pm, 'config.ini')

    def valores_repetidos(self, valor, lista):
        '''
        -> This will find the index of an equal value inside a list
        :param valor: The value to be searched
        :param lista: The list
        :return: Will return the pos of the repeated value. If there is no repeated value, then will return -1
        '''
        pos = -1
        for c in range(0, len(lista)):
            if valor in lista[c]:
                pos = c
            else:
                pass
        return pos

    def gerar_lista_pixels(self, debug=False):
        """
        -> This will generate a list containg the RGB of each pixel in the image
        :param debug: If it is true, it will print a confirmation for each X and Y RGB generated
        :return: Will return the list containg the RGB of each pixel
        """
        imagem = Image.open(Pm.photo(self))
        pixel = imagem.load()
        tamanho = imagem.size

        lista = list()

        for x in range(0, tamanho[0]):
            for y in range(0, tamanho[1]):
                cor_pixel_atual = pixel[x, y]
                if len(cor_pixel_atual) == 4 and cor_pixel_atual[3] == 0:
                    if debug == True and cor_pixel_atual != (0, 0, 0, 0):
                        print(cor_pixel_atual)
                        print('Há translucidade. Passando')
                        sleep(0.5)
                    else:
                        pass
                else:
                    if self.valores_repetidos(cor_pixel_atual, lista) == -1:
                        dict = {(cor_pixel_atual): [(x, y)]}
                        lista.append(dict.copy())
                    else:
                        tupla = (x, y)
                        lista[self.valores_repetidos(cor_pixel_atual, lista)][cor_pixel_atual].append(tupla[:])
        return lista

    def tamanho_foto(self):
        """
        -> This will return a tuple with the X and Y size of the photo
        :return: Will return a tuple with the X and Y size of the photo
        """
        imagem = Image.open(Pm.photo(self))
        return imagem.size


class Funcoes(Pm):
    def __init__(self):
        """
        -> Constructor
        """
        Pm.__init__(self, 'config.ini')

    def pegar_lista_dict(self, dict, debug=False):
        """
        -> This will return the key values of an dictionary inside a list
        :param dict: The dictionary
        :param debug: If true, will print the debug things
        :return: The list containing the key values
        """
        if debug:
            print('len dict = ', len(dict))
        lista = list()
        for key in dict.keys():
            lista.append(key)
        if debug:
            print(lista)
        return lista

    def editar_cor(self, r, g, b, delay=True):
        """
        -> A function for changing the color of the selected tool
        :param r: The R value
        :param g: The G value
        :param b: The B value
        :param delay: If true, delay will happen before certain events
        :return: No return
        """
        r = str(r)
        g = str(g)
        b = str(b)

        # Moving to edit an added color
        pyautogui.moveTo(x=Pm.colorPalette_colorpos(self)[0], y=Pm.colorPalette_colorpos(self)[1])
        if delay:
            sleep(2)
        pyautogui.click(button='right')
        pyautogui.moveTo(x=Pm.colorPalette_colorpos(self)[0] + 8, y=Pm.colorPalette_colorpos(self)[1] + 5)
        pyautogui.click(button='left')

        # Moving to edit the R value
        pyautogui.moveTo(x=Pm.colorSelector_rpos(self)[0], y=Pm.colorSelector_rpos(self)[1])
        pyautogui.click(button='left')
        pyautogui.write(r, interval=0.10)

        # Moving to edit the G value
        pyautogui.moveTo(x=Pm.colorSelector_gpos(self)[0], y=Pm.colorSelector_gpos(self)[1])
        pyautogui.click(button='left')
        pyautogui.write(g, interval=0.10)

        # Moving to edit the B value
        pyautogui.moveTo(x=Pm.colorSelector_bpos(self)[0], y=Pm.colorSelector_bpos(self)[1])
        pyautogui.click(button='left')
        pyautogui.write(b, interval=0.10)

        # Moving to OK button
        pyautogui.moveTo(x=Pm.colorSelector_okbutton(self)[0], y=Pm.colorSelector_okbutton(self)[1])
        if delay:
            sleep(1)
        pyautogui.click(button='left')
        pyautogui.click(button='left')

    def mudar_ferramenta(self):
        """
        -> This will change the Paint's tool
        :return: No return
        """
        ferramenta = Pm.draw_tool(self)
        espessura = Pm.draw_thickness(self)
        opacidade = Pm.draw_opacity(self)
        espessura_pos = Pm.draw_thicknesspos(self)
        opacidade_pos = Pm.draw_opacitypos(self)

        ferramentas = {'pencil': (1699, 212), 'crayon': (1786, 214), 'pixelpen': (1876, 155)}
        if ferramenta not in ferramentas:
            raise ValueError('Ferramenta não está na lista de ferramentas')
        try:
            int(espessura)
        except:
            raise TypeError('Espessura não é um número inteiro.')

        # Muda a ferramenta
        pyautogui.moveTo(x=ferramentas[ferramenta][0], y=ferramentas[ferramenta][1])
        pyautogui.click(button='left')

        # Muda a espessura
        pyautogui.moveTo(espessura_pos[0], espessura_pos[1])
        pyautogui.click(button='left')
        pyautogui.write(str(espessura))
        pyautogui.move(-80, 0)
        pyautogui.click(button='left')

        # Muda a opacidade
        pyautogui.moveTo(opacidade_pos[0], opacidade_pos[1])
        pyautogui.click(button='left')
        pyautogui.write(str(opacidade))
        pyautogui.move(-80, 0)
        pyautogui.click(button='left')

    def pos_inicial_desenho(self, pos_tamanhoDesenho, pos_centro_canvas):
        """
        -> This will set the initial position where the cursor will be moved, then it will start to draw
        :param pos_tamanhoDesenho: Must be a tuple with two values. The first value is the X size of the photo. The second value is the Y size of the photo
        :param pos_centro_canvas: Must be a tuple with two values. The first value is the X position of the canvas' center. The second value is the Y position of the canvas' center
        :return: Will return the initial position of the drawing
        """
        x = pos_tamanhoDesenho[0]
        y = pos_tamanhoDesenho[1]
        x_metade = x//2
        y_metade = y//2

        pyautogui.moveTo(pos_centro_canvas[0], pos_centro_canvas[1]) # Centraliza
        pyautogui.move(0, y_metade * -1) # Move para cima
        pyautogui.move(x_metade * -1, 0) # Move para a esquerda
        posicao = pyautogui.position()
        return posicao

    def desenhar(self, pos_tamanho_desenho, pos_centro_canvas, lista_pixels, debug=False):
        """
        -> This will draw the photo on the Paint's canvas
        :param pos_tamanho_desenho: Must be a tuple with two values. The first value is the X size of the photo. The second value is the Y size of the photo
        :param pos_centro_canvas: A tuple with the X and Y position of the canvas' center
        :param lista_pixels: The list containing the pixels. Must be generated using the gerar_lista_pixels() method
        :param debug: If true, will print the debug things
        :return: No return
        """
        pos_inicial = self.pos_inicial_desenho(pos_tamanho_desenho, pos_centro_canvas)

        cores_diferentes = len(lista_pixels)

        for c in range(0, cores_diferentes):
            r = self.pegar_lista_dict(lista_pixels[c], c)[0][0]
            g = self.pegar_lista_dict(lista_pixels[c], c)[0][1]
            b = self.pegar_lista_dict(lista_pixels[c], c)[0][2]
            if len(self.pegar_lista_dict(lista_pixels[c], c)[0]) == 4:
                a = self.pegar_lista_dict(lista_pixels[c], c)[0][3]
            else:
                pass

            if debug:
                print(r, g, b)

            pos_diferentes = len(lista_pixels[c][self.pegar_lista_dict(lista_pixels[c], c)[0]])

            if debug:
                print('Quantidade de posições diferentes =', pos_diferentes)

            self.editar_cor(r, g, b)

            for count in range(0, pos_diferentes):
                try:
                    x=lista_pixels[c][(r, g, b, a)][count][0]
                    y=lista_pixels[c][(r, g, b, a)][count][1]
                except:
                    x=lista_pixels[c][(r, g, b)][count][0]
                    y=lista_pixels[c][(r, g, b)][count][1]
                if debug:
                    print(f'x = {x}; y = {y}')

                pyautogui.moveTo(x=pos_inicial[0] + x, y=pos_inicial[1] + y, _pause=False)
                pyautogui.click(button='left', _pause=False)
                sleep(Pm.delay(self))


debugs = Debug() # The Debug class variable
foto = Imagem() # The Imagem class variable
func = Funcoes() # The Funcoes class variable

Pm('config.ini').escrever() # This will write the "config.ini" file, in case it doesn't exist
print(debugs.tamanho_monitor()) # This will print the computer's resolution
debugs.centralizar_canvas() # This will centralize the canvas
debugs.verificar_imagem_tamanho(foto.tamanho_foto()) # This is going to verify the image size
lista = foto.gerar_lista_pixels() # This is going to generate a list containing the pixels
func.mudar_ferramenta() # This will change the drawing tool to the selected one on the "config.ini"
sleep(3)

Thread(target=func.desenhar, args=[foto.tamanho_foto(), debugs.centro_canvas(), lista]).start() # This will thread the "desenhar" method
Thread(target=debugs.fechar_programa).start() # This will thread the fechar_programa method, so the user will be able to exit the program anyways
