n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite o terceiro número:'))
#achando o menor valor
menor= n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print (f"O menor valor digitado foi {menor}")

#achando o maior valor
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print (f"O maior valor digitado foi {maior}")

