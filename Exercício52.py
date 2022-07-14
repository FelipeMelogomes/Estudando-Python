número = int(input('Digite um número: '))
tot = 0
for c in range(1,número + 1):
    if número % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O número {} foi divisível {} vezes'.format(número, tot))
if tot == 2:
    print('NÃO È PRIMO!')
else:
    print(' NÃO É PRIMO!')