from math import hypot, pow, sqrt

catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))

'''# Por expressão algébrica
hipotenusa = sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2))'''

# Por método hypot()
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
