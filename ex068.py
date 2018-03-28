# Faça um programa que jogue par ou ímpar com o computador. O jogo
# só será interrompido quando o jogador PERDER, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

jogos = 0

while True:
    jogador = -1
    escolha = ' '

    while 0 <= jogador <= 10:
        jogador = int(input('Digite um número: '))

    while escolha not in 'PI':
        escolha = str(input('Escolha par ou ímpar [P/I]: ')).upper().strip()[0]

    computador = randint(1, 10)

    if (jogador + computador) % 2 == 0:
        soma = 'P'
        resultado = 'par'

    else:
        soma = 'I'
        resultado = 'ímpar'

    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print(f'A soma deu {num + computador} e o resultado foi {resultado}.')

    if escolha == soma:
        print('Você venceu!')
        print('Vamos jogar novamente...')
        jogos += 1

    else:
        print('Você perdeu!')
        print('GAME OVER!')
        break

print(f'Você venceu {jogos} vez(es) até perder!')
