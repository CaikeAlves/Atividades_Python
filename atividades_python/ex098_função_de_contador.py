from time import sleep
def underline():
    print('~'*20)

def contador(a,b,c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        for r in range(a,b+1,c):
            print (r, end=' ', flush=True)
            sleep(0.5)
        print('Fim!')
    else:
        for r in range(a,b-1,-c):
            print (r, end=' ', flush=True)
            sleep(0.5)
        print('Fim!')


contador(1,10,1)
underline()
contador(10,0,2)
underline()
print('Agora sua vez:')
underline()
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = abs(int(input('Passos: ')))
if p == 0:
    p = 1
contador(i,f,p)