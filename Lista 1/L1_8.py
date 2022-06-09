import os
os.system('cls')

a = b = c = d = e = f = 0

a = float(input('Digite um valor para a: '))
b = float(input('Digite um valor para b: '))
c = float(input('Digite um valor para c: '))
d = float(input('Digite um valor para d: '))
e = float(input('Digite um valor para e: '))
f = float(input('Digite um valor para f: '))

x = (c*e-b*f)/(a*e-b*d)
y = (a*f-c-d)/(a*e-b*d)

print('O valor de x é igual a: ', x, '\nO valor de y é igual a: ', y)