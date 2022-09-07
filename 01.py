#1
#programador: Eduardo Costa
#data da última atualização: 31/08/2022

salario = float(input('Forneça o salário atual: '))
salarioInicial = salario
salarioNovo = salario
percentual = 0

if salario <= 280.0:
  salarioNovo *= 1.2
  percentual = 20
elif 280.0 < salario <= 700.0:
  salarioNovo *= 1.15
  percentual = 15
elif 700.0 < salario < 1500.0:
  salarioNovo *= 1.1
  percentual = 10
else:
  salarioNovo *= 1.05
  percentual = 5

aumento = salarioNovo - salario

print('Salário antes do reajuste: R$ %.2f' %salarioInicial)
print('Percentual de aumento aplicado: %.2f' %percentual, '%')
print('Valor do aumento: R$ %.2f' %aumento)
print('Novo salário: R$ %.2f' %salarioNovo)
