# Q2
# código#preço#quantidade#dias restantes de validade


# Subprograma
def lerArquivo(nome):

  dados = open(nome, "r")
  linha = dados.readline()
  todosProdutos = []

  while linha != "":
    produto = dict()
    valores = linha.split("#")
    produto["codigo"] = valores[0]
    produto["preco"] = valores[1]
    produto["qtd"] = valores[2]

    if "\n" in valores[3]:
      for i in range(0, len("\n")):
        valores[3] = valores[3].replace("\n", "")

    produto["validade"] = valores[3]
    todosProdutos.append(produto)

    linha = dados.readline()

  dados.close()
  return todosProdutos

def imprime(vals):
  for produto in vals:

    for chave in produto:
      print(chave, ":", produto[chave], end=" ")
    print()

  return None

def listarProdutosVencendo(vals):
  produtosVencendo = [] 

  for produto in vals:
    if int(produto["validade"]) < 7:
      produtosVencendo.append(produto)

  return produtosVencendo

def listarProdutosCliente(nomeArquivo, vals):
  dados = open(nomeArquivo, "r")
  linha = dados.readline()
  codigos = []

  while linha != "":

    if "\n" in linha:
      for i in range(0, len("\n")):
        linha = linha.replace("\n", "")

    codigos.append(linha)

    linha = dados.readline()

  for codigo in codigos:
    cont = True
    
    for produto in vals:
      if produto["codigo"] == codigo:
        print(codigo +" "+ "Preço:", produto["preco"] +" "+ "Qtd:", produto["qtd"])
        cont = False

    if cont == True:
      print(codigo +" "+ "Indisponível")

  dados.close()
  return None

# Programa Principal

nomeArquivo = input()
produtos = lerArquivo(nomeArquivo)
print("------------TODOS OS PRODUTOS-------------------")
imprime(produtos)
print("------------PRODUTOS VENCENDO-------------------")
listaVencidos = listarProdutosVencendo(produtos)
imprime(listaVencidos)
arquivoCliente = input()
listaCliente = listarProdutosCliente(arquivoCliente, produtos)