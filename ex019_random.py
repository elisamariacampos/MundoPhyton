import random
a1 = str(input('Digite o nome do aluno 1:'))
a2 = str(input('Digite o nome do aluno 2:'))
a3 = str(input('Digite o nome do aluno 3:'))
al = [a1, a2, a3]
print(f'O sorteado para o ir ao quadro foi {random.choice(al)}')

