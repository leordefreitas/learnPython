# Dia 16/09/20

"""
a = int(input())
b = int(input())
c = int(input())

if a >= b + c or b >= a + c or c >= a + b:
  print("Nao pode ser um triangulo!!??!?!?!?!") 
elif a == b == c:
  print("Triangulo equilatero!!!")
elif a == b or c == b or b == c:
  print("Triangulo isoceles!!!")
else:
  print("Triangulo escaleno")
 """

""" array = []

for aluno in range(21):
  nome = input().split(" ")
  array.append(nome[0])

print(array) """


n = int(input())

ano = 0
meses = 0
dias = 0

while n > 0:
  dias += 1

  if dias == 30:
    meses += 1
    dias = 0
    if meses == 12:
      ano += 1
      meses = 0

  n -= 1

print("%i ano(s)\n%i mes(es)\n%i dia(s)" %(ano, meses, dias))