# COMPARACAO DE SUBSTRING
# sub
def fazConjunto(frase):
  conjunto = set()
  for letra in frase:
    conjunto.add(letra)
  return conjunto
# pp
valor1 = input() 
while valor1 != "":
  conjunto1 = fazConjunto(valor1)
  valor2 = input()
  conjunto2 = fazConjunto(valor2)
  qtdFinal = len(conjunto1.intersection(conjunto2))
  print(qtdFinal)

  valor1 = input()