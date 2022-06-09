import os
os.system('cls')
import math

x1 = float(input('\nDigite a abscissa do ponto 1: '))
y1 = float(input('\nDigite a ordenada do ponto 1: '))
x2 = float(input('\nDigite a abscissa do ponto 2: '))
y2 = float(input('\nDigite a ordenada do ponto 2: '))
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print('\nA distância entre os dois pontos é igual a: ', d)