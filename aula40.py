"""
exercicio 1
Escreva uma nested function que forneça um número (x da função menor) elevado
a outro (N da função maior)

def exp(n):
    def eleva(x):
        print(x**n)
    return eleva

"""

"""
exercicio 2
Escreva um programa usando uma nested function que permita imprimir a taboada
de 1 até um n dado
"""
def tabuada1(x):
    def tabuada2(y):
        print("Para o número %i."%x)
        if y <= 10:
            print("%i * %i ="%(x, y), (tabuada2(y+1)))

"""
Exemplo:
>>>
Digite um número: 3
Para o número 1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10

Para o número 2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20

Para o número 3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30

>>>
"""



