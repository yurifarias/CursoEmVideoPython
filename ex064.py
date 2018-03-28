# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que
# é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

repetições = 0
número = 0
soma = 0
número = int(input('Digite um número [999 para parar]: '))

while número != 999:
    repetições += 1
    soma += número
    número = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma é igual a {}'.format(repetições, soma))
