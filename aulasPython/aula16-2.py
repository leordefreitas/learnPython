"""
 Dados n e uma seqüência de n números inteiros, determinar o comprimento de
 um segmento crescente de comprimento máximo.

Exemplos:
Na seqüência   5,  10,  3,  2,  4,  7,  9,  8,  5
o comprimento do segmento crescente máximo é 4.

Na seqüência   10,  8,  7,  5,  2
o comprimento de um segmento crescente máximo é 1.
"""

# 5,  10,  3,  2,  4,  7,  9,  8,  5

#ant = 5
#seg = 1
#segMAX = 1
#--------------------------------
#prox = 10
#10 > 5 --> seg + 1
#--------------------------------
#ant = 10
#prox = 3
#3 > 10 --> parou
# --> seg > segMAX --> segMAX = seg => seg = 1

#--------------------------------
#ant = 3
#prox = 2
# 2 > 3 --> parou
# --> seg > segMAX --> seg = 1
#-*- coding: utf-8 -*-

n = int(input("Digite a quantidade de números: "))
m = int(input("Digite o 1 número: "))
seg = a = cont = segMAX = 1                       #cont é apenas para rodar o while

while cont < n:
	prox = int(input("Digite o %i número: "%(cont+1)))
	if prox > m:
		seg += 1
	else:
		seg = 1
	if seg > segMAX:
		segMAX = seg
	cont += 1
print("O maior sequência de segmentos é ", segMAX)



