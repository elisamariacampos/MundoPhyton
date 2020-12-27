nome = str(input('Digite o seu nome completo:')).strip()
print(f'Seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
f = nome.split()
print(f[0])
g = len(f[0])
print(f"Seu primeiro nome tem {(g)} letras")




