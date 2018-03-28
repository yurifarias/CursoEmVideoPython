# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais;
# - Isósceles: dois lados iguais;
# - Escaleno: todos os lados diferentes.

r1 = float(input('Digite o comprimento do primeiro segmento de reta: '))
r2 = float(input('Digite o comprimento do segundo segmento de reta: '))
r3 = float(input('Digite o comprimento do terceiro segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os três segmentos de retas formam um triângulo ', end='')

    if r1 == r2 == r3:
        print('EQUILÁTERO!')

    elif r1 != r2 != r3:
        print('ESCALENO!')

    else:
        print('ISÓSCELES!')

else:
    print('Os três segmentos de retas não formam um triângulo.')
