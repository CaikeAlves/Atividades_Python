#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
c = 0
from random import randint
while True:
    print('-=-'*10)
    n = int(input('Digite um numero: '))
    print('-=-'*10)
    e = input('Faça sua escolha: \n[ 1 ] Par \n[ 2 ] Impar\n')
    m = randint(0, 10)
    n += m
    if n % 2 == 0:
        v = '1'
    else:
        v = '2'
    print(f'A maquina escolheu {m} e deu {'Par' if v == '1' else 'Impar'}')
    if e != v:
        break
    c += 1
print(f'Voce venceu {c} vezes')
