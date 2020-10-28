# Q2
# SUBPROGRAMAS
def produtoExiste(listaNaoExi, listaCod, listaPre, numPro, qtd):
  if numPro not in listaCod:
    listaNaoExi.append(numPro)
    return 0
  else:
    for index in range(len(listaCod)):
      if listaCod[index] == numPro:
        soma = listaPre[index] * qtd
  return soma
def imprimeFinal(valsNaoExistem, valGasto):
  print()
  print("Os seguintes produtos não existem:")
  for val in valsNaoExistem:
    print("   %i" %(val))
  print()
  print("O total gasto foi de R$ %.2f" %(valGasto))
  return None
# PROGRAMA PRINCIPAL
qtdProdutos = int(input("Quantidade de produtos: "))
contador = 0
listaProdutosCodigo = []
listaProdutosPreco = []

while contador < qtdProdutos:
  codigoProduto, precoProduto = map(int, input("Digite o código e o preco do produto separados por espaço: ").split())
  listaProdutosCodigo.append(codigoProduto)
  listaProdutosPreco.append(precoProduto)
  contador += 1

valorGasto = 0
listaProdutosNaoExistem = []

print()
codProCompradoQtdComprado = list(map(int, input("Código do produto comprado e a quantidade, separados por espaço: ").split()))


while codProCompradoQtdComprado != []:
  valorGasto += produtoExiste(listaProdutosNaoExistem, listaProdutosCodigo, listaProdutosPreco, codProCompradoQtdComprado[0], codProCompradoQtdComprado[1])
  codProCompradoQtdComprado = list(map(int, input("Código do produto comprado e a quantidade, separados por espaço: ").split()))

imprimeFinal(listaProdutosNaoExistem, valorGasto)