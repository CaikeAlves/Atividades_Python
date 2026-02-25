#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
s = 0
n = int(input('Digite um numero: '))
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[32m{c}', end=' ')
        s += 1
    else:
        print(f'\033[31m{c}', end=' ')

if s == 2:
    print('\nO seu numero é primo')
else:
    print('\nO seu numero não é primo')
