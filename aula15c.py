"""
Dizemos que um inteiro positivo n é perfeito se for igual à soma de
seus divisores positivos diferentes de n.

Exemplo: 6 é perfeito, pois 1+2+3 = 6.
       Dado um inteiro positivo n, verificar se n é perfeito.
"""

n = int(input("Digite um número: "))
cont, soma = 2 ,1
while cont < n:
	if n % cont == 0:
		soma += cont
	cont += 1
if soma == 0:
	print("O número %i é perfeito."%(n))
else:
	print("O número %i não é perfeito."%(n))
