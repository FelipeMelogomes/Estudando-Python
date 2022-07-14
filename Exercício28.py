# Jogo de adivinhar o número que a 'Máquina pensou'

from random import randint
from time import sleep
computador = randint(0, 20) #Faz o computador "pensar".
print('-=-' * 20 )
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20 )
jogador = int(input('Em que número voçê pensou? ')) #Jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Voçê conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}!'.format(computador, jogador))


