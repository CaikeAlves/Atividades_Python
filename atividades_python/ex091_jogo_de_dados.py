from random import randint
from time import sleep
from operator import itemgetter
lugar = 0
partidas = dict()
print('Valores Sortiados')
for c in range(1,5):
    partidas['jogador' + str(c)] = randint(1,6)
    print(f'O {'jogador' + str(c)} tirou {partidas["jogador" + str(c)]} no dado')
    sleep(1)
rank = sorted(partidas.items(),key = itemgetter(1), reverse=True) #crio uma lista e falo pra organizar de acordo com o segundo elemento e dps dalo que organize aocontrario
print('='*20)
print('Classificação')
print('='*20)
for k,v in rank:
    lugar += 1
    sleep(2)
    print(f'{lugar}º lugar: {k} com {v}')
