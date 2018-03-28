nome = str(input('Digite seu nome completo: ')).strip()

separados = nome.split()

print('Seu nome em maiúsculas: {}.'.format(nome.upper()))
print('Seu nome em minúsculas: {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))
