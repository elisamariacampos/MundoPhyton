from random import randint
itens = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)
print('''Qual a sua jogada?
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador = int(input('Sua opção:'))
if jogador > 2:
    print('Opção Inválida. Jogue novamente.')
print('_=' * 25)
print(f"O computador escolheu {itens[computador]} e você escolheu {itens[jogador]}.")
print('_=' * 25)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador ==2:
        print('Computador vence')
    else:
        print('Jogada Inválida')
elif computador == 1:
    if jogador  == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador ==2:
        print('Jogador vence')
    else:
        print('Jogada Inválida')
elif computador == 2:
    if jogador  == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador ==2:
        print('Empate')
    else:
        print('Jogada Inválida')

