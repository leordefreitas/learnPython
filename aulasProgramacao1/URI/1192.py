# 19/11

# sp
def calculaCodigo(palavra):
  val = 0
  if palavra[0] == palavra[2]:
    val = (int(palavra[0]) * int(palavra[2]))
  elif ord(palavra[1]) < 97:
    val = int(palavra[2]) - int(palavra[0])
  else:
    val = int(palavra[0]) + int(palavra[2])
  return val
# pp
vezes = int(input())
contador = 0

while contador < vezes:
  codigo = input()
  valor = calculaCodigo(codigo)
  print(valor)
  contador += 1