#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
print('-=-'*20)
print('NACIONAL')
soma = caro = 0
pbarato = 999999999
while True:
    print('-=-'*20)
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    print('-=-'*20)
    soma += preco
    if preco > 1000:
        caro += 1
    if pbarato > preco:
        pbarato = preco
        barato = produto
    escolha = input('Pressione para continuar: [N/S]').upper()
    if  escolha == 'N':
        break
print(f'O valor total das compras foi R${soma:.2f} sendo que {caro} produtos custam mais de R$1000 e o produto mais barato foi {barato}')
