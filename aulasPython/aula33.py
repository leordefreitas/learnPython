"""
EXERCICIO 1
Faça um programa com uma função chamada somaImposto.

A função possui dois parâmetros formais:
    1 - taxaImposto, que é a quantia de imposto sobre vendas expressa em
        porcentagem
    2 - custo, que é o custo de um item antes do imposto.

A função “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImposto(taxaImposto, custo):
    vendasAlteradas = custo * (taxaImposto/100)
    return vendasAlteradas

"""

"""
EXERCICIO 2
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
uma para fazer a conversão e uma para a saída. Assim, a função para efetuar as
conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores
de entrada todas as vezes que desejar.

rodada = True
def alterado (hora, minuto):
    if hora > 12:
        alt = hora - 12
    else:
        alt = hora
    return print("A hora modifica ficou %i:%i."%(alt, minuto))

while rodada:
    hora = int(input("Digite as horas: "))
    minuto = int(input("Digite os minutos: "))
    alterado(hora, minuto)

    saida = int(input("Deseja continuar(sim=1 ou não=0): "))
    if saida == 0:
        rodada = False
 """