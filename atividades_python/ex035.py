a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if a > b and a > c:
    r = b + c > a
elif b > a and b > c:
    r = a + c > b
else:
    r = a + b > c
if r == True:
    print('\033[32mEsses segmentos podem fazer um triangulo\033[m')
else:
    print('\033[31mEsses segmentos não podem fazer um triangulo\033[m')