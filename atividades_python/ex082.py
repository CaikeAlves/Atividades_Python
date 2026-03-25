#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
numeros = []
impares = []
pares = []
while True:
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
print(f'Os numeros digitados foram: {numeros}.\nOs numeros pares foram: {pares}. \nOs numeros impares foram: {impares}.')
