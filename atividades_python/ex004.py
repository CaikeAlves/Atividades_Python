a=input('Digite algo:')
print(type(a))

if a.isnumeric():
    print('É número')
else:
    print('Não é número')

if a.isalpha():
     print('Só é composto por letras')
else:
     print('Não está composto só com letras')

if a.isupper():
    print('Esta todo com letras Maiusculas')
else:
    print('Não está todo letras maiusculas')

if a.isalnum():
    print('É um alfanumerico')
else:
    print('Não é um alfanumerico')

if a.islower():
    print('Esta tudo com letras minusculas')
else:
    print('Não esta tudo com letras minusculas')