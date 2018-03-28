from math import floor, trunc

número = float(input('Digite um número decimal: '))

'''# Convertendo para int
print('A porção inteira do número {} é {}'.format(número, int(número)))'''

# Usando math.floor()
print('A porção inteira do número {} é {}'.format(número, floor(número)))

'''# Usando math.trunc()
print('A porção inteira do número {} é {}'.format(número, trunc(número)))'''
