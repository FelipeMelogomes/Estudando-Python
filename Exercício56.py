somaidade = 0
médiaidade = 0
maioridadehomen = 0
homenvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('------ {} PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        homenvelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        homenvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

médiaidade = somaidade / 4
print('A média idade do grupo é de {} anos.'.format(médiaidade))
print('O homen mais velho tem {} Anos e se chama {}.'.format(maioridadehomen, homenvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))

