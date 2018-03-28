# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida.
# - Média abaixo de 5.0: REPROVADO;
# - Média entre 5.0 e 6.9: RECUPERAÇÃO;
# - Média 7.0 ou superior: APROVADO.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2

if média >= 7:
    print('Parabéns! Sua média é {:.1f} e você foi APROVADO!'.format(média))

elif média < 5:
    print('Que pena! Sua média é {:.1f} e você foi REPROVADO!'.format(média))

else:
    print('RECUPERAÇÃO! Sua média é {:.1f} e você deve fazer uma recuperação.'.format(média))
