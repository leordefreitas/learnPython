# 21/09/20

# subprograma
def primo(numero):
  for divisor in range(2, 1 + int(numero**0.5)):
    if numero % divisor == 0:
      return False

  return numero > 1

def perfeito(numero):
  somaDosDivisores = 1
  for divisor in range(2, numero // 2 + 1):
    if numero % divisor == 0:
      somaDosDivisores += divisor

  return numero == somaDosDivisores

def mostraBinario(numero):
  resposta = ""

  while numero > 0:
    resposta = str(numero % 2) + resposta
    numero = numero // 2

  print(resposta)
  return None


def mostraNaBase(numero, b):
  resposta = ""

  while numero > 0:
    resposta = str(numero % b) + resposta
    numero = numero // b

  print("Base " + str(b) + ": " + resposta)
  return None

# # exercicio 1
""" 
inicio, fim = input().split()
inicio, fim = int(inicio), int(fim)

inicio, fim = map(int, input().split())

for x in range(inicio, fim+1):
  if primo(x) or perfeito(x):
    print(x)

"""


# # exercicio 2
# programa usando o perfeito()

"""
valores = list(map(int, input().split()))

for x in valores:
  if primo(x) or perfeito(x):
    print(x)

"""

# # exercicio 3
valores = list(map(int, input().split()))
for x in valores:
  print("Decimal " + str(x) + ":")
  for base in range(2, 10):
    mostraNaBase(x, base)

