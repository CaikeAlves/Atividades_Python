#Exercício Python 088: Faça um programa que ajude um jogador da MEGASENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo numa lista composta.
from time import sleep # Biblioteca dá tempo para aparecer o print
from random import randint #Biblioteca para da os numeros aleatorios
palpite_de_todos_jogos = list()
palpite_de_jogo = list()
print('-'*40)
print(f'{'PALPITE PARA MEGA SENA':^40}') # O caracter ^ centraliza e o 40 é para centralizar em 40 caracteres e o ":" para juntar a expressao e a formatação
print('-'*40)
quantos_jogos = int(input('Quantos jogos deseja gerar: '))
for i in range(quantos_jogos):
    while len(palpite_de_jogo) <6:
        n = randint(1, 60)
        if n not in palpite_de_jogo:
            palpite_de_jogo.append(n)
    palpite_de_todos_jogos.append(palpite_de_jogo)
    palpite_de_jogo = list()
for jogo in palpite_de_todos_jogos:
    print(sorted(jogo))
    sleep(1)