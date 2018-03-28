# Crie um programa que leia o ano de
# nascimento de sete pessoas. No
# final, mostre quantas pessoas
# ainda não atingiram a maioridade e
# quantas jão são maiores.

from datetime import datetime

maiores = 0
menores = 0

for c in range(1, 8):
    ano = int(input('Digite o ano em que a {}ª pessoa nasceu: '.format(c)))

    if datetime.today().year - ano < 18:
        menores += 1

    else:
        maiores += 1

print('Existem {} pessoas maiores de idade.'.format(maiores))
print('Existem {} pessoas menores de idade.'.format(menores))
