km = float(input('Qual é a distacias da sua viagem: '))
if km <= 200:
    print(f'A sua viagem deu {km * 0.50 :.2f}')
else:
    print(f'A sua viagem deu {km * 0.45 :.2f}')
