# Calcular seno, Cosseno e tangente de um valor

import math
angulo = float(input(' Digite o Ângulo: '))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print('O Ãngulo de {} tem o seno de {:.2f} Cosseno de {:.2f} e a tangente de {:.2f} '.format(angulo,s,c,t))

