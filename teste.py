"""
matriz = [[1, 2, 3, 4],[5, 6, 7, 8]]

pos1 = 11
pos2 = 12
elemento1 = matriz[pos1//10 - 1][pos1%10 -1]
elemento2 = matriz[pos2//10 - 1][pos2%10-1]
matriz[pos1//10-1][pos1%10-1] = elemento2
matriz[pos2//10-1][pos2%10-1] = elemento1

print(matriz)



f = (lambda x, y, z: x+y+z)

print(f(1, 1, 1))
'''