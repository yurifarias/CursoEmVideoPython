# Faça um programa que calcule a soma
# entre todos os números ímpares que são
# múltiplos de três e que se encontram no
# intervalo de 1 até 500.

soma = 0
quantidade = 0

for c in range(3, 501, 6):
    soma += c
    quantidade += 1

print('A soma dos {} valores é {}.'.format(quantidade, soma))
