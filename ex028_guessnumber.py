from random import randint
from time import sleep
computador = randint(0, 10)
print('Eu vou pensar em um número. Duvido você adivinhar!')
game = int(input('Em que número estou pensando?'))
print ("Processando...")
sleep(2)
if game == 2:
    print('Parabéns, você acertou!')
else:
    print('Que pena! Tente de novo!')