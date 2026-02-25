v = int(input('Velocidade media atual do seu carro: '))
m = (v - 80) * 7
if v < 80:
    print('Tenha um bom dia. Dirija com segurança!')
else:
    print(f'Voce foi multado, tera que pagar uma multa no valor de {m} R$.')
