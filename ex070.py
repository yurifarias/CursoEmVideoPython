# Crie um programa que leia o nome e o
# preço de vários produtos. O programa
# deverá perguntar se o usuário vai
# continuar. No final, mostra:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.

gastos = acima1000 = contador = 0
continuar = ' '

while True:
    produto = str(input('Digite o produto: ')).strip()
    preço = float(input('Digite o valor: R$'))

    contador += 1
    gastos += preço

    if contador == 1:
        maisBarato = preço

    if preço < maisBarato:
        maisBarato = preço
        produtoMaisBarato = produto

    if preço > 1000:
        acima1000 += 1

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    if continuar == 'N':
        break

print(f'Você gastou R${gastos} nas compras.')
print(f'{acima1000} produto(s) foi/foram acima de R$1000.')
print(f'O produto mais barato foi: {produtoMaisBarato}.')
