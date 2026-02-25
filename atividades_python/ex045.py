from random import  choice
m = choice (['Tesoura','Pedra','Papel'])
p = int(input('''Escolha oque voce quer jogar:
[ 1 ] Tesoura
[ 2 ] Pedra
[ 3 ] Papel
'''))
print(f'A maquina escolheu {m}')
if p == 1 and m == 'Tesoura' or p == 2 and m =='Pedra' and p == 2 or m == 'Papel' and p == 3:
    print('\033[33mEMPATE\033[m')
elif p == 1 and m == 'Papel' or p == 2 and m == 'Tesoura' or p == 3 and m == 'Pedra':
    print('\033[32mGANHOU\033[m')
else:
    print('\033[31mPERDEU\033[m')
