from main import Debug
from main import Funcoes
from time import sleep

debug = Debug()
func = Funcoes()

debug.centralizar_canvas()
func.mudar_ferramenta()
func.editar_cor(255, 0, 0)
debug.desenhar4cantos()