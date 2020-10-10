# Sudoku
"""
vetor=[]
teste = int(input())
for a in range(teste) :
    falso=False
    matriz=[]
    for i in range(9) :
        matriz.append(list(map(int,input().split(" "))))
    for linha in matriz :
        for coluna in linha :
            if linha.count(coluna)>1 : falso=True
    for i in range(9) :
        x=[]
        for linha in matriz :
            if not(linha[i] in x) : x.append(linha[i])
        if len(x)!=9 :
            falso=True
    for linham in range(0,9,3) :
        x1=[]
        x2=[]
        x3=[]
        for linha in range(linham,linham+3) :
            for colunam in range(0,9,3) :
                for coluna in range(colunam,colunam+3) :
                    if colunam==0 :
                        if not(matriz[linha][coluna] in x1) : x1.append(matriz[linha][coluna])
                    if colunam==3 :
                        if not(matriz[linha][coluna] in x2) : x2.append(matriz[linha][coluna])
                    if colunam==6 :
                        if not(matriz[linha][coluna] in x3) : x3.append(matriz[linha][coluna])
        if len(x2)!=9 : falso=True
        if len(x3)!=9 : falso=True
        if len(x1)!=9 : falso=True
    vetor.append([])
    vetor[-1].append("Instancia " + str(a+1))
    if falso : vetor[-1].append("NAO")
    else : vetor[-1].append("SIM")
for i in vetor :
    print(i[0])
    print(i[1])
    print()
"""

# Square Matrix III
"""
number = int(input())
array1 = [0] * number
array2 = [0] * number

while number != 0:
 
  valorAlterando1 = 1
  for x in range(len(array1)):
    array2 = [0] * number
    valorAlterando2 = 1
    for y in range(len(array2)):
      if y == 0:
        array2[y] = valorAlterando1
      else:
        array2[y] = valorAlterando2
      valorAlterando2 *= 2
    valorAlterando1 *= 2
    array1[x] = array2
    

  print(array1)
  print()
  

  number = int(input())
  array1 = [0] * number
  array2 = [0] * number
"""

# Matrix of Squares
"""
qtdMatrizes = int(input())
tamanhoMatriz = int(input())
array = []

for i in range(tamanhoMatriz):
  num = input().split()
  for i in num:
    num[index(i)] = int(i)
"""

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