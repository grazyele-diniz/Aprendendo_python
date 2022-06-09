import os
os.system('cls')
import math

confirma = 0

while confirma != 1:
    vet = []
    i = 0
    med = 0
    var = 0
    print()
    for i in range(10):
        vet.append(float(input(f'Digite o {i+1}° valor: ')))
        med = med + vet[i]/10
    for i in range(10):
        var = var + (1/9)*(vet[i] - med)**2
    dp = math.sqrt(var)

    print('\nO desvio padrão é igual a {:.3f}'.format(dp))

    confirma = int(input('\nDigite a opção desejada: \n1 - SAIR ou 2 - REPETIR: '))
    if confirma != 1 and confirma != 2:
        confirma = int(input('\nEscolha uma das opções existentes: \n1 - SAIR ou 2 - REPETIR: '))
print()
print('-'*10, 'Programa encerrado pelo usuário!', '-'*10)