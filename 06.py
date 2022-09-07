#6
#programador: Eduardo Costa
#data da última atualização: 04/09/2022

import math

a = float(input('Forneça a:'))
if a != 0:
  b, c = float(input('Forneça b:')), float(input('Forneça c:'))
  delta = b ** 2 - 4 * a * c
  if delta > 0:
    x1 = ((b * -1) + (delta ** 0.5)) / (2 * a)
    x2 = ((b * -1) - (delta ** 0.5)) / (2 * a)
    print(x1, ',', x2)
  elif delta == 0:
    x1 = ((b * -1) + (delta ** 0.5)) / (2 * a)
    print(x1)
  else:
    print('Não possui raízes reais.')  
else:
  print('Não é uma equação do segundo grau.')
