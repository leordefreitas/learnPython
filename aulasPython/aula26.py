"""
EXERCICIO 1
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []
for i in range(1, 6):
	vetor = int(input("Digite o vetor %i de 5: "%(i)))
	lista.append(vetor)
print(lista)
"""
"""
EXERCICIO 2
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

medio = 0
lista = []
for i in range(1, 5):
	nota = float(input("Digite a nota %i de 4: "%(i)))
	medio += nota
	lista.append(nota)
print(lista, " e a média é %.2g."%(medio/4))
"""
"""
EXERCICIO 3
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os dois vetores.
"""
lpar = []
limpar = []

for i in range(1, 20):
	num = int(input("Digite o número %i de 20:"%(i)))
	if num == 0 or num % 2 == 0:
		lpar.append(num)
	else:
		limpar.append(num)
print("A lista par é composta pelos seguintes números: ", lpar)
print("A lista ímpar é composta pelos seguintes números: ", limpar)