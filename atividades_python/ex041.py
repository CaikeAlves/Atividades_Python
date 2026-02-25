#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
a = date.today().year
i = int(input('Diga o ano de nascimento: '))
r = a - i
print(f'O atleta tem {r} anos')
if r <= 9:
    print('Mirim')
elif r <= 14:
    print('infantil')
elif r <= 19:
    print('Junior')
elif r <= 25:
    print('Sênior')
else:
    print('Master')