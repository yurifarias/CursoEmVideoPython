from math import cos, sin, tan, radians

ângulo = float(input('Digite um ângulo em graus: '))

print('Seu cosseno vale {:.2f}.'.format(cos(radians(ângulo))))
print('Seu seno vale {:.2f}.'.format(sin(radians(ângulo))))
print('Sua tangente vale {:.2f}.'.format(tan(radians(ângulo))))
