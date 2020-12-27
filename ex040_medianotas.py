a = float(input('Qual a sua nota em matematica?'))
b = float(input('Qual a sua nota em portugues?'))
media = (a + b) / 2
print(f"A sua média é {media :.1f}.")
if media < 5.0:
    print('Você está reprovado.')
elif 5.0 < media < 6.9:
    print('Você está em recuperação')
elif media >= 7.0:
    print('Parabéns, aprovado!')
