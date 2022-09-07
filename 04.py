#4
#programador: Eduardo Costa
#data da última atualização: 04/09/2022

n1 = float (input('Forneça a nota da primeira parcial: '))
n2 = float (input('Forneça a nota da segunda parcial: '))
med = (n1+n2)/2

if med >= 9:
  conc='A'
elif med >= 7.5:
  conc='B'
elif med >= 6:
  conc='C'
elif med >= 4:
  conc = 'D'
else:
  conc = 'E' 
print('Média: %2.1f' %med)
print(conc)

if (conc == 'E') or (conc == 'D'): #mensagem
  print('REPROVADO')
else:
  print('APROVADO')
