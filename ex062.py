# Melhore o DESAFIO 61, perguntando
# para o usuário se ele quer mostrar
# mais alguns termos. O programa
# encerra quando ele disser que quer
# mostrar 0 termos.

termo1 = int(input('Digite o valor do primeiro termo: '))
razão = int(input('Digite a razão da progressão aritimética: '))
repetições = 10
termo = termo1

t = 1

while t != 0:

    if t <= repetições:
        print('O {:2}o termo vale {:2}'.format(t, termo))

        termo = termo1 + t * razão
        t += 1

    else:
        novas = int(input('Digite quantas mais repetições você quer: '))

        if novas == 0:
            t = 0

        else:
            repetições += novas

print('Você finalizou a PA com {} termos'.format(repetições))
