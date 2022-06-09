import os
os.system('cls')

n1 = float(input('\nDigite a nota 1: '))
n2 = float(input('\nDigite a nota 2: '))
n3 = float(input('\nDigite a nota 3: '))

media = (n1 + n2 + n3)/3

if media >= 9:
    print('\nConceito A')
elif media < 9 and media >= 7.5:
    print('\nConceito B')
elif media < 7.5 and media >= 6:
    print('\nConceito C')
elif media < 6 and media >= 4:
    print('\nConceito D')
elif media < 4:
    print('\nConceito E')

