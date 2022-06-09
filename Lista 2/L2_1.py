import os
os.system('cls')

g1 = float(input('\nDigite o índice de poluição do 1° Grupo: '))
g2 = float(input('\nDigite o índice de poluição do 2° Grupo: '))
g3 = float(input('\nDigite o índice de poluição do 3° Grupo: '))

if g1 >= 0.3:
    print('\nAs empresas do 1° Grupo devem suspender as atividades.')
else:
    print('\nTudo certo com as empresas do 1° Grupo.')
if g2 >= 0.4:
    print('\nAs empresas do 2° Grupo devem suspender as atividades.')
else:
    print('\nTudo certo com as empresas do 2° Grupo.')
if g3 >= 0.5:
    print('\nAs empresas do 3° Grupo devem suspender as atividades\n.')
else:
    print('\nTudo certo com as empresas do 3° Grupo\n.')
