"""
exercicio 1
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

o	Fatorial de: 5
o	5! =  5 . 4 . 3 . 2 . 1 = 120


num = int(input("Fatorial de: "))
fatorial = 1
linha2 = str()
for i in range(num-1, 0, -1):
    fatorial *= i
    linha2 += " . " + str(i)
print(str(num) + "! = " + str(num) + linha2 + " = " + str(num * fatorial))
"""

