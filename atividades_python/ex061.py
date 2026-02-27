#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
contador = 0
pa = int(input('Digite o primeiro termo da PA: '))
termo = int(input('Digite a razao: '))
while contador != 10:
    contador += 1
    print(f'{pa}', end=' → ')
    pa = pa+termo
print('FIM')