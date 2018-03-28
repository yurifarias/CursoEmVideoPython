# Crie um programa que leia vários números inteiros pelo teclado. No
# final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

resposta = 'S'
soma = 0
menor = 0
maior = 0
contagem = 1

while resposta == 'S':
    num = int(input('Digite um número: '))

    if contagem == 1:
        menor = num
        maior = num

    else:
        if num > maior:
            maior = num

        elif num < menor:
            menor = num

    soma += num

    resposta = str(input('Você deseja continuar [S/N]: ')).strip().upper()

    if resposta == 'S':
        contagem += 1

print('Você digitou {} números e a média foi {:.2f}.'.format(contagem, soma / contagem))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))
