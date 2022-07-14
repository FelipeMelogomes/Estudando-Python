print('Gerador de PA')
print('->' *20)
pa1 = int(input('Primeira PA: '))
razão = int(input('Razão da PA: '))
termo = pa1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voçê quer mostrar a mais? '))
print('FIM')
print('Progressão finalizada com {} termos mostrados.'.format(total))