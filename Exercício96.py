# CALCULAR PERÍMETRO DE TERRENO USANDO FUNÇÃO


def Aréa(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m2.')



print('Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA (m):'))
comprimento = float(input('COMPRIMENTO (m):'))
Aréa(largura, comprimento)



