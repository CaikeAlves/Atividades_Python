from datetime import date
a = int(input('Digite o ano de nascimento: '))
a = date.today().year - a
if a == 18:
    print('\033[1mEsta na hora de se alistar!')
elif a >= 19:
    print(f'\033[31mJá passou o prazo de {a - 18} anos para se alistar!')
else:
    print(f'falta {18 - a} anos para se alistar!')
