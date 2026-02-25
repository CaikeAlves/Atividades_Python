#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessários para vencer.
from random import randint
print('Vou pensar em um numero entre 1 e 10')
jogador = int(input('Em que numero eu pensei? '))
maquina = randint(1, 10)
if maquina > jogador:
    print('Meu numero maior')
elif maquina < jogador:
    print('Meu numero menor')
while maquina != jogador:
    jogador = int(input('tente novamente: '))
    if maquina > jogador:
        print('Meu numero maior')
    elif maquina < jogador:
        print('Meu numero menor')
print('\033[32mVoce acertou')