# -*- coding: utf-8 -*-

n = int(input("Digite o número de pessoas: "))
m = 1
while m <= n:

	a = int(input("Digite o dia de nascimento da pessoa %i: "%(m)))
	b = int(input("Digite o mês de nascimento da pessoa %i: "%(m)))
	c = int(input("Digite o ano de nascimento da pessoa %i: "%(m)))
	d = int(input("Idade desejada da pessoa %i: "%(m)))
	print("A pessoa %i fará %i anos na data %i/%i/%i." %( m, d, a, b, c+d))
	m += 1

