jogador = dict()
gols = list()
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['jogos'] = int(input('Quantos jogos ele jogou: '))
for i in range(0,jogador['jogos']):
    gol = int(input(f'Quantos gol no seu {i+1}º jogo: '))
    gols.append(gol)
jogador['gols'] = gols
jogador['total'] = sum(jogador['gols'])
print (20*'-=-')
print (jogador)
print (20*'-=-')
for k,v in jogador.items():
    print (f'O campo {k} tem o valor {v} ')
print (20*'-=-')
print (f'O jogador {jogador["nome"]} jogou {jogador["jogos"]} partidas')
for i,pt in enumerate(jogador['gols'],start=1):
    print(f'Na partida {i}, fez {pt} gols')
print(f'foi um total de {jogador["total"]} gols')
