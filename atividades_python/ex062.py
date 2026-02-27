#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
contador = 0
pedido = 10
pa = int(input('Digite o primeiro termo da PA: '))
termo = int(input('Digite a razao: '))
while contador < pedido:
    contador += 1
    if contador < pedido:
        print(f'{pa}', end=' → ')
    elif contador == pedido:
        print(f'{pa}.',)
    pa = pa+termo
    if contador == pedido:
        mais = int(input('\nQuantos termos a mais quer mostrar a mais: '))
        pedido += mais
print(f'Foi um total de {contador} termos.')