#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = ('zero','um', 'Dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero de 0 à 20: '))
    if 0 <= numero <= 20:
        print(extenso[numero])
        print('=' * 10)
    else:
        numero = int(input('tente novamente, digite um numero de 0 à 20: '))
    escolha = input('Quer ver outro número? [N/S] ').strip().upper()[0]
    print('=' * 10)
    if escolha in 'N':
        break
