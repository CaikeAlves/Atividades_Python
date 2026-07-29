jogador = dict()
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['jogos'] = int(input('Quantos jogos ele jogou: '))
for i in range(0,jogador['jogos']):
    print(f'Quantos gol no seu {i+1}º: ')
