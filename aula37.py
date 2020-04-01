"""
Escreva o jogo dos números como descrito na aula. Utilize as funções escritas
em aula e mais três feitas agora:
    1 - VerificaSeVenceu: Recebe uma matriz 4x4 e verifica se os números estão
    ordenados de forma que o jogador venceu
    2 - VerificaJogada: Verifica se a jogada escolhida pelo usuário é válida
    3 - ImprimeJogo: Função que imprime o jogo na tela do usuário
Você pode fazer quantas funções adcionais quanto quiser

Organize o seu jogo dentro da função main. Dê para o usuário a toda rodada
a opção de desistir(0) ou de inserir uma posição(1), a posição inserida
será feita colocando a linha e coluna da matriz, por exemplo 11 significa que
estamos nos referenciando ao elemento da linha 1 coluna 1, 32 se referencia ao
elemento da linha 3 coluna 2
"""
import random
matriz = []
matrizAlt = []

def main():
    geraMatriz()
    verificaJogada()
    









#Verifica se os números estã ordenados de forma que o jogador venceu.
def verificaSeVenceu():
    global matriz
    if matriz == [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]:
        print("O jogador é o vencedor!")

#Responsável pela geração da matriz a ser resolvida pelo jogador.  
def geraMatriz():
    global matriz
    listaInicial = list(range(1, 17))
    for i in range(4):
        linha = []
        for j in range(4):
            x = random.choice(listaInicial)
            linha.append(x)
            listaInicial.remove(x)
        matriz.append(linha)
    print(matriz)

#Troca o elemento da mesma matriz por outro de dentro.
def trocaElemento(pos1, pos2):
    global matriz
    elemento1 = matriz[pos1//10 -1][pos1%10 -1]
    elemento2 = matriz[pos2//10 -1][pos2%10-1]
    matriz[pos1//10-1][pos1%10-1] = elemento2
    matriz[pos2//10-1][pos2%10-1] = elemento1

#Verifica se a jogada escolhida pelo usuário é válida.
def verificaJogada():
    numPossiveis = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44]
    pos1 = int(input("Digite a posição 1: "))
    pos2 = int(input("Digite a posição 2: "))
    for k in numPossiveis:
        if pos1 != k or pos2 != k:
            print("Você digitou um número inadequado.")
            pos1 = int(input("Digite a posição 1: "))
            pos2 = int(input("Digite a posição 2: "))
        

#Função que imprime o jogo na tela do usuário.

def imprimeJogo():
    global matrizAlt
    imprimir = bool(int(input("Deseja visualizar o seu jogo(1-sim ou 0-não): ")))
    while imprimir:
        print(matrizAlt)    
        imprimir = bool(int(input("Deseja visualizar o seu jogo(1-sim ou 0-não): ")))


main()