print('='*30)
print('10 termos de uma PA')
print('='*30)
primeiro = int(input('Qual o primeiro termo da sua PA?'))
razao = int(input('Qual o valor da razao?'))
decimo = primeiro +(10 - 1) * razao
#formula matematica do enesimo termo de uma PA
for n in range (primeiro,decimo + razao, razao):
    print(n, end='-')
print('Acabou')

