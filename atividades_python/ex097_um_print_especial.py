def escreva(frase):
    underline = len(frase)+4
    print ('~'*underline)
    print (f'{frase:^{underline}}')
    print ('~'*underline)


escreva('Python')
escreva('Casa Bahia')