# EXEMPLO 1
# sub
def preencher(valores):
  for ind in range(len(valores)):
    valores[ind] = int(input("Elemento["+str(ind)+"]="))
  return None
# esse e o mais eficiente quando ele achar o certo ele para
def buscaElementos(valores, procurado):
  for indice in range(len(valores)):
    if valores[indice] == procurado:
      return indice
  return -1
#  mais ineficiente ele percorre toda a lista
# def buscaElementos(valores, procurado):
#   local = -1
#   for indice in range(len(valores)):
#     if valores[indice] == procurado:
#       local = indice
#   return local
def escreverRespostas(valor, pos):
  if pos < 0:
    print(valor, "nao foi encontrado")
  else:
    print(valor, "foi encontrado na posicao", pos)
  return

# pricipal
numeros = [0] * 10
dado = int(input("Escolha valor a ser procurado: "))
onde = buscaElementos(numeros, dado)
escreverRespostas(dado, onde)