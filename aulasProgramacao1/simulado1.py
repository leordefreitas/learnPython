# exercicio 1
# feito em aula pelo professor
"""
def ehPrimo(n):
  return n > 1 # nao esta completo depois completar!!!!!!!

totalDeNumerosLidos = totalDeNumerosPrimos = 0

numero = int(input()) # le o primeiro
  while numero != 0:
    totalDeNumerosLidos += 1
    if ehPrimo(numero):
      totalDeNumerosPrimos += 1
    numero = int(input()) # le o proximo

print("Quantidade de Lidos:", totalDeNumerosLidos)
print("Quantidade de Primos:", totalDeNumerosPrimos)
"""

# exercicio 2
# feito pelo professor
"""
def maior(nums):
  oMaiorValor = nums[0]

  for i in nums:
    if i > oMaiorValor:
      oMaiorValor = i

  return oMaiorValor

linhaLida = input()

if linhaLida = "":
  print("Nenhum numero foi lido!!!")

else:
  somaDosMaiores = qtdLinhas = 0

  while linhaLida != "":
    qtdLinhas += 1
    numeros = list(map(int, linhaLida.split()))
    qualMaior = maior(numeros)
    somaDosMaiores += qualMaior
    linhaLida = input()

  print("Media dos Maiores: %.1f" %(somaDosMaiores/qtdLinhas))
"""
"""
# exercicio 3
# feito na aula pelo professor

# subprogramas
def lerPontos():
  pts = []
  x, y = map(float, input().split()) # pq o inteiro esta contido, pega o primeiro
  while (x, y) != (0, 0): # DeMorgan x != 0 or y != 0
    pts.append((x, y))
    x, y = map(float, input().split()) # pega o proximo
  return pts

def calculaCentroide(lista):
  qtdPontos = len(lista)
  somaXs = somaYs = 0
  for (x, y) in lista: # isso usar as tulipas e bem mais simples
    somaXs += x
    somaYs += y
  return somaXs / qtdPontos, somaYs / qtdPontos

def encontraMaisProximo(ponto, lista):
  def distancia(pA, pB):
    return ((pA[0] - pB[0])**2 + (pA[1] - pB[1])**2)**0.5

  ptMaisProximo = lista[0]
  distMaisProximo = distancia(lista[0], ponto)

  for pt in pontos:
    distAtual = distancia(pt, ponto)

    if distAtual < distMaisProximo:
      distMaisProximo = distAtual
      ptMaisProximo = pt
  return ptMaisProximo

# programa
pontos = lerPontos()

pontoCentroide = calculaCentroide(pontos)
print("Centroide  =", pontoCentroide)

pontoMaisProximo = encontraMaisProximo(pontoCentroide, pontos)
print("Ponto mais proximo =", pontoMaisProximo)
"""