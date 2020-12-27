viagem = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar sua viagem!')
if viagem <= 200:
    valor = viagem * 0.50
else:
    valor = viagem * 0.45
print(f'E o preçø da sua passagem será de R${valor :.2f}.')


