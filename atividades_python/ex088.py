#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from selectors import SelectSelector
from time import sleep
from random import randint
jogo = list()
palpites = list()
print('-'*40)
print('{:^40}'.format('PALPITE PARA MEGA SENA'))
print('-'*40)
quantos_jogos = int(input('Quantos jogos deseja gerar: '))
for game in range(jogos):
    for valor in range(6):
        p = randint(1, 60)
        for numero in palpites:
            if p != numero:
                palpites.append(palpite)
            else:
    palpites.append(palpite)
    palpite = list()
print('-='*40)

for palpite in palpites:
    print(sorted(palpite))
