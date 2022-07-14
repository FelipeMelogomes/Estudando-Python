times = ('Corinthians', 'Palmeiras','Santos', 'Grêmio', 'Cruzeiro',
        'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlêtico-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória','Coritiba','Avaí', 'Ponte Preta',
        'Atlético-GO')

print('-=-' * 15)
print(f'Lista de Times do Brasileirão: {times}')
print('-=-' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=-' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=-' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
print('-=-' * 15)

