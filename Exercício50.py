soma = 0
cont = 0
for contador in range(1, 7):
    num = int(input('Digite o {} valor: '.format(contador)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voçê informou {} números PARES e a soma foi {}'.format(cont, soma))