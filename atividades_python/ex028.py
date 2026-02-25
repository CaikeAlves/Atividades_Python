from random import randint
from time import sleep
p = randint(1, 5)
print('-=-' * 20)
print('Pensei em um numero inteiro de 0 a 5')
print('-=-' * 20)
n = int(input('Irei pensar em um numero de um a 5, tente adivinhar: '))
print('PROCESSANDO...')
sleep(3)
if n == p:
    print('Parabens vc acertou')
else:
    print(f'Voce errou, eu pensei em {p}')