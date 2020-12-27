km = int(input('Qual a quantidade de km percorridos?'))
dias = int(input('Por quantos dias você alugou o carro?'))
pago = (dias * 60) + (km * 0.15)
print(f'O total do seu aluguel tem valor de R${pago :.2f}.')


