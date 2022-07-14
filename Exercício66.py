soma = cont =  0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break   # Tira a flag da soma de valores.
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}')