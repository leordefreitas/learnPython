"""
Dados n e uma seqüência de n números inteiros, determinar quantos segmentos
de números iguais consecutivos compõem essa seqüência.

Exemplo: A seguinte seqüência é formada por 5 segmentos de números iguais:
5,  2,  2,  3,  4,  4,  4,  4,  1,  1 
"""

#ant = 5
#seg = 1
#n = 10
#cont = 0
#-----------------------------------------
#prox = 2
#ant == prox -->
#ant != prox --> seg += 1
#ant = prox = 2
#--------------------------------------
#ant = 2
#prox = 2
#ant == prox
#ant = prox
#-------------------------------------

#-*- coding: utf-8 -*-

n = int(input("Digite o tamanho da sequência: "))
ant = int(input("Digite o número 1: "))
seg = 1
num = 2
cont = 1    # cont é para fazer o while rodar

while cont < n:
	prox = int(input("Digite o número %i: "%(num)))
	if ant != prox:
		seg += 1
	ant = prox
	num += 1
	cont += 1
print("A quantidade de números diferentes é %i. "%(seg))

