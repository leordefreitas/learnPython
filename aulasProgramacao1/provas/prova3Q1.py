# Prova 3
# num1#num2#num3#num4#num5#num6#cpfApostador#numAposta#loterica

# Subprograma

def armazenandoDadosAposta(arquivo, vals):

  dados = open(arquivo, "r")
  linha = dados.readline()
  # print(linha)
  if linha == "":
    print("VAZIO – Nenhuma aposta registrada!!")
  array6 = []
  array5 = []
  array4 = []
  array3 = []

  # saber o total de apostas
  ope2 = 0
  while linha != "":
    ope2 += 1

    valsLinha = linha.split("#")

    # tirando o \n
    if "\n" in valsLinha[8]:
      for i in range(0, len("\n")):
        valsLinha[8] = valsLinha[8].replace("\n", "")
    # print(valsLinha)

    # formando tupla 
    tupla = (str(valsLinha[6]), int(valsLinha[7]), str(valsLinha[8]))
    # print(tupla)

    ope1 = 0
    for i in range(0, 6):
      for val in vals:
        if int(valsLinha[i]) == val:
          # print(int(valsLinha[i]), val)
          ope1 += 1

    if ope1 == 6:
      array6.append(tupla)
      # print(array6)

    elif ope1 == 5:
      array5.append(tupla)
      # print(array5)

    elif ope1 == 4:
      array4.append(tupla)
      # print(array4)

    elif ope1 == 3:
      array3.append(tupla)
      # print(array3)


    tupla = ()
    linha = dados.readline()

  # declarando os dicionarios
  dicionario = dict()
  dicionario["6"] = array6
  dicionario["5"] = array5
  dicionario["4"] = array4
  dicionario["3"] = array3

  dados.close()
  return dicionario, ope2


def premiandoApostas(vals, totalApostas):

  totalPremios = 0
  print("\nTotal apostado: R$ %.2f" %(totalApostas))
  print("Total recebido pelas lotéricas: R$ %.2f \n" %(totalApostas * 0.03))

  if len(vals["6"]) > 0:
    resultado6 = (totalApostas * 0.7) / len(vals["6"])
    print("JOGOS QUE ACERTARAM 6 NÚMEROS!!!")
    print(vals["6"])
    print("O valor recebido, por cada: R$ %.2f" %(resultado6))
    print()
    totalPremios += resultado6 * len(vals["6"])

  else:
    print("ACUMULADO!!!")
    print("Total acumulado: R$ %.2f \n" %(totalApostas * 0.7))

  
  if len(vals["5"]) > 0:
    resultado5 = (totalApostas * 0.2) / len(vals["5"])
    print("JOGOS QUE ACERTARAM 5 NÚMEROS!!!")
    print(vals["5"])
    print("O valor recebido, por cada: R$ %.2f" %(resultado5))
    print()
    totalPremios += resultado5 * len(vals["5"])
  else:
    print("NINGUÉM ACERTOU 5 NÚMEROS!!!\n")

  if len(vals["4"]) > 0:
    resultado4 = (totalApostas * 0.05) / len(vals["4"])
    print("JOGOS QUE ACERTARAM 4 NÚMEROS!!!")
    print(vals["4"])
    print("O valor recebido, por cada: R$ %.2f" %(resultado4))
    print()
    totalPremios += resultado4 * len(vals["4"])
  else:
    print("NINGUÉM ACERTOU 4 NÚMEROS!!!\n")

  if len(vals["3"]) > 0:
    resultado3 = (totalApostas * 0.03) / len(vals["3"])
    print("JOGOS QUE ACERTARAM 3 NÚMEROS!!!")
    print(vals["3"])
    print("O valor recebido, por cada: R$ %.2f" %(resultado3))
    totalPremios += resultado3 * len(vals["3"])
  else:
    print("NINGUÉM ACERTOU 3 NÚMEROS!!!")

  print("\nO total pago em prêmios: R$ %.2f" %(totalPremios))

  

  return None


# Programa Principal

nomeArquivo = input("Digite o nome do arquivo: ")
resultadoNum = list(map(int, input("Digite os números sorteados(separados por espaço): ").split()))
dicionarioApostas, totalApostas = armazenandoDadosAposta(nomeArquivo, resultadoNum)
premiandoApostas(dicionarioApostas, totalApostas)