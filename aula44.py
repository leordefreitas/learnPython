"""
exercicio 1
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos
saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5
Segundo Salto: 6.1
Terceiro Salto: 6.2
Quarto Salto: 5.4
Quinto Salto: 5.3

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m

listaValor = []
listaSaltos = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
aux = True
media = 0
while aux:
    nomeAtleta = input("Atleta: ")
    if nomeAtleta == str():
        print("Programa encerrado!")
        break
    for i in listaSaltos:
        valorSaltos = float(input(i + " Salto: "))
        media += valorSaltos
        strValor = str(valorSaltos)
        listaValor.append(strValor)
    media /= 5
    strMedia = str(media)
    break
if nomeAtleta != str():
    print("Resultado final:")
    print("Atleta: " + nomeAtleta)
    print("Saltos: " + listaValor[0] + ' - ' + listaValor[1] + ' - ' + listaValor[2] + ' - ' + listaValor[3] + ' - ' + listaValor[4])
    print("Média dos saltos: " + strMedia + " m")
"""
"""
exercicio 2
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos
restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a
sua média, conforme a descrição acima informada (retirar o melhor e o pior salto
e depois calcular a média com as notas restantes). As notas não são informados
ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

Tente colocar a impressão do resultado em um único print


aux = True

while aux:
    nomeAtleta = input("Atleta: ")
    if nomeAtleta == str():
        break
    valorNota = float(input("Nota: "))
    maiorNota = valorNota
    menorNota = valorNota
    soma = valorNota

    for i in range(6):
        valorNota = float(input("Nota: "))
        soma += valorNota
        if valorNota > maiorNota:
            maiorNota = valorNota
        if valorNota < menorNota:
            menorNota = valorNota
        else:
            continue
    media = (soma - (menorNota + maiorNota))/5
    break
if nomeAtleta != str():
    print("Resultado final:\n" + "Atleta: " + nomeAtleta + "\n" + "Melhor nota: " + str(maiorNota) + "\n" + "Pior nota: " + str(menorNota) + "\n" + "Média: " + str(media))

"""


