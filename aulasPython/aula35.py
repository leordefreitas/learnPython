""" 
exercício 1
Escreva uma função que obtenha a multiplicação de vários números de entrada

vezes = 1
def multiplica(*num):
    vezes = 1
    for y in num:
        vezes *= y
    return vezes


print(multiplica(1, 2))

"""
"""
exercício 2
Escreva uma função que obtenha o maior número de uma sequência de números
"""

def maiorNum(*num):
    aux = num[0]
    for i in num:
        

        if i > aux:
            aux = i
    return aux
print(maiorNum(10, 1, 3, 0, 5))