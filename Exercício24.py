# Programa que verifica sem tem 'SANTO' na palavra digitada

cidade = str(input('Digite um cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')