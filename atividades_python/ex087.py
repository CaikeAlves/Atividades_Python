# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[], [], []]
numeros_pares = []
coluna = pares = linha = soma_terceia_coluna =  0

for m in range(0, 9):
    n = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
    coluna += 1
    matriz[linha].append(n)
    if n % 2 == 0:
        pares += n
        numeros_pares.append(n)
    if coluna == 3:
        soma_terceia_coluna += n
    if coluna == 3:
        coluna = 0
        linha += 1
for linha in matriz:
    print(linha)

print(f'Os numeros pares digitados foram: {numeros_pares} e a somas deles é {pares}')
print(f'A soma da terceira coluna foi {soma_terceia_coluna}')
print(f'O maior valor da segunda linha foi {max(matriz[1])}')
