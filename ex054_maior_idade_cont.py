from datetime import date
cont = 0
men = 0
for c in range (1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    maior = date.today().year - ano
    if maior >= 21:
        cont = cont +1
    else:
        men = men + 1
print(f'\nAo todo tivemos {cont} pessoas maiores de idade.')
print(f'E também tivemos {men} pessoas menores de idade.')