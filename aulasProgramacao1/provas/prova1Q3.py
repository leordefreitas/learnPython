# Q3
# SUBPROGRAMAS
def gerarMatriz(vals):
  from random import randint
  matrizFinal = []
  for indLin in range(vals[0]):
    linhaMatriz = []
    for indCol in range(vals[1]):
      valor = randint(vals[2], vals[3])
      linhaMatriz.append(valor)
    matrizFinal.append(linhaMatriz)
  return matrizFinal
def imprimeMatriz(vals):
  for lin in range(len(vals)):
    for col in range(len(vals[lin])):
      print("%4d" %(vals[lin][col]), end="")
    print()
  return None
def semPrimos(vals):
  linSemPri = []
  for linha in vals:
    aux1 = 0
    for valor in linha:
      if valor > 1:
        aux2 = 0
        for divisor in range(2, valor):
          if valor % divisor == 0:
            aux2 += 1
        if aux2 == 0:
          aux1 += 1
          continue
    if aux1 > 0:
      continue
    else:
      linSemPri.append(linha)
  return linSemPri

# PROGRAMA PRINCIPAL
valores = list(map(int, input("Digite qtd linhas e colunas, número aleatório no intervalo: ").split()))
matriz = gerarMatriz(valores)
print()
print("Matriz:")
imprimeMatriz(matriz)
linhasSemPrimo = semPrimos(matriz)
print()
print("Linhas que não possuem primos:")
imprimeMatriz(linhasSemPrimo)

