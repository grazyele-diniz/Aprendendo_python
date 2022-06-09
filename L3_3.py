import os
os.system('cls')

confirma = 0

while confirma != 1:
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    soma = 0
    print()
    for l in range(0,3):
        for c in range(0,3):
            matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
            if l == c:
                soma = soma + matriz[l][c]

    print('\nA matriz digitada é:\n')
    for l in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[l][c]:^5}]', end = '')
        print()
        
    print('\nA soma dos elementos da diagonal principal é igual a:', soma)

    confirma = int(input('\nDigite a opção desejada: \n1 - SAIR ou 2 - REPETIR: '))
    if confirma != 1 and confirma != 2:
        confirma = int(input('\nEscolha uma das opções existentes: \n1 - SAIR ou 2 - REPETIR: '))
print()
print('-'*10, 'Programa encerrado pelo usuário!', '-'*10)


