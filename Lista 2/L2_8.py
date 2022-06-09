import os
os.system('cls')

print('Você deverá digitar 10 números inteiros.')
print()

num = []
contador = 0
   
for i in range(10):
    num.append(int(input(f'Digite o {[i+1]}ª número: ')))
    if num[i] % 2 == 0:
        contador = contador + 1

print('\nA quantidade de números positivos é: ', contador)
num.sort()
print('\nO menor número é:', num[0], '\nO maior número é: ', num[9])
print('-'*28, 'Fim!', '-'*28)