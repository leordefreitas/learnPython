# Q1
# SUBPROGRAMAS
def qualMaior(vals):
  valMaior = vals[0]
  for val in vals:
    if val > valMaior:
      valMaior = val
  return valMaior
def qualMenor(vals):
  valMenor = vals[0]
  for val in vals:
    if val < valMenor:
      valMenor = val
  return valMenor
def qualMedia(vals):
  soma = 0
  for val in vals:
    soma += val
  return soma / len(vals)
def qualMaisProximoMedia(vals, num):
  valMaisProx = vals[0]
  operador1 = 0

  # determiando um valor para o operador
  if valMaisProx <= num:
    operador1 = num - valMaisProx
  else:
    operador1 = valMaisProx - num

  # achando se tem mais proximo
  for val in vals:
    operador2 = 0
    if val <= num:
      operador2 = num - val
      if operador2 < operador1:
        operador1 = operador2
        valMaisProx = val
    else:
      operador2 = val - num
      if operador2 < operador1:
        operador1 = operador2
        valMaisProx = val
  return valMaisProx
def imprimeLinha(valMaior, valMenor, valMedia, valMaisProx):
  print()
  print("O menor número é %i e o maior número é %i" %(valMenor, valMaior))
  print("A média dos valores é %.2f e o valor mais próximo da média é %i" %(valMedia, valMaisProx))
  print()
  return None
def imprimeFinal(valMaiorTodos, valMenorTodos, valLinhas):
  print("O menor de todos os valores lidos é %i" %(valMenorTodos))
  print("O maior de todos os valores lidos é %i" %(valMaiorTodos))
  print("O total de linhas é %i" %(valLinhas))
  return None

# PROGRAMA PRINCIPAL
valores = list(map(int, input().split()))
qtdLinhas = 0
ligado = True

if valores == []:
  print("Nenhum número foi lido!!!")
  ligado = False

else:
  maiorTodos = valores[0]
  menorTodos = valores[0]
  # condicao determinada no while para so rodar quando tiver valor no valores
  while ligado:
      
    maior = qualMaior(valores)
    menor = qualMenor(valores)
    media = qualMedia(valores)
    maisProximoMedia = qualMaisProximoMedia(valores, media)
    imprimeLinha(maior, menor, media, maisProximoMedia)

    # condicao para determinar qual o maior e o menor valor
    if maiorTodos < maior:
      maiorTodos = maior
    elif menorTodos > menor:
      menorTodos = menor
    qtdLinhas += 1

    # input das listas
    valores = list(map(int, input().split()))
    if valores == []:
      ligado = False

  imprimeFinal(maiorTodos, menorTodos, qtdLinhas)