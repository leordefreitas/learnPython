"""
Queremos números naturais que sejam produtos de três
números consecutivos

Exemplo: 120 é procurado, pois 4.5.6 == 120.
Dado um inteiro não-negativo n, verificar se n é procurado.
"""
#40 ?
# 1 X 2 X 3 == 6
# 2 X 3 X 4 == 24
# 3 X 4 X 5 == 60

#120
# 1 X 2 X 3 == 6
# 2 X 3 X 4 == 24
# 3 X 4 X 5 == 60
# 4 X 5 X 6 == 120
# -*- coding: utf-8 -*-

num = int(input("Digite um número: "))

i = 1
j = 2
k = 3
while i * j * k < num:
	i += 1
	j += 1
	k += 1

if i * j * k == num:
	print("O %i é prucurado" %(num))
else:
	print("O %i não é procurado" %(num))


