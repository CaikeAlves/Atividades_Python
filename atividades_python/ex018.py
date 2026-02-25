from math import cos, sin, tan , radians
n = float(input('Digite o angulo: '))
r = radians(n)
print(f'O seno de {n} é  {sin(r):.2f}')
print(f'O cosseno de {n} é {cos(r):.2f}')
print(f'A tangente de {n} é {tan(r):.2f}')