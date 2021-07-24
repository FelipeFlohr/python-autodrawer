# Python Autodrawer for Paint 3D

EN: A script designed for autodrawing pictures in Paint 3D. Right now the program is entirely written in Brazilian Portuguese, although you can easily use it without any knowledge about Portuguese. Check out the introduction for the script.

PT-BR: Um script feito para desenhar imagens automaticamente no Paint 3D. Veja a seguir as noções básicas de como utilizar o script.

## EN: How to use it | PT-BR: How to use it

:warning: EN: **IT IS VERY IMPORTANT FOR YOU TO READ THIS PART** :warning:

:warning: PT-BR: **É DE SUMA IMPORTÂNCIA QUE VOCÊ LEIA ESTA PARTE** :warning:

### EN: The first step | PT-BR: O primeiro passo

EN: The first step is to run the script and then close. Once you did it, a file called **config.ini** will be on the root folder of the script, open it. Now we are going to see the parameters to change inside the file.

PT-BR: O primeiro passo é executar o script e fechar logo em seguida. Uma vez feito, um arquivo chamado **config.ini** irá aparecer na pasta raiz do script, abra-o. Agora veremos os parâmetros dentro do arquivo.

### EN: The "config.ini" file | PT-BR: O arquivo "config.ini"

EN: The **config.ini** is the file for changing the parameters. Let's take a look on what we can change here :arrow_heading_down:

PT-BR: O arquivo **config.ini** serve para mudar os parâmetros. Vamos dar uma olhada no que nós conseguimos mexer aqui :arrow_heading_down:

1.  `photo` **EN**: The file you want to draw on Paint 3D. images/photo.png by default. Must be inside the _images_ folder by default | **PT-BR**: O arquivo que você deseja desenhar no Paint 3D. images/photo.png por padrão. Deve estar dentro da pasta *images* por padrão.

2. `monitor_x` **EN**: The X size of your resolution. If you don't know the X size of your resolution, you can run the get_resolution.py inside the _tools_ folder to get it. 1920 by default. Must be an integer | **PT-BR**: O tamanho X da sua resolução. Se você não sabe o tamanho X da sua resolução, você pode abrir o arquivo get_resolution.py dentro da pasta _tools_ para obte-lá. 1920 por padrão. O valor deve ser do tipo integer por padrão.

3. `monitor_y` **EN**: The Y size of your resolution. If you don't know the Y size of your resolution, you can run the get_resolution.py inside the _tools_ folder to get it. 1080 by default. Must be an integer | **PT-BR**: O tamanho X da sua resolução. Se você não sabe o tamanho Y da sua resolução, você pode abrir o arquivo get_resolution.py dentro da pasta _tools_ para obte-lá. 1080 por padrão. O valor deve ser do tipo integer por padrão.

4.  `canvas_topleftx` **EN**: The X position of the top left corner of your canvas. 434 by default. Must be an integer. We will cover about "canvas" later | **PT-BR**: A posição X do canto superior esquerdo do seu canvas. 434 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

5.  `canvas_toplefty` **EN**: The Y position of the top left corner of your canvas. 315 by default. Must be an integer. We will cover about "canvas" later | **PT-BR**: A posição Y do canto superior esquerdo do seu canvas. 315 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

6.  `canvas_bottomrightx` **EN**: The X position of the Bottom Right Corner of your canvas. 1273 by default. Must be an integer. We will cover about "canvas" later | **PT-BR**: A posição X do canto inferior direito do seu canvas. 1273 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

7.  `canvas_bottomrighty` **EN**: The Y position of the Bottom Right Corner of your canvas. 862 by default. Must be an integer. We will cover about "canvas" later | **PT-BR**: A posição Y do canto inferior direito do seu canvas. 862 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

8.  `canvas_zoom` **EN**: Paint 3D's zoom value. 33 by default. Must be an integer. We will cover about "canvas" later | **PT-BR**: Valor do zoom no Paint 3D. 33 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

9. `canvas_zoompos` **EN**: A tuple with two values. The first one is the X position of the zoom selector on the screen. The second one is the Y value of the zoom selector on the screen. (1576, 102) by default. Must be a tuple | **PT-BR**: Uma tupla com dois valores. O primeiro valor é a posição X do selecionador de zoom na tela. O segundo valor é a posição Y do selecionador de zoom na tela. (1576, 102) by default. O valor deve ser uma tupla.

