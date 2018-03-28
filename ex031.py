quilometragem = float(input('Digite a distância, em km, para onde você está viajando: '))

preço = quilometragem * 0.5 if quilometragem <= 200 else quilometragem * 0.45

print('Sua passagem custará R${:.2f}.'.format(preço))
