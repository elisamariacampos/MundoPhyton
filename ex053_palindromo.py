frase = str(input('Digite uma frase:')).strip().upper()
#strip elimina espacos antes e depois
palavras = frase.split()
#split divide palavras
junto = ''.join(palavras)
#junto agrega tudo
print(f'Você digitou a frase {junto}')
i = frase[::-1].strip().upper()
inverso = i.split()
ijunto = ''.join(inverso)
print(f'O inverso de {junto} é {ijunto}.')
if ijunto == junto:
    print('Esse é um palíndromo')
else:
    print('Não é um palíndromo.')

#outra forma
frase = str(input('Digite uma frase:')).strip().upper()
#strip elimina espacos antes e depois
palavras = frase.split()
#split divide palavras
junto = ''.join(palavras)
#junto agrega tudo
print(f'Você digitou a frase {junto}')
i = frase[::-1].strip().upper()
