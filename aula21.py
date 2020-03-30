"""
EXERCICIO 1
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    a.	o produto do dobro do primeiro com metade do segundo .
    b.	a soma do triplo do primeiro com o terceiro.
    c.	o terceiro elevado ao cubo.


num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um número real: "))

print("A resposta da questão a é", float((2 * num1) * (num2 / 2.0)))
print("A resposta da questão b é", float((num1 * 3.0) + num3))
print("A resposta da questão c é", float(num3 ** 3.0))


"""

"""
EXERCICIO 2
Faça um Programa que peça um número e
informe se o número é inteiro ou decimal. Se o número for decimal,
arredonde o número
0.4 = 3.4 - 3


num = float(input("Digite um número: "))

if num == int(num):
	print("Esse número é inteiro.")
elif num != int(num):
	print("Esse número é decimal, ele arredondado fica", round(num))
"""
"""
EXERCICIO 3
Dados x real e n natural, calcular uma aproximação para cos x através dos
n primeiros termos da seguinte série:
cos x = 1/1 - (x**2)/2! + (x**4)/4! - (x**6)/6! + ... + ((-1)**k)*(x**2k)/((2k)!)

Compare com os resultados de sua calculadora!

x = float(input("Digite o número de x: "))
n = int(input("Digite o número de n: "))
cosx = 1

for i in range(1, n+1):
	aux = 1
	while aux < i:
		cosx += (-1**i)*(x**(2*i))/((2*i)*aux)
		aux += 1
print(cosx)
"""