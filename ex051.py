# Desenvolva um programa que leia o
# primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros
# termos dessa progressão.

a0 = int(input('Digite um número inteiro: '))
r = int(input('Digite a razão da progressão: '))

for c in range(0, 11):
    print(a0 + r * c, end=' -> ')

print('Acabou!')
