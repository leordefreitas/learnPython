"""
São dados dois números inteiros positivos p e q,
sendo que o número de dígitos de p é menor ou igual ao número de dígitos de q.
Verificar se p é um subnúmero de q.

Exemplos:
p = 23, q = 57238, p é subnúmero de q.
p = 23, q = 258347, p não é subnúmero de q.
"""
p = int(input("Digite o valor de p: "))
q = int(input("Digite o valor de q: "))
aux_p = p
cont_d = 0

# contador de dígitos
while aux_p != 0:
	p //= 10
	cont_d += 1

#Comparação
#p é sub de q --> paro execução
#q == 0
aux_q = q
comparando = True
while comparando == False:
	subnum = aux_q%(10**cont_d)
	if subnum == p:
		comparando = False
		print("%i é subnúmero de %i"%(p, q))
	aux_q //= 10
	if aux_q == 0:
		comparando = False
	else:
		print("%i é não é subnúmero de %i"%(p, q))

