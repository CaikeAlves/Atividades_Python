s = float(input('Digite o seu salario: '))
if s <= 1250:
    s = s * 1.15
else:
    s = s * 1.10
print(f'com o aumento seu salario novo é de \033[1mR${s:.2f}\033[m')