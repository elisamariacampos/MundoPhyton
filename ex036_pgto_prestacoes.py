print('Oi, vamos estudar o seu pedido de empréstimo?')
casa = float (input('Escreva o valor da casa que você quer comprar? R$'))
salario = float (input('Qual o valor mensal do seu salário? R$'))
anos = int (input('Em quantos anos você quer pagar?'))
tempopgto = anos * 12
teto = salario * (30 / 100)
print (f"Seu teto mensal é de {teto}")
prestacao = casa / tempopgto
if prestacao > teto:
    print ('Sinto muito, seu empréstimo não pode ser aprovado')
else:
    print ('Parabéns, você pode solicitar um empréstimo!')
