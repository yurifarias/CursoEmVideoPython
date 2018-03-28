r1 = float(input('Digite o comprimento do primeiro segmento de reta: '))
r2 = float(input('Digite o comprimento do segundo segmento de reta: '))
r3 = float(input('Digite o comprimento do terceiro segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os três segmentos de retas formam um triângulo.')
else:
    print('Os três segmentos de retas não formam um triângulo.')
