# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
# fechados na ordem correta.
expressao = input('Digite uma expressão:' )
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simbolo)
            break
if len(pilha) > 0:
    print('\033[31mA expressão está errada')
else:
    print('\033[32mA expressão está correta')
