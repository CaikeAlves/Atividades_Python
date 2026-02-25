dia = int(input('Quantos dias usou o carro? '))
km = float(input('Quantos KM rodou? '))
print(f'Como foi rodado {dia}KM em {km} dias te que se pago R${dia * 60 + km * 0.15:.2f}')