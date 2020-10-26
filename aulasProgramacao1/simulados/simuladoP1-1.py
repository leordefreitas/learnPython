# Simulado P1 Q1
# sub
def cria3D(qPs, qLs, qCs, vMin, vMax):
  from random import randint
  vals = []
  for p in range(qPs):
    novaMatriz = []
    for lin in range(qLs):
      novaLinha = []
      for col in range(qCs):
        valor = randint(vMin, vMax)
        novaLinha.append(valor)
      novaMatriz.append(novaLinha)
    vals.append(novaMatriz)
  return vals
def mostrar3D(vals):
  print("Conteudo da Matriz:")
  for p in range(len(vals)):
    print("Plano %d:" %(p+1))
    for lin in range(len(vals[p])):
      for col in range(len(vals[p][lin])):
        print("%4d" %(vals[p][lin][col]), end="")
      print()
    print()
  return None
def calculaMedia(vals):
  qtdElems = len(vals) * len(vals[0]) * len(vals[0][0])
  soma = 0
  for matrizesValores in vals:
    for linhaValores in matrizesValores:
      for valor in linhaValores:
        soma += valor
  return soma / qtdElems
def achaMaior(vals):
  valMaior = vals[0][0][0]
  for matrizesValores in vals:
    for linhaValores in matrizesValores:
      for valor in linhaValores:
        if valor > valMaior:
          valMaior = valor
  return valMaior
def mostraOcorrencias(vals, valor):
  print("Posicoe em que o maior valor o corre:")
  for p in range(len(vals)):
    for l in range(len(vals[p])):
      for c in range(len(vals[p][l])):
        if vals[p][l][c] == valor:
          print("Plano %d, Linha %d, Coluna %d" %(p+1, l+1, c+1))
  return None
# pp
qtdPlanos, qtdLinhas, qtdColunas = map(int, input().split())
valMinimo, valMaximo = map(int, input().split())

valores = cria3D(qtdPlanos, qtdLinhas, qtdColunas, valMinimo, valMaximo)
mostrar3D(valores)
media = calculaMedia(valores)
print("Media dos valores: %.2f" %(media))
print()
maior = achaMaior(valores)
print("Maior valor na matriz:", maior)
mostraOcorrencias(valores, maior)