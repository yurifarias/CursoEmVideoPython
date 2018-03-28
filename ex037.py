# Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número inteiro: '))

print('''Escolha uma base para conversão:
[1] Conversão para binário
[2] Conversão para octal
[3] Conversão para hexadecimal''')

opção = int(input('Digite sua opção: '))

if opção == 1:
    print('{} em binário é {}.'.format(num, bin(num)[2:]))

elif opção == 2:
    print('{} em octal é {}'.format(num, oct(num)[2:]))

elif opção == 3:
    print('{} em hexadecimal é {}'.format(num, hex(num)[2:]))

else:
    print('Digite 1, 2 ou 3 para que seja realizada alguma conversão!')
