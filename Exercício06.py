# Escreva o dobro, o triplo e a raiz quadrada de um valor

n = int(input('Digite um número:  '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O Dobro de {} vale {}'.format(n, d ))
print('O Triplo de {} vale {}'.format(n, t ))
print('A raiz quadrada de {} vale {:.2f}'.format(n, r))