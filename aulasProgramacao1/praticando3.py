# aula dia 07/10
"""
# EXEMPLO 1, Linhas com maior soma, colunas com maior
def mostrar(vals):
  print("Conteudo da Matriz:")
  for numeros in vals:
    for valor in numeros:
      print("%4d"%valor, end="")
    print()
  print("Fim da Matriz")
  return None

def criarAleatorio(qtdLin, qtdCol, min, max):
  from random import randint
  vals = []
  for lin in range(qtdLin):
    novaLinha = []
    for col in range(qtdCol):
      numero = randint(min, max)
      novaLinha.append(numero)
    vals.append(novaLinha)
  return vals

def localizaLinha(vals):

  def somar(numeros):
    soma = 0
    for num in numeros:
      soma += num
    return soma

  linhaMaior = 0
  somaMaior = somar(vals[0])
  for lin in range(1, len(vals)):
    somaAtual = somar(vals[lin])
    if somaAtual > somaMaior:
      somaMaior = somaAtual
      linhaMaior = lin
  return linhaMaior, somaMaior # posso definir desa forma para que receba o valor na mesma linha

def localizaColuna(vals):

  def somaColuna(coluna, matriz): # gravar isso, pois pode ser muito util, para colunas
    soma = 0
    for linhaDeValores in matriz:
      soma += linhaDeValores[coluna]
    return soma

  colunaMaior = 0
  somaColunaMaior = somaColuna(0, vals)
  for col in range(len(vals[0])):
    somaAtual = somaColuna(col, vals)
    if somaAtual > somaColunaMaior:
      somaColunaMaior = somaAtual
      colunaMaior = col
  return colunaMaior, somaColunaMaior
# PP
valores = criarAleatorio(5, 7, -10, +10)
mostrar(valores)
linhaMaiorSoma, somaDosValores = localizaLinha(valores)
print("Linha:", linhaMaiorSoma)
print(valores[linhaMaiorSoma], "=", somaDosValores)
colunaMaiorSoma, somaDosValoresNaColuna = localizaColuna(valores)
print("Coluna de Maior Soma:", colunaMaiorSoma)
print("Soma Total na Coluna:", somaDosValoresNaColuna)
"""

# EXEMPLO 2, String
# Ler carta, manter em uma linha. Mostrar Carta.
# Perguntar que palavra deve ser substituida e seu novo conteudo
# Mostrar novamente a carta apos a substituicao

# Subs
def ler():
  linhas = []
  linha = input()
  while linha != "":
    linhas.append(linha)
    linha = input()
  return linhas

def mostrar(linhas):
  print("Texto:")
  for linhas in linhas:
    print(linhas)
  print()
  return None

def  substituirTodas(pAntiga, pNova, linhas): # usando replace e mais facil, tambem fazer por esse
  for i in range(len(linhas)):                # exemplo para que fique mais facil
    novaLinha = linhas[i].replace(pAntiga, pNova)
    linhas[i] = novaLinha
  return None

def inverter(linhas):
  for i in range(len(linhas)// 2):            # isso usar como molde para inverter, a ordem das linhas
    linhas[i], linhas[len(linhas)-1-i] = linhas[len(linhas)-1-i], linhas[i]      
  return None                   

def inverterCadaLinha(linhas):
  for i in range(len(linhas)):
    linhaInvertida = ""
    for letra in linhas[i]:
      linhaInvertida = letra + linhaInvertida  # ela desse modo entra invertida somando
    linhas[i] = linhaInvertida
  return None

# PP
linhasDaCarta = ler()
mostrar(linhasDaCarta)
antiga, nova = input().split()
substituirTodas(antiga, nova, linhasDaCarta)
mostrar(linhasDaCarta)
inverter(linhasDaCarta)
mostrar(linhasDaCarta)
inverterCadaLinha(linhasDaCarta)
mostrar(linhasDaCarta)
