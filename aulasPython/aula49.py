import random

FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palavras = 'formiga babuino encefalo elefante girafa hamburger chocolate giroscópio'.split()

def main():
    """
    Função Principal do programa
    """
    global FORCAIMG

    print("F O R C A")
    letrasErradas = ""
    letrasAcertadas = ""
    palavraSecreta = geraPalavraAleatória().upper()
    jogando = True

    while jogando:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)

        palpite = recebePalpite(letrasErradas + letrasAcertadas)

        if palpite in palavrasSecreta:
            letrasAcertadas += palpite

            if VerificaSeGanhou(palavraSecreta, letrasAcertadas):
                print("Exato! A palavra secreta e " + palavrasSecreta + "! Voce ganhou.")
                jogando = False
            else:
                letrasErradas += palpite

                if len(letrasErradas) == len(FORCAIMG) - 1:
                    imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)

                    print("Voce excedeu seu numero de palpites.")
                    print("Depois de" + str(len(letrasErradas))+"letras erradas e" + str(len(letrasAcertadas)) + "letras acertadas, a palavra era" + palavrasSecreta + ".")
                    
                    jogando = False
            if not jogando:
                if JogarNovamente():
                    letrasAcertadas = ""
                    letrasErradas = ""
                    jogando = True
                    palavrasSecreta = geraPalavraAleatória().upper()







def geraPalavraAleatória():
    """
    Função que retorna uma string a partir da
    lista de palavras global
    """
    global palavras
    return random.choice(palavras)

def imprimeComEspaços(palavra):
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaço entre suas letras ou strings
    """
    for letra in palavra:
        print(letra, end = " ")
    print()
    
def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    """
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta
    """
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)]+'\n')

    print("Letras Erradas: ", end = " ")
    imprimeComEspaços(letrasErradas)

    vazio = "_"*len(palavraSecreta)

    for i in range(len(palavraSecreta)):#isso ja estava feito nao tem que entender 
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]
    imprimeComEspaços(vazio)

def recebePalpite(palpitesFeitos):
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado
    """
    while True:
        palpite = input("Adivinhe uma letra\n")
        palpite.upper()

        if len(palpite) != 1:
            print("Coloque um unica letra.")
        elif palpite in palpitesFeitos:
            print("Voce ja realizou esse palpite.")
        elif not 'A' <= palpite <= 'Z':
            print("Por favor digite uma letra.")
        else:
            return palpite
        
def JogarNovamente():
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """
    return input("Voce quer jogar novamente? (sim ou nao").upper().startswith('S')

def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    """
    Função que verifica se o usuário acertou todas as
    letras da palavra secreta
    """
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break


main()