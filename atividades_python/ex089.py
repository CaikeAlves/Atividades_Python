#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa
# lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.
boletim = list()
aluno = list()
while True:
    aluno.append(input('Nome: '))
    aluno.append(int(input('Primeira nota: ')))
    aluno.append(int(input('Segunda nota: ')))
    escolha = input('Deseja adicionar mais um? (N/S)').upper().strip()
    boletim.append(aluno)
    aluno = list()
    if escolha == 'S':
        pass
    else:
        break
for posicao,al in enumerate(boletim):
    print(f'Id: {posicao + 1} Aluno: {al[0]} Nota final: {(al[1] + al[2]) / 2}')
while True:
    escolha = int(input('Deseja consulta a nota de algum aluno  digite o id do aluno caso não queira digite 999.'))
    if escolha == 999:
        print(f'Ate à proxima')
        break
    else:
        print(boletim[escolha - 1])





