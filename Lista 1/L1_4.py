import os
os.system('cls')

idade_dias = int(input('\nDigite sua idade em dias: '))
resto = idade_dias%365
anos = (idade_dias - resto)/365
dias = resto%30
meses = (resto - dias)/30

print('\nSua idade é:\n', anos, 'anos\n', meses, 'meses\n',dias, 'dias\n')
