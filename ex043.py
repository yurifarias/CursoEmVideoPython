# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso;
# Entre 18.5 e 25: Peso ideal;
# Entre 25 e 30: Sobrepeso;
# Entre 30 e 40: Obesidade;
# Acima de 40: Obesidade mórbida.

peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em m: '))

imc = peso / (altura ** 2)

print('O IMC desta pessoa é {:.1f}.'.format(imc))

if imc < 18.5:
    print('Este IMC indica que a pessoa está abaixo do peso.')

elif imc < 25:
    print('Este IMC indica que a pessoa está com o peso ideal.')

elif imc < 30:
    print('Este IMC indica que a pessoa está com sobrepeso.')

elif imc < 40:
    print('Este IMC indica que a pessoa está com obesidade.')

else:
    print('Este IMC indica que a pessoa está com obesidade mórbida.')
