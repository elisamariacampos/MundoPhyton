print('Oi, vamos calcular o valor final do seu produto?')
preco = float(input(f'Digite o preço do produto:'))
print('''Você pode escolher entre as seguintes opções de pagamento:
[1]Dinheiro/cheque
[2]À vista no cartão.
[3]No cartão em até 2x.
[4]No cartão em 3x ou mais.''')
forma = int(input('Qual a sua forma de pagamento?'))
if forma == 1:
    print(f"Você precisa pagar o valor de R$ {preco - ((10 / 100) * preco) :.2f}.")
elif forma == 2:
    cartao = preco - ((5 / 100) * preco)
    print(f"Você precisa pagar o valor de R$ {cartao :.2f}.")
elif forma  == 3:
    parc2 = preco / 2
    print(f"Você precisa pagar o valor de R$ {parc2f :.2} por mês.")
elif forma == 4:
    parc3 = preco + ((20 / 100) * preco)
    totaparc = int(input('Quantas parcelas?'))
    parcela = parc3 / totaparc
    print(f"Sua compra de R${preco} vai sair por {totaparc} parcelas de R${parcela :.2f} com juros.")
    print(f'O valor vai passar de R${preco} para {totaparc * parcela} no final.')
else:
    print('Opção inválida de pagamento. Tente novamente.')

