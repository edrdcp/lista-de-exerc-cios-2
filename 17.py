#17
#programador: Eduardo Costa
#data da última atualização: 04/09/2022

morango = float(input('Forneça a quantidade de morangos em kg: '))
maca = float(input('Forneça a quantidade de maçãs em kg:'))
valor = 0

if morango <= 5:
    valor += morango * 2.5
else:
    valor += morango * 2.2
if maca <= 5:
    valor += maca * 1.8
else:
    valor += maca * 1.5

if (morango + maca) > 8 or valor > 25:
    valor -= valor * 0.1

print('O valor a ser pago é R$ %.2f' %valor)
