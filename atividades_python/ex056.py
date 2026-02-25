#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
maior = 0
media = 0
novas = 0
for c in range(1, 5):
    n = input(f'Nome da {c}º pessoa: ')
    i = int(input(f'Idade {c}º pessoa: '))
    s = int(input(f'Digite o sexo:\n[ 1 ] - Masculino\n[ 2 ] - Feminino\n '))
    media += i
    if i > maior and s == 1:
        maior = i
        velho = n
    if i < 20 and s == 2:
        novas += 1
media = (media/4)
print(f'A media de idade do grupo é {round(media)},o  homem mais velho é o {velho} com {maior} anos. e tem {novas} mulheres com menos de 20 anos.')
