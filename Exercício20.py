# Lista dos alunos digitados no programa

import random
a = str(input('Primeiro Aluno: '))
a1 = str(input('Segundo Aluno: '))
a2 = str(input('Terceiro Aluno: '))
a3 = str(input('Quarto Aluno: '))
lista = [a, a1, a2, a3]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)