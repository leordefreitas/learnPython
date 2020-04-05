"""
exercico 1
Escreva uma programa que pegue a lista
abaixo e forneça uma nova lista apenas com números ímpares


lista= [788, 587, 61, 309, 426, 420, 801, 178, 80, 329, 831, 524, 545, 475,
        815, 958, 190, 41, 901, 432, 435, 6, 137, 679, 36, 243, 604, 826,
        758, 304, 319, 507, 404, 792, 105, 667, 438, 693, 802, 165, 527,
        814, 548, 96, 683, 602, 302, 219, 376, 914, 478, 175, 360, 266,
        555, 306, 223, 547, 214, 387, 62, 919, 908, 899, 772, 363, 270,
        723, 346, 921, 424, 75, 869, 250, 969, 633, 460, 108, 808, 5, 631,
        766, 846, 303, 600, 683, 343, 258, 904, 194, 111, 245, 412, 552,
        631, 49, 170, 246, 702, 783]

listaImpar = []

for i in lista:
    if i & 2 == 0:
        continue
    listaImpar.append(i)


print(listaImpar)
"""     
        
"""
exercicio 2 = INCOMPLETO
Escreva uma função que produza a soma dos primeiros
n números de uma lista com tamanho m

import random

lista = []

def criarLista():
    tamanhoLista = int(input("Digite o tamanho da lista: "))
    for i in range(tamanhoLista):
        num = int(input("Digite um número %i de %i: "%(i+1, tamanhoLista)))
        lista.append(num)
    return lista


def main():
    global lista
    criarLista()
    n = int(input("Digite a quantidade a ser somada: "))
    for j in range(n):
"""


