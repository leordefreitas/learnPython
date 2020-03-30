"""
EXERCICIO 1
O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia um conjunto indeterminado de temperaturas, e informe
ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.

7, 5, 3524, 5, 5, 7, 67, 2, 78

num = int(input("Digite a quantidade de temperaturas: "))
temp = float(input("Digite a temperatura 1: "))
maior = menor = media = temp

for i in range(2, num+1):
	temp = float(input("Digite a temperatura %i: "%(i)))
	if temp > maior:
		maior = temp
	if temp < menor:
		menor = temp
	media += temp
print("A maior temperatura é %.2f e a menor é %.2f e a média é %.2f."%(maior, menor, (media/num)))
"""
"""
EXERCICIO 2
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.

turmas = int(input("Quantidades de turmas: "))
media = 0
for i in range(1, turmas+1):
	alunos = int(input("Quantidade de alunos para a turma %i: "%(i)))
	while alunos > 40 or alunos < 0:
		print("Número de alunos inválido.")
		alunos = int(input("Quantidade de alunos para a turma %i: "%(i)))
	media += alunos
print("A média de alunos por turma é %.2f."%(media/turmas))
"""
"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os
reajustes.

o	Faça um programa que recebe o salário de um colaborador e o
        reajuste segundo o seguinte critério, baseado no salário atual:

o	salários até R$ 280,00 (incluindo) : aumento de 20%
o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o	salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o	o salário antes do reajuste;
o	o percentual de aumento aplicado;
o	o valor do aumento;
o	o novo salário, após o aumento.

sal = float(input("Digite o salário: "))
aum20 = sal*0.20
aum15 = sal*0.15
aum10 = sal*0.10
aum5 = sal*0.05
salfinal = 0

if sal <= 280:
	salfinal = sal+(aum20)
	print("O salário incial é %.2f, o percentual de aumento é de 20, o valor de aumento é %.2f o novo salário é %.2f."%(sal, aum20, salfinal))
if sal > 280 and sal <=700:
	salfinal = sal+(aum15)
	print("O salário incial é %.2f, o percentual de aumento é de 15, o valor de aumento é %.2f o novo salário é %.2f."%(sal, aum15, salfinal))
if sal > 700 and sal <=1500:
	salfinal = sal+(aum10)
	print("O salário incial é %.2f, o percentual de aumento é de 10, o valor de aumento é %.2f o novo salário é %.2f."%(sal, aum10, salfinal))
if sal > 1500:
	salfinal = sal+(aum5)
	print("O salário incial é %.2f, o percentual de aumento é de 5, o valor de aumento é %.2f o novo salário é %.2f."%(sal, aum5, salfinal))
"""
"""
EXERCICIOS 3
Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua
altura em metros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com
suas alturas.
"""
cont = 2
aux = 1
maior = menor = alt = float(input("Digite a altura do aluno 1: "))


for i in range(2, cont+1):
	if alt > maior:
		maior = alt
		num1 = aux
	if alt < menor:
		menor = alt
		num2 = aux
	aux += 1
	alt = float(input("Digite a altura do aluno %i: "%(i)))

print("O aluno %i com altura %.2f é o mais baixo e o aluno %i com altura %.2f é o mais alto."%(num2, menor, num1, maior))




