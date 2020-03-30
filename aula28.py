"""
EXERCICIO 1
Recebendo entradas inteiras do usuário que só devem ser interrompidas com a
entrada do número -1, e recebendo um elemento qualquer, calcular o número
de vezes que esse elemento aparece na sequência digitada pelo usuário


ent = int(input("Digite o número para a sequência: "))
lista = []
lista.append(ent)
while ent != -1:
	ent = int(input("Digite o número para a sequência: "))
	lista.append(ent)
	if ent == -1:
		e = int(input("Digite o valor e: "))
		print("O número %i aparece %i."%(e, lista.count(e)))

"""
"""
EXERCICIO 2
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor
foi conseguido.

import random
lista = []

for i in range(100):
	lista.append(random.randint(1, 6))
print("O valor 1 aparece %i."%(lista.count(1)))
print("O valor 2 aparece %i."%(lista.count(2)))
print("O valor 3 aparece %i."%(lista.count(3)))
print("O valor 4 aparece %i."%(lista.count(4)))
print("O valor 5 aparece %i."%(lista.count(5)))
print("O valor 6 aparece %i."%(lista.count(6)))
"""
"""
EXERCICIO 3
Uma grande emissora de televisão quer fazer uma enquete entre os seus
telespectadores para saber qual o melhor jogador após cada jogo.
Para isto, faz-se necessário o desenvolvimento de um programa, que será
utilizado pelas telefonistas, para a computação dos votos.

Sua equipe foi contratada para desenvolver este programa, utilizando a
linguagem de programação Python.
Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador.
Um número de jogador igual zero, indica que a votação foi encerrada.
Se um número inválido for digitado, o programa deve ignorá-lo,
voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:

a.	O total de votos computados;
b.	Os números e respectivos votos de todos os jogadores que receberam votos;
c.	O percentual de votos de cada um destes jogadores;
d.	O número do jogador escolhido como o melhor jogador da partida,
        juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como
votos. O resultado aparece ordenado pelo número do jogador.
O programa deve fazer uso de listas.

Exemplo de execução:
>>> 
Enquete: Quem foi o melhor jogador?

Informe um valor entre 1 e 23 ou 0 para sair!

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da Votação: 

Foram computados 8 votos

Jogador          Votos          %
   9                4          50.0%
  10                3          37.5%
  11                1          12.5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50.0% do total de votos.
>>> 
"""

print("Quem foi o melhor jogador?")
print("Informe um valor entre 1 e 23 ou 0 para sair!")
num = int(input("Número do jogador (0=fim): "))
lista = []

while num != 0:
	if 1 <= num >= 23:
		lista.append(num)

	num = int(input("Número do jogador (0=fim): "))


print("Resultado da Votação:")
print("")
print("Foram computados %i votos"%(len(lista)))
print("Jogador     Votos     %")

for j in range(lista2):
	print("%i          %i        %i%%"%(j, lista.count(j), (100*lista.count(j)))/(cont))
print("")

	

