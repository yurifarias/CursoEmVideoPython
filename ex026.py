frase = str(input('Escreva uma frase: ')).strip().lower()

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('a')))
print('Ela aparece pela primeira vez na posição {}.'.format(frase.find('a') + 1))
print('Ela aparece pela última vez na posição {}.'.format(frase.rfind('a') + 1))
