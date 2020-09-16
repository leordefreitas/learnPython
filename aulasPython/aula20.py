"""
EXERCICO 1
Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

 .	A mensagem "Aprovado", se a média for maior ou igual a 7,
        com a respectiva média alcançada;

a.	A mensagem "Reprovado", se a média for menor do que 7,
        com a respectiva média alcançada;

b.	A mensagem "Aprovado com Distinção", se a média for igual a 10.
nota1 = float(input("Digite a 1 nota: "))
nota2 = float(input("Digite a 2 nota: "))
nota3 = float(input("Digite a 3 nota: "))

media = (nota1 + nota2 + nota3) // 3

if media == 10:
	print("Aprovado com Distinção, media %i."%(media))
elif media >= 7:
	print("Aprovado, media %i."%(media))
else:
	print("Reprovado, media %i."%(media))
"""
"""
EXERCICO 2
Dado um inteiro positivo n, calcular e imprimir o valor da seguinte soma:
    S = 1/n + 2/(n-1) + 3/(n-2) + ... + n/1

n = int(input("Digite o valor de n: "))
soma = 0.0
for i in range(1, n + 1):
	soma += i / (n - i + 1)
print("O valor da soma é %i."%(soma))
"""
"""
EXERCICIO 3
Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.	


alt = float(input("Digite a sua altura: "))
sexo = input("Digite seu sexo(m/f): ")
aux = 0
if sexo == "m":
	aux = (70.7*alt) - 58
	print(aux)
elif sexo == "f":
	aux = (62.1*alt) - 44.7
	print(aux)
"""
"""
EXERCICIO 4
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer
as consistências, informando ao usuário nas seguintes situações:

    a.	Se o usuário informar o valor de A igual a zero, a equação não é do
    segundo grau e o programa não deve fazer pedir os demais valores,
    sendo encerrado;

    b.	Se o delta calculado for negativo, a equação não possui raizes reais.
    Informe ao usuário e encerre o programa;

    c.	Se o delta calculado for igual a zero a equação possui apenas uma raiz
    real; informe-a ao usuário;

    d.	Se o delta for positivo, a equação possui duas raiz reais; informe-as
    ao usuário;

delta = b**2 - 4*a*c
raiz = (-b +ou-(delta**(1/2)))/(2*a)

"""

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
delta = b**2.0 - 4.0*a*c

if a == 0:
	print("Essa equação não é de segundo grau.")
x1 = (-b+((b**2.0 - 4.0*a*c)**1.0/2.0)) / (2.0*a)
x2 = (-b-((b**2.0 - 4.0*a*c)**1.0/2.0)) / (2.0*a)
if delta == 0:
	print("As raízes são %i e %i sendo que essa equação não possui raízes reais."%(x1, x2))
elif (-b+((b**2.0 - 4.0*a*c)**1.0/2.0)) / (2.0*a) == 0 or (-b-((b**2.0 - 4.0*a*c)**1.0/2.0)) / (2.0*a) == 0:
	print("As raízes são %i e %i sendo que essa equação possui apenas uma raiz real."%(x1, x2))
elif delta > 0:
	print("As raízes são %i e %i sendo que essa equação possui duas raízes reais."%(x1, x2))
else:
	print("As raízes são %i e %i."%(x1, x2))