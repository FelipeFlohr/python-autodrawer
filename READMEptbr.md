# Python Autodrawer para o Paint 3D

Um script feito para desenhar imagens automaticamente no Paint 3D. Veja a seguir as noções básicas de como utilizar o script.

## 1. Requisitos

- [Windows 10+](https://www.microsoft.com/software-download/windows10)
- [Paint 3D](https://www.microsoft.com/en-us/p/paint-3d/9nblggh5fv99?source=lp&activetab=pivot:overviewtab)
- [Python 3.8+](https://www.python.org/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Keyboard](https://pypi.org/project/keyboard/)
- [Pillow](https://pypi.org/project/Pillow/)

## 2. How to use it

:warning: **É DE SUMA IMPORTÂNCIA QUE VOCÊ LEIA ESTA PARTE** :warning:

### 2.1 O primeiro passo

O primeiro passo é executar o script e fechar logo em seguida. Uma vez feito, um arquivo chamado **config.ini** irá aparecer na pasta raiz do script, abra-o. Agora veremos os parâmetros dentro do arquivo.

### 2.2 O arquivo "config.ini"

O arquivo **config.ini** serve para mudar os parâmetros. Vamos dar uma olhada no que nós conseguimos mexer aqui :arrow_heading_down:

1.  `photo` O arquivo que você deseja desenhar no Paint 3D. images/photo.png por padrão. Deve estar dentro da pasta *images* por padrão.

2. `monitor_x` O tamanho X da sua resolução. Se você não sabe o tamanho X da sua resolução, você pode abrir o arquivo get_resolution.py dentro da pasta _tools_ para obte-lá. 1920 por padrão. O valor deve ser do tipo integer por padrão.

3. `monitor_y` O tamanho X da sua resolução. Se você não sabe o tamanho Y da sua resolução, você pode abrir o arquivo get_resolution.py dentro da pasta _tools_ para obte-lá. 1080 por padrão. O valor deve ser do tipo integer por padrão.

4.  `canvas_topleftx` A posição X do canto superior esquerdo do seu canvas. 434 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

5.  `canvas_toplefty` A posição Y do canto superior esquerdo do seu canvas. 315 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

6.  `canvas_bottomrightx` A posição X do canto inferior direito do seu canvas. 1273 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

7.  `canvas_bottomrighty` A posição Y do canto inferior direito do seu canvas. 862 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

8.  `canvas_zoom` Valor do zoom no Paint 3D. 33 por padrão. O valor deve ser do tipo integer. Você verá mais sobre "canvas" a seguir.

9. `canvas_zoompos` Uma tupla com dois valores. O primeiro valor é a posição X do selecionador de zoom na tela. O segundo valor é a posição Y do selecionador de zoom na tela. (1576, 102) by default. O valor deve ser uma tupla.

10.  `keyboard_interruptionKey` A tecla usada para interromper o programa. 'space' por padrão. O valor deve ser uma tecla compatível com a [lista de teclas do PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys).
 
11.  `colorSelector_rpos` Uma tupla com dois valores. O primeiro valor é a posição X da cor R no selecionador de cores. O segundo valor é a posição Y da cor R no selecionador de cores. (1145, 493) por padrão. O valor deve ser uma tupla.

12.  `colorSelector_gpos` Uma tupla com dois valores. O primeiro valor é a posição X da cor G no selecionador de cores. O segundo valor é a posição Y da cor G no selecionador de cores. (1145, 550) por padrão. O valor deve ser uma tupla.

13.  `colorSelector_bpos` Uma tupla com dois valores. O primeiro valor é a posição X da cor B no selecionador de cores. O segundo valor é a posição Y da cor B no selecionador de cores. (1145, 606) por padrão. O valor deve ser uma tupla.

14.  `colorSelector_okbutton` Uma tupla com dois valores. O primeiro valor é a posição X do botão de OK no selecionador de cores. O segundo valor é a posição Y do botão de OK no selecionador de cores. (851, 728) por padrão. O valor deve ser uma tupla.

15.  `colorPalette_colorpos` Uma tupla com dois valores. O primeiro valor é a posição X da cor para ser trocada na palheta de cores. O segundo valor é a posição Y do cor para ser trocada na palheta de cores. (1695, 997) por padrão. O valor deve ser uma tupla.

16.  `draw_tool` A ferramenta que você deseja usar. As ferramentas disponíveis são: "pencil, crayon, pixelpen". 'pencil' por padrão.

17.  `draw_thickness` A espessura da ferramenta. 6 por padrão. O valor deve ser do tipo integer e maior que 0.

18. `draw_opacity` A opacidade da ferramenta. 60 por padrão. O valor deve ser do tipo integer maior que 0 e menor que 101.

19.  `draw_thicknesspos` Uma tupla com dois valores. O primeiro é a posição X do selecionador de espessura na tela. O segundo valor é a posição Y no selecionador de espessura na tela. (1866, 285) por padrão. O valor deve ser uma tupla.

20.  `draw_opacitypos` Uma tupla com dois valores. O primeiro é a posição X do selecionador de opacidade na tela. O segundo valor é a posição Y do selecionador de opacidade na tela. (1863, 365) por padrão. O valor deve ser uma tupla.

21.  `delay` O valor do delay de desenhar pixels no canvas. :warning: **ATENÇÃO** :warning:: Valores mais baixos podem causar travamentos ou bugs no Paint 3D. Se você estiver presenciando bugs/glitches/erros com o valor padrão, por favor AUMENTE-O. 0.01 por padrão. O valor deve ser do tipo float.

### 2.2.1 Entendendo os parâmetros com o Paint 3D

Repare na captura de tela abaixo.

![](README/example4.png)

Repare que cada número representa um tópico acima com as respectivas posições. Agora, repare o tópico 14 (o parâmetro `colorPalette_colorpos`): se é a sua primeira vez usando Paint 3D e/ou você nunca criou uma cor personalizada, aperte o botão com o símbolo "+" e crie uma cor personalizada (pode ser qualquer cor, apenas crie). Agora repare na captura de tela abaixo.

![](README/example5.png)

Se você clicar com o botão direito do mouse na cor personalizada e clicar em _editar_, este editor de cores irá abrir. E novamente: cada número está relacionado com um tópico acima. Para pegar as posições da tela, o próximo tópico irá abordar isto.

### 2.2.2 Pegando as posições na tela

Como você pode ver, as posições X e Y dos valores dentro do arquivo _config.ini_ são específicamente feitos para a minha resolução (1920x1080, Full HD), então, se você têm uma resolução diferente, muito provavelmente você irá precisar mudar alguns valores. Para pegar as coordenadas da tela, há o script *get_x_y.py* que irá te ajudar no mesmo. Então, abra-o (eu recomendo abrir o script com o Prompt de Comando) e aperte Control (pode ser tanto o esquerdo como o direito) para pegar a posição atual do cursor. Veja a captura de tela abaixo.

![](README/example1.png)

Repare que as posições X e Y no prompt são 0, isso é porque meu cursor estava no canto superior esquerdo (todavia, o cursor não foi capturado na captura de tela). Obviamente, se você mudar a posição do cursor, as coordenadas irão mudar também.

### 2.3 Entendendo o "canvas"

O canvas é a área na qual o programa irá usar para desenhar. Repare na captura de tela abaixo.

![](README/example2.png)

Eu abri uma imagem simples: uma folha A4 virada na horizontal com uma margem preta num fundo preto. O ponto é: eu somente quero que o script desenhe dentro da margem, então, como é que eu faço isso? É fácil: é só pegar as posições XY do canto superior esquerdo e do canto inferior direito e colocá-las nos parâmetros `canvas_topleftx`, `canvas_toplefty`, `canvas_bottomrightx`, `canvas_bottomrighty` dentro do arquivo _config.ini_. Se você deseja conferior a área desenhável que você possui, basta rodar o script *draw_drawingarea.py* que irá desenhar automáticamente as margens para você. Olhe o exemplo abaixo.

![](README/example3.png)

Uma vez que eu rodei o script *draw_drawingarea.py*, uma margem vermelha foi desenhada representando o espaço desenhável que eu tenho. O programa apenas irá desenhar dentro dessa área. Além disso, o desenho será no centro do "canvas". Também repare que a imagem é 4000x2250px e o meu zoom está em 33%, pois é a melhor escolha para mim. Obviamente, se você tiver uma imagem diferente e/ou um monitor diferente, você terá que mudar os parâmetros dentro de _config.ini_.

## 3. Rodando o script

Uma vez que você configurou cada parâmetro e coordenada no arquivo _config.ini_ e no _main_ (se sua resolução não for 1920x1080), apenas rode o script e deixe o Paint 3D como sua janela ativa. O script irá rodar sem nenhum problema se você seguiu todos os passos acima. Você pode ver o script rodando no vídeo abaixo.

[![Video](README/thumbnail.png)](https://www.youtube.com/watch?v=mbPgQSFNbo4 "Video")

Se você seguiu todos os passos acima, provavelmente você não irá encontrar nenhum problema, mas caso encontre, provavelmente estará relacionado ás suas coordenadas de tela, então fique atento pois você talvez tenha que mudar as configurações dentro do *config.ini* e do arquivo _main_

## 4. FAQ

Q: **EN**: Paint 3D está crashando/travando/bugando, como eu resolvo isso?

- R: Como está escrito no _config.ini_, isso provavelmente está relacionado ao parâmetro `delay`. Você provavelmente irá precisar aumentar o valor para parar os travamentos no Paint 3D.

Q: Teria como você explicar brevemente como este script funciona?

- R: Este script funciona iterando com cada pixel na foto desejável, e então, colocando os valores R/G/B/A dentro de uma lista. Com esta lista, o script irá automaticamente usar o teclado e o mouse (como um Macro) para trabalhar no Paint 3D e automaticamente desenhar dentro do canvas.

Q: Para que sistema foi projetado os valores padrões?

- R: Os valores padrões foram projetados para um monitor 1920x1080, rodando-os num canvas 4000x2250px. Então se você deseja rapidamente usar o script, apenas mudar o parâmetro `photo` dentro do arquivo *config.ini* e ajuste o canvas para 4000x2250px no Paint 3D.

Q: Há um bug na qual eu desejo reportar, como posso contactá-lo?

- R: Você pode abrir uma discussão aqui neste repositório ou me chamar no meu email: *felipeflohrlol@gmail.com*. Sinta-se a vontade para me chamar lá.

Q: Por que você fez isso? Isso é inútil.

- R: O motivo de eu ter feito este script é porque a minha professora de artes estava mandando muita tarefa para eu fazer (sério, muita tarefa mesmo), e já que eu estou fazendo EAD, eu pensei em fazer este script como uma maneira de me ajudar a fazer as tarefas.
