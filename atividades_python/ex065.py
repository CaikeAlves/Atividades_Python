# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
maior = soma = menor= contador = escolha = 0
while escolha != 'N':
    valor = int(input('Digite um valor: '))
    escolha = input('Quer continuar? [S/N] ').upper()
    if 0 == menor:
        menor = valor
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    soma += valor
    contador += 1
media = soma / contador
print(f'O menor numero digitado foi {menor} e o maior foi {maior} e a media é {media} e Foi no total de {contador} numeros digitados.')