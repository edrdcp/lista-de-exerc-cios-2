#5
#programador: Eduardo Costa
#data da última atualização: 04/09/2022

l0, l1, l2 = float(input('Forneça um lado do triângulo: ')), float(input('Forneça um lado do triângulo: ')), float(input('Forneça um lado do triângulo: '))

if (l0 + l1 >= l2) and (l1 + l2 >= l0) and (l2 + l0 >= l1):
  print('Os lados formam um triângulo.')
  if l0 == l1 == l2:
    print('Triângulo Equilátero.')
  elif l0 != l1 != l2:
    print('Triângulo Escaleno.')
  elif (l0 == l1) or (l1 == l2) or (l0 == l2):
    print('Triângulo Isósceles.')
else:
  print('Os lados não formam um triângulo.')   
