# aula dia 07/10

# Linhas com maior soma, colunas com maior
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