#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
p = float(input('Digite o valor da sua compra: R$ '))
e = int(input('''Qual sera a forma de pagamento:
[ 1 ] Dinheiro 
[ 2 ] Cartão 
'''))
if e == 1:
    print(f'O valor da sua compra ficou R${p * 0.90:.2f} pois teve 10% de desconto')
else:
    c = int(input('Em quantas vezes irá fazer no cartão: '))
    if c == 1:
        print(f'O valor da sua compra ficou no total de R${p * 0.95:.2f} pois teve 5% de desconto.')
    elif c == 2:
        print(f'O valor da sua compra ficou no total de R${p:.2f}.')
    elif c > 2:
        print(f'O valor da sua compra ficou no total de {c}X R${p * 1.20 / c:.2f}.')
