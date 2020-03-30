"""
Dado um numero n de empresas, e um numero m de meses,
e o ganho e gastos positivos e inteiros de cada empresa para cada mes,
imprimir se a empresa nesses meses ficou com défict, lucro ou indiferente e
imprimir o valor correspondente a essa balança

Exemplo de Execução:

Digite o numero de empresas: 3
Digite o numero de meses: 2

Empresa 1:
Mes 1:
Digite o ganho da empresa no mes: 500
Digite o gasto da empresa no mes: 500

Mes 2:
Digite o ganho da empresa no mes: 600
Digite o gasto da empresa no mes: 600

A empresa 1 ficou indiferente(balança = R$ 0)

Empresa 2:
Mes 1:
Digite o ganho da empresa no mes: 500
Digite o gasto da empresa no mes: 600

Mes 2:
Digite o ganho da empresa no mes: 800
Digite o gasto da empresa no mes: 1000

A empresa 2 fechou com défict de R$ -300

Empresa 3 :
Mes 1 :
Digite o ganho da empresa no mes: 800
Digite o gasto da empresa no mes: 500

Mes 2 :
Digite o ganho da empresa no mes: 1100
Digite o gasto da empresa no mes: 1000

A empresa 3 fechou com lucro de R$ 400
"""
#-*- coding: utf-8 -*-

print("----- PROGRAMA PARA EMPRESAS -----")
print("")
n = int(input("Digite o numero de empresas: "))
m = int(input("Digite o numero de meses: "))

empresa = 1
print("")
while empresa <= n:
	mes = 1
	print("Empresa ", empresa)
	while mes <= m:
		print("Mês ", mes)
		print("")
		ganho = int(input("Digite o ganho da empresa no mes: "))
		gasto = int(input("Digite o gasto da empresa no mes: "))
		balanco = ganho - gasto)
		mes = mes + 1
		print("")

		if balanco > 0:
			print("A empresa", empresa, "fechou com lucro de R$ ", balanco)
		elif balanco == 0:
			print("A empresa", empresa, " ficou indiferente")
		else:
			print("A empresa", empresa,"fechou com défict de R$ ", balanco)
		print("")
	empresa = empresa + 1


