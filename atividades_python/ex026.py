frase = input('Digite uma frase: ').lower()
a = frase.count('a')
frase = frase.replace(" ","")
print(f'Na sua frase aparece {a} vezes a letra "A"')
ar = frase.rfind('a') + 1
al = frase.find('a') + 1
print(f'A letra "A" aparece à primera vez na posição {al}º.')
print(f'A letra "A" a ultima vez a aparece e na posição {ar}º.')