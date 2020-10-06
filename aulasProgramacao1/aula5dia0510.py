# aula 5, dia 05/10
"""
#  EXEMPLO 1
# subprogramas
def escrever(valores):
  for item in valores:
    print(item, end=" ")
  print()
  return None

def ler(valores):
  # tipo de entrada de valores
  for ind in range(len(valores)):
    valores[ind] = float(input("vs["+str(ind+1)+"]="))
  return None

def ordenar(valores):
  def ondeMenor(vals, inicio):
    posMenor = inicio
    for p in range(inicio+1, len(vals)):
      if vals[p]<vals[posMenor]:
        posMenor = p
    return posMenor
  for ind in range(len(valores)-1):
    posicao = ondeMenor(valores, ind)
    tempo = valores[ind]
    valores[ind] = valores[posicao]
    valores[posicao] = tempo
  return None

# crio um vetor de tamanho 10
TAM = 10
numeros = [0.0]*TAM
escrever(numeros)
ler(numeros)
ordenar(numeros)
escrever(numeros)


# tipo diferente de ler um vetor, essa e para ler ele somente em uma linha
def ler(numeros):
  linha = input("Digite os valores separados em espacos?")
  partes = linha.split()
  for ind in range(len(valores)) :
    valores[ind] = float(partes[ind])
  return None

# EXEMPLO 2

def listaAprovadosReprovados(estudantes, notas, minimo):
  for pos in range(len(estudantes)):
    media = (notas[pos][0]+notas[pos][1]+notas[pos][2])/3
    if media >= minimo:
      print(estudantes[pos], "Aprovado com nota: ", media)
  print("---------------------------------")
  for pos in range(len(estudantes)):
    media = (notas[pos][0]+notas[pos][1]+notas[pos][2])/3
    if media < minimo:
      print(estudantes[pos], "Reprovado com nota", media)
  return None

alunos ["Maria", "Lucas", "Ana"]
resultados = [[5, 6, 8], [2, 10, 6], [5, 8, 5]]

print(alunos)
print(resultados)
listaAprovadosReprovados(alunos, resultados, 6)


# EXEMPLO 3

# usando o append()
def listaAprovadosReprovados(infos, minimo):
  return None

def leAlunosComNotas(qtdAlunos, qtdNotas):
  resposta = []
  for indAluno in range(qtdAlunos):
    nome = input("Diga o nome do aluno "+str(indAluno+1)+":")
    linha = [nome,[]]
    for indNota in range(qtdNotas):
      nota = float(input("Diga a nota"+str(indNota+1)+" = "))
      linha[1].append(nota)
    resposta.append(linha)
  return resposta

resultados = leAlunosComNotas(5, 3)
listaAprovadosReprovados(resultados, 6)

# aula 5 dia 06/10
# EXEMPLO 4

def avalia(expressao):
  valor = 0
  if expressao != "":
    partes = expressao.split("+")
    for p in partes:
      valor = valor + float(p)
  return valor

lida = input("Entre com uma expressao numerica valida: ")
print("{"+lida"} =", avalia(lida.strip()))
"""

# EXEMPLO 5

def preencher():
  itens = []
  nome = input("Nome do Produto: ")
  while nome != "Fim":
    qtd = int(input("Quantidade: "))
    preco = float(input("Preco unitario: "))
    itens.append((nome, qtd, preco))
    nome = input("Nome do Produto: ")
  return itens

def processa(itens):
  total = 0.0
  for (nome, qtd, preco) in itens:
    total += qtd * preco
    print("Nome:", nome, "Quantidade:", qtd, "Preco:", preco)
  print("Total Gasto:", total)
  return None

compras = preencher()
processa(compras)
