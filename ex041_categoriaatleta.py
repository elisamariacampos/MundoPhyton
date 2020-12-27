from datetime import date
atual = date.today().year
ano = int(input('Qual o ano do seu nascimento?'))
idade = atual - ano
print(f'O atleta tem {idade} anos. Sua categoria é:')
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <=19:
    print('Junior')
elif 19 < idade <= 20:
    print('Senior')
elif idade > 20:
    print('Master')