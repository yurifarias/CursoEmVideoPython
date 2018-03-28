real = float(input('Digite o valor em real para convertê-lo: R$'))

dolar = real / 3.27

print('Com R${:.2f} você pode comprar U${:.2f}.'.format(real, dolar))
