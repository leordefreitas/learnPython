
lista = []
i = True
while i:     
    num = int(input("Digite um número: "))
    if num == -1:
        i = False
    if num > 10 and num % 2 == 0:
        lista.append(num)
print(lista)
    

