# Q2
# nome do país#tipo da medalha#modalidade

# Subprograma
def listandoMedalhas(arquivo):
  ouro = set()
  prata = set()
  bronze = set()

  dados = open(arquivo, "r")
  linha = dados.readline()

  while linha != "":

    valsLinha = linha.split("#")

    # tirando o \n
    if "\n" in valsLinha[2]:
      for i in range(0, len("\n")):
        valsLinha[2] = valsLinha[2].replace("\n", "")

    if valsLinha[1] == "ouro":
      if valsLinha[1] not in ouro:
        ouro.add(valsLinha[0])

    if valsLinha[1] == "prata":
      if valsLinha[1] not in prata:
        prata.add(valsLinha[0])

    if valsLinha[1] == "bronze":
      if valsLinha[1] not in bronze:
        bronze.add(valsLinha[0])



    linha = dados.readline()


  dados.close()
  return ouro, prata, bronze
def imprimeMedalhas(medOuro, medPrata, medBronze):
  print("\nPaises que ganharam OURO:")
  for val in medOuro:
   print("\t"+val)

  print("\nPaises que ganharam PRATA:")
  for val in medPrata:
    print("\t"+val)

  print("\nPaises que ganharam BRONZE:")
  for val in medBronze:
    print("\t"+val)


  print("\nPaises que ganharam pelo menos uma medalha:")
  # fiz isso pois achei mais facil
  uniaoOuroPrata = medOuro.union(medPrata)
  uniaoTodasMedalhas = uniaoOuroPrata.union(medBronze)
  for val in uniaoTodasMedalhas:
    print("\t"+val)


  print("\nPaises que ganharam todas as medalhas:")
  intersecaoOuroPrata = medOuro.intersection(medPrata)
  intersecaoTodasMedalhas = intersecaoOuroPrata.intersection(medBronze)
  for val in intersecaoTodasMedalhas:
    print("\t"+val)



  return None

# Programa Principal

nomeArquivo = input("Digite o nome do arquivo: ")
paisesOuro, paisesPrata, paisesBronze = listandoMedalhas(nomeArquivo)
imprimeMedalhas(paisesOuro, paisesPrata, paisesBronze)
