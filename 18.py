#18
#programador: Eduardo Costa
#data da última atualização: /09/2022

print('Forneça o tipo de carne comprada')
tipo = int(input('Digite 1 para Filé Duplo, 2 para Alcatra ou 3 para Picanha: '))
quantidade = float(input('Forneça a quantidade de carne em kg: '))
print('Forma de Pagamento')
pagamento = int(input('Digite 1 para pagamento no cartão Tabajara ou 2 para pagamento por outro meio: '))

preco = 0

print('CUPOM FISCAL')
if tipo == 1:
  if quantidade <= 5:
    preco += quantidade * 4.9
  else:
    valor += quantidade * 5.8
  print('Tipo da carne: Filé Duplo')  

if tipo == 2:
  if quantidade <= 5:
    preco += quantidade * 5.9
  else:
    preco += quantidade * 6.8
  print('Tipo da carne: Alcatra')

if tipo == 3:
  if quantidade <= 5:
    preco += quantidade * 6.9
  else:
    preco += quantidade * 7.8
  print('Tipo da carne: Picanha')

if pagamento == 1:
  desconto = preco * 0.05
  precoFinal = preco - desconto
  tipoPag = 'Cartão Tabajara'
else:
  precoFinal = preco
  desconto = 0.00
  tipoPag = 'Outro meio (Dinheiro, Cartão ou PIX)'

print('Kg: ', quantidade)
print('Preço total: R$ %.2f' %preco)
print('Tipo de pagamento', tipoPag)
print('Desconto: R$ %.2f' %desconto)
print('Valor a pagar: R$ %.2f' %precoFinal)
