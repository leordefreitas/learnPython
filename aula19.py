"""
EXERCICIO 1
Dados três números naturais,
verificar se eles formam os lados de um triângulo retângulo.

lado1**2 + lado2**2 == lado3**2
lado3**2 + lado1**2 == lado2**2
lado2**2 + lado3**2 == lado1**2

lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1**2 + lado2**2 == lado3**2 or lado3**2 + lado1**2 == lado2**2 or lado2**2 + lado3**2 == lado1**2:
	print("O triângulo é retângulo.")
else:
	print("O triângulo não é retângulo.")

"""
"""
EXERCICIO 2
Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de
divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados.



n = int(input("Digite um número: "))

div = 0
for i in range(1, n+1):
	primo = True
	j = 2
	
	while j < i and primo:
		div += 1
		if i % j == 0:
			primo = False
		j += 1
		
		

	if primo:
		print(i)

print("A quantidade de divisões é %i."%(div))
"""
"""
EXERCICIO 3
Dados n e dois números inteiros positivos i e j diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou
de j e ou de ambos.

Exemplo: Para n = 6 , i = 2 e j = 3 a saída deverá ser : 0,2,3,4,6,8.

n = int(input("Digite o número de n: "))
i = int(input("Digite o número de i: "))
j = int(input("Digite o número de j: "))


0 ate 999999999999999999 --> range


cal --> 

n = int(input("Digite o número de n: "))
i = int(input("Digite o número de i: "))
j = int(input("Digite o número de j: "))

cont = 0
aux = 0

while cont < n:
	if aux % i == 0 or aux % j == 0:
		print(aux)
		cont += 1
	aux += 1
"""
"""
EXERCICO 4
Dados dois números inteiros positivos i e j diferentes de 0,
imprimir todos os divisores comuns de i e j.

Exemplo: i = 2 e j = 3 a saída deverá ser : 1
i = 9, j = 21 a saída deverá ser: 1, 3
"""
i = int(input("Digite o número de i: "))
j = int(input("Digite o número de j: "))

aux = 1

while aux <= i and aux <= j:
	if i % aux == 0 and j % aux == 0:
		print(aux)
	aux += 1