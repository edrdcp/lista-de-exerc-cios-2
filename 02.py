#2
#programador: Eduardo Costa
#data da última atualização: 31/08/2022

ganhoPorHora = float(input('Quanto você ganha por hora?: R$ '))
horasPorMes = int(input('Número de horas trabalhadas no mês: '))

salarioBruto = ganhoPorHora * horasPorMes
fgts = salarioBruto * 0.11
sindicato = salarioBruto * 0.03
inss = salarioBruto * 0.1

if 900 >= salarioBruto:
  ir = 0
elif 1500 >= salarioBruto:
  ir = salarioBruto * 0.05
elif 2500 >= salarioBruto:
  ir = salarioBruto * 0.1
else:
  ir = salarioBruto * 0.2

salarioLiquido = salarioBruto - (ir + sindicato + inss)

print('Salário Bruto: R$ %.2f' %salarioBruto)
print('IR: R$ %.2f' %ir)
print('INSS: R$ %.2f' %inss)
print('FGTS: R$ %.2f' %fgts)
print('Sindicato: R$ %.2f' %sindicato)
print('Salário Líquido: R$ %.2f' %salarioLiquido)
