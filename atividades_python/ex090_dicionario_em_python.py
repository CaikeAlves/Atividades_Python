# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.
nome = input('Digite seu nome: ')
media = float(input('Digite a sua nota: '))
aluno = {'nome': nome,'media': media }
if aluno['media'] >= 7:
    aluno['situação'] = 'Passou'
elif aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovou'
for k,v in aluno.items():
    print(f'{k} é = {v}')
