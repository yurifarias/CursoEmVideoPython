# Escreva um programa que leia um número n inteiro qualquer e
# mostre na tela os n primeiros elementos de uma Sequência de
# Fibonacci.
# Ex:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

fibonacci = [0, 1]

n = int(input('Digite quantos números você quer mostrar da Sequência de Fibonacci: '))
t1 = 0
t2 = 1
c = 1

while c <= n:
    if c <= 0:
        print('Digite um número positivo e maior que 0!')

    elif c == 1:
        print('O {:2}o termo é {}'.format(c, t1))

    elif c == 2:
        print('O {:2}o termo é {}'.format(c, t2))

    else:
        t3 = t1 + t2
        print('O {:2}o termo é {}'.format(c, t3))
        t1 = t2
        t2 = t3

    c += 1

print('FIM')
