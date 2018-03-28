velocidade = float(input('Você está dirigindo com que velocidade? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Multado! Você excedeu o limite de velocidade que é 80km/h.')
    print('Sua multa custará R${:.2f}!'.format(multa))
print('Tenha um bom dia. Dirija com cuidado.')
