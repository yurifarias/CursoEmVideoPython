# Crie um programa que leia dois
# valores e mostre um menu como o
# ao lado na tela:
# Seu programa deverá realizar a
# operação solicitada em casa caso.
#
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opção = 0

while opção != 5:

    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')

    opção = int(input('Digite sua opção: '))

    if opção == 1:

        print('A soma entre {} e {} é {}.'.format(num1, num2, num1 + num2))

    elif opção == 2:

        print('A multiplicação entre {} e {} é {}.'.format(num1, num2, num1 * num2))

    elif opção == 3:

        print('O maior número entre {} e {} é {}.'.format(num1, num2, max(num1, num2)))

    elif opção == 4:

        num1 = int(input('Digite o novo primeiro número: '))
        num2 = int(input('Digite o novo segundo número: '))

    elif opção == 5:
        print('Finalizando...')

    else:
        int(input('Por favor, digite um número válido: '))
