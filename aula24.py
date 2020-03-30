"""
EXERCICIO 1
Escreva um programa para testar se a estatistíca proposta no filme
'Quebrando a banca' é verdadeira. Utilize o módulo random para tais testes.


teste = int(input("Número de testes: "))
porc = porc1 = 0
import random

for i in range(1, teste+1):
	a = random.randrange(1, 4)
	b = random.randint(1, 3)
	if a == b:
		porc += 1
	else:
		porc1 += 1
print("A chance de não trocar de porta é %.2g%%."%((100*porc)/teste))
print("A chance de trocar de porta é %.2g%%."%((100*porc1)/teste))
"""
"""
EXERCICIO 2
Escreva um programa para simular o jogo das portas. Faça um programa que tenha
a saída como a seguinte:

Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!
Escolha uma porta: 3
Você escolheu a porta 3, mas
eu lhe informo que na porta 2 há um bode.
Deseja trocar de porta (1 - Sim/ 0 - Não): 1
Ganhou um carro!
"""
print("Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!")
porta = int(input("Escolha uma porta: "))
import random
bode = random.randint(1, 3)
premio = random.randint(1, 3)
print("Você escolheu a porta %i, mas eu lhe informo que na porta %i há um bode."%(porta, bode))
if porta == bode:
	print("Você perdeu!")
if porta != bode:
	troca = int(input("Deseja trocar de porta (1 - Sim/ 0 - Não): "))
	if troca == 0:
		porta = porta
	if porta == premio:
		print("Ganhou um carro!")
	else:
		print("Você perdeu!")
