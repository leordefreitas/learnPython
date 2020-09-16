""" 
exercicio 1
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


letra = input("Digite o sexo: ")
if letra == 'm' or letra == 'M':
    print("M - Masculino")
elif letra == 'f' or letra == 'F':
    print("F - Feminino")
else:
    print("Sexo invalido.")
"""
"""
exercicio 2
Faça dois funções: Uma que coloque uma string em maiusculo e outra
que coloque uma str em minusculo

def main():
    palavra = "Chiclete"
    print(maiusculo(palavra))
    print(minusculo(palavra))


def minusculo(string):
    minusculo = ""
    for char in string:
        if "A" <= char <= "Z":
            char = chr(ord(char) + (ord("a") - ord("A")))
        minusculo += char
    return minusculo

def maiusculo(string):
    maiusculo = ""
    for char in string:
        if "a" <= char <= "z":
            char = chr(ord(char) - (ord("a") - ord("A")))
        maiusculo += char
    return maiusculo


main()

"""
"""
exercicio 3
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.


def main():
    usuario = input("Digite o usuario: ")
    senha = input("Digite a senha: ")
    while maiusculo(senha) == maiusculo(usuario):
        print("Nao pode ter a senha igual ao usuario!!")
        usuario = input("Digite o usuario: ")
        senha = input("Digite a senha: ")







def maiusculo(string):
    maiusculo = ""
    for char in string:
        if "a" <= char <= "z":
            char = chr(ord(char) - (ord("a") - ord("A")))
        maiusculo += char
    return maiusculo


main()
"""

"""
exercicio 4
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
a.	"Telefonou para a vítima?"
b.	"Esteve no local do crime?"
c.	"Mora perto da vítima?"
d.	"Devia para a vítima?"
e.	"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

def main():
    contador = 0
    perguntaA = input("Telefonou para a vitima? ")
    perguntaB = input("Esteve no local do crime? ")
    perguntaC = input("Mora perto da vitima? ")
    perguntaD = input("Devia para a vitima? ")
    perguntaE = input("Ja trabalhou com a vitima? ")

    if maiusculo(perguntaA) == ("SIM"):
        contador += 1
    if maiusculo(perguntaB) == ("SIM"):
        contador += 1
    if maiusculo(perguntaC) == ("SIM"):
        contador += 1
    if maiusculo(perguntaD) == ("SIM"):
        contador += 1
    if maiusculo(perguntaE) == ("SIM"):
        contador += 1
    
    if contador == 2:
        print("A pessoa e suspeita!")
    if contador == 3 or contador == 4:
        print("A pessoa e cumplice!!")
    if contador == 5:
        print("A pessoa e o ASSASSINO!!!")
    if contador < 2:
        print("A pessoa e inocente.")






def maiusculo(string):
    maiusculo = ""
    for char in string:
        if "a" <= char <= "z":
            char = chr(ord(char) - (ord("A") - ord("a")))
        maiusculo += char
    return maiusculo


main()
"""
"""
exercicio 5
Faça um Programa que pergunte em que turno você estuda. Peça para digitar
M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.
"""
turno = input("Em qual turno voce trabalha: ")
if turno == "M" or turno == "m":
    print("Bom dia!!")

elif turno == "V" or turno == "v":
    print("Bom tarde!!")

elif turno == "N" or turno == "n":
    print("Bom noite!!")
else:
    print("Valor invalido")