dias = float(input('Digite o número de dias de aluguel: '))
kms = float(input('Digite a quantidade de kms rodados: '))

aluguelDias = (60 * dias)
aluguelKms = (0.15 * kms)
aluguel = aluguelDias + aluguelKms

print('O aluguel custou R${:.2f}, sendo R${:.2f} por dias alugados e '
      'R${:.2f} por kms rodados.'.format(aluguel, aluguelDias, aluguelKms))
