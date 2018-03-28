número = int(input('Digite um número de 1 a 9999: '))

uni = número // 1 % 10
dez = número // 10 % 10
cen = número // 100 % 10
mil = número // 1000 % 10

print('Unidades: {}'.format(uni))
print('Dezenas: {}'.format(dez))
print('Centenas: {}'.format(cen))
print('Milhares: {}'.format(mil))
