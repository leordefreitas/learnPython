
# EXEMPLO 1
# sub
def preencher(valores):
  for ind in range(len(valores)):
    valores[ind] = int(input("Elemento["+str(ind)+"]="))
  return None
##### busca simples, ele e muito custoso como algoritimo
# def buscaModa(valores):
#   auxiliar = [0] * len(valores)
#   for indice in range(len(valores)):
#     auxiliar[indice] = 1
#     for varre in range(indice + 1, len(valores)):
#       if valores[varre] == valores[indice]:
#         auxiliar[indice] += 1
#   ondeModa = 0
#   for i in range(1, len(auxiliar)):
#     if auxiliar[i] > auxiliar[ondeModa]:
#       ondeModa = i
#     return valores[ondeModa]
##### busca de um vetro ordenado
def buscaModa(valores):
  moda = valores[0]
  ind = 0
  frequencia = 1
  while ind < len(valores) - 1:
    ind = ind + 1
    if valores[ind] == valores[ind - frequencia]:
      moda = valores[ind]
      frequencia = frequencia + 1
  return moda

# principal
numeros = [0] * 10
preencher(numeros)
moda = buscaModa(numeros)

print(moda)

# EXEMPLO 2
# sub
def preencher(valores):
  for ind in range(len(valores)):
    valores[ind] = int(input("Elemento["+str(ind)+"]="))
  return None
#### metodo de selecao
# # somente troca os valores nada de mais
# def trocar(vals, posX, posY):
#   temp = vals[posX]
#   vals[posX] = vals[posY]
#   vals[posY] = temp
#   return None
# # ele somente percorre encontrando o menor valor no vetor
# def selecionarMenor(vals, inicio):
#   localMenor = inicio
#   for pos in range(inicio + 1, len(vals)):
#     if vals[pos] < vals[localMenor]:
#       localMenor = pos
#   return localMenor
# def ordena(valores):
#   for ind in range(len(valores) - 1):
#     menor = selecionarMenor(valores, ind)
#     trocar(valores, ind, menor)
#   return None
#### metodo bolha, bem mais rapido e bem melhor de ser trabalhodo
#### ele somente empurra o elemento para o final da fila
def trocar(vals, posX, posY):
  temp = vals[posX]
  vals[posX] = vals[posY]
  vals[posY] = temp
  return None
def ordena(valores):
  for tamanho in range(len(valores) - 1, 0, -1):
    for i in range(tamanho):
      if valores[i] > valores[i + 1]:
        trocar(valores, i, i + 1)
  return None

# principal
numeros = [0] * 10
preencher(numeros)
print("Vetor lido:", numeros)
ordena(numeros)
print("Vetor Ordenado:", numeros)