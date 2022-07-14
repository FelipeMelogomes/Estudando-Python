palavra= str(input('Digite uma palavra: ')).strip().upper()
palavra2= ''.join(palavra.split())
palavra3= palavra2[::-1]

if palavra2 == palavra3:
    print('{} é um palindromo'.format(palavra))

else:
    print('{} não é um palindromo'.format(palavra))