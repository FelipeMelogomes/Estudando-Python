# Escolher nome aleatório

import random
aleatorio = str(input('Primeiro Aluno: '))
aleatorio2 = str(input('Segundo Aluno: '))
aleatorio3 = str(input('Terceiro Aluno: '))
aleatorio4 = str(input('Quarto Aluno: '))
lista = [ aleatorio, aleatorio2, aleatorio3, aleatorio4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
