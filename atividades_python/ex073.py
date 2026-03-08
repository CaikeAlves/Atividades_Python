# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
time = ('Palmeiras', 'São Paulo', 'Corinthians', 'Bahia', 'Fluminense', 'Athletico-PR', 'Bragantino', 'Grêmio', 'Chapecoense', 'Mirassol', 'Flamengo', 'Coritiba', 'Santos', 'Botafogo', 'EC Vitória', 'Remo', 'Atlético-MG', 'Internacional', 'Cruzeiro', 'Vasco da gama')
print('=' * 40)
print('Os cinco primeiros colocados são:' ', '.join(time[0:5]))
print('=' * 40)
print('Os últimos quadros  colocados' ', '.join(time[-4:]))
print('=' * 40)
print('Os times em ordem alfabética:', sorted(time))
print('=' * 40)
print(f'{time.index('Chapecoense')}º posição da Chapecoense')
print('=' * 40)
