#8
#programador: Eduardo Costa
#data da última atualização: /09/2022

print('Forneça uma data no formato dd/mm/aaaa')
dia, mes, ano = int(input('Dia:')), int(input('mes:')), int(input('Ano:'))
valida = 0

#CORRIGIR NO CASO DO USUÁRIO COLOCAR DIA 0

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
  if(dia <= 31):
    valida = 1
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
  if(dia<=30):
    valida = 1
elif mes == 2:
  if (ano%400==0) or ((ano % 4 == 0) and (a % 100!=0)): #verifica se é bissexto
    if dia <= 29:
      valida = 1
  elif dia <= 28:
    valida = 1

#print('Data fornecida: ', dia, '/', mes, '/', ano)

if valida == 1:
  print('Data válida')
else:
  print('Data inválida')
