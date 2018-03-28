from random import randint
from time import sleep

print('Estou pensando em um número de 0 a 5. Tente adivinhar!')

número = randint(0, 5)

tentativa = int(input('Digite seu palpite: '))

print('Um segundo, por favor...')

sleep(2)

if tentativa == número:
    print('Parabéns! Você me venceu!')
else:
    print('Errou! Eu pensei em {}, não em {}.'.format(número, tentativa))
