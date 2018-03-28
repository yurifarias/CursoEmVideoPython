# A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de
# acordo com a idade:
# - Até 9 anos: MIRIM;
# - Até 14 anos: INFANTIL;
# - Até 19 anos: JUNIOR;
# - Até 25 anos: SÊNIOR;
# - Acima: MASTER.

from datetime import date

anoNascimento = int(input('Digite o seu ano de nascimento: '))
anoHoje = date.today().year
idade = anoHoje - anoNascimento

print('Você tem {} anos.'.format(idade))

if idade <= 9:
    print('Sua categoria é: MIRIM.')

elif idade <= 14:
    print('Sua categoria é: INFANTIL.')

elif idade <= 19:
    print('Sua categoria é: JUNIOR.')

elif idade <= 25:
    print('Sua categoria é: SÊNIOR.')

else:
    print('Sua categoria é: MASTER.')
