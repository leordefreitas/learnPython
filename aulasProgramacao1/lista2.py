# Sudoku

"""array = []
num = int(input())

for ind in range(num):
    falso = False
    casoSudoku = []
    for i in range(9):
        casoSudoku.append(list(map(int,input().split(" "))))

    for linha in casoSudoku:

        for coluna in linha:
            if linha.count(coluna) > 1: 
              falso = True
    for i in range(9):
        caso = []
        for linha in casoSudoku:
            if not(linha[i] in caso): 
              caso.append(linha[i])

        if len(caso) != 9:
            falso = True
    for linham in range(0,9,3):
        caso1=[]
        caso2=[]
        caso3=[]
        for linha in range(linham, linham + 3):
            for colunam in range(0, 9, 3):
                for coluna in range(colunam, colunam + 3):
                    if colunam == 0:
                        if not(casoSudoku[linha][coluna] in caso1): 
                          caso1.append(casoSudoku[linha][coluna])
                    if colunam == 3:
                        if not(casoSudoku[linha][coluna] in caso2): 
                          caso2.append(casoSudoku[linha][coluna])
                    if colunam == 6:
                        if not(casoSudoku[linha][coluna] in caso3): 
                          caso3.append(casoSudoku[linha][coluna])
        if len(caso2) != 9: 
          falso = True
        if len(caso3) != 9:
           falso = True
        if len(caso1) != 9: 
          falso = True
    array.append([])
    array[-1].append("Instancia " + str(ind+1))
    if falso: 
      array[-1].append("NAO")
    else: 
      array[-1].append("SIM")
for ind in array :
    print(ind[0])
    print(ind[1])
    print()"""

"""
# Square Matrix III
# sub
def criarArray(valor):
  tabela = [0] * valor

  for i1 in range(len(tabela)):
    variandoTabela = [0] * valor
    for i2 in range(len(variandoTabela)):
      if i1 == 0 and i2 == 0:
        variandoTabela[i2] = 1
      elif i2 == 0:
        variandoTabela[i2] = tabela[i1 - 1][1]
      else:
        variandoTabela[i2] = variandoTabela[i2 - 1] * 2
    tabela[i1] = variandoTabela
  return tabela
def mostrar(valores):
  # tabelaPronta = ""
  # for lista in valores:
  #   for ind in range(len(lista)):
  #     if ind == (len(lista) - 1):
  #       print("%d" %(lista[ind]), end="\n")
  #     else:
  #       print("%d" %(lista[ind]), end=" ")
  # print(tabelaPronta)
  size = len(str(valores[len(valores) - 1][len(valores) - 1])) + 1
  for line in range(len(valores)):
    for column in range(len(valores)):
      if column == 0:
        print(str(valores[line][column]).rjust(size-1), end="")
      else:
        print(str(valores[line][column]).rjust(size), end="")
    print()
  return None

# PP
numero = int(input())
arrayMostrar = []
while numero != 0:
  arrayMostrar.append(numero)
  numero = int(input())
for cada in arrayMostrar:
  mostrar(criarArray(cada))
  print()
"""


# Matrix of Squares
# sub
def quadradoMatriz(valores):
  for linha in valores:
    for ind in range(len(linha)):
      linha[ind] *= linha[ind]
  return None
def mostrar(valores, numMostrar):
  sizeValores = [0] * len(valores)
  for lin in range(len(valores)):
    for col in range(len(valores)):
      if sizeValores[col] < valores[lin][col]:
        sizeValores[col] = len(str(valores[lin][col]))

  # for linha in valores:
  #   for coluna in linha:
      # if coluna > maiorValor:
      #   maiorValor = coluna
  # size = len(str(maiorValor)) + 1
  print("Quadrado da matriz #%i:" %(numMostrar))
  for line in range(len(valores)):
    for column in range(len(valores)):
      if column == 0:
        print(str(valores[line][column]).rjust(sizeValores[column]), end="")
      else:
        print(str(valores[line][column]).rjust(sizeValores[column] + 1), end="")
    print()
  return None

# PP
qtdMatrizesCalcular = int(input())
tamanhoMatriz = int(input())
contador2 = 0
matrizMostrar = []
while contador2 < qtdMatrizesCalcular:
  matriz = []
  contador1 = 0
  while contador1 < tamanhoMatriz:
    num = list(map(int, input().split()))
    matriz.append(num)
    contador1 += 1
  quadradoMatriz(matriz)
  matrizMostrar.append(matriz)
  contador2 += 1
  if contador2 < qtdMatrizesCalcular:
    tamanhoMatriz = int(input())

