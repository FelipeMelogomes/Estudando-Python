# Conversor de Moedas

real = float(input('Quanto dinheiro voçê tem na carteira?:R$'))
dolar = real / 5.61
euro = real / 6.33
FrancoSuiço = real / 6.08
Dolarcanadense = real / 4.45
LibraEsterlina = real / 7.43
Yuan = real / 0.89
LiraTurca = real / 0.41
print('Com R${:.2f} voçê pode comprar DOLAR {:.2f}'.format(real, dolar ))
print('Com R${:.2f} voçê pode comprar EURO {:.2f}'.format(real, euro))
print('Com R${:.2f} voçê pode comprar FrancoSuiço {:.2f}'.format(real, FrancoSuiço))
print('Com R${:.2f} voçê pode comprar DolarCanadense {:.2f}'.format(real, Dolarcanadense))
print('Com R${:.2f} voçê pode comprar LibraEsterlina {:.2f}'.format(real, LibraEsterlina))
print('Com R${:.2f} voçê pode comprar Yuan {:.2f}'.format(real, Yuan))
print('Com R${:.2f} voçê pode comprar LiraTurca {:.2f}'.format(real, LiraTurca))