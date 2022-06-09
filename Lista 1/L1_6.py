import os
os.system('cls')

total_seg = int(input('\nDigite o tempo total em segundos: '))

resto = total_seg%3600
horas = (total_seg - resto)/3600
seg = resto%60
min = (resto - seg)/60

print('O tempo de duração foi de:\n', horas, 'horas\n', min, 'minutos\n', seg, 'segundos\n')