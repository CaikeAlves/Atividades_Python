# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = []
while True:
    numero = (int(input('Digite um valor: ')))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    elif numero in numeros:
        print('Valor duplicado na lista, ele não será adicionado. ')
    escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
print(f'Os valores digitados foram {sorted(numeros)}.')
