somai= 0
cont = 0
for p in range (1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper()).strip()
    somai = somai + idade
    media = somai / 4
    if p == 1:
        maior = idade
        chama = nome
    else:
        if idade > maior and sexo == "M":
            maior = idade
            chama = nome
    if sexo == "F" and idade < 20:
        cont = cont + 1
print(f'\nA média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maior} anos ese chama {chama}.')
print(f'Ao todos são {cont} mulheresc com menos de 20 anos.')