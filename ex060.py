# Faça um programa que leia um número
# qualquer e mostre o seu fatorial.
#
# Ex:
# 5! = 5 * 4 * 3 * 2 * 1 = 120

fatorial = 1
num = int(input('Digite um número para se calcular o seu fatorial: '))
while num > 0:
    fatorial *= num
    num -= 1

print(fatorial)
