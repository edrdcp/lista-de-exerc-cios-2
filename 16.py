#16
#programador: Eduardo Costa
#data da última atualização: /09/2022

litros = float(input("Forneça o número de litros vendidos: "))
combustivel = input("Digite A para Álcool ou G para gasolina: ")
preco = 0

if combustivel.upper() == "A":
    preco = litros * 1.9
    if litros <= 20:
        preco -= 1.9 * litros * 0.03
    else:
        preco -= 1.9 * litros * 0.05
elif combustivel.upper() == "G":
    preco = litros * 2.5
    if litros <= 20:
        preco -= 2.5 * litros * 0.04
    else:
        preco -= 2.5 * litros * 0.06
print("O preço a pagar é R$ %.2f" %preco)
