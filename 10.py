#10
#programador: Eduardo Costa
#data da última atualização: 04/09/2022

n1 = float (input('Forneça a nota da primeira parcial: '))
n2 = float (input('Forneça a nota da segunda parcial: '))
n3 = float (input('Forneça a nota da terceira parcial: '))
med = (n1+n2+n3)/3

if med >= 7:
  if med == 10:
    print('Aprovado com Distinção. Média: %.2f ' %med)
  else:
    print('Aprovado. Média: %.2f ' %med)
else:
  print('Reprovado. Média: %.2f ' %med)
