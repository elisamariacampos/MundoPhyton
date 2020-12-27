print('---='*20)
print('Analisador de Triângulo')
print('---='*20)
r1 = int(input('Tamanho da reta a:  '))
r2 = int(input('Tamanho da reta b:  '))
r3 = int(input('Tamanho da reta c:  '))
if r1 <  r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses segmentos podem formar triângulo ', end='')
    if r1 == r2 == r3:
        print('equilátero.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('isóceles')
    elif r1 != r2 != r3 != r1:
        print('escaleno.')
else:
    print('Desiste, isso não dá triângulo!')

