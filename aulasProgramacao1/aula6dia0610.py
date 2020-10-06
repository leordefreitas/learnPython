"""
# EXEMPLO 1
# sub
def preencher(valores):
  for ind in range(len(valores)):
    valores[ind] = int(input("Elemento["+str(ind)+"]="))
  return None
##### esse e o mais eficiente quando ele achar o certo ele para
# def buscaElementos(valores, procurado):
#   for indice in range(len(valores)):
#     if valores[indice] == procurado:
#       return indice
#   return -1
##### mais ineficiente ele percorre toda a lista
# def buscaElementos(valores, procurado):
#   local = -1
#   for indice in range(len(valores)):
#     if valores[indice] == procurado:
#       local = indice
#   return local
##### usando o while
# def buscaElementos(valores, procurado):
#   local = -1
#   indice = 0
#   while indice < len(valores):
#     if valores[indice] != procurado:
#       indice = indice + 1
#     else:
#       local = indice
#       indice = len(valores)
##### usando o while, mais simples e nao percorrendo todos os valores
##### da lista
# def buscaElementos(valores, procurado):
#   indice = 0
#   while indice < len(valores):
#     if valores[indice] != procurado:
#       indice = indice + 1
#     else:
#       return indice
#   return -1
##### busca binaria, procura apartir de um ponto diferente, lembrando
##### somente pode ser crescente ou decrescente
def buscaElementos(valores, procurado):
  inicio = 0
  fim = len(valores) - 1
  meio = (inicio + fim) // 2
  while (inicio < fim) and (procurado != valores[meio]):
    if procurado > valores[meio]:
      inicio = meio + 1
    else:
      fim = meio - 1
    meio = (inicio + fim) // 2
  if procurado != valores[meio]:
    local = -1
  else:
    local = meio
  return local
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
"""

# EXEMPLO 2
# sub
def preencher(valores):
  for ind in range(len(valores)):
    valores[ind] = int(input("Elemento["+str(ind)+"]="))
  return
def buscarMenorMaiorElementos(valores):
  menor = valores[0]
  maior = valores[0]
  for indice in range(1, len(valores)):
    if menor > valores[indice]:
      menor = valores[indice]
    elif maior < valores[indice]:
      maior = valores[indice]
  return [menor, maior]
def escrever(infos):
  print("O menor elemento =", infos[0], "e o maior elemento =", infos[1])
  return None

# principal
numeros = [0] * 10
preencher(numeros)
extremos = buscarMenorMaiorElementos(numeros)
escrever(extremos)
