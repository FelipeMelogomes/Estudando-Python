# Calcula os Km e preço de passagem. baseado na sua distãncia de viagem

viagem = float(input('Qual é a distância da sua viagem? '))
print('Voçê está prester a começar uma viagem de {}Km.'.format(viagem))
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))