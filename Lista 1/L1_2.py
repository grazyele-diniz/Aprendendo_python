import os
os.system('cls')
import math

a = int(input('\nDigite um primeiro número positivo: '))
while a < 0:
    a = int(input('\nO número deve ser positivo! Tente novamente: '))
b = int(input('\nDigite um segundo número positivo: '))
while b < 0:
    b = int(input('\nO número deve ser positivo! Tente novamente: '))
c = int(input('\nDigite um terceiro número positivo: '))
while c < 0:
    c = int(input('\nO número deve ser positivo! Tente novamente: '))
r = math.pow(a+b,2)
s = math.pow(b+c,2)
d = (r+s)/2
print('\nO valor da expressão é igual a: ', d)