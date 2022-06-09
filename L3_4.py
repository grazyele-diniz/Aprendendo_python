import os
os.system('cls')

confirma = 0

while confirma != 1:
    matriz = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    soma_col_impar = 0
    soma_col_2_4 = 0
    contador = 0
    print()
    for l in range(0,3):
        for c in range(0,6):
            matriz[l][c] = float(input(f'Digite um valor para [{l+1}, {c+1}]: '))
            if c%2 == 0: # a coluna par em python corresponde às colunas ímpares matematicamente
                soma_col_impar = soma_col_impar + matriz[l][c]
            if c == 1 or c == 3:
                soma_col_2_4 = soma_col_2_4 + matriz[l][c]
                contador = contador + 1

    print('\nA matriz digitada foi:\n')
    for l in range(0,3):
        for c in range(0,6):
            print(f'[{matriz[l][c]:^5}]', end = '')
        print()

    print('\nA soma dos elementos das colunas ímpares é igual a:', soma_col_impar)
    print('\nA média dos elementos da segunda e quarta colunas é igual a:', soma_col_2_4/contador)

    print('\nOs elementos da sexta coluna receberão a soma dos elementos das colunas 1 e 2:')
    for l in range(0,3):
            matriz[l][5] = matriz[l][0] + matriz[l][1]

    print('\nA matriz modificada é:\n')
    for l in range(0,3):
        for c in range(0,6):
            print(f'[{matriz[l][c]:^5}]', end = '')
        print()

    confirma = int(input('\nDigite a opção desejada: \n1 - SAIR ou 2 - REPETIR: '))
    if confirma != 1 and confirma != 2:
        confirma = int(input('\nEscolha uma das opções existentes: \n1 - SAIR ou 2 - REPETIR: '))
print()
print('-'*10, 'Programa encerrado pelo usuário!', '-'*10)