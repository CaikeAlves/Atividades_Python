import random
print('Iremos fazer um sorteio entre os alunos para isso preciso que coloque o nome dos alunos a baixo:')
a1 = input('primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = a1, a2, a3, a4
print(f'O escolhido foi {random.choice(alunos)}.')