from PIL import Image
from time import sleep

class Imagem:
    def __init__(self, foto : str):
        '''
        -> Constructor
        :param foto: The address of your image
        '''
        self.foto = foto

    def valores_repetidos(self, valor, lista):
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
                else:
                    if self.valores_repetidos(cor_pixel_atual, lista) == -1:
                        dict = {(cor_pixel_atual): [(x, y)]}
                        lista.append(dict.copy())
                    else:
                        tupla = (x, y)
                        lista[self.valores_repetidos(cor_pixel_atual, lista)][cor_pixel_atual].append(tupla[:])
        return lista

    def tamanho_foto(self):
        imagem = Image.open(self.foto)
        return imagem.size
    
    def substituircor(self, cororiginal, corsubstituir, nomearquivo):
        imagem = Image.open(self.foto)
        pixel = imagem.load()
        tamanho = imagem.size
        tamanho_x = tamanho[0]
        tamanho_y = tamanho[1]

        for x in range(0, tamanho_x):
            for y in range(0, tamanho_y):
                if pixel[x, y] == cororiginal:
                    pixel[x, y] = corsubstituir
                    #print('Pixel substituido')
                else:
                    pass
        imagem.save(nomearquivo)


imagem = Imagem('tools/image/deutsche volke.png')

lista = imagem.gerar_lista_pixels(imagem.tamanho_foto()[0], imagem.tamanho_foto()[1])
print(lista[0].keys())
print('Há {} cores diferentes.'.format(len(lista)))
imagem.substituircor((255, 255, 255, 255), (255, 255, 20, 0), 'preussens.png')