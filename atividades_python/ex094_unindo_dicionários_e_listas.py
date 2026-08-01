povo = list()
pessoa = dict()
media = 0
mulheres = list()
velhos = list()
while True:
    pessoa['nome'] = (input('Digite o nome: '))
    while True:
        sexo = input('Digite seu sexo(M/F): ').upper().strip()
        if sexo in 'MF':
            break
        else:
            print ('Digite somente M ou F.')
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Digite a idade: '))
    povo.append(pessoa)
    pessoa = dict()
    while True:
        resposta = input('Quer cadastra mais alguem(S/N)? ').upper().strip()
        if resposta in 'SN':
            break
        else:
            print ('Digite somente S ou N')
    if resposta == 'N':
        break
for i in povo:
    if i['sexo'] == 'F':
        mulheres.append(i['nome'])
    media += i['idade'] 
media = media / len(povo)
for i in povo:
    if media < i['idade']:
        velhos.append(i)
print(f'Foram no total de {len(povo)} pessoas cadastradas')
print(f'A media de idade é {media:.2f} anos.')
print(f'As mulheres cadastradas foram {mulheres}')
print(f'Lista das pessoas que estão acima da média:')
for p in velhos:
    print(f"nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']} ")
