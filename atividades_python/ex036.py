s = float(input('Qual é seu salário: '))
c = float(input('Valor da casa: '))
a = int(input('Em quantos anos pretende pagar: '))
p = 12 * a
v = c / p
r = s * 0.30
if v >= r:
    print(f'\033[31mVoce não poderar comprar a casa pois o valor da parcela ficou de {v:.2f} em X{p}.')
else:
    print(f'\033[32mVoce poderar comprar a casa a parcela ficou de {v:.2f} em X{p}.')
