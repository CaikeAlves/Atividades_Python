#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nota = (n1 + n2) / 2
if nota >= 7:
    print('\033[32mAprovado!!!\033[m')
elif nota >= 5:
    print('voce esta em recuperação')
elif nota < 5:
    print('\033[31mReprovado!!!\033[m')