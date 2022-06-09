import os
os.system('cls')

print('Você deverá digitar sua idade completa em anos, meses e dias:')
anos = int(input('\nDigite quantos anos: '))
meses = int(input('\nDigite quantos meses: '))
dias = int(input('\nDigite quantos dias: '))
idade_dias = anos*365 + meses*30 + dias
print('\nSua idade em dias é: ', idade_dias, ' dias')
