time = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = input('Nome do jogador: ')
    jogador['jogos'] = int(input('Quantas partidas jogadas: '))
    for c in range(0,jogador['jogos']):
        g = int(input(f'Quantos gols no {c+1}º jogo: '))
        gols.append(g)
    jogador['gols'] = gols
    time.append(jogador)
    resposta = input('Deseja cadastrar alguem mais(N/S):').upper()
    if resposta == 'N':
        break
print (time)
