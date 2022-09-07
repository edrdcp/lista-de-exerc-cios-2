#15
#programador: Eduardo Costa
#data da última atualização: 04/09/2022

respostasPositivas = 0

resposta = input("Telefonou para a vítima? (S / N): ")
if resposta.upper() == "S":
  respostasPositivas += 1

resposta = input("Esteve no local do crime? (S / N): ")
if resposta.upper() == "S":
    respostasPositivas += 1

resposta = input("Mora perto da vítima? (S / N): ")
if resposta.upper() == "S":
    respostasPositivas += 1

resposta = input("Devia para a vítima? (S / N): ")
if resposta.upper() == "S":
    respostasPositivas += 1

resposta = input("Já trabalhou com a vítima? (S / N): ")
if resposta.upper() == "S":
    respostasPositivas += 1

if respostasPositivas < 2:
    print("Inocente")
elif respostasPositivas == 2:
    print("Suspeita")
elif respostasPositivas < 5:
    print("Cúmplice")
else:
    print("Assassino")
