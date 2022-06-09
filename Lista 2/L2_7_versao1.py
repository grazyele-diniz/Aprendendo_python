import os
os.system('cls')

vet = []

i = 0
for i in range(999):
    vet.append(int(input('Digite um valor: ')))
    while vet[i]<0:
        vet.append(int(input('Digite um valor : ')))
    if vet[i]>2*vet[i-1]:
        break
print(vet)
print('-'*28, 'Fim!', '-'*28)

