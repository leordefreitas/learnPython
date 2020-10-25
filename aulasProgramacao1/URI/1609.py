# CONTANDO CARNEIRINHOS
# sub
def quantosSaoDiferentes(array):
  conjunto = set()
  for cada in array:
    conjunto.add(cada)
  print(len(conjunto))
  return None
# pp
vezes = int(input())
contador = 0

while contador < vezes:
  qtdCarneirinhos = int(input())
  arrayCarneirinhos = input().split()
  quantosSaoDiferentes(arrayCarneirinhos)
  contador += 1