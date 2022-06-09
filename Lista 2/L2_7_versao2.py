import os
os.system('cls')
print('\nVocê deverá digitar números inteiros e positivos.')
vetor = []
i = 0
vetor.append(float(input(f'\nDigite o {i+1}º número: ')))
while vetor[0] <= 0:
   vetor[0] = float(input('O número deve ser positivo! Tente novamente: ')) 

i = i + 1
while i >= 0:
    vetor.append(float(input(f'\nDigite o {i+1}° número: ')))
    while vetor[i] <= 0:
        vetor[i] = float(input('O número deve ser positivo! Tente novamente: '))
    if vetor[i] > 2*vetor[i-1]:
        break
    else:
        i = i + 1

print('\nOs números digitados foram:\n', vetor)
print('-'*25, 'Fim!', '-'*25)