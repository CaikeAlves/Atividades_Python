# Crie um programa que vai ler vários números e colocar numa lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = []
contador = 0
tem = False
while True:
    numeros.append(int(input('Diga um valor: ')))
    contador += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
numeros.sort(reverse=True)
print('-=' * 30)
print(f'Foi digitado {contador} numeros.')
print(f'A ordem decrescente da lista é : {numeros}')
for numero in numeros:
    if numero == 5:
        tem = True
        break
if tem:
    print('Tem o numero 5 na lista')
else:
    print('Não tem o numero 5 na lista')
