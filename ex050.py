# Desenvolva um programa que leia seis
# números inteiros e mostre a soma
# apenas daqueles que forem pares. Se
# o valor digitado for ímpar,
# desconsidere-o.

soma = 0

for c in range(0, 6):
    num = int(input('Digite um número: '))

    if (num % 2) == 0:
        soma += num

print('A soma de todos os números pares é {}.'.format(soma))
