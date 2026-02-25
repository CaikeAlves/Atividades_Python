#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = ''
while sexo != 'M' or sexo != 'F':
    sexo = input('Digite seu sexo: [M/F] ').upper()
print('Seu sexo registrado com sucesso!')