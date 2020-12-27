soma = 0
cont = 0
for n in range (1,501,2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
        #pode ser soma+= n tambem
        #print(n, end=' ')
print(f'A soma de todos os {cont} valores é {soma}')


