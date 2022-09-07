#14
#programador: Eduardo Costa
#data da última atualização: 04/09/2022

a, b = float(input('Forneça o primeiro número: ')), float(input('Forneça o segundo número: '))
op = input('Operação desejada (+, -, *, /): ')

if op == '+':
  resultado = a + b
elif op == '-':
  resultado = a + b
elif op == '*':
  resultado = a + b
elif op == '/':
  if b != 0:
    resultado = a + b
  else:
    print('Erro, divisor não pode ser 0')

print(resultado)
if (resultado // 1) % 2 == 0:
  print('Par.')
else:
  print('Ímpar.')

if resultado >= 0:
  print('Positivo.')
else:
  print('Negativo.')

if resultado % 1 == 0:
  print('Inteiro.')
else:
  print('Decimal')
