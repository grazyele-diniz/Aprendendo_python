import os
os.system('cls')
import math

confirma = 0

while confirma != 1:
    y = float(input(('\nDigite um número inteiro e positivo: ')))
    while y < 0:
        y = float(input('\nO número deve ser inteiro e positivo!\nTente novamente: '))
    i = 0
    dif = 1
    x = [y/2]
    while dif >= 0.1:
        z = x[i] -((x[i]**2)-y)/(2*x[i])
        x.append(z)
        dif = math.fabs(x[i+1] - x[i])
        i += 1

    print('\nA raiz quadrada aproximada pelo método de Newton-Raphson é {:.4f}'.format(x[i]))
    print('\nA raiz quadrada calculada pela função sqrt é {:.4f}'.format(math.sqrt(y)))
    print('\nA diferença entre as raízes calculadas pelos dois métodos é {:.8f}'.format(x[i]-math.sqrt(y)))

    confirma = int(input('\nDigite a opção desejada: \n1 - SAIR ou 2 - REPETIR: '))
    if confirma != 1 and confirma != 2:
        confirma = int(input('\nEscolha uma das opções existentes: \n1 - SAIR ou 2 - REPETIR: '))
print()
print('-'*10, 'Programa encerrado pelo usuário!', '-'*10)