9.  `keyboard_interruptionKey` **EN**: The keyboard key to interrupt the program. 'space' by default. Must be a key compatible with [PyAutoGUI's keys](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys) | **PT-BR**: A tecla usada para interromper o programa. 'space' por padrão. O valor deve ser uma tecla compatível com a [lista de teclas do PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys).
 
10.  `colorSelector_rpos` **EN**: A tuple with two values. The first one is the X position of the R value in the color picker. The second one is the Y position of the R value in the color selector. (1145, 493) by default. Must be a tuple | **PT-BR**: Uma tupla com dois valores. O primeiro valor é a posição X da cor R no selecionador de cores. O segundo valor é a posição Y da cor R no selecionador de cores. (1145, 493) por padrão. O valor deve ser uma tupla.

11.  `colorSelector_gpos` **EN**: A tuple with two values. The first one is the X position of the G value in the color picker. The second one is the Y position of the G value in the color selector. (1145, 550) by default. Must be a tuple | **PT-BR**: Uma tupla com dois valores. O primeiro valor é a posição X da cor G no selecionador de cores. O segundo valor é a posição Y da cor G no selecionador de cores. (1145, 550) por padrão. O valor deve ser uma tupla.

12.  `colorSelector_bpos` **EN**: A tuple with two values. The first one is the X position of the B value in the color picker. The second one is the Y position of the B value in the color selector. (1145, 606) by default. Must be a tuple | **PT-BR**: Uma tupla com dois valores. O primeiro valor é a posição X da cor B no selecionador de cores. O segundo valor é a posição Y da cor B no selecionador de cores. (1145, 606) por padrão. O valor deve ser uma tupla.

13.  `colorSelector_okbutton` **EN**: A tuple with two values. The first one is the X position of the OK button in the color picker. The second one is the Y position of the OK button in the color selector. (851, 728) by default. Must be a tuple | **PT-BR**: Uma tupla com dois valores. O primeiro valor é a posição X do botão de OK no selecionador de cores. O segundo valor é a posição Y do botão de OK no selecionador de cores. (851, 728) por padrão. O valor deve ser uma tupla.

14.  `colorPalette_colorpos` **EN**: A tuple with two values. The first one is the X position of the color to be changed in the color palette. The second one is the Y position of the color to be changed in the color palette. (1695, 997) by default. Must be a tuple | **PT-BR**: Uma tupla com dois valores. O primeiro valor é a posição X da cor para ser trocada na palheta de cores. O segundo valor é a posição Y do cor para ser trocada na palheta de cores. (1695, 997) por padrão. O valor deve ser uma tupla.

15.  `draw_tool` **EN**: The tool you want to use. The available tools are: "pencil, crayon, pixelpen". 'pencil' by default | **PT-BR**: A ferramenta que você deseja usar. As ferramentas disponíveis são: "pencil, crayon, pixelpen". 'pencil' por padrão.

16.  `draw_thickness` **EN**: The thickness of the tool. 6 by default. Must be an integer > 0 | **PT-BR**: A espessura da ferramenta. 6 por padrão. O valor deve ser do tipo integer e maior que 0.

17. `draw_opacity` **EN**: The opacity of the tool. 60 by default. Must be an integer > 0 and < 101 | **PT-BR**: A opacidade da ferramenta. 60 por padrão. O valor deve ser do tipo integer maior que 0 e menor que 101.

19.  `draw_thicknesspos` **EN**: A tuple with two values. The first one is the X position of the thickness selector on the screen. The second one is the Y position of the thickness selector on the screen. (1866, 285) by default. Must be a tuple | **PT-BR**: Uma tupla com dois valores. O primeiro é a posição X do selecionador de espessura na tela. O segundo valor é a posição Y no selecionador de espessura na tela. (1866, 285) por padrão. O valor deve ser uma tupla.

20.  `draw_opacitypos` **EN**: A tuple with two values. The first one is the X position of the opacity selector on the screen. The second one is the Y position of the opacity selector on the screen. (1863, 365) by default. Must be a tuple | **PT-BR**: Uma tupla com dois valores. O primeiro é a posição X do selecionador de opacidade na tela. O segundo valor é a posição Y do selecionador de opacidade na tela. (1863, 365) por padrão. O valor deve ser uma tupla.

21.  `delay` **EN**: The delay value of drawing pixels on the canvas. :warning: **WARNING** :warning:: Lower values might crash/glitch Paint 3D. If you are experiencing glitches even with the default value, please INCREASE the value. 0.001 by default. Must be a float | **PT-BR**: O valor do delay de desenhar pixels no canvas. :warning: **ATENÇÃO** :warning:: Valores mais baixos podem causar travamentos ou bugs no Paint 3D. Se você estiver presenciando bugs/glitches/erros com o valor padrão, por favor AUMENTE-O. 0.001 por padrão. O valor deve ser do tipo float.

### EN: Getting the screen positions | PT-BR: Pegando as posições na tela

EN: As you may see, the X and Y position of the values inside the _config.ini_ file are designed specifically for my resolution (1920x1080, Full HD), so if you have a different resolution, you'll need to change some values. To get the screen coordinates, there's a script inside the _tools_ folder called *get_x_y.py* that will help you. So, run it (I would recommend open it with Command Prompt) and press Control (can be both left or right) to get the current XY cursor position. Check out the screenshot below.

PT-BR: Como você pode ver, as posições X e Y dos valores dentro do arquivo _config.ini_ são específicamente feitos para a minha resolução (1920x1080, Full HD), então, se você têm uma resolução diferente, muito provavelmente você irá precisar mudar alguns valores. Para pegar as coordenadas da tela, há o script *get_x_y.py* que irá te ajudar no mesmo. Então, abra-o (eu recomendo abrir o script com o Prompt de Comando) e aperte Control (pode ser tanto o esquerdo como o direito) para pegar a posição atual do cursor. Veja a captura de tela abaixo.

<img scr = "README/get_x_y_example.png">