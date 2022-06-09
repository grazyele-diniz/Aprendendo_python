import os
os.system('cls')

a = [1,0,5,-2,-5,7]
print('\nO vetor inicial é:\n')
for i in range (len(a)):
    print('a[{}] = '.format(i), a[i])

soma = a[0] + a[1] + a[5]
print('\nA soma de a[{}] + a[{}] + a[{}] = '.format(0,1,5), soma)

a[3] = 100

print('\nO vetor final é:\n')
for i in range (len(a)):
    print('a[{}] = '.format(i), a[i])
print('-'*10, 'Fim!', '-'*10)