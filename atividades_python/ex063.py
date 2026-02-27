# Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma Sequência de Fibonacci.
a = 0
b = 1
print('-=-'*10)
print('SEQUENCIA DE FIBONACCI')
print('-=-'*10)
n = int(input('Quantos termos da Sequência de Fibonacci?: '))
print('~'*30)
while n > 0:
    n -= 1
    if n != 0:
        print(f'{a}',  end = ' → ')
    elif n == 0:
        print(f'{a} → FIM')
    c = a + b
    a = b
    b = c
print('~'*30)
