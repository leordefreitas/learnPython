# insert(posicao, novoElemento) -> serve para eu colocar aonde eu quero
# EXEMPLO 2

# sub
def preencher(listaElems, qtd, min, max):
  from random import randint
  for item in range(qtd):
    listaElems.append(randint(min, max))
  return None
# PP
qtdNumeros = int(input())
minimo = int(input())
maximo = int(input())
numeros = []
preencher(numeros, qtdNumeros, minimo, maximo)
print(numeros)

