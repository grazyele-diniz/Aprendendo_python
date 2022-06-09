import os
os.system('cls')

def adicao(x):
    print("\nVocê escolheu a tabuada de ADIÇÃO do ", x, ":")
    print('-'*55)
    for i in range(1,11):
        print(x, " + ", i, " = ", x+i)
        
def subtracao(x):
    print("\nVocê escolheu a tabuada de SUBTRAÇÃO do ", x, ":")
    print('-'*55)
    for i in range(1,11):   
        print(x+i, " - ", x, " = ", i)
       
def multiplicacao(x):
    print("\nVocê escolheu a tabuada de MULTIPLICAÇÃO do ", x, ":")
    print('-'*55)
    for i in range(1,11):   
        print(x, " x ", i, " = ", x*i)

def divisao(x):
    print("\nVocê escolheu a tabuada de DIVISÃO do ", x, ":")
    print('-'*55)
    for i in range(1,11):
        print(x/i, " / ", x, " = ", i)

print('\nEsse programa calcula a tabuada de um número.' + '\nEscolha o número correspondente a operação desejada:' + '\n1-adição, 2-subtração, 3-multiplicação ou 4-divisão\n')
operacao = int(input('A operação desejada é: '))
if operacao < 1 or operacao > 4:
    print("\nEscolha uma das opções existentes!")
    operacao = int(input("\n1-adição, 2-subtração, 3-multiplicação ou 4-divisão"))

tabuada = {1:adicao, 2:subtracao, 3:multiplicacao, 4:divisao}

x = int(input("\nEscolha um número de 1 a 10 para calcular a tabuada: "))

if x < 1 or x > 10:
    print("\nO número deve estar entre 1 e 10!")
    x = int(input("\nTente novamente: "))


tabuada.get(operacao)(x)
print('-'*55)