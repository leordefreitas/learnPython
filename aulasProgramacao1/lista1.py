# exercicio, Interval 2
"""
qtd = int(input())

contador = 0
dentro = 0
fora = 0

while contador < qtd:
  num = int(input())

  if num >= 10 and num <= 20:
    dentro += 1

  elif num < 10 or num > 20:
    fora += 1
  
  contador += 1

print("%i in" %(dentro))
print("%i out" %(fora))
"""

# exercicio, Score Validation
"""
contadorValido = 0
somaNota = 0

while contadorValido < 2:
  nota = float(input())

  if nota < 0 or nota > 10:
    print("nota invalida")
  else:
    contadorValido += 1
    somaNota += nota

media = somaNota / 2
print("media = %.2f" %(media))
"""

# exercicio, Divisors I
"""
num = int(input())
num1 = num + 1
contador = 1

while contador < num1:
  resto = num % contador 

  if resto == 0:
    print(contador)

  contador += 1
"""

# exercicio, Array Replacement I
"""
contador = 0
while contador < 10:
  num = int(input())

  if num <= 0:
    num = 1
  
  print("X[%i] = %i" %(contador + 1, num))

  contador += 1
"""

# exercicio, Array fill I

num = int(input())
contador = 0
multiplicacao = num
array = []

if num < 50:
  while contador < 10:
    print("N[%i] = %i" %(contador, multiplicacao))
    multiplicacao *= 2
    contador += 1