contador3 = 4
for ind in range(len(matrizMostrar)):
  mostrar(matrizMostrar[ind], contador3)
  if ind != len(matrizMostrar) - 1:
    print()
  contador3 += 1

# Canteen Queue FEITO
"""
vezes = int(input())
contador = 0
def trocar(vals, posX, posY):
  temp = vals[posX]
  vals[posX] = vals[posY]
  vals[posY] = temp
  return None
def ordena(valores):
  for tamanho in range(len(valores) - 1, 0, -1):
    for i in range(tamanho):
      if valores[i] < valores[i + 1]:
        trocar(valores, i, i + 1)
  return None

while contador < vezes:
  qtdAlunos = int(input())
  notasAlunos = list(map(int, input().split()))
  comparacao = notasAlunos.copy()
  ordena(notasAlunos)
  mudanca = len(notasAlunos)
  for i in range(len(notasAlunos)):
    if comparacao[i] != notasAlunos[i]:
      mudanca -= 1

  print(mudanca)
  contador += 1
  """

# Even and Odd
"""
vezes = int(input())
contador = 0
arrayPar = []
arrayImpar = []

while contador < vezes:
  num = int(input())
  if num % 2 == 0:
    arrayPar.append(num)
  else:
    arrayImpar.append(num)

  contador += 1

arrayPar.sort()
arrayImpar.sort(reverse=True)
arrayPar += arrayImpar
for num in arrayPar:
  print(num)
"""

# Sort by Length
"""
vezes = int(input())
contador = 0

while contador < vezes:
  linha = input().split()
  linha.sort(key=len, reverse=True)
  linhaMostrar = ""
  for ind in range(len(linha)):
    if ind == len(linha) - 1:
      linhaMostrar += linha[ind]
    else:
      linhaMostrar += linha[ind] + " "
  print(linhaMostrar)


  contador += 1
"""

# Black and White
"""
def trocar(vals, troca, trocado):
  novoArray = vals.copy()
  for i in range(len(novoArray)):
    if novoArray[i] == troca:
      novoArray[i] = trocado
    else:
      novoArray[i] = troca
  return novoArray

# PP
sequencia = input().split()
valores = []

while sequencia != ["*", "*"]:
  jogoInicial = list(sequencia[0])
  jogoFinal = list(sequencia[1])
  qtdMudancas = 0

  qtdNInical = jogoInicial.count("N")
  qtdNFinal = jogoFinal.count("N")

  if jogoInicial == jogoFinal:
    qtdMudancas = 0
    
  else:
    tempArray = trocar(jogoInicial, "B", "N")
    if tempArray == jogoFinal:
      qtdMudancas += 1
    elif qtdNFinal > qtdNInical:
      tempArray2 = trocar(jogoInicial, "N", "N")
      if jogoFinal == tempArray2:
        qtdMudancas += 1
      else:
        for i in range(len(tempArray2)):
          if tempArray2[i] != jogoFinal[i]:
            qtdMudancas += 1
    else:
      for i in range(len(jogoInicial)):
          if jogoInicial[i] != jogoFinal[i]:
            qtdMudancas += 1

  valores.append(qtdMudancas)
  sequencia = input().split()

for i in valores:
  print(i)
"""

# Encryption
"""
# sub
def pulando3Casas(vals):
  novoVals = []
  for ind in range(len(vals)):
    operador = 0
    if ord(vals[ind]) <= 64 or ord(vals[ind]) >= 173 or vals[ind] == " ":
      novoVals.append(vals[ind])
    elif ord(vals[ind]) <= 96 and ord(vals[ind]) >= 91:
      novoVals.append(vals[ind])
    else:
      operador = ord(vals[ind]) + 3
      novoVals.append(chr(operador))
  return novoVals
def pulando1CasaMetade(vals):
  novoCodigo = []
  for ind in range(len(vals)):
    if ind > int(len(vals) / 2) - 1:
      if chr(35) == vals[ind] or ord(vals[ind]) >= 48 and ord(vals[ind]) <= 57 or vals[ind] == " ":
        novoVals.append(vals[ind])
      else:
        operador = ord(vals[ind]) - 1
        novoVals.append(chr(operador))
    else:
      novoVals.append(vals[ind])
  return novoVals

# PP
vezes = int(input())
contador = 0

while contador < vezes:
  mensagem = list(input())
  codificando = pulando3Casas(mensagem)
  codificando.reverse()
  codificando1 = pulando1CasaMetade(codificando)
  mostar = ""
  for car in codificando1:
    mostar += car
  print(mostar)

  contador += 1
"""