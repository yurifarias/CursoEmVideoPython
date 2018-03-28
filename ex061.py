# Refaça o DESAFIO 51, lendo o primeiro
# termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão
# usando a estrutura while.

termo1 = int(input('Digite o valor do primeiro termo: '))
razão = int(input('Digite a razão da progressão aritimética: '))

t = 1

while t < 11:
    print('O {:2}o termo vale {:2}'.format(t, termo1 + razão * (t - 1)))
    t += 1
