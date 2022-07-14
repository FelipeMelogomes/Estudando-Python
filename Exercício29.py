# Verificador de velocidade permitida de um Veículo

carro = float(input('Qual é a velocidade atual do carro? '))
if carro > 80:
    print('MULTADO! Voçê excedeu o limite permitido que é de 80km/h')
    multa = (carro-80) * 7
    print('Voçê deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um Bom dia! Dirija com segurança!')
