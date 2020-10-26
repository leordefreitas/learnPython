# set() -> e para determinar um conjunto, ela ceita integral, float, strings e tuplas
# nao e acessada por indice
"""
escolhidos = set()
# add -> adiciona um elemento no conjunto, caso o elemento nao exista no conjunto
escolhidos.add(13)
escolhidos.add(4)
print(escolhidos)
# discard() -> retira um elemento do conjunto
escolhidos.discard(4)
print(escolhidos)
# len() -> retorna a cardinalidade do conjunto
print(len(escolhidos))
"""

# EXEMPLO 1
# escolhidos = set()
# for i in range(5):
#   nome = input("Digite seu nome: ")
#   escolhidos.add(nome)
#   print(escolhidos)

# OPERADORES DE CONJUNTOS
# # a.union(b) -> a em uniao com b
# print({1, 3, 4}.union({1, 2, 5}))
# # a.intersection(b) -> a em intersecao com b
# print({1, 3, 4}.intersection({1, 2, 5}))
# # a.difference(b) -> os valores diferentes de a em b
# print({1, 3, 4}.difference({1, 2, 5}))
# print({1, 3}.difference({2, 4}))

# EXEMPLO 2
# ano = {"jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"}
# feriasFimAno = {"jan", "fev", "dez"}
# feriasMeioAno = {"jul"}
# ferias = feriasFimAno.union(feriasMeioAno)
# periodoLetivo = ano.difference(ferias)
# print(periodoLetivo)

# na igualdade e diferenca nao precisa estar na ordem os conjuntos
# >= -> conten
# <= -> esta contido
# {1, 3} <= {1, 2, 3, 4}
# {1, 3} <= {1, 3}
# {} <= {1, 3}

# a in b -> o in pode ser utilizado igual no for

# EXEMPLO 3
# # sub
# def imprime(num, osPrimos):
#   print("Primos entre 2 e", num, ":")
#   for candidato in range(2, num+1):
#     if candidato in osPrimos:
#       print(candidato, end=" ")
#   print()
#   return None
# def eratostenes(num):
#   resposta = set()
#   vazio = set()
#   crivo = set(range(2, num+1))
#   prox = 2
#   while crivo != vazio:
#     while not (prox in crivo):
#       prox += 1
#     resposta.add(prox)
#     j = prox
#     while j <= num:
#       crivo.discard(j)
#       j += prox
#   return resposta
# # pp
# n = int(input("Diga o valor: "))
# primos = eratostenes(n)
# imprime(n, primos)

# EXEMPLO 3
# sub
def perfilComum(habitantes, caracteristicas, grupo):
  comuns = caracteristicas
  for ident in range(len(habitantes)):
    if ident in grupo:
      comuns = comuns & habitantes[ident]
    print("As caracteristicas em comum sao:")
  for c in caracteristicas:
    if c in comuns:
      print(c, end=" ")
    print()
  return NOne

# pp
caracteristicas = {"esporte", "tv", "cinema", "livro", "jornal", "teatro", "musica"}
alunos = [{"tv", "cinema", "livro"}, {"cinema", "musica"}, {"cinema", "tv", "teatro"}]
perfilComum(alunos, caracteristicas, {2, 0})