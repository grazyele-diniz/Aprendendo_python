import os
os.system('cls')

custo_fab = float(input('\nO custo de fábrica do veículo é: '))
taxa_dist = 0.28
imposto = 0.45
custo_consum = (1 + taxa_dist + imposto)*custo_fab

print('\nO custo do veículo ao consumidor é igual a: {:.2f}'.format(custo_consum) , ' reais')