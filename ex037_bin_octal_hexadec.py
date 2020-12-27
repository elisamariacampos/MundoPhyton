num = int (input('Escreva um número qualquer:'))
print('Você quer converter para (1) binario,(2) octal e(3))hexadecimal?')
opcao = int(input("Sua opção:"))
if opcao == 1:
    print(f"{num} convertido para binario é igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para pctal é igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para hexadecimal é igual a {hex(num)[2:]}")
else:
    print('Opção inválida. Tente novamente.')