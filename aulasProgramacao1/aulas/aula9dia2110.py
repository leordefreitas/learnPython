# /0 -> significa o fim do arquivo
# /n -> fim da linha
# open(caminho do arquivo, modo de abertura)
# modos de operacao sao: "r" -> apenas leitura, "w" -> apenas escrita, "a" -> escrita no final do arquivo
# sempre que open() executar o close()
# exeplo
# dados = open("exemplo.txt", "w")
# dados.close()

# metodos
# dados.readline() -> ler as linhas do arquivo

# exemplo 1
# dados = open("teste.txt", "r")
# linha = dados.readline()
# print(linha)
# dados.close()

# exemplo 2
# programa que le o arquivo que vc bota o nome no input
# nomeArquivo = input()
# dados = open(nomeArquivo, "r")
# linha = dados.readline()
# while linha != "":
#   print(linha)
#   linha = dados.readline()
# dados.close()

# exemplo 3
# nomeArquivo = input()
# dados = open(nomeArquivo, "r")
# linha = dados.readline()
# for linha in dados:
#   print(linha)
# dados.close()

# write() -> colocar mais informacao no arquivo tanto "a" como "w"

# exemplo 1
# dados = open("teste.txt", "w")
# dados.write("qualquer dado pode ser escrito \n")
# dados.close()

# exemplo 2
# nomeArquivo = input()
# quantasLinhas = int(input("Quantas linhas: "))
# dados = open(nomeArquivo, "w")

# for i in range(quantasLinhas):
#   nova = input("Linha" + str(i + 1) + ":")
#   dados.write(nova + "\n")
# dados.close()

# exemplo 3
# SUB
# def criaArqPts(nome, qtd, min, max):
#   from random import randint
#   arq = open(nome, "w")
#   for pos in range(qtd):
#     arq.write(str(randint(min,max))+" "+str(randint(min,max))+"\n")
#   arq.close()
#   return None
# def mostra(nome):
#   arq = open(nome, "r")
#   for pt in arq:
#     print(pt, end="")
#   arq.close()
#   return None
# # PP
# criaArqPts("pontos.txt", 30, 0, 400)
# mostra("pontos.txt")

# exemplo 4
# sub
# def centroide(nome):
#   arquivo = open(nome, "r")
#   qtdPts = 0
#   somaX = 0
#   somaY = 0
#   for coordenada in arquivo:
#     partes = coordenada.split()
#     somaX += float(partes[0])
#     somaY += float(partes[1])
#     qtdPts += 1
#   arquivo.close()
#   if qtdPts == 0:
#     print(arquivo.name, "- vazio!!!")
#   else:
#     print("Ponto calculado: (", somaX/qtdPts, ",", somaY/qtdPts, ").")
#   return None
# # pp
# centroide("pontos.txt")

# exemplo 5
# copiando um arquivo
# sub
# def mostra(nome):
#   infos = open(ome, "r")
#   for linha in infos:
#     print(linha.strip())
#   infos.close()
#   return None
# def copiar(nomeOrigem, nomeDestino):
#   orig = open(nomeOrigem, "r")
#   dest = open(nomeDestino, "w")
#   for linha in orig:
#     dest.write(linha)
#   orig.close()
#   dest.close()
#   return None
# # pp
# nomes = input("Escreva os nomes dos arquivos, original e destino: ").split()
# mostra(nomes[0])
# copiar(nomes[0], nomes[1])
# mostra(nomes[1])

# exemplo 6
# colocando alguma coisa no final do arquivo
# nome = input("Diga o nome do arquivo que deseja anexar linha ao final: ")
# arquivo = open(nome, "a")
# novaLinha = input("Digite uma nova linha: ")
# arquivo.write(novaLinha + "\n")
# arquivo.close()