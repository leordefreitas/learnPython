# lista.insert(posicao, novoElemento) -> serve para eu colocar aonde eu quero
# lista.pop(pos) -> remove o ultimo elemento de uma lista se nao for indicado o pos
# lista.remove(x) -> primeira aparicao do x e removido
# lista.sort() -> ordena a lista em uma ordem crescente ou decrescente
# cons(item, dados) -> retorna uma nova lista sendo que (item) e o primeiro elemento e (dados) o resto
# isinstance(item, list) -> o (item) indica o valor que eu quero verificar e (list) e o tipo que eu quero 
# sabe se e isso que eu coloquei em list


"""
# EXEMPLO 1
# sub
def preencher(listaElems, qtd, min, max):      
  from random import randint
  for item in range(qtd):
    listaElems.append(randint(min, max))         # min e max serve para determinar o valores no randint()
  return None                                    
# PP
qtdNumeros = int(input())
minimo = int(input())
maximo = int(input())
numeros = []
preencher(numeros, qtdNumeros, minimo, maximo)
print(numeros)
"""

# EXEMPLO 2
# sub
def preencher(listaElems, qtd, min, max):      
  from random import randint
  for item in range(qtd):
    listaElems.append(randint(min, max))         # min e max serve para determinar o valores no randint()
  return None
def removerDuplicatas(elementos):
  indice = 0
  while indice < len(elementos):
    if elementos.count(elementos[indice]) == 1:
      indice += 1
    else:
      elementos.remove(elementos[indice])
  return None
# PP
numeros = []
preencher(numeros, 100, 0, 40)
print(numeros)
removerDuplicatas(numeros)
print(numeros)

# EXEMPLO 3

def ehLista(item):                          # se for list vai retornar Truee consequentemente o ehAtomo()
  return isinstance(item, list)             # vai ser False pq ele e o contrrio de ehLista()
def ehAtomo(item):
  return not ehLista(item)
def soma(dados):
  if dados == []:
    return 0
  else:
    if ehAtomo(car(dados)):                 # ele faz a soma de forma recursiva entao ele chama denovo a 
      return car(dados) + soma(cdr(dados))  # a funcao soma()
    else:
      return soma(car(dados)) + soma(cdr(dados))
      





# esse programa vai somar todos os valores de (dados) recursivamente
def soma(dados):
  if dados == []:
    return 0
  else:
    return car(dados) + soma(cdr(dados))

