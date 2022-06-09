import os
os.system('cls')

confirma = 0

while confirma != 1:
    vetor = []
    i = 0
    print()
    for i in range(10):
        vetor.append(float(input(f'Digite o {i+1}° valor: ')))

    maximo = max(vetor)
    minimo = min(vetor)

    print('\nO maior elemento do vetor é', [maximo], f'na [{(vetor.index(maximo)+1)}]° posição.')
    print('\nO menor elemento do vetor é', [minimo], f'na [{(vetor.index(minimo)+1)}]° posição.')

    confirma = int(input('\nDigite a opção desejada: \n1 - SAIR ou 2 - REPETIR: '))
    if confirma != 1 and confirma != 2:
        confirma = int(input('\nEscolha uma das opções existentes: \n1 - SAIR ou 2 - REPETIR: '))
print()
print('-'*10, 'Programa encerrado pelo usuário!', '-'*10)