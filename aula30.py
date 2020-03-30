"""
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando
for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
a.	Mostre a quantidade de valores que foram lidos;@
b.	Exiba todos os valores na ordem em que foram informados@
c.	Exiba todos os valores na ordem inversa à que foram informados@
d.	Calcule e mostre a soma dos valores;@
e.	Calcule e mostre a média dos valores;
f.	Calcule e mostre a quantidade de valores acima da média calculada;
g.	Calcule e mostre a quantidade de valores abaixo de sete;
h.	Encerre o programa com uma mensagem;
"""

lista = []
aux = True
cont = 0

while aux:
    num = int(input("Digite um número: "))
    if num == -1:
        aux = False
    else:
        lista.append(num)
        cont += 1


#A
print("O total de valores lidos foi de", cont)

#B
print(lista)

#C
rev = lista[::-1]
print(rev)

#D
soma = 0
for i in lista:
    soma += i
print(soma)

#E
c = len(lista)
media = soma / c
print(media)

#F
maior = []
for j in lista:
    if j > media:
        maior.append(j)
print(maior)

#G
menor = []
for k in lista:
    if k < 7:
        menor.append(k)
print(menor)

#H
print("Seu programa funcionou muito bem!")