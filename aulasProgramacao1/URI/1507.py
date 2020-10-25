# SUBSEQUENCIAS
# sub
def comparando(palavra, palavraASerComparada):
  if palavra in palavraASerComparada:
    print("Yes")
  else:
    print("No")
  return None
# pp
vezes = int(input())
contador = 0

while contador < vezes:
  sequeciaCaracteres = input()

  qtdSubsequecias = int(input())
  contador1 = 0
  while contador1 < qtdSubsequecias:
    caracteresComparar = input()
    comparando(caracteresComparar, sequeciaCaracteres)
    contador1 += 1
    
  contador += 1