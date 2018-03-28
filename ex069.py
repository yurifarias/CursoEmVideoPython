# Crie um programa que leia a idade e o
# sexo de várias pessoas. A cada
# pessoa cadastrada, o programa
# deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
# A) Quantas pessoas tem
#    mais de 18 anos.
# B) Quantos homens foram
#    cadastrados.
# C) Quantas mulheres tem
#    menos de 20 anos.

maiores18 = homens = mMenos20 = 0

while True:
    idade = 0
    sexo = ' '
    continuar = ' '

    while idade < 1:
        idade = int(input('Digite a idade: '))

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]

    if idade > 18:
        maiores18 += 1

    if sexo == 'M':
        homens += 1

    else:
        if idade < 20:
            mMenos20 += 1

    while continuar != 'N':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    if continuar == 'N':
        break

print(f'{maiores18} é/são maior(es) de idade.')
print(f'{homens} homem(ns) foram cadastrados.')
print(f'{mMenos20} mulher(es) tem menos de 20 anos.')
