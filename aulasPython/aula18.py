"""
EXERCICIO 1
Dados n e n seqüências de números inteiros não-nulos@,
cada qual seguida por um 0,
calcular a soma dos números pares de cada seqüência.

sequencia1
Digite um número: 


s = int(input("Digite o número de sequência: "))
seq = 1

for i in range(s):
	soma = 0
	print("Sequência %i"%(seq))
	n = 1
	while n != 0:
		n = int(input("Digite um número: "))
		if n % 2 == 0:
			soma += n
	print("O resultado da sequência %i é %i."%(seq, soma))
	seq += 1
	i += 1
"""
"""
EXERCICIO 2
Peça para o usuario entrar com o ínicio e o fim da tabuada@
e imprima a tabuada correspondente dentro dos intervalos considerados
Exemplo:
Começo = 1     
Fim = 3

Para o 1:
1X1 = 1
1X2 = 2
1X3 = 3

Para o 2:
2X1 = 2
2X2 = 4
2X3 = 6

Para o 3:
3X1 = 3
3X2 = 6
3X3 = 9

e = int(input("Valor de entrada tabuada: "))
f = int(input("Valor fim da tabuada: "))
print("")
aux_j = aux_i = 0

for j in range(1, f+1):
	
	print("Para o %i:"%(j))
	print("")

	for i in range(e, f+1):
		oper = j * i
		
		print("%iX%i = %i"%(j, i, oper))
"""

"""
EXERCICIO 3
Dados dois naturais m e n determinar, entre todos os pares de números naturais
(x,y) tais que x < m e y < n, um par para o qual o valor da expressão
x*y - x**2 + y seja máximo e calcular também esse máximo.

m=5
n=3

"""

m = int(input("Digite o primeiro número: "))
n = int(input("Digite o segundo número: "))
aux_c = 0

for x in range(m+1):

	for y in range(n+1):
		calc = (x * y) - (x ** 2) + y
		
		if calc > aux_c:
			aux_c = calc
	

print("O maior resultado é %i com os números %i e %i."%(aux_c, x, y))

