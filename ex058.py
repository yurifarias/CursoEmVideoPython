# Melhore o jogo do DESAFIO 028 onde o computador vai
# "pensar" em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessários para
# vencer.

from random import randint

acertou = False
num = randint(1, 10)
palpites = 0

tentativa = int(input('Escolhi um número de 0 a 10, tente adivinhá-lo: '))

while not acertou:

    palpites += 1

    if tentativa > num:

        tentativa = int(input('Menos! tente novamente: '))

    elif tentativa < num:

        tentativa = int(input('Mais! tente novamente: '))

    else:

        print('Parabéns, você acertou! O número que escolhi foi {}.'.format(tentativa))
        print('Você acertou em {} palpites!'.format(palpites))
        acertou = True
