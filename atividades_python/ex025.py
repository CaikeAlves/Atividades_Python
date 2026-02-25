n = input('Digite seu nome completo: ').lower()
r = n.find('silva')
if r == -1:
    print('Não tem Silva no seu nome')
else:
    print('Seu nome tem Silva')