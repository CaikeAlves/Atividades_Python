#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
opcao = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
while opcao != 5:
    opcao = int(input('qual das opções voce deseja fazer:\n[ 1 ] Somar \n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Números\n[ 5 ] sair do programa\n'))
    if opcao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif opcao == 2:
        soma = n1 * n2
        print(f'{n1} X {n2} = {soma}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O numero maior é {n1}')
        else:
            print(f'O numero maior é {n2}')
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
print('Fim do programa')
