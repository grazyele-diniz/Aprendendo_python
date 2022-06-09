import os
os.system('cls')

i = 0
vetor = []

for i in range(5):
    vetor.append(float(input('\nDigite um valor positivo: ')))
    while vetor[i] < 0:
        vetor[i] = float(input('\nO valor deve ser positivo! Tente novamente: '))

vetor.sort()

print('\nO menor valor é: ', vetor[0], '\nO maior valor é: ',vetor[4])