#9
#programador: Eduardo Costa
#data da última atualização: /09/2022

print('Forneça um número inteiro menor que 1000')
n = int(input())
if n >= 1000:
  print('Forneça um número inteiro menor que 1000')
else:
  unidade = n % 10
  n1 = (n - unidade) / 10
  dezena = int(n1 % 10)
  centena = int((n1 - dezena) / 10)

if unidade == 1:
  uniPrint = 'unidade'
elif unidade > 1:
  uniPrint = 'unidades'

if dezena == 1:
  dezPrint = 'dezena'
elif dezena > 1:
  dezPrint = 'dezenas'

if centena == 1:
  cenPrint = 'centena'
elif centena > 1:
  cenPrint = 'centenas'

if unidade > 0 and dezena > 0 and centena > 0:
  print(centena, cenPrint, dezena, dezPrint, unidade, uniPrint)

elif unidade > 0 and dezena > 0 and centena == 0:
  print(dezena, dezPrint, unidade, uniPrint)

elif unidade > 0 and dezena == 0 and centena > 0:
  print(centena, cenPrint, unidade, uniPrint)

elif unidade == 0 and dezena > 0 and centena > 0:
  print(centena, cenPrint, dezena, dezPrint)

elif unidade == 0 and dezena == 0 and centena > 0:
  print(centena, cenPrint)

elif unidade == 0 and dezena > 0 and centena == 0:
  print(dezena, dezPrint)

elif unidade > 0 and dezena == 0 and centena == 0:
  print(unidade, uniPrint)
