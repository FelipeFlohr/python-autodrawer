dict = {'tamanhofoto_x': 696, 'tamanhofoto_y': 874}

medidaideal = str(input('Digite o eixo para a resolução recomendada (ex: x; y): '))
medidaint = int(input('Digite o valor para o eixo: '))

while True:
    if dict[f'tamanhofoto_{medidaideal}'] > medidaint:
        dict[f'tamanhofoto_x'] -= 1
        dict[f'tamanhofoto_y'] -= 1
    else:
        break

print('x = {}; y = {}'.format(dict['tamanhofoto_x'], dict['tamanhofoto_y']))