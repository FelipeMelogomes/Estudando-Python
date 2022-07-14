# Verifica quem é o maior valor digitado e o menor

p = int(input('Primeiro Valor: '))
s = int(input('Segundo Valor: '))
t = int(input('Terceiro valor: '))
# Verificando quem é o menor
menor = p
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t
# Verificando quem é o maior
maior = p
if s > p and s < t:
    maior = s
if t > p and t > s:
    maior = t
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
