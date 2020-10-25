# COMBINADOR
# sub
def organizador(palavra1, palavra2):
  palavraFinal = ""

  menor = palavra1
  maior = palavra2
  if len(palavra2) < len(palavra1):
    menor = palavra2
    maior = palavra1
  

  for index in range(len(menor)):
    palavraFinal += palavra1[index]
    palavraFinal += palavra2[index]

  resto = slice(len(menor), len(maior))
  palavraFinal += maior[resto]

  return palavraFinal
# pp
vezes = int(input())
contador = 0

while contador < vezes:
  palavras = input().split()
  palavrasOrganizada = organizador(palavras[0], palavras[1])
  print(palavrasOrganizada)
  contador += 1



