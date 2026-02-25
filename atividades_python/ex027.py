n = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer!')
p = n.split()[0]
u = n.split()[-1]
print(f'Seu primeiro nome é {p}.')
print(f'Seu ultimo nome é {u}.')