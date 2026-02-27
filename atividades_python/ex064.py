#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag).
valor = 0
soma = 0
contador = 0
while 999 != valor:
    valor = int(input('Digite um valor[999 para parar]: '))
    if valor != 999:
        soma += valor
    contador += 1
print(f'São no total de {contador} numeros digitados e a soma entre eles {soma}.')
