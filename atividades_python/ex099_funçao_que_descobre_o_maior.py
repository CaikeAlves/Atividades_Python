def maior(*a):
    if not a:
        print ('Não foram informado nenhum valor.')
    else:
        tam = len(a)
        maior = max(a)
        print (f'{a} Foram informados {tam} ao todo')
        print (f'O maior valor iformado foi {maior}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()