#Crie um programa que declare uma matriz de dimensão 3×3 e
# preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
contador = 0
linha = 0
for m in range(0, 9):
    n = int(input(f'Digite o valor para [{linha}, {contador}]: '))
    contador += 1
    matriz[linha].append(n)
    if contador == 3:
        contador = 0
        linha += 1
print(f'{matriz[0][0]} {matriz[0][1]} {matriz[0][2]}')
print(f'{matriz[1][0]} {matriz[1][1]} {matriz[1][2]}')
print(f'{matriz[2][0]} {matriz[2][1]} {matriz[2][2]}')