#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
print('Digite uma frase qualquer quer irei dizer se é um palindromo')
f = input('Digite uma frase: ')
f = f.replace(' ','').lower()
f_i = f [::-1]
print(f)
print(f_i)
if f == f_i:
    print('É um palindromo')
else:
    print('Não é um palindromo')
