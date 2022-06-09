import os
os.system('cls')

confirma = 0

while confirma != 1:
    vetor = []
    inverso = []
    i = 0
    print()
    for i in range(12):
        vetor.append(float(input(f'Digite o {i+1}° valor: ')))
    
    inverso = [num for num in reversed(vetor)]
    print('\nOs números digitados na ordem inversa são:', inverso)
    vetor.sort()
    print('\nOs números digitados em ordem crescente sâo:', vetor)

    confirma = int(input('\nDigite a opção desejada: \n1 - SAIR ou 2 - REPETIR: '))
    if confirma != 1 and confirma != 2:
        confirma = int(input('\nEscolha uma das opções existentes: \n1 - SAIR ou 2 - REPETIR: '))
print()
print('-'*10, 'Programa encerrado pelo usuário!', '-'*10)