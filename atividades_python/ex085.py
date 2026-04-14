#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.
numeros = list()
pares = list()
impares = list()
for c in range(1, 8):
    n = int(input(f'Digite o {c}º numero: '))
    numeros.append(n)
print(f'Os numeros digitados foram {numeros}')
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'Os numeros pares digitados foram {pares}')
print(f'Os numeros impares digitados foram {impares}')