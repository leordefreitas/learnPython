# Q3

# Subprograma

def puxandoDoArquivo(nome):
  dados = open(nome, "r")
  linha = dados.readline()
  numeros = []

  while linha != "":
    arrayLinhas = linha.split()

    for i in range(len(arrayLinhas)):
      if "\n" in arrayLinhas[i]:
        for i in range(0, len("\n")):
          arrayLinhas[i] = arrayLinhas[i].replace("\n", "")
          numeros.append(arrayLinhas[i])
      else:
          numeros.append(arrayLinhas[i])

    linha = dados.readline()

  dados.close()
  return numeros

def substituindoPorZero(vals):
  arraySubstituido = [] + vals

  for i in range(len(arraySubstituido)):
    if primo(arraySubstituido[i]) == True:
      arraySubstituido[i] = 0

  return arraySubstituido

def imprime(vals):
  for index in range(len(vals)):
    print("%4d" %(int(vals[index])), end=" ")
    if index%10 == 0 and index != 0:
      print()
      
  return None

def primo(num):
  numero = int(num)
  for divisor in range(2, 1 + int(numero**0.5)):
    if numero % divisor == 0:
      return False

  return numero > 1

# Programa Principal

nomeArquivo = input("Digite o nome do arquivo: ")
valores = puxandoDoArquivo(nomeArquivo)
print("\n----------TODOS OS NUMEROS------------")
imprime(valores)
valoresSubstituidos = substituindoPorZero(valores)
print("\n\n----------PRIMOS TROCADOS POR 0------------")
imprime(valoresSubstituidos)