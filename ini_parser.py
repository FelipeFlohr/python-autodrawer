class Parser:
    def __init__(self, nomeArquivo):
        '''
        -> Constructor
        :param nomeArquivo: The name of the file you want to generate
        '''
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
photo = images/photo.png # < - String. The file you want to draw on Paint 3D. Must be inside the 'images' folder by default
monitor_x = 1920 # <- Integer. The X size of your monitor. 1920 by default
monitor_y = 1080 # <- Integer. The Y size of your monitor. 1080 by default
canvas_topleftx = 434 # <- Integer. The X position of the Top Left Corner of your canvas. 434 by default
canvas_toplefty = 315 # <- Integer. The Y position of the Top Left Corner of your canvas. 315 by default
canvas_bottomrightx = 1273 # <- Integer. The X position of the Bottom Right Corner of your canvas. 1273 by default
canvas_bottomrighty = 862 # <- Integer. The Y position of the Bottom Right Corner of your canvas. 862 by default
canvas_zoom = 33 # <- Integer. The zoom you want your canvas to be. 33 by default
canvas_zoompos = (1576, 102) # <- Tuple. A tuple with two values. The first one is the X position of the zoom selector. The second one is the Y position of the zoom selector. (1576, 102) by default
keyboard_interruptionKey = space # <- String. The keyboard key to interrupt the program. 'space' by default
colorSelector_rpos = (1145, 493) # <- Tuple. A tuple with two values. The first one is the X position of the R value in the color selector. The second one is the Y position of the R value in the color selector. (1145, 493) by default
colorSelector_gpos = (1145, 550) # <- Tuple. A tuple with two values. The first one is the X position of the G value in the color selector. The second one is the Y position of the G value in the color selector. (1145, 550) by default
colorSelector_bpos = (1145, 606) # <- Tuple. A tuple with two values. The first one is the X position of the B value in the color selector. The second one is the Y position of the B value in the color selector. (1145, 606) by default
colorSelector_okbutton = (851, 728) # <- Tuple. A tuple with two values. The first one is the X position of the OK button in the color selector. The second one is the Y position of the OK button in the color selector. (851, 728) by default
colorPalette_colorpos = (1695, 997) # <- Tuple. A tuple with two values. The first one is the X position of the color to be changed in the color palette. The second one is the Y position of the color to be changed in the color palette. (1695, 997) by default
draw_tool = pencil # <- String. The tool you want to use. The available tools are: pencil, crayon, pixelpen. 'pencil' by default
draw_thickness = 6 # <- Integer. The thickness of the tool. Must be > 0. 6 by default
draw_opacity = 60 # <- Integer. The opacity of the tool. Must be > 0 and < 101. 60 by default
draw_thicknesspos = (1866, 285) # <- Tuple. A tuple with two values. The first one is the X position of the thickness selector on the screen. The second one is the Y position of the thickness selector on the screen. (1866, 285) by default
draw_opacitypos = (1863, 365) # <- Tuple. A tuple with two values. The first one is the X position of the opacity selector on the screen. The second one is the Y position of the opacity selector on the screen. (1863, 365) by default
delay = 0.01 # Float. The delay of drawing pixels on the canvas. WARNING: Lower values might crash/glitch Paint 3D. If you are experiencing glitches even with the default value, please INCREASE the value. 0.01 by default
''')
        except:
            print('Arquivo já existente')

    def contarLinhas(self):
        '''
        -> This will count how many lines there is on the file
        :return: The total amount of lines
        '''
        arquivo = open(f'{self.nomeArquivo}', 'r')
        linhas = 0
        for linha in arquivo:
            if linha != '\n':
                linhas += 1
        arquivo.close()
        return linhas

    def linhas(self):
        '''
        -> This will generate a list where each index is one line of the file
        :return: Return a list where each index is one line
        '''
        linha = open('{}'.format(self.nomeArquivo), 'r')
        linhatotal = linha.readlines()
        listanova = list()
        for index in linhatotal:
            linhanova = index.replace('\n', '').strip()
            listanova.append(linhanova[:])
        return listanova

    def procurarParametro(self, param):
        '''
        -> This will search every line trying to find the specified parameter.
        :param param: The parameter you want to seach
        :return: Returns the entire string containg the parameter
        '''
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
        '''
        -> Will find the "=" position on the line
        :param linha: The line you want to find the "=" position
        :return: Return the index position of "="
        '''
        posIgual = -1
        for c in range(0, len(linha)):
            if linha[c] == '=':
                posIgual = c
            else:
                pass
        return posIgual

    def posComent(self, linha):
        '''
        -> Will find the "#" position on the line
        :param linha: The line you want to find the "#" position
        :return: Return the index position of "#"
        '''
        posComent = -1
        for c in range(0, len(linha)):
            if linha[c] == '#':
                posComent = c
            else:
                pass
        return posComent

    def argumento(self, linha, type):
        '''
        -> Will return the value specified for the parameter
        :param linha: The line you want to return the value
        :param type: The type you want to return the values. Currently, there are this options: 'tuple_int', 'int', 'str', 'float'. Please, specify correctly to each one
        :return: Will return the value for the line.
        '''
        TIPOS = ['tuple_int', 'int', 'str', 'float']
        arg =  linha[self.posIgual(linha) + 1 : self.posComent(linha)].strip()
        if type not in TIPOS:
            raise TypeError('Type not available')
        if type == 'tuple_int':
            try:
                argtupla = arg.replace('(', '').replace(')', '').replace(' ', '').split(',')
                lista = list(argtupla)
                listanova = list()
                for item in lista:
                    integer = int(item)
                    listanova.append(integer)
                return tuple(listanova)
            except Exception:
                raise TypeError('Not possible to convert to the specified type.')
        elif type == 'int':
            try:
                return int(arg)
            except Exception:
                raise TypeError('Not possible to convert to the specified type.')
        elif type == 'str':
            try:
                return arg
            except Exception:
                raise TypeError('Not possible to convert to the specified type.')
        elif type == 'float':
            try:
                return float(arg)
            except Exception:
                raise TypeError('Not possible to convert to the specified type.')


class Parameters(Parser):
    '''
    -> Each method in this class does the same thing. Just the parameter changes
    '''
    pass

    def photo(self):
        return self.argumento(self.procurarParametro('photo'), 'str')

    def monitor_x(self):
        return self.argumento(self.procurarParametro('monitor_x'), 'int')

    def monitor_y(self):
        return self.argumento(self.procurarParametro('monitor_y'), 'int')

    def canvas_topleftx(self):
        return self.argumento(self.procurarParametro('canvas_topleftx'), 'int')

    def canvas_toplefty(self):
        return self.argumento(self.procurarParametro('canvas_toplefty'), 'int')

    def canvas_bottomrightx(self):
        return self.argumento(self.procurarParametro('canvas_bottomrightx'), 'int')

    def canvas_bottomrighty(self):
        return self.argumento(self.procurarParametro('canvas_bottomrighty'), 'int')

    def canvas_zoom(self):
        return self.argumento(self.procurarParametro('canvas_zoom'), 'int')

    def canvas_zoompos(self):
        return self.argumento(self.procurarParametro('canvas_zoompos'), 'tuple_int')

    def keyboard_interruptionKey(self):
        return self.argumento(self.procurarParametro('keyboard_interruptionKey'), 'str')

    def colorSelector_rpos(self):
        return self.argumento(self.procurarParametro('colorSelector_rpos'), 'tuple_int')

    def colorSelector_gpos(self):
        return self.argumento(self.procurarParametro('colorSelector_gpos'), 'tuple_int')

    def colorSelector_bpos(self):
        return self.argumento(self.procurarParametro('colorSelector_bpos'), 'tuple_int')

    def colorSelector_okbutton(self):
        return self.argumento(self.procurarParametro('colorSelector_okbutton'), 'tuple_int')

    def colorPalette_colorpos(self):
        return self.argumento(self.procurarParametro('colorPalette_colorpos'), 'tuple_int')

    def draw_tool(self):
        return self.argumento(self.procurarParametro('draw_tool'), 'str')

    def draw_thickness(self):
        return self.argumento(self.procurarParametro('draw_thickness'), 'int')

    def draw_opacity(self):
        return self.argumento(self.procurarParametro('draw_opacity'), 'int')

    def draw_thicknesspos(self):
        return self.argumento(self.procurarParametro('draw_thicknesspos'), 'tuple_int')

    def draw_opacitypos(self):
        return self.argumento(self.procurarParametro('draw_opacitypos'), 'tuple_int')

    def delay(self):
        return self.argumento(self.procurarParametro('delay'), 'float')

if __name__ == '__main__':
    pass
else:
    Parameters('config.ini').escrever()