maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Qual o peso da {p}ª pessoa?'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior} KG.')
print(f'O menor peso lido foi de {menor} KG.')


#outraforma
#lista= []
#for c in range (1,6):
#    lista.append(int(input ('Qual o peso da {}ª pessoa? ' .format (c))))
#print ('O maior peso é', max(lista))
#print ('O menor peso é', min(lista))
