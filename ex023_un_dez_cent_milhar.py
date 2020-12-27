num = int(input('Digite um número:'))
#n = str(num)
#print(f'Analisando o número {(num)}')
#print(f'A unidade é {n[3]}')
#print(f'A dezena é {n[2]}')
#print(f'A centena é {n[1]}')
#print(f'O milhar é {n[0]}')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
n = num // 1000 % 10
print(f'unidade {u}')
print(f'dezena {d}')
print(f'centena {c}')
print(f'milhar {n}')