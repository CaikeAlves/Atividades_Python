time = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = input('Nome do jogador: ')
    jogador['jogos'] = int(input('Quantas partidas jogadas: '))
    for c in range(0,jogador['jogos']):
        g = int(input(f'Quantos gols no {c+1}º jogo: '))
        gols.append(g)
    jogador['gols'] = gols [:]
    jogador['total'] = sum(gols)
    gols = list()
    time.append(jogador.copy())
    jogador = dict()
    resposta = input('Deseja cadastrar alguem mais(N/S):').upper()
    if resposta == 'N':
        break
print (f'{"Cod":<5}{"Nome":<10}{"Gols":<15}{"total":<5}')
print ('=='*20)
for n,atleta in enumerate(time):
    print(f'{n:<5}{atleta["nome"]:<10}{str(atleta["gols"]):<15}{atleta["total"]:<5}')
while True:
    resposta = int(input(f'Deseja ver o levantamento de um jogador? digite o cod dele, caso queira sair digite (999)'))
    if resposta == 999:
        break
    else:
        for n,atleta in enumerate(time):
            if n == resposta:
                print(f'No levantamento do jogador {atleta["nome"]}')
                for p,gol in enumerate(atleta['gols']):
                    print(f'No jogo {p+1}º fez {gol}')