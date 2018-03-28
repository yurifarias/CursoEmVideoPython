# Crie um programa que simule o funcionamento
# de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de
# R$50, R$20, R$10 e R$1.

valor = int(input('Digite quanto deseja sacar: '))

cédulas50 = valor // 50

valor %= 50

cédulas20 = valor // 20

valor %= 20

cédulas10 = valor // 10

valor %= 10

cédulas1 = valor

print(f'Você terá {cédulas50} cédulas de R$50,')
print(f'Você terá {cédulas20} cédulas de R$20,')
print(f'Você terá {cédulas10} cédulas de R$10,')
print(f'Você terá {cédulas1} cédulas de R$1.')
