a = int(input('Escreva um número inteiro:'))
b = int(input('Agora, escolha outro para comparar:'))
if a > b:
    print('O primeiro valor é maior')
elif a < b:
    print('O segundo valor é maior')
elif a == b:
    print('Não existe valor maior, os dois são iguais')