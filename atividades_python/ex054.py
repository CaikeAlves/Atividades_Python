#Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    i = int(input('Digite o ano de nascimento: '))
    i = date.today().year - i
    if i >= 18:
        maior += 1
    else:
        menor += 1
print(f'Dessas sete pessoas: são {maior} de maior e {menor} de menor')