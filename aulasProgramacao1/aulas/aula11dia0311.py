# dict() -> atribui uma chave vazia
# pares1 = dict()
# print(pares1)
# adicionando uma chave com um valor
# pares1[13] = "Valor da Sorte"
# print(pares1)
# deletando, ali mostra como e posso declarar com chaves os valores
# pares3 = {51:"Boa ideia", 13: "Valor da Sorte", 31: "Dia do Azar"}
# del pares3[13]
# print(pares3)
# len() -> achar o comprmento dessas chaves
# print(len(pares3))
# d.items() -> retorna todos os pares
# d.keys() -> retorna todas as chaves
# d.values() -> retorna todos os valores
# ACHAR OS VALORES NA CHAVE
"""
for chave in pares:
  print(chave, ":", pares[chave])
for chave, valor in pares.items():
  print(chave, ":", valor)
for chave in sorted(pares):
  print(chave, ":", pares[chave])
for chave in sorted(pares.keys()):
  print(chave, ":", pares[chave])
"""
# get(chave) -> pode pegar o valor daquela chave pelo get()

# exemplo 1
# pares = dict()
# for i in range(5):
#   nome = input("Digite nome: ")
#   fone = input("Digite o telefone de "+nome+": ")
#   pares[nome] = fone
#   print(pares)

# exemplo 2
# sub
# def mostrar(prods):
#   for chave, valor in sorted(prods.items()):
#     print(chave, "-", valor)
#   return None
# def preencher(prods, entradas):
#   for i in range(entradas):
#     cod = input("Codigo: ")
#     desc = input("Descricao: ")
#     qtd = int(input("Quantidade: "))
#     preco = float(input("Valor: "))
#     data = input("Limite de Validade - dd/mm/aa: ")
#     partes = data.split("/")
#     prods[cod] = [desc, qtd, preco, (int(partes[0]), int(partes[1]), int(partes[2]))]
#   return None
# def vender(prods, codsQtds):
#   totalGasto = 0
#   for chave in codsQtds:
#     if chave not in prods:
#       print(chave, "- Codigo Inexistente")
#     else:
#       item = prods[chave]
#       if item[1] < codsQtds[chave]:
#         print(chave, "- Quantidade Insuficiente")
#       else:
#         item[1] -= codsQtds[chave]
#         pros[chave] = item
#         print(item[0], "x"+codsQtds[chave], "- Subtotal:", item[2]*codsQtds[chave])
#         totalGasto += item[2]*codsQtds[chave]
#   print("Total da Nota Fiscal:", totalGasto)
#   return None
# # pp
# produtos = {}
# preencher(produtos, 5)
# mostrar(produtos)
# vender(produtos, {"xkk":3, "yzb":2})
# mostrar(produtos)