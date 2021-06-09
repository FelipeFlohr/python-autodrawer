from ctypes.wintypes import PLARGE_INTEGER
import pyautogui
from PIL import Image
from time import sleep
import keyboard

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

    def centralizar_canvas(self): # Bug -> Esse método não funciona se o NumLock estiver ligado
        '''
        -> This function centralizes the canvas on your screen. You will need to open Paint 3D to centralize
        :return: No return
        '''
        print('Abra o paint em 5 segundos')
        sleep(5)
        pyautogui.moveTo(self.monitor_x//2, self.monitor_y//2)
        pyautogui.click(button='right')
        pyautogui.move(20, 210)
        pyautogui.click(button='left')
        pyautogui.click(button='left')
        for _ in range(4):
            keyboard.press_and_release('pagedown')
            sleep(1)
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
        sleep(2)
        pyautogui.moveTo(pos_centroCanvas[0], pos_centroCanvas[1])
    
    def mover_cursor_4cantos_desenho(self, pos_tamanhoDesenho, pos_centroCanvas=(856, 592), desenhar=True):
        x = pos_tamanhoDesenho[0]
        y = pos_tamanhoDesenho[1]
        xmetade = x//2
        ymetade = y//2

        if desenhar == True:
            # Move o cursor para baixo
            pyautogui.moveTo(pos_centroCanvas[0], pos_centroCanvas[1])
            pyautogui.move(0, ymetade)
            #print(f'Movido x=0 y={ymetade}')

            # Clica e arrasta o cursor até o topo
            pyautogui.drag(0, (ymetade * 2)*-1, button='left')
            #print(f'Movido x=0 y={(ymetade * 2)*-1}')

            # Move o cursor para o centro
            pyautogui.moveTo(pos_centroCanvas[0], pos_centroCanvas[1])

            # Move o cursor para a direita
            pyautogui.move(xmetade, 0)
            #print(f'Movido x={xmetade} y=0')

            # Clica e arrasta o cursor até a esquerda total
            pyautogui.drag((xmetade * 2)*-1, 0, button='left')
            #print(f'Movido x={(xmetade * 2)*-1} y=0')

            # Aqui começa a fazer o quadrado
            # Faz a linha na inferior
            pyautogui.moveTo(pos_centroCanvas[0], pos_centroCanvas[1]) # Centraliza
            pyautogui.move(0, ymetade) # Move para baixo
            pyautogui.move(xmetade, 0) # Move para a direita
            pyautogui.drag((xmetade * 2)*-1, 0, button='left') # Clica e arrasta para a esquerda total
            pyautogui.drag(0, (ymetade * 2)*-1, button='left') # Clica e arrasta até o topo
            pyautogui.drag((xmetade * 2), 0, button='left') # Clica e arrasta para a direita total
            pyautogui.drag(0, ymetade * 2, button='left') # Clica e arrasta até a parte inferior
        else:
            pyautogui.moveTo(pos_centroCanvas[0], pos_centroCanvas[1]) # Centraliza
            pyautogui.move(0, ymetade) # Move para baixo
            pyautogui.move(xmetade, 0) # Move para a direita
            pyautogui.move((xmetade * 2)*-1, 0) # Move para a esquerda total
            pyautogui.move(0, (ymetade * 2)*-1) # Move até o topo
            pyautogui.move((xmetade * 2), 0) # Move para a direita total
            pyautogui.move(0, ymetade * 2) # Move até a parte inferior


class Imagem:
    def __init__(self, foto : str):
        '''
        -> Starter
        :param foto: The address of your image
        '''
        self.foto = foto

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
                if debug == True:
                    print('COORDENADA: x={} y={} | RGB: {}'.format(x, y, pixel[x, y]))
                dict = {'xy': (x, y), 'rgb': pixel[x, y]}
                lista.append(dict.copy())
        return lista

    def limpar_lista(self, lista):
        lista_nova = lista[:]
        cor_anterior = (0, 0 ,0)
        contagem_inicio = 1
        contagem_final = 1
        for c in range(0, len(lista)):
            if c == 0:
                cor_anterior = lista[c]['rgb']
            else:
                if lista[c]['rgb'] == cor_anterior:
                    contagem_final += 1
                else:
                    del lista_nova[contagem_inicio:contagem_final]
                    contagem_inicio = 1
                    contagem_final = 1
        return lista_nova

    def tamanho_foto(self):
        imagem = Image.open(self.foto)
        return imagem.size


class Funcoes:
    def __init__(self, pos_r=(1145, 493), pos_g=(1145, 550), pos_b=(1145, 606), pos_cores=(1695, 997), pos_okbutton=(851, 728)):
        self.pos_r = pos_r
        self.pos_g = pos_g
        self.pos_b = pos_b
        self.pos_cores = pos_cores
        self.pos_okbutton = pos_okbutton

    def editar_cor(self, r, g, b):
        '''
        -> A function for changing the color of the selected tool
        :param r: The R value
        :param g: The G value
        :param b: The B value
        :return: No return
        '''
        r = str(r)
        g = str(g)
        b = str(b)

        # Moving to edit an added color
        pyautogui.moveTo(x=self.pos_cores[0], y=self.pos_cores[1])
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
        sleep(1)
        pyautogui.click(button='left')
        pyautogui.click(button='left')
    
    def mudar_ferramenta(self, ferramenta, espessura, espessura_pos=(1866, 285)):
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
    
    def pos_inicial_desenho(self, pos_tamanhoDesenho, pos_centroCanvas=(856, 592)):
        x = pos_tamanhoDesenho[0]
        y = pos_tamanhoDesenho[1]
        xmetade = x//2
        ymetade = y//2

        pyautogui.moveTo(pos_centroCanvas[0], pos_centroCanvas[1]) # Centraliza
        pyautogui.move(0, ymetade * -1) # Move para cima
        pyautogui.move(xmetade * -1, 0) # Move para a esquerda
        posicao = pyautogui.position()
        return posicao
    
    def cor_proximopixel(self, lista_pixels, count):
        try:
            valores = lista_pixels[count + 1]['rgb']
            if len(valores) == 4:
                return (-2, -2, -2)
            else:
                return valores
        except:
            return (0, 0, 0)
    
    def desenhar(self, pos_tamanhoDeseho, lista_pixels, pos_centroCanvas=(856, 592)):
        pos_inicial = self.pos_inicial_desenho(pos_tamanhoDeseho)
        cor_anterior = (-1, -1, -1)
        cor_proximopx = (0, 0, 0)

        if cor_anterior == (-1, -1, -1):
            try:
                cor = (lista_pixels[0]['rgb'][0], lista_pixels[0]['rgb'][1], lista_pixels[0]['rgb'][2], lista_pixels[0]['rgb'][3])
                cor_anterior = (-2, -2, -2)
            except:
                self.editar_cor(r=lista_pixels[0]['rgb'][0], g=lista_pixels[0]['rgb'][1], b=lista_pixels[0]['rgb'][2])
                cor_anterior = (lista_pixels[0]['rgb'][0], lista_pixels[0]['rgb'][1], lista_pixels[0]['rgb'][2])

        for c in range(0, len(lista_pixels)):
            if c == 0:
                if cor_anterior == (-2, -2, -2):
                    pass
                else:
                    pyautogui.moveTo(pos_inicial[0], pos_inicial[1])
                    pyautogui.click(button='left')
                    cor_proximopx = self.cor_proximopixel(lista_pixels, c)
            else:
                if cor_proximopx == (-2, -2, -2):
                    cor_proximopx = self.cor_proximopixel(lista_pixels, c)
                else:
                    if cor_anterior == cor_proximopx:
                        pyautogui.dragTo(x=pos_inicial[0] + lista_pixels[c]['xy'][0], y=pos_inicial[1] + lista_pixels[c]['xy'][1], button='left')
                        cor_anterior = cor_proximopx
                        cor_proximopx = self.cor_proximopixel(lista_pixels, c)
                    else:
                        self.editar_cor(cor_proximopx[0], cor_proximopx[1], cor_proximopx[2])
                        pyautogui.dragTo(x=pos_inicial[0] + lista_pixels[c]['xy'][0], y=pos_inicial[1] + lista_pixels[c]['xy'][1], button='left')
                        cor_anterior = cor_proximopx
                        cor_proximopx = self.cor_proximopixel(lista_pixels, c)


debugs = Debug(434, 315, 1273, 862)
foto = Imagem('files/images/imagemteste.png')
func = Funcoes()

# pos inicial = (600, 336)

print(debugs.tamanho_monitor())
lista = foto.gerar_lista_pixels(foto.tamanho_foto()[0], foto.tamanho_foto()[1])
debugs.centralizar_canvas()
func.mudar_ferramenta('pixelpen', 1)
sleep(3)
func.desenhar(foto.tamanho_foto(), lista)