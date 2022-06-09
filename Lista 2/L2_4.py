import os
os.system('cls')

print('Você deve digitar a idade e o peso de 7 pessoas.')
print()

media = 0
contador = 0
   
for i in range(1,8):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    media = media + idade/7
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    print()
    if peso > 90:
        contador = contador + 1

print('\nA médias das idades é igual a: {:.2f}'.format(media), '\nO número de pessoas com mais de 90 kg é: ', contador)