num = int(input('Digite um número para teste:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;33m', end='')
        tot +=1
    else:
        print('\033[1;34m', end='')
    print(f'{c}', end=' ')

print(f'\nO número {c} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')

#OUTRA RESOLUCAO:
#frase = input("Qual a frase? ").upper().replace(" ", "")
#if frase == frase[::-1]:
    #print("A frase é um palíndromo")
#else:
    #print("A frase não é um palíndromo")
