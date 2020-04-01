"""
Bancário. Escreva um programa que registre o caixa de um banco. O programa
começa perguntando se o usuário quer criar uma conta ou fechar o programa. Se
ele escolher fechar o programa escreve uma mensagem de agradecimento e fecha,
caso contrário ele vai pedir que usuário selecione um número com 6 dígitos
e, então, se o número não existir no registro do banco, ele irá pedir um valor
de depósito. Depois o banco perguntara se se deseja ver o saldo do banco, se sim
ele deverá imprimir o balanço geral do banco, senão ele entrará em loop.
"""

contas = []
saldo = 0


def main():
    perguntaInicial = int(input("Deseja usar o programa(1-sim ou 0-não): "))
    if perguntaInicial == 0:
        print("Foi um prazer lhe ajudar.")
    else:
        criarConta()
        verSaldo()
        continuar = bool(int(input("Deseja continuar usando esse programa(1-sim ou 0-não): ")))
        while continuar:
            criarConta()
            verSaldo()
            continuar = bool(int(input("Deseja continuar usando esse programa(1-sim ou 0-não): ")))


def criarConta():
    global contas, saldo
    numConta = int(input("Digite um número para conta: "))
    while numConta in contas:
        print("Número já existente.")
        conta = int(input("Digite um número para conta: "))
    contas.append(numConta)  

    valor = float(input("Digite o valor de depósito: "))    
    while valor <= 0:
        print("Valor abaixo do previsto.")
        valor = float(input("Digite o valor de depósito: "))
    saldo += valor



def verSaldo():
    global saldo
    verMensagem = bool(int(input("Deseja ver o saldo(1-sim e 0-não: ")))
    while verMensagem:
        print("Seu saldo é R$%.2f."%saldo)
        verMensagem = bool(int(input("Deseja ver o saldo(1-sim e 0-não: ")))

main()


