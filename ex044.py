# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto;
# - À vista no cartão: 5% de desconto;
# - Em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros.

preço = float(input('Digite o valor das suas compras: R$'))

print('Formas de pagamento.')
print('[ 1 ] - À vista no dinheiro/cheque.')
print('[ 2 ] - À vista no cartão.')
print('[ 3 ] - 2x no cartão.')
print('[ 4 ] - 3x ou mais no cartão.')

dígito = int(input('Digite sua opção: '))

if dígito == 1:
    preço *= 0.9
    print('Você terá 10% de desconto e sua compra sairá por R${:.2f}.'.format(preço))

elif dígito == 2:
    preço *= 0.95
    print('Você terá 5% de desconto e sua compra sairá por R${:.2f}.'.format(preço))

elif dígito == 3:
    print('Sua compra sairá por R${:.2f}, com parcelas '
          'de R${:.2f}.'.format(preço, preço / 2))

elif dígito == 4:
    parcelas = int(input('Digite o número de parcelas: '))

    if parcelas >= 3:
        preço *= 1.2
        print('Você terá 20% de juros e sua compra sairá por R${:.2f} '
              'em parcelas de R${:.2f}.'.format(preço, preço / parcelas))

    else:
        print('Você digitou um número inválido de parcelas.')

else:
    print('Você não digitou uma opção válida!')
