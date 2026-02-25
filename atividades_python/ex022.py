nome = input('Escreva seu nome completo: ').strip()
print('Analisando seu nome...')
print(nome.upper())
print(nome.lower())
nome_sem_espaco = nome.replace(" ", "")
print(f'Seu nome tem {len(nome_sem_espaco)} caracteres.')
primeira_palavra = nome.split()[0]
print(f'Seu primeiro nome é {primeira_palavra}.')
print(f'Seu primeiro nome tem {len(primeira_palavra)}.')
