#Faça um programa que leia um número qualquer e mostre o seu fatorial. = 0
soma = 1
numero = int(input('Digite um numero: ')) +1
while 1 != numero:
    numero -= 1
    soma = numero * soma
    if numero != 1:
        print(f'{numero}', end=' X ')
    elif numero == 1:
        print(f'{numero}', end=f' = {soma}')
