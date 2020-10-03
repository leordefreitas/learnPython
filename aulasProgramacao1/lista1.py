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
  
  print("X[%i] = %i" %(contador, num))

  contador += 1
"""

# exercicio, Array fill I
"""
num = int(input())
contador = 0
multiplicacao = num
array = []

if num < 50:
  while contador < 10:
    print("N[%i] = %i" %(contador, multiplicacao))
    multiplicacao *= 2
    contador += 1
"""

# exercicio, Array change I
"""
array = []
count = 0

while count < 20:
  num = int(input())

  array.insert(0, num)
  count += 1

count1 = 0
for j in array:
  print("N[%i] = %i" %(count1, j))
  count1 += 1 
"""

# exercicio, Column in Array
"""
line = int(input())
ope = input()

arrayLine = []
arrayFull = []

soma = 0
count = 0
while count < 12:
  count1 = 0
  while count1 < 12:
    num = float(input())
    arrayLine.append(num)

    count1 += 1

  arrayFull.append(arrayLine)
  arrayLine = []
  count += 1

for i in arrayFull[line]:
  soma += i

if ope == "S":
  print("%.1f" %(soma))
elif ope == "M":
  print("%.1f" %(soma/12))
"""
# exercicio, Welcome to the Winter!


n = list(map(int, input().split(" ")))

if n[0] > n[1] and n[1] <= n[2]:
  print(":)")

elif n[0] < n[1] and n[1] >= n[2]:
  print(":(")

elif n[0] < n[1] and n[1] < n[2] and (n[1] - n[0]) > (n[2] - n[1]):
  print(":(")

elif n[0] < n[1] and n[1] < n[2] and (n[1] - n[0]) <= (n[2] - n[1]):
  print(":)")

elif n[0] > n[1] and n[1] > n[2] and (n[0] - n[1]) > (n[1] - n[2]):
  print(":)")

elif n[0] > n[1] and n[1] > n[2] and (n[0] - n[1]) <= (n[1] - n[2]):
  print(":(")

elif n[0] == n[1] and n[1] < n[2]:
  print(":)")

elif n[0] == n[1] and n[1] > n[2]:
  print(":(")



# exercicio, Fast Fibonacci
"""
def Fibonacci(num):
  valor = ((((1 + (5**0.5)) / 2)**num - ((1 - (5**0.5)) / 2)**num)) / (5**0.5)
  return valor

numero = int(input())
print("%.1f" %(Fibonacci(numero)))
"""
# exercicio, Above the Main Diagonal !!!!!!!!!!!!!!!!!!!!!!!!
"""
ope = input()

arrayLine = []
arrayFull = []

soma = 0
count = 0
while count < 12:
  count1 = 0
  while count1 < 12:
    num = float(input())
    arrayLine.append(num)

    count1 += 1

  arrayFull.append(arrayLine)
  arrayLine = []
  count += 1

for i in arrayFull:
  arrayLineLen = len(arrayLine)
  for


if ope == "S":
  print("%.1f" %(soma))
elif ope == "M":
  print("%.1f" %(soma/12))
"""

# exercicio, Banknotes
"""
newValue = int(input())
value = newValue

n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

while value > 0:
  if value >= 100:
    value -= 100
    n100 += 1
  elif value >= 50:
    value -= 50
    n50 += 1
  elif value >= 20:
    value -= 20
    n20 += 1
  elif value >= 10:
    value -= 10
    n10 += 1
  elif value >= 5:
    value -= 5
    n5 += 1
  elif value >= 2:
    value -= 2
    n2 += 1
  elif value >= 1:
    value -= 1
    n1 += 1

print(newValue, end="\n")
print("%i nota(s) de R$ 100,00" %(n100), end="\n")
print("%i nota(s) de R$ 50,00" %(n50), end="\n")
print("%i nota(s) de R$ 20,00" %(n20), end="\n")
print("%i nota(s) de R$ 10,00" %(n10), end="\n")
print("%i nota(s) de R$ 5,00" %(n5), end="\n")
print("%i nota(s) de R$ 2,00" %(n2), end="\n")
print("%i nota(s) de R$ 1,00" %(n1), end="\n")
"""

# exercicio, Array Selection I
"""
count = 0

while count < 100:
  num = float(input())
  if num <= 10:
    print("A[%.0f] = %.1f" %(count, num))
  
  count += 1
"""
  
# exercicio, Game Time with Minutes
"""
def transEmNumeral(num1, num2):
  valor = (num1 * 60) + num2
  return valor

def tempo(m):
  horas = minutos = 0

  while m > 0:
    if m >= 60:
      horas += 1
      m -= 60
    else:
      minutos = m
      m = 0

  return [horas, minutos]

num = list(map(int, input().split(" ")))

start = [num[0], num[1]]
end = [num[2], num[3]]
duration = 0

if start[0] == end[0] and start[1] == end[1]:
  duration = 1440

elif start[0] == end[0] and start[1] > end[1]:
  duration = (transEmNumeral(end[0], end[1]) + 1440) - transEmNumeral(start[0], start[1])

elif start[0] > end[0]:
  duration = (transEmNumeral(end[0], end[1]) + 1440) - transEmNumeral(start[0], start[1])

else:
  duration = transEmNumeral(end[0], end[1]) - transEmNumeral(start[0], start[1])

resultado = tempo(duration)

print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(resultado[0], resultado[1]))
"""

# exercicio, Number Frequence
"""
vezes = int(input())
count = 0
arrayTodos = []
arrayDiferente = []

while count < vezes:
  numero = int(input())
  
  if numero not in arrayTodos:
    arrayDiferente.append(numero)
    arrayTodos.append(numero)
  else:
    arrayTodos.append(numero)

  count += 1

mostrarNum = sorted(arrayDiferente)

for i in mostrarNum:
  quantasVezes = arrayTodos.count(i)
  print("%i aparece %i vez(es)" %(i, quantasVezes))
"""

# exercicio, Fibonacci Array
"""
def Fibonacci(num):
  valor = ((((1 + (5**0.5)) / 2)**num - ((1 - (5**0.5)) / 2)**num)) / (5**0.5)
  return valor

vezes = int(input())
count = 0
array = []

while count < vezes:
  num = int(input())
  if num >= 0 and num <= 60:
    print("Fib(%i) = %i" %(num, Fibonacci(num)))

  count += 1
"""

# exercicio, Array Fill IV
"""
count = 0
par = []
impar = []

while count < 15:
  num = int(input())

  # PAR
  if num % 2 == 0:
    par.append(num)

    if len(par) >= 5:
      acres = 0

      for i in par:
        print("par[%i] = %i" %(acres, i))
        acres += 1

      par = []

  # IMPAR
  elif num % 2 != 0:
    impar.append(num)
    
    if len(impar) >= 5:
      acres = 0

      for i in impar:
        print("impar[%i] = %i" %(acres, i))
        acres += 1

      impar = []

  count += 1
  
a1 = a2 = 0

for i in impar:
  print("impar[%i] = %i" %(a1, i))
  a1 += 1

for i in par:
  print("par[%i] = %i" %(a2, i))
  a2 += 1
"""

# exercicio, Lowest Number and Position
"""
vezes = int(input())

array = input().split(" ")
numero = []

for i in array:
  numero.append(int(i)) 

menorNumero = numero[0]

for i in numero:
  if i < menorNumero:
    menorNumero = i


print("Menor valor: %i" %(menorNumero))
print("Posicao: %i" %(numero.index(menorNumero)))
"""