import os
os.system('cls')

print('\nEsse programa calcula a tabuada de um número.' + '\nEscolha o número correspondente a operação desejada:' + '\n1-adição, 2-subtração, 3-multiplicação ou 4-divisão\n')
operacao = int(input('A operação desejada é: '))
if operacao < 1 or operacao > 4:
    print("\nEscolha uma das opções existentes!")
    operacao = int(input("\n1-adição, 2-subtração, 3-multiplicação ou 4-divisão"))
   
x = int(input("\nEscolha um número de 1 a 10 para calcular a tabuada: "))

if x < 1 or x > 10:
    print("\nO número deve estar entre 1 e 10!")
    x = int(input("\nTente novamente: "))

i = 1
#caso 1 - adição
if operacao == 1:
    print("\nVocê escolheu a tabuada de ADIÇÃO do ", x, ":")
    print('-'*55)
    for i in range(10+1):
        print(x, " + ", i, " = ", x+i)
    
        
#caso 2 - subtração
if operacao == 2:
    print("\nVocê escolheu a tabuada de SUBTRAÇÃO do ", x, ":")
    print('-'*50)
    for i in range(10+1):   
        print(x+i, " - ", x, " = ", i)
       
#caso 3 - multiplicação
if operacao == 3:
    print("\nVocê escolheu a tabuada de MULTIPLICAÇÃO do ", x, ":")
    print('-'*55)
    for i in range(10+1):   
        print(x, " x ", i, " = ", x*i)

#caso 4 - divisão
if operacao == 4:
    print("\nVocê escolheu a tabuada de DIVISÃO do ", x, ":")
    print('-'*55)
    for i in range(10+1):
        print(x/i, " / ", x, " = ", i)

print('-'*55)