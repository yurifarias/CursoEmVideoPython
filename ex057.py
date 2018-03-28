# Faça um programa que leia o sexo de uma
# pessoa, mas só aceita os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação
# novamente até ter um valor correto.

sexo = str(input('Digite seu sexo: [M/F] ')).strip()[0]

while sexo not in 'MFmf':

    print('Dados inválidos!')
    sexo = str(input('Por favor, digite seu sexo: [M/F] ')).strip()[0]

print('Dados salvos com sucesso!')
