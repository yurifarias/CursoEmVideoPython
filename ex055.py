# Faça um programa que leia o peso de
# cinco pessoas. No final, mostre qual
# foi o maior e o menor peso lidos.

menor = 0
maior = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa em kg: '))

    if peso > maior:
        maior = peso

    if menor == 0:
        menor = peso

    else:
        if peso < menor:
            menor = peso

print('O maior peso é {:.1f}kg.'.format(maior))
print('O menor peso é {:.1f}kg.'.format(menor))
