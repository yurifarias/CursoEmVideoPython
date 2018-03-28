# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNascimento = int(input('Digite o ano que você nasceu: '))

anoHoje = date.today().year
idade = anoHoje - anoNascimento

if idade > 18:
    print('Você tem {} anos e seu tempo para alistamento já passou.'.format(idade))
    print('Você deveria ter se alistado há {} atrás.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(anoNascimento + 18))

elif idade < 18:
    print('Você tem {} anos e ainda não precisa se alistar.'.format(idade))
    print('Você só precisa se alistar em {} anos.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(anoNascimento + 18))

else:
    print('Você tem 18 anos e precisa se alistar agora!')
