# Desenvolva um programa que leia o nome, idade e
# sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos.

médiaIdade = 0
maiorIdade = 0
nomeMaiorIdade = ''
menorVinte = 0
tudoCerto = True

for c in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Sexo: M/F: ')).strip()

    médiaIdade += idade

    if sexo in 'Mm':

        if idade > maiorIdade:
            maiorIdade = idade
            nomeMaiorIdade = nome

    elif sexo in 'Ff':

        if idade < 20:

            menorVinte += 1

    else:

        tudoCerto = False

if tudoCerto:
    print('A média de idade do grupo vale {:.1f}.'.format(médiaIdade / 4))
    print('O homem mais velho é {} e ele tem {} anos de idade.'.format(nomeMaiorIdade, maiorIdade))
    print('Temos {} mulheres com menos de 20 anos.'.format(menorVinte))

else:
    print('Você digitou o sexo de alguma pessoa errado!')
