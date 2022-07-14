# Pega valor inteiro de qualquer número

from math import trunc
num = float(input('Digite um Número? '))
print(' O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))