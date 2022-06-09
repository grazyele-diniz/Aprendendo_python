import os
os.system('cls')

print('\nVocê deverá escolher dois númeiros inteiros e positivos:')

a = int(input('\nDigite o primeiro número: '))
while a < 0:
    a = int(input('\nO número deve ser inteiro e positivo!\n Tente novamente:  '))
    
b = int(input('\nDigite o segundo número: '))
while b < 0:
    b = int(input('\nO número deve ser inteiro e positivo!\n Tente novamente:  '))
   
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
   
resto = maior % menor
mdc = menor
   
while resto > 0:
    maior = menor
    menor = resto
    resto = maior % menor
    mdc = menor
   
print('\nO MDC entre ', [a,b], ' é: ', mdc)
print('-'*28, 'Fim!', '-'*28)