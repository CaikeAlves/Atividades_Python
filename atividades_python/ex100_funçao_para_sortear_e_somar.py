#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
# mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
def sortear():
    sorteado = list()
    for s in range(0,5):
        sort = randint(1,10)
        sorteado.append(sort)
        print(f'{sort}', end=' ', flush= True)
        sleep(0.5)
    print('Fim!')
    return sorteado

def somarpar(lista):
    soma = 0
    for s in lista:
        if s%2 == 0:
            soma += s
    print(soma)
sorteado = sortear()
somarpar(sorteado)
