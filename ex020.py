from random import shuffle

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

lista = [nome1, nome2, nome3, nome4]

shuffle(lista)

print('A ordem de apresentação será {}, {}, {} e {}.'.format(lista[0], lista[1], lista[2], lista[3]))
