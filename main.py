import pyautogui
from PIL import Image
from time import sleep
from sys import exit as sair

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

class Debug:
    def __init__(self, inicio_canvas_x, inicio_canvas_y, final_canvas_x, final_canvas_y, monitor_x=1920, monitor_y=1080):
        '''
        -> Starter
        :param inicio_canvas_x: The upper left X position of your canvas
        :param inicio_canvas_y: The upper left Y position of your canvas
        :param final_canvas_x: The bottom right X position of your canvas
        :param final_canvas_y: The bottom right Y position of your canvas
        :param monitor_x: The X size of your monitor
        :param monitor_y: The Y size of your monitor
        '''
        self.inicio_canvas_x = inicio_canvas_x
        self.inicio_canvas_y = inicio_canvas_y
        self.final_canvas_x = final_canvas_x
        self.final_canvas_y = final_canvas_y
        self.monitor_x = monitor_x
        self.monitor_y = monitor_y

    def centralizar_canvas(self, zoom=33, debug=False): # Bug -> Esse método não funciona se o NumLock estiver ligado
        '''
        -> This will centralize the canvas based on the specified zoom
        :param zoom: A number that will set the zoom. Must be an integer
        :param debug: This will print the debug things
        :return: No return
        '''
        print('Abra o paint em 5 segundos')
        sleep(5)
        pyautogui.moveTo(self.monitor_x//2, self.monitor_y//2)
        pyautogui.click(button='right')
        pyautogui.move(20, 210)
        pyautogui.click(button='left')
        pyautogui.click(button='left')
        pyautogui.moveTo(x=1576, y=102)
        pyautogui.click(button='left')
        pyautogui.write(str(zoom))
        if debug == True:
            print('Canvas centralizado!')

    def mover_cursor_4cantos(self, delay=False):
        '''
        -> This will move your cursor to all the edges of your canvas. It is just for debugging
        :param delay: Turn on/off the delay for moving the cursor
        :return:
        '''
        if delay == True:
            print('Movendo o cursor do Mouse para os quatro quantos do canvas em 5...')
            sleep(5)
        else:
            print('Movendo o cursor do Mouse para os quatro quantos do canvas...')
        posoriginal_x, posoriginal_y = pyautogui.position()
        pyautogui.moveTo(self.inicio_canvas_x, self.inicio_canvas_y)
        sleep(1)
        pyautogui.moveTo(self.inicio_canvas_x, self.final_canvas_y)
        sleep(1)
        pyautogui.moveTo(self.final_canvas_x, self.inicio_canvas_y)
        sleep(1)
        pyautogui.moveTo(self.final_canvas_x, self.final_canvas_y)
        pyautogui.moveTo(posoriginal_x, posoriginal_y) # Retorna para a oposição original

    def tamanho_monitor(self):
        '''
        -> Just get the resolution of your monitor
        :return: Return a string with your monitor's resolution
        '''
        return 'DEBUG: O tamanho do seu monitor é: {}x{}'.format(pyautogui.size()[0], pyautogui.size()[1])

    def mostrar_pos_mouse(self, secs=15):
        '''
        -> This will print the position of your cursor
        :secs: The amount of seconds this method will be running
        :return: no return
        '''
        for c in range(0, secs):
            pos = pyautogui.position()
            print(pos)
            sleep(0.5)
    
    def centralizar_cursor(self, delay=True, pos_centroCanvas=(856, 592)):
        '''
        -> This will move the cursor to the center of the screen
        :param delay: If true, a delay will be set before the cursor be moved
        :param pos_centroCanvas: A tuple with two values. The first value is the X position of the center of the canvas, and the second is the Y position of the center of the canvas
        :return: No return
        '''
        sleep(2)
        pyautogui.moveTo(pos_centroCanvas[0], pos_centroCanvas[1])


class Imagem:
    def __init__(self, foto : str):
        '''
        -> Starter
        :param foto: The address of your image
        '''
        self.foto = foto
    
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

    def gerar_lista_pixels(self, canvas_x, canvas_y, debug=False):
        '''
        -> This will generate a list containg the RGB of each pixel in the image
        :param canvas_x: The X size of your image
        :param canvas_y: The Y size of your image
        :param debug: If it is true, it will print a confirmation for each X and Y RGB generated
        :return: Will return the list containg the RGB of each pixel
        '''
        imagem = Image.open(self.foto)
        pixel = imagem.load()
        tamanho = imagem.size
        if tamanho[0] > canvas_x or tamanho[1] > canvas_y:
            raise ValueError('O Tamanho da foto é maior que o tamanho da área do canvas. Por favor, reduza o tamanho da foto ou aumente o tamanho do canvas.')

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
                elif cor_pixel_atual[0] > 10 and cor_pixel_atual[1] > 10 and cor_pixel_atual[2] > 10:
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
        '''
        -> This will return a tuple with the X and Y size of the photo
        :return: Will return a tuple with the X and Y size of the photo
        '''
        imagem = Image.open(self.foto)
        return imagem.size


class Funcoes:
    def __init__(self, pos_r=(1145, 493), pos_g=(1145, 550), pos_b=(1145, 606), pos_cores=(1695, 997), pos_okbutton=(851, 728)):
        '''
        -> Starter
        :param pos_r: A tuple with two values. The first one is the X position of the R value in the color changer. The second one is the Y position of the R value in the color changer
        :param pos_g: A tuple with two values. The first one is the X position of the G value in the color changer. The second one is the Y position of the G value in the color changer
        :param pos_b: A tuple with two values. The first one is the X position of the B value in the color changer. The second one is the Y position of the B value in the color changer
        :param pos_cores: A tuple with two values. The first one is the X position of the color to be changed in the color pallette. The second one is the Y position of the color to be changed in the color pallette
        :param pos_okbutton: A tuple with two values. The first one is the X position of the OK button in the color changer. The second one is the Y position of the OK button in the color changer
        '''
        self.pos_r = pos_r
        self.pos_g = pos_g
        self.pos_b = pos_b
        self.pos_cores = pos_cores
        self.pos_okbutton = pos_okbutton

    def pegarListaDict(self, dict, debug=False):
        '''
        -> This will return the key values of an dictionary inside a list
        :param dict: The dictionary
        :param debug: If true, will print the debug things
        :return: The list containing the key values
        '''
        if debug == True:
            print('len dict = ', len(dict))
        lista = list()
        for key in dict.keys():
            lista.append(key)
        if debug == True:
            print(lista)
        return lista

    def editar_cor(self, r, g, b, delay=True):
        '''
        -> A function for changing the color of the selected tool
        :param r: The R value
        :param g: The G value
        :param b: The B value
        :param delay: If true, delay will happen before certain events
        :return: No return
        '''
        r = str(r)
        g = str(g)
        b = str(b)

        # Moving to edit an added color
        pyautogui.moveTo(x=self.pos_cores[0], y=self.pos_cores[1])
        if delay == True:
            sleep(2)
        pyautogui.click(button='right')
        pyautogui.moveTo(x=self.pos_cores[0] + 8, y=self.pos_cores[1] + 5)
        pyautogui.click(button='left')

        # Moving to edit the R value
        pyautogui.moveTo(x=self.pos_r[0], y=self.pos_r[1])
        pyautogui.click(button='left')
        pyautogui.write(r, interval=0.10)

        # Moving to edit the G value
        pyautogui.moveTo(x=self.pos_g[0], y=self.pos_g[1])
        pyautogui.click(button='left')
        pyautogui.write(g, interval=0.10)

        # Moving to edit the B value
        pyautogui.moveTo(x=self.pos_b[0], y=self.pos_b[1])
        pyautogui.click(button='left')
        pyautogui.write(b, interval=0.10)

        # Moving to OK button
        pyautogui.moveTo(x=self.pos_okbutton[0], y=self.pos_okbutton[1])
        if delay == True:
            sleep(1)
        pyautogui.click(button='left')
        pyautogui.click(button='left')
    
    def mudar_ferramenta(self, ferramenta, espessura, opacidade, espessura_pos=(1866, 285), opacidade_pos=(1863, 365)):
        '''
        -> This will change the Paint's tool
        :param ferramenta: The tool. The available tools are: "pencil", "crayon", "pixelpen"
        :param espessura: The thickness of the tool. Must be an integer
        :param opacidade: The opacity of the tool. Must be an integer
        :param espessura_pos: A tuple with two values. The first value is the X position of the thickness on the screen. The second value is the Y position of the thickness on the screen
        :param opacidade_pos: A tuple with two values. The first value is the X position of the opacity on the screen. The second value is the Y position of the opacity on the screen
        :return: No return
        '''
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
    
    def pos_inicial_desenho(self, pos_tamanhoDesenho, pos_centroCanvas=(856, 592)):
        '''
        -> This will set the initial position where the cursor will be moved, then it will start to draw
        :param pos_tamanhoDesenho: Must be a tuple with two values. The first value is the X size of the photo. The second value is the Y size of the photo
        :param pos_centroCanvas: Must be a tuple with two values. The first value is the X position of the canvas' center. The second value is the Y position of the canvas' center
        :return: Will return the initial position of the drawing
        '''
        x = pos_tamanhoDesenho[0]
        y = pos_tamanhoDesenho[1]
        xmetade = x//2
        ymetade = y//2

        pyautogui.moveTo(pos_centroCanvas[0], pos_centroCanvas[1]) # Centraliza
        pyautogui.move(0, ymetade * -1) # Move para cima
        pyautogui.move(xmetade * -1, 0) # Move para a esquerda
        posicao = pyautogui.position()
        return posicao
    
    def desenhar(self, pos_tamanhoDeseho, lista_pixels, debug=False):
        '''
        -> This will draw the photo on the Paint's canvas
        :param pos_tamanhoDeseho: Must be a tuple with two values. The first value is the X size of the photo. The second value is the Y size of the photo
        :param lista_pixels: The list containing the pixels. Must be generated using the gerar_lista_pixels() method
        :param debug: If true, will print the debug things
        :return: No return
        '''
        try:
            pos_inicial = self.pos_inicial_desenho(pos_tamanhoDeseho)

            cores_diferentes = len(lista_pixels)

            for c in range(0, cores_diferentes):
                r = self.pegarListaDict(lista_pixels[c], c)[0][0]
                g = self.pegarListaDict(lista_pixels[c], c)[0][1]
                b = self.pegarListaDict(lista_pixels[c], c)[0][2]
                if len(self.pegarListaDict(lista_pixels[c], c)[0]) == 4:
                    a = self.pegarListaDict(lista_pixels[c], c)[0][3]
                else:
                    pass

                if debug == True:
                    print(r, g, b)
                
                pos_diferentes = len(lista_pixels[c][self.pegarListaDict(lista_pixels[c], c)[0]])

                if debug == True:
                    print('Quantidade de posições diferentes =', pos_diferentes)
                
                self.editar_cor(r, g, b)

                for count in range(0, pos_diferentes):
                    try:
                        x=lista_pixels[c][(r, g, b, a)][count][0]
                        y=lista_pixels[c][(r, g, b, a)][count][1]
                    except:
                        x=lista_pixels[c][(r, g, b)][count][0]
                        y=lista_pixels[c][(r, g, b)][count][1]
                    if debug == True:
                        print(f'x = {x}; y = {y}')

                    pyautogui.moveTo(x=pos_inicial[0] + x, y=pos_inicial[1] + y)
                    pyautogui.click(button='left')
        except KeyboardInterrupt:
            sair


debugs = Debug(434, 315, 1273, 862)
foto = Imagem('images/lupa jpg.jpg')
func = Funcoes()

# pos inicial = (600, 336)

print(debugs.tamanho_monitor())
lista = foto.gerar_lista_pixels(1273, 862)
debugs.centralizar_canvas()
func.mudar_ferramenta('pencil', 6, 30)
sleep(3)
func.desenhar(foto.tamanho_foto(), lista, debug=False)