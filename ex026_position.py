frase = str(input('Digite uma frase:')).lower().strip()
print(f'A letra A aparece {frase.count("a")} vezes.')
#print('A letra A aparece {} vezes'.format(frase.count('a')))
print(f"A primeira letra a aparece na {frase.find ('a')} posição.")
print(f"A última letra a aparece na {frase.rfind ('a')+1} posição.")


