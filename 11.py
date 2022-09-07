#11
#programador: Eduardo Costa
#data da última atualização: 05/09/2022

saque = int(input('Valor do saque [R$10-R$600]: '))
if saque < 10 or saque > 600:
  print('Erro')
  saque = int(input('Valor do saque [R$10-R$600]: '))

x = saque #variavel auxiliar

cem = int(x / 100)
x = x % 100  #resto da divisão
cinquenta = int(x / 50) #replica a lógica até chegar em 1 real
x = x % 50
dez = int(x / 10)
x = x % 10
cinco = int(x / 5)
x = x % 5
um = x
    
print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  1,00 = ',um)
