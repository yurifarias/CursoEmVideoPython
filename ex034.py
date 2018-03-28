salário = float(input('Digite o valor do salário: R$'))

if salário <= 1250:
    salário *= 1.15
else:
    salário *= 1.10

print('O salário inicial será aumentado para R${:.2f}'.format(salário))
