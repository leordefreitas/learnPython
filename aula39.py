"""
exercicio 1
Escreva uma função recursiva que imprima de um número x até um y
"""
def sequencia(x, y):
    if x < y:
        return x
    return print(sequencia(x+1,y))

sequencia(1, 5)



"""
exercicio 2
Escreva uma função recursiva que retorna a soma de n até zero
"""