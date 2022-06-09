import os
os.system('cls')

confirma = 0

while confirma != 1:
    cartao = input(f'Digite o número completo do cartão: ')
    digitos = list(map(int,cartao))

    while len(digitos) != 16:
        cartao = input(f'Número incorreto! Tente novamente: ')
        digitos = (map(int,cartao))

    if digitos[0] != 3 and digitos[0] != 4 and digitos[0] != 5 and digitos[0] != 6:
        print('\nNúmero inválido!')
    else:
        if digitos[0] == 4:
            print('\nVISA')
        elif digitos[0] == 5 and (digitos[1] >= 1 or digitos[1] <= 5):
            print('\nMASTERCARD')
        elif digitos[0] == 3 and (digitos[1] == 4 or digitos[1] == 7):
            print('\nAMERICAN EXPRESS')
        elif (digitos[0] == 5 and (digitos[1] == 0 or digitos[1] >= 6)) or (digitos[0] == 6 and digitos[1] <= 9):
            print('\nMAESTRO')
        else:
            print('\nOUTRA BANDEIRA')
    #CÁLCULO DO DÍGITO VERIFICADOR
    soma_impares = 0
    i = 0
    for i in range(0,15,2):
        dobro = 2*digitos[i]
        if dobro > 9:
            dobro_str = str(dobro)
            lista_dobro = list(map(int,dobro_str))
            d = sum(lista_dobro)
            soma_impares = soma_impares + d
        else:
            soma_impares = soma_impares + dobro

    soma_pares = 0
    for j in range(1,14,2):
        soma_pares = soma_pares + digitos[j]
    
    soma = str(soma_impares + soma_pares)
    lista_soma = list(map(int,soma))
    tam = len(lista_soma)
    verificador = 10 - lista_soma[tam-1]

    if digitos[15] == verificador:
        print('\nCARTÃO VÁLIDO')
    else:
        print('\nCARTÃO INVÁLIDO')
    print('='*55)

    confirma = int(input('\nDigite a opção desejada: \n1 - SAIR ou 2 - REPETIR: '))
    if confirma != 1 and confirma != 2:
        confirma = int(input('\nEscolha uma das opções existentes: \n1 - SAIR ou 2 - REPETIR: '))
print()
print('='*10, 'Programa encerrado pelo usuário!', '='*10)