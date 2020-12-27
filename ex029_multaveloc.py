velocidade = float (input ('Qual a velocidade atual do carro?'))
if velocidade > 80:
    print ('MULTADO! Reduza a velocidade e dirija com segurança!')
    multa = (velocidade - 80) * 7
    print (f'Você deve pagar uma multa de {multa :.2f}')
print('Tenha um bom dia e dirija com segurança!')
