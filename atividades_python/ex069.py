#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

contador = meninas = homens = maiores = 0
while True:
    contador += 1
    print('-=-'*10)
    input(f'Digite o nome da {contador}º pessoa: ')
    sexo = input('Digite o sexo [M/F]: ').upper()
    idade = int(input('Digite a idade: '))
    print('-=-'*10)
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        meninas += 1
    escolha = input('Quer continuar? [S/N] ').upper()
    if escolha == 'N':
        break
print('-=-'*10)
print(f'Você cadastrou {contador} pessoas dessas pessoas cadastradas {maiores} são maiores de 18 anos, foram {homens} homens cadastrados e {meninas} mulheres menores de 20 anos')
print('-=-'*10)
