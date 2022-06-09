import os
os.system('cls')

print('\nEscolha uma das opções:\n 1 - Ordem crescente\n 2 - Ordem decrescente\n 3 - Maior no meio')
i = int(input('\nSua opção é: '))
while i < 1 or i > 3:
    print('\nEscolha uma das opções existentes!')
    print('\n 1 - Ordem crescente\n 2 - Ordem decrescente\n 3 - Maior no meio')
    i = int(input('\nSua opção é: '))

a = float(input('\nDigite o valor de a: '))
b = float(input('\nDigite o valor de b: '))
c = float(input('\nDigite o valor de c: '))

num = [a, b, c]

if i == 1:
    num.sort()
    print('\nEm ordem crescente: ', num)
elif i == 2:
    num.sort(reverse=True)
    print('\nEm ordem decrescente: ', num)
else:
    num.sort()
    print('\nO maior número no meio: ', [num[0], num[2], num[1]])
print()
print('-'*28, 'Fim!', '-'*28)