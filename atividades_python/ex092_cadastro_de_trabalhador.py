from datetime import date
trabalhador = dict()
trabalhador['nome'] = input('Digite é seu nome: ')
nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - nascimento
clt = int(input('Carteira de trabalho '))
if clt == 0:
    trabalhador['carteira de trabalho (0 se nao tiver)'] = 'não tem'
else:
    trabalhador['carteira de trabalho'] = clt
    trabalhador['ano de contratação'] = int(input('Seu ano de contratação: '))
    trabalhador['salário'] = int(input('Salario: R$'))
    trabalhador['aposentadoria'] = ((trabalhador['ano de contratação'] - date.today().year) + 35) + trabalhador['idade']
    trabalhador['ano da aposentadoria'] = trabalhador['aposentadoria'] + nascimento
for k,v in trabalhador.items():
    print(f'{k}: {v}')
