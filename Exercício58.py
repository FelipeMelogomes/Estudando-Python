from random import randint
computador = randint(0, 20)
print('Olá sou seu computador...  Acabei de pensar em um número entre 0 e 20.')
print('Será que voçê consegue adivinhar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... Tente mais uma vez.')
        elif jogador > computador:
            print('MENOS... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns !')
