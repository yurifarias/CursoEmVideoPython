# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

valor = float(input('Digite o valor da casa que pretende comprar: R$'))
salário = float(input('Digite o seu salário: R$'))
anos = int(input('Digite por quantos anos você pretende pagar: '))

meses = anos * 12
parcela = valor / meses

if parcela < (0.3 * salário):
    print('Parabéns! \033[1;32mVocê pode financiar\033[m sua nova casa com parcelas'
          ' de R${:.2f} por {} meses.'.format(parcela, meses))
else:
    print('Que pena! \033[1;31mNão será possível financiar\033[m a casa'
          ' pois as prestações (R${:.2f}) equivalem mais que 30% do seu salário.')
