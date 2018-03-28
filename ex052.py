# Faça um programa que leia um
# número inteiro e diga se ele é
# ou não um número primo.

num = int(input('Digite um número inteiro: '))
repetições = 0

for c in range(1, num + 1):
    if num % c == 0:
        repetições += 1
        print('\033[31m{} '.format(c), end='')

    else:
        print('\033[33m{} '.format(c), end='')

print('\n\033[mO número foi dividido {} vezes.'.format(repetições))

if repetições == 2:
    print('O número é primo!')

else:
    print('O número não é primo!')
