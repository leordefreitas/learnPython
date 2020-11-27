# Q1

# Subprograma
def comparandoPalavras(arquivo):
  vals = open(arquivo, "r")

  arrayQtdEPalavras = []

  linha = vals.readline()
  while linha != "":
    arrayLinha = linha.split(" ")
    for pos in range(len(arrayLinha)):
      manuseio = True
    
      for i in range(len(arrayQtdEPalavras)):

        if arrayLinha[pos] in arrayQtdEPalavras[i]:
          arrayQtdEPalavras[i][1] += 1
          manuseio = False

      if manuseio == True:
        arrayQtdEPalavras.append([arrayLinha[pos], 1])


    linha = vals.readline()

  vals.close()
  return arrayQtdEPalavras

def imprimeFinal(vals):
  valorMaior = []

  if vals == []:
    print("VAZIO – Nenhuma!!!")

  else:
    valorMaior.append(vals[0])
    for i in range(len(vals)):
      if vals[i][1] > valorMaior[0][1]:
        valorMaior = []
        valorMaior.append(vals[i])
      elif vals[i][1] == valorMaior[0][1] and vals[i][0] != valorMaior[0][0]:
        valorMaior.append(vals[i])
    
    for ii in range(len(valorMaior)):
      
      print("\nA palavra que mais aconteceu foi a %s - %i vezes." %(valorMaior[ii][0], valorMaior[ii][1]))

  return None
  

# Programa Principal

nomeArquivo = input("Digite o nome de arquivo: ")

qtdPalavras = comparandoPalavras(nomeArquivo)
imprimeFinal(qtdPalavras)