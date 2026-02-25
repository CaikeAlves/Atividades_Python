# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao: '))
f = 0
print(f'{p}', end=' → ')
for c in range(1,10 ):
    f = r + f
    print(f'{p + f}', end =' → ')
print('Acabou')