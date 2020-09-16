"""
Calcule n! usando o for loop
5! = 5X4X3X2X1 = 120

EXERCICIO 1
n = int(input("Digite o fatorial: "))
m = n + 1
fatorial = 1 

EXERCICIO 2
for i in range(1, m):
	fatorial *= i
print("O resultado é %i."%(fatorial))

EXERCICIO 3
n = 5
for i in range(n, n*11, +5):
	num_t = i * (i+1) // 2
	print("O número triangular de %i é %i."%(n, num_t))
	n += 5

EXERCICIO 4	
Numa eleição existem três candidatos.@
Faça um programa que peça o número total de eleitores.@
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.

candidato 1 --> if voto == 1 --> for i range()
candidato 2 -->
candidato 3 -->

num_t = int(input("Digite o número total de eleitores: "))
voto = int(input("Vote cand1 = 1, cand2 = 2, cand3 = 3: "))

print("Votos cand1 = %i, cand2 = %i, cand3 = %i.")


"""

num_t = int(input("Digite o número total de eleitores: "))


q1 = q2 = q3 = 0
eleitor = 1

for i in range(1, num_t+1):
	voto = int(input("Vote eleitor %i cand1 = 1, cand2 = 2, cand3 = 3: "%(eleitor)))
	if voto == 1:
		q1 += 1
	if voto == 2:
		q2 += 1
	if voto == 3:
		q3 += 1
	eleitor += 1


print("Votos cand1 = %i, cand2 = %i, cand3 = %i."%(q1, q2, q3))