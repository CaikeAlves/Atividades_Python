#Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um numero: '))
print('Qual será a base de conversão')
print('Digite [ 1 ] Binário')
print('Digite [ 2 ] Octal')
print('Digite [ 3 ] Hexadecimal')
s = int(input('Digite sua opcao: '))
if s == 1:
    r = bin(n)
    print(f'Convertido para Binário fica: {r[2:]}')
elif s == 2:
    r = oct(n)
    print(f'Convertido para Octal fica: {r[2:]}')
elif s == 3:
    r = hex(n)
    print(f'Convertido para Hexadecimal fica: {r[2:]}')
else:
    print('Digite uma opcao valida!')