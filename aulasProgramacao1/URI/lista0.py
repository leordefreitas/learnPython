# A = int(input(""))
# B = int(input(""))
# X = A + B

# print("X =", X, end="\n")

""" r = float(input(""))
n = 3.14159
a = n * r**2

print("A=%.4f" %(a), end="\n") """

""" a = float(input(""))
b = float(input(""))
if a >= 0 and a <= 10:
  if b >= 0 and b <= 10:
    media = ((3.5 * a) + (7.5 * b)) / 11
    print("MEDIA = %.5f" %(media), end="\n")
     """

""" a = int(input(""))
b = int(input(""))
c = int(input(""))
d = int(input(""))
calc = (a * b) - (c * d)
print("DIFERENCA =", calc) """

""" num = int(input(""))
hours = int(input(""))
value = float(input(""))
salary = value * hours

print("NUMB'  ER =", num, end="\n")
print("SALARY = U$ %.2f" %(salary), end="\n") """

""" x = int(input(""))
y = float(input(""))
spent = x / y

print("%.3f km/l" %(spent)) """

""" n = int(input(""))
hours = 0
minutes = 0
seconds = 0

while n > 0:
  seconds += 1

  if seconds == 60:
    minutes += 1
    seconds = 0
    if minutes == 60:
      hours += 1
      minutes = 0

  n -= 1

print("%i:%i:%i" %(hours, minutes, seconds))

 """

""" num1 = input("").split(" ")
num2 = input("").split(" ")
x1 = float(num1[0])
y1 = float(num1[1])
x2 = float(num2[0])
y2 = float(num2[1])

distance = (((x2 - x1)**2) + ((y2 - y1)**2)) ** (1/2)

print("%.4f" %(distance)) """

""" distance = int(input(""))

minutes = distance * 2

print("%i minutos" %(minutes)) """

""" n = int(input())

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
      dias = -5

  n -= 1

print("%i ano(s)\n%i mes(es)\n%i dia(s)" %(ano, meses, dias)) """

""" salary = float(input(""))
percentual = 0
earned = 0

if salary >= 0 and salary <= 400:
  percentual = 0.15
  earned = salary * percentual
elif salary >= 400.01 and salary <= 800:
  percentual = 0.12
  earned = salary * percentual
elif salary >= 800.01 and salary <= 1200:
  percentual = 0.10
  earned = salary * percentual
elif salary >= 1200.01 and salary <= 2000:
  percentual = 0.07
  earned = salary * percentual
elif salary > 2000:
  percentual = 0.04
  earned = salary * percentual

new_salary = salary + earned
percentual = int(percentual * 100)

print("Novo salario: %.2f" %(new_salary))
print("Reajuste ganho: %.2f" %(earned))
print("Em percentual: %i %%" %(percentual)) """

""" number = int(input(""))

if number == 61:
  print("Brasilia")
elif number == 71:
  print("Salvador")
elif number == 11:
  print("Sao Paulo")
elif number == 21:
  print("Rio de Janeiro")
elif number == 32:
  print("Juiz de Fora")
elif number == 19:
  print("Campinas")
elif number == 27:
  print("Vitoria")
elif number == 31:
  print("Belo Horizonte")
else:
  print("DDD nao cadastrado")
 """
""" 
x = 1
while x <= 100:
  operator = x % 2
  if operator == 0:
    print(x)
  x += 1
 """

""" number = int(input("")) 

x = 1
while x <= number:
  operator = x % 2
  if operator != 0:
    print(x)
  x += 1 """
"""
num1 = int(input(""))
num2 = int(input(""))

if num1 > num2:
  soma = 0 
  num2 += 1
  while num2 < num1:
    operator = num2 % 2
    if operator != 0:
      soma += num2
    num2 += 1
  print(soma)

elif num2 > num1:
  soma = 0
  num1 += 1
  while num1 < num2:
    operator = num1 % 2
    if operator != 0:
      soma += num1
    num1 += 1
  print(soma)

elif num1 == num2:
  print(0)
"""

# times = int(input(""))

# if times != 0:
#   result = input("").split(" ")

"""
done = []
case = 1

while case == 1:
  times = int(input(""))

  if times == 0:
    break

  result = input("").split(" ")

  cont_mary = 0
  cont_john = 0
  for num in result:

    if num == "0":
      cont_mary += 1

    elif num == "1":
      cont_john += 1

  done.append("Mary won %i times and John won %i times" %(cont_mary, cont_john))

for frase in done:
  print(frase)

 """

""" outlets = input("").split(" ")
new_outlets = []

for num in outlets:
  new_outlets.append(int(num))

count = 0
sum_all = 0

for num in new_outlets:
  if count == 3:
    sum_all += num
  else:
    sum_all += (num - 1)

  count += 1

print(sum_all) """

"""
i = input("").split(" ")

new_i = []
for n in i:
  new_i.append(int(n))

value = 0.0
if new_i[0] == 1:
  value = 4 * new_i[1]
elif new_i[0] == 2:
  value = 4.5 * new_i[1]
elif new_i[0] == 3:
  value = 5 * new_i[1]
elif new_i[0] == 4:
  value = 2 * new_i[1]
elif new_i[0] == 5:
  value = 1.5 * new_i[1]

print("Total: R$ %.2f" %(value))
"""

i = input("").split(" ")

new_i = []
for n in i:
  new_i.append(float(n))

new_i[0] *= 2
new_i[1] *= 3
new_i[2] *= 4

soma = 0
for n in new_i:
  soma += n

media = soma / 10

# 7 ou acima
if media >= 7:
  print("Media: %.1f" %(media))
  print("Aluno aprovado.")

# 5 ou abaixo
if media < 5:
  print("Media: %.1f" %(media))
  print("Aluno reprovado.")

# aluno exame
if media >= 5 and media <= 6.9:
  print("Media: %.1f" %(media))
  print("Aluno em exame.")

  nota_exame = float(input(""))
  print("Nota do exame: %.1f" %(nota_exame))
  
  new_media = (nota_exame + media) / 2

  if new_media >= 5:
    print("Aluno aprovado.")
  elif new_media < 5:
    print("Aluno reprovado.")

  print("Media final: %.1f" %(new_media))


