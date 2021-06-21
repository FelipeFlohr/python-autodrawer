class Parser:
    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo

    def escrever(self):
        '''
        -> Irá gerar um arquivo .ini de configurações na pasta raíz. Caso o arquivo já exista, nada acontecerá
        :return: sem retorno
        '''
        try:
            arquivo = open(f'{self.nomeArquivo}', 'x')
            arquivo.write('''# ---File Configs---
# This is the file where you are going to put your configs in
# Please, be cautious to not fill some parameter with the wrong value
#
# THIS IS YOUR CANVAS
# -> x=int y=int------------------ <- x=int y=int
#               |                |
#               |     CANVAS     |
#               |                |
# -> x=int y=int------------------ <- x=int y=int
#
photo = photo.png # < - String. The file you want to draw on Paint 3D. Must be inside the 'images' folder by default
canvas_topleftx = 434 # <- Integer. The X position of the Top Left Corner of your canvas. 434 by default
canvas_toplefty = 315 # <- Integer. The Y position of the Top Left Corner of your canvas. 315 by default
canvas_bottomrightx = 1273 # <- Integer. The X position of the Bottom Right Corner of your canvas. 1273 by default
canvas_bottomrighty = 862 # <- Integer. The Y position of the Bottom Right Corner of your canvas. 862 by default
canvas_zoom = 33 # <- Integer. The zoom you want your canvas to be. 33 by default
keyboard_interruptionKey = space # <- String. The keyboard key to interrupt the program. 'space' by default
colorSelector_rpos = (1145, 493) # <- Tuple. A tuple with two values. The first one is the X position of the R value in the color selector. The second one is the Y position of the R value in the color selector. (1145, 493) by default
colorSelector_gpos = (1145, 550) # <- Tuple. A tuple with two values. The first one is the X position of the G value in the color selector. The second one is the Y position of the G value in the color selector. (1145, 550) by default
colorSelector_bpos = (1145, 606) # <- Tuple. A tuple with two values. The first one is the X position of the B value in the color selector. The second one is the Y position of the B value in the color selector. (1145, 606) by default
colorSelector_okbutton = (851, 728) # <- Tuple. A tuple with two values. The first one is the X position of the OK button in the color selector. The second one is the Y position of the OK button in the color selector. (851, 728) by default
colorPalette_colorpos = (1695, 997) # <- Tuple. A tuple with two values. The first one is the X position of the color to be changed in the color palette. The second one is the Y position of the color to be changed in the color palette. (1695, 997) by default
draw_tool = pencil # <- String. The tool you want to use. The available tools are: pencil, crayon, "pixelpen. pencil by default
draw_thickness = 6 # <- Integer. The thickness of the tool. Must be > 0. 6 by default
draw_opacity = 60 # <- Integer. The opacity of the tool. Must be > 0 and <= 100. 60 by default
draw_thicknesspos = (1866, 285) # <- Tuple. A tuple with two values. The first one is the X position of the thickness selector on the screen. The second one is the Y position of the thickness selector on the screen. (1866, 285) by default
draw_opacitypos = (1863, 365) # <- Tuple. A tuple with two values. The first one is the X position of the opacity selector on the screen. The second one is the Y position of the opacity selector on the screen. (1863, 365) by default
delay = 0.001 # Float. The delay of drawing pixels on the canvas. WARNING: Lower values might crash/glitch Paint 3D. If you are experiencing glitches even with the default value, please INCREASE the value. 0.001 by default
''')
        except:
            print('Arquivo já existente')

    def contarLinhas(self):
        arquivo = open(f'{self.nomeArquivo}', 'r')
        linhas = 0
        for linha in arquivo:
            if linha != '\n':
                linhas += 1
        arquivo.close()
        return linhas
    
    def linhas(self):
        linha = open('{}'.format(self.nomeArquivo), 'r')
        linhatotal = linha.readlines()
        listanova = list()
        for index in linhatotal:
            linhanova = index.replace('\n', '').strip()
            listanova.append(linhanova[:])
        return listanova
    
    def procurarParametro(self, param):
        listaLinhas = self.linhas()
        linha = -1
        contagem = 0
        while True:
            if contagem >= len(listaLinhas):
                raise IndexError('Parâmetro não encotrado na lista.')
            if listaLinhas[contagem][0] == '' or listaLinhas[contagem][0] == '#' or listaLinhas[contagem][0] == ' ':
                contagem += 1
            elif param in listaLinhas[contagem]:
                linha = contagem
                break
            else:
                contagem+= 1
                pass
        return listaLinhas[linha]
    
    def posIgual(self, linha):
        posIgual = -1
        for c in range(0, len(linha)):
            if linha[c] == '=':
                posIgual = c
            else:
                pass
        return posIgual

    def posComent(self, linha):
        posComent = -1
        for c in range(0, len(linha)):
            if linha[c] == '#':
                posComent = c
            else:
                pass
        return posComent

    def argumento(self, linha, type):
        tipos = ['tuple_int', 'int', 'str', 'float']
        arg =  linha[self.posIgual(linha) + 1 : self.posComent(linha)].strip()
        if type not in tipos:
            return TypeError('Type not available')
        if type == 'tuple_int':
            try:
                argtupla = arg.replace('(', '').replace(')', '').replace(' ', '').split(',')
                lista = list(argtupla)
                listanova = list()
                for item in lista:
                    integer = int(item)
                    listanova.append(integer)
                return tuple(listanova)
            except:
                raise TypeError('Not possible to convert to the specified type.')
        elif type == 'int':
            try:
                return int(arg)
            except:
                raise TypeError('Not possible to convert to the specified type.')
        elif type == 'str':
            try:
                return arg
            except:
                raise TypeError('Not possible to convert to the specified type.')
        elif type == 'float':
            try:
                return float(arg)
            except:
                raise TypeError('Not possible to convert to the specified type.')

