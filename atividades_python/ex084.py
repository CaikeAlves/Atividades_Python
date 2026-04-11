#Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = list()
pessoa = list()
quantidade = 0
peso = 0
pena = 999
pesada = list ()
leve = list()
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    continuar = input('Deseja continuar? [S/N] ').upper().strip()
    quantidade += 1
    if continuar == 'N':
        break
for p in pessoas:
    if p[1] > peso:
        pesada.clear()
        peso = p[1]
        pesada.append(p[0])
    elif p[1] == peso:
        pesada.append(p[0])
for p in pessoas:
    if p[1] < pena:
        leve.clear()
        pena = p[1]
        leve.append(p[0])
    elif p[1] == pena:
        leve.append(p[0])
print(f'Foram cadastradas {quantidade} pessoas.')
print(f'a pessoa mais pesada é {pesada} com {peso}Kg.')
print(f'A pessoa mais leve é {leve} com {pena}Kg.')
