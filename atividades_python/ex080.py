# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
for c in range(0, 5):
    digitado =(int(input('Digite um valor: ')))
    colocado = False
    for numero in numeros:
        if numero >= digitado:
            numeros.insert(numeros.index(numero), digitado)
            colocado = True
            print(f'Seu numero foi adicionado na  posição {numeros.index(numero)} lista...')
            break
    if not colocado:
        numeros.append(digitado)
        print('O valor digitado foi adicionado no final da lista...')
print(numeros)


#numeros = [3,7,9]
#digitado = 5
#for pos, valor in enumerate(numeros):
#    if valor >= digitado:
#        numeros.insert(pos, digitado)
#        break
#print(numeros
