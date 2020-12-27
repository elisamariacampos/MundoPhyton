peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura em metros?'))
IMC = peso / (altura ** 2)
print(f'Seu IMC é {IMC :.1f}.')
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 < IMC <= 25:
    print('Você está no peso ideal!')
elif 25 < IMC <= 30:
    print('Está com um certo sobrepeso.')
elif 30 < IMC <= 40:
    print('Atenção! Você está obeso e precisa se cuidar!')
elif IMC > 40:
    print('Obesidade mórbiad. Procure um médico com urgência.')