from time import sleep
print('=' * 30)
print('{:^30}'.format('BANCO LP'))
print('=' * 30)
valor = int(input('Informe o valor para sacar? R$'))
tempo1 = print('SISTEMA INICIALIZANDO...')
tempo = print('CARREGANDO SISTEMA..')
aguarde = print('POR FAVOR. AGUARDE.')
sleep(2)
total = valor
céd = 50
totalcéd = 0
while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO LP ! Tenha um bom dia! ')