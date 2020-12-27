from datetime import date
atual = date.today().year
ano = int (input('Qual o ano do seu nascimento?'))
idade: int = (atual - ano)
print(f"Quem nasceu em {ano} tem {idade} anos em {atual}.")
if idade > 18:
    print ('Você já passou do tempo do alistamento')
    print (f'Você está atrasado em {(idade - 18)} anos para o seu alistamento.')
elif idade == 18:
    print ('Esse é o seu ano de alistamento')
elif idade < 18:
    print ('Espere até os 18 anos para se alistar.')
    print (f"Faltam {(18 - idade)} anos para o seu alistamento.")
