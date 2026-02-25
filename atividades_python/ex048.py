#Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(3, 501, 3):
        if c % 2 != 0:
            s = s + c
            cont = cont + 1
print(f'O valor somado é {s} e são {cont} numeros.')
