#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que
# tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if a > b and a > c:
    r = b + c > a
elif b > a and b > c:
    r = a + c > b
else:
    r = a + b > c
if r:
    print('\033[32mEsses segmentos podem fazer um triangulo\033[m')
    if a == b == c:
        print('Esse triangulo é EQUILÁTERO')
    elif a == b or b == c or c == a:
        print('Esse triangulo é ISÓSCELES')
    else:
        print('Esse triangulo é ESCALENO')
else:
    print('\033[31mEsses segmentos não podem fazer um triangulo\033[m')