import random
print('Coloque os alunos a baixo para fazer o uma ordem aleatoria entre eles:')
a1 = input('Primeiro alunos: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print(f'O sorteio ficou a seguinte ord em {alunos}.')