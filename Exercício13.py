# Calcular desconto (segundo programa)

salario = float(input('Digite o preço?R$'))
preçoavista = salario + (salario * 15 / 100)
preçoapraso = salario - (salario * 15 / 100)
print('O produto a praso custa R${:.2f}, á vista custa R${:.2f} com 15% de desconto'.format(salario,preçoapraso,preçoavista))