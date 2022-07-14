soma = 0
cont = 0
for contador1 in range(1, 501, 2):
    if contador1 % 3 == 0:
        cont += 1
        soma += contador1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