class Parameters(Parser):
    pass

    def photo(self):
        return self.argumento(self.procurarParametro('photo'), 'str')

    def canvas_topleftx(self):
        return self.argumento(self.procurarParametro('canvas_topleftx', 'int'))

    def canvas_toplefty(self):
        return self.argumento(self.procurarParametro('canvas_toplefty', 'int'))

    def canvas_bottomrightx(self):
        return self.argumento(self.procurarParametro('canvas_bottomrightx', 'int'))

    def canvas_bottomrighty(self):
        return self.argumento(self.procurarParametro('canvas_bottomrighty', 'int'))

    def canvas_zoom(self):
        return self.argumento(self.procurarParametro('canvas_zoom', 'int'))

    def keyboard_interruptionKey(self):
        return self.argumento(self.procurarParametro('keyboard_interruptionKey', 'str'))

    def colorSelector_rpos(self):
        return self.argumento(self.procurarParametro('colorSelector_rpos', 'tuple_int'))

    def colorSelector_gpos(self):
        return self.argumento(self.procurarParametro('colorSelector_gpos', 'tuple_int'))

    def colorSelector_bpos(self):
        return self.argumento(self.procurarParametro('colorSelector_bpos', 'tuple_int'))

    def colorSelector_okbutton(self):
        return self.argumento(self.procurarParametro('colorSelector_okbutton', 'tuple_int'))

    def colorPalette_colorpos(self):
        return self.argumento(self.procurarParametro('colorPalette_colorpos', 'tuple_int'))

    def draw_tool(self):
        return self.argumento(self.procurarParametro('draw_tool', 'str'))

    def draw_thickness(self):
        return self.argumento(self.procurarParametro('draw_thickness', 'int'))

    def draw_opacity(self):
        return self.argumento(self.procurarParametro('draw_opacity', 'int'))

    def draw_thicknesspos(self):
        return self.argumento(self.procurarParametro('draw_thicknesspos', 'tuple_int'))

    def draw_opacitypos(self):
        return self.argumento(self.procurarParametro('draw_opacitypos', 'tuple_int'))

    def delay(self):
        return self.argumento(self.procurarParametro('delay', 'float'))