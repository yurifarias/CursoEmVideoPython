# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

item = ('Pedra', 'Papel', 'Tesoura')

print('[ 0 ] - Pedra')
print('[ 1 ] - Papel')
print('[ 2 ] - Tesoura')
escolha = int(input('Digite a sua escolha: '))

escolhaPC = randint(0, 2)

if escolha < 0 or escolha > 2:
    print('Erro! Digite 1, 2 ou 3.')

else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')

    print('Você escolheu {}'.format(item[escolha]))
    print('O computador escolheu {}'.format(item[escolhaPC]))

    if (escolha == 0 and escolhaPC == 2) or (escolha == 1 and escolhaPC == 0) or (escolha == 2 and escolhaPC == 1):
        print('Você venceu!')

    elif escolha == escolhaPC:
        print('Empate!')

    else:
        print('Você perdeu!')
