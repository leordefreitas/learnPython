# aula syncrona dia 14/10
"""
# EXEMPLO 1
# sub
def calculaMDC(a, b):
  if a > b:
        a, b = b, a                            # posso fazer isso para inverter os valores
      for divisor in range(a, 1, -1):          # -1 e o passo que ele percorre
    if a % divisor == 0 and b % divisor == 0:  # comeca de cima para baixo por isso nao precisa 
          return divisor                       # percorrer todos somente o primeiro que corresponder 
      return 1                                 # a questao

# PP
n1, n2 = map(int, input().split())
mdc = calculaMDC(n1, n2)
print("MDC:", mdc)
"""
"""
# EXEMPLO 2
# sub


# PP
numero = int(input())
qtd = 0
soma = 0
menor = numero
while numero != 0:
  if numero < menor:
    menor = numero
  soma += numero
  qtd += 1
  numero = int(input())
print("Quantidade de Numeros:", qtd)
print("Menor Numero Lido:", menor)
print("Media dos Numeros: %.1f" %(soma/qtd))
"""
"""
# EXEMPLO 3
# sub
def lerTeste():
  return list(map(float, input().split()))

def calculaMedia(vals):
  soma = 0
  for valor in vals:
    soma += valor
  return soma/len(vals)
# PP
somaDasMedias = 0
qtdTeste = int(input())
for teste in range(qtdTeste):
  valores = lerTeste()
  media = calculaMedia(valores)
  somaDasMedias += media
  print("Teste %d : Media = %.1f" %(teste + 1, media))
print("Media das Medias = %.1f" %(somaDasMedias / qtdTeste))
"""

# EXEMPLO 4
# sub
def geraAleatoriamenteDNA(tamanho):
  from random import randint
  bases = "CTGA"
  dna = ""
  for i in range(tamanho):
    dna += bases[randint(0,3)]
  return dna
def contaOcorrencias(doenca, paciente):
  total = paciente.count(doenca)
  return total

# PP
qtdNucleosideosPaciente = int(input())
dnaPaciente = geraAleatoriamenteDNA(qtdNucleosideosPaciente)
print("DNA do Paciente:", dnaPaciente)
dnaDoenca = input()
ocorrencias = contaOcorrencias(dnaDoenca, dnaPaciente)
print("Quantidade de Ocorrencias:", ocorrencias)