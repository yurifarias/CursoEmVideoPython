from random import choice

primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno: ')

listaAlunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]

escolhido = choice(listaAlunos)

print('O aluno escolhido foi: {}.'.format(escolhido))
