import os
os.system('cls')

def GeradorMatriz(n_lin, n_col):
    return [[0]*n_col for _ in range(n_lin)]

n_linhas = 5
n_colunas = 5
print()

Matriz = GeradorMatriz(n_linhas, n_colunas)

for l in range(n_linhas):
    for c in range(n_colunas):
        Matriz[l][c] = int(input(f'Digite um valor para {[l,c]}: '))

print('\nA matriz digitada é:\n')
for l in range(n_linhas):
    for c in range(n_colunas):
        print(f'{Matriz[l][c]:^5}', end = '')
    print()

i = 0
diagonal_principal = []
triangular_superior = []
triangular_inferior = []
soma_principal = 0

for l in range(n_linhas):
    for c in range(n_colunas):
        if l == c:
            diagonal_principal.append(Matriz[l][c])
            soma_principal = soma_principal + Matriz[l][c]
        if l < c:
            triangular_superior.append(Matriz[l][c])
        if l > c:
            triangular_inferior.append(Matriz[l][c])

maior_superior = max(triangular_superior)
menor_inferior = min(triangular_inferior)
for l in range(n_linhas):
    for c in range(n_colunas):
        if l < c:
            if Matriz[l][c] == maior_superior:
                superior_l = l
                superior_c = c
        if l > c:
            if Matriz[l][c] == menor_inferior:
                inferior_l = l
                inferior_c = c

l = 0
diagonal_secundaria = []
soma_secundaria = 0

for c in range(4, -1, -1):
    diagonal_secundaria.append(Matriz[l][c])
    soma_secundaria += Matriz[l][c]
    l += 1

sub_principal_secundaria = soma_principal - soma_secundaria

print('\nA diferença entre a soma dos elementos da diagonal principal e a soma dos elementos da diagonal secundária é: ', sub_principal_secundaria)
print('\nO maior elemento acima da diagonal principal é ', maior_superior, 'na posição', [superior_l,superior_c])
print('\nO menor elemento abaixo da diagonal principal é ', menor_inferior, 'na posição', [inferior_l,inferior_c])

print
print('='*30, 'Fim do programa', '='*30)