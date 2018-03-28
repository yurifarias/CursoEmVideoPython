comprimento = float(input('Digite o comprimento da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = comprimento * altura
litros = area / 2

print('A quantidade de tinta necessária para pintar {:.2f}m² ({:.2f} x {:.2f})'
      ' de parede é de {:.2f}l.'.format(area, comprimento, altura, litros))
