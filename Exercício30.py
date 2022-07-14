# Verifica se um número é ímpar ou par

número = int(input('Digite um número? '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR '.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))