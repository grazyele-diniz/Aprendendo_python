import os
os.system('cls')

confirma = 0

while confirma != 1:
    a = int(input(('\nDigite um número inteiro e positivo: ')))
    while a < 0:
        a = int(input('\nO número deve ser inteiro e positivo!\nTente novamente: '))

    lista = list(range(1, a+1, 1))
    pares = []
    
    for i in range(len(lista)-1):
        if lista[i] % 2 == 0:
            pares.append(lista[i])

    print(f'\nOs números inteiros pares existentes entre 1 e {a} são: ', pares)
    
    confirma = int(input('\nDigite a opção desejada: \n1 - SAIR ou 2 - REPETIR: '))
    if confirma != 1 and confirma != 2:
        confirma = int(input('\nEscolha uma das opções existentes: \n1 - SAIR ou 2 - REPETIR: '))
print()
print('-'*10, 'Programa encerrado pelo usuário!', '-'*10)