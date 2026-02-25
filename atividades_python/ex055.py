#Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 999
for c in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O menor peso é de {menor}Kg e o maior peso é de {maior}Kg.')