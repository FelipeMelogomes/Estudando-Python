# Calcular Hipotenusa

import math
ch = float(input('Digite o cateto 1? '))
ch2 = float(input('Digite o Cateto 2? '))
hi = math.hypot(ch, ch2)
print(' A hipotenusa é {:.2f}'.format(hi))