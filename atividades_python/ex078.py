#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
pos_maior = []
pos_menor = []
pos = 0
for c in range(0, 5):
    num = int(input(f'posição {c+1}º Digite um número: '))
    lista.append(num)
maior = max(lista)
menor = min(lista)
for valor in lista:
    pos += 1
    if maior == valor:
        pos_maior.append(pos)
    if menor == valor:
        pos_menor.append(pos)
print(f'Os valores digitados foram {lista}.')
print(f'O maior valor digitado foi {maior} e está na {pos_maior}ª posição.')
print(f'O menor valor digitado foi {menor} e está na {pos_menor}ª posição.')
