from time import sleep
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('PROGRAMA CARREGANDO.....')
    print('Aguarde alguns segundos')
    sleep(2)
    if n < 0:
        break
    print('<->' * 30)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('<->' * 30)
print('PROGRAMA TABUADA ENCERRADO.')