# Crie um programa que leia
# uma frase qualquer e diga
# se ela é um palíndromo,
# desconsiderando os
# espaços.
#
# Ex:
# APÓS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
palavrasJuntas = ''.join(palavras)
fraseAoContrário = palavrasJuntas[::-1]

if fraseAoContrário == palavrasJuntas:
    print('É um palíndromo!')

else:
    print('Não é um palíndromo!')
