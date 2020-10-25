# LED
# sub
def separadorLetras(numerosEntrada):
  arrayNumeros = []
  for num in numerosEntrada:
    arrayNumeros.append(int(num))
  return arrayNumeros
def contandoLeds(array, tabelaComparar):
  soma = 0
  for num in array:
    soma += tabelaComparar[num]
  return soma
def imprime(valor):
  print("%i leds" %(valor))
  return None
# pp
qtdLeds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
vezes = int(input())
contador = 0
while contador < vezes:
  placaLed = input()
  numeros = separadorLetras(placaLed)
  totalLeds = contandoLeds(numeros, qtdLeds)
  imprime(totalLeds)

  contador += 1