#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
d = 0
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        d = n + d
print(f'A soma do numeros pares digitados foi {d}